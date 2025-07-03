# app/llm/function_dispatcher/intersight_dispatcher.py
from typing import Any
from app.llm.function_dispatcher import register
from app.llm.platform_clients.intersight_client import IntersightClient

@register('GetAaaAuditRecordList')
def GetAaaAuditRecordList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAaaAuditRecordList(body=body, **kwargs)

@register('GetAaaAuditRecordByMoid')
def GetAaaAuditRecordByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAaaAuditRecordByMoid(body=body, **kwargs)

@register('GetAaaRetentionConfigList')
def GetAaaRetentionConfigList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAaaRetentionConfigList(body=body, **kwargs)

@register('GetAaaRetentionConfigByMoid')
def GetAaaRetentionConfigByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAaaRetentionConfigByMoid(body=body, **kwargs)

@register('GetAaaRetentionPolicyList')
def GetAaaRetentionPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAaaRetentionPolicyList(body=body, **kwargs)

@register('GetAaaRetentionPolicyByMoid')
def GetAaaRetentionPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAaaRetentionPolicyByMoid(body=body, **kwargs)

@register('GetAccessIpAddressList')
def GetAccessIpAddressList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAccessIpAddressList(body=body, **kwargs)

@register('GetAccessIpAddressByMoid')
def GetAccessIpAddressByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAccessIpAddressByMoid(body=body, **kwargs)

@register('GetAccessPolicyList')
def GetAccessPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAccessPolicyList(body=body, **kwargs)

@register('GetAccessPolicyByMoid')
def GetAccessPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAccessPolicyByMoid(body=body, **kwargs)

@register('GetAccessPolicyInventoryList')
def GetAccessPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAccessPolicyInventoryList(body=body, **kwargs)

@register('GetAccessPolicyInventoryByMoid')
def GetAccessPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAccessPolicyInventoryByMoid(body=body, **kwargs)

@register('GetAdapterConfigPolicyList')
def GetAdapterConfigPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAdapterConfigPolicyList(body=body, **kwargs)

@register('GetAdapterConfigPolicyByMoid')
def GetAdapterConfigPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAdapterConfigPolicyByMoid(body=body, **kwargs)

@register('GetAdapterExtEthInterfaceList')
def GetAdapterExtEthInterfaceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAdapterExtEthInterfaceList(body=body, **kwargs)

@register('GetAdapterExtEthInterfaceByMoid')
def GetAdapterExtEthInterfaceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAdapterExtEthInterfaceByMoid(body=body, **kwargs)

@register('GetAdapterHostEthInterfaceList')
def GetAdapterHostEthInterfaceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAdapterHostEthInterfaceList(body=body, **kwargs)

@register('GetAdapterHostEthInterfaceByMoid')
def GetAdapterHostEthInterfaceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAdapterHostEthInterfaceByMoid(body=body, **kwargs)

@register('GetAdapterHostFcInterfaceList')
def GetAdapterHostFcInterfaceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAdapterHostFcInterfaceList(body=body, **kwargs)

@register('GetAdapterHostFcInterfaceByMoid')
def GetAdapterHostFcInterfaceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAdapterHostFcInterfaceByMoid(body=body, **kwargs)

@register('GetAdapterHostIscsiInterfaceList')
def GetAdapterHostIscsiInterfaceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAdapterHostIscsiInterfaceList(body=body, **kwargs)

@register('GetAdapterHostIscsiInterfaceByMoid')
def GetAdapterHostIscsiInterfaceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAdapterHostIscsiInterfaceByMoid(body=body, **kwargs)

@register('GetAdapterUnitList')
def GetAdapterUnitList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAdapterUnitList(body=body, **kwargs)

@register('GetAdapterUnitByMoid')
def GetAdapterUnitByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAdapterUnitByMoid(body=body, **kwargs)

@register('GetAdapterUnitExpanderList')
def GetAdapterUnitExpanderList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAdapterUnitExpanderList(body=body, **kwargs)

@register('GetAdapterUnitExpanderByMoid')
def GetAdapterUnitExpanderByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAdapterUnitExpanderByMoid(body=body, **kwargs)

@register('GetApicAciPodList')
def GetApicAciPodList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicAciPodList(body=body, **kwargs)

@register('GetApicAciPodByMoid')
def GetApicAciPodByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicAciPodByMoid(body=body, **kwargs)

@register('GetApicApplicationList')
def GetApicApplicationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicApplicationList(body=body, **kwargs)

@register('GetApicApplicationByMoid')
def GetApicApplicationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicApplicationByMoid(body=body, **kwargs)

@register('GetApicApplicationEndpointGroupList')
def GetApicApplicationEndpointGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicApplicationEndpointGroupList(body=body, **kwargs)

@register('GetApicApplicationEndpointGroupByMoid')
def GetApicApplicationEndpointGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicApplicationEndpointGroupByMoid(body=body, **kwargs)

@register('GetApicBridgeDomainList')
def GetApicBridgeDomainList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicBridgeDomainList(body=body, **kwargs)

@register('GetApicBridgeDomainByMoid')
def GetApicBridgeDomainByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicBridgeDomainByMoid(body=body, **kwargs)

@register('GetApicExternalRoutedLayerThreeDomainList')
def GetApicExternalRoutedLayerThreeDomainList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicExternalRoutedLayerThreeDomainList(body=body, **kwargs)

@register('GetApicExternalRoutedLayerThreeDomainByMoid')
def GetApicExternalRoutedLayerThreeDomainByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicExternalRoutedLayerThreeDomainByMoid(body=body, **kwargs)

@register('GetApicFabricLeafNodeList')
def GetApicFabricLeafNodeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicFabricLeafNodeList(body=body, **kwargs)

@register('GetApicFabricLeafNodeByMoid')
def GetApicFabricLeafNodeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicFabricLeafNodeByMoid(body=body, **kwargs)

@register('GetApicFabricLeafNodeInterfaceList')
def GetApicFabricLeafNodeInterfaceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicFabricLeafNodeInterfaceList(body=body, **kwargs)

@register('GetApicFabricLeafNodeInterfaceByMoid')
def GetApicFabricLeafNodeInterfaceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicFabricLeafNodeInterfaceByMoid(body=body, **kwargs)

@register('GetApicOutList')
def GetApicOutList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicOutList(body=body, **kwargs)

@register('GetApicOutByMoid')
def GetApicOutByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicOutByMoid(body=body, **kwargs)

@register('GetApicSubnetList')
def GetApicSubnetList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicSubnetList(body=body, **kwargs)

@register('GetApicSubnetByMoid')
def GetApicSubnetByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicSubnetByMoid(body=body, **kwargs)

@register('GetApicTenantList')
def GetApicTenantList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicTenantList(body=body, **kwargs)

@register('GetApicTenantByMoid')
def GetApicTenantByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicTenantByMoid(body=body, **kwargs)

@register('GetApicVpcGroupList')
def GetApicVpcGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicVpcGroupList(body=body, **kwargs)

@register('GetApicVpcGroupByMoid')
def GetApicVpcGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicVpcGroupByMoid(body=body, **kwargs)

@register('GetApicVrfsList')
def GetApicVrfsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicVrfsList(body=body, **kwargs)

@register('GetApicVrfsByMoid')
def GetApicVrfsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApicVrfsByMoid(body=body, **kwargs)

@register('GetApplianceAppOpStatusList')
def GetApplianceAppOpStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceAppOpStatusList(body=body, **kwargs)

@register('GetApplianceAppOpStatusByMoid')
def GetApplianceAppOpStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceAppOpStatusByMoid(body=body, **kwargs)

@register('GetApplianceAppStatusList')
def GetApplianceAppStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceAppStatusList(body=body, **kwargs)

@register('GetApplianceAppStatusByMoid')
def GetApplianceAppStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceAppStatusByMoid(body=body, **kwargs)

@register('GetApplianceAutoRmaPolicyList')
def GetApplianceAutoRmaPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceAutoRmaPolicyList(body=body, **kwargs)

@register('GetApplianceAutoRmaPolicyByMoid')
def GetApplianceAutoRmaPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceAutoRmaPolicyByMoid(body=body, **kwargs)

@register('GetApplianceBackupList')
def GetApplianceBackupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceBackupList(body=body, **kwargs)

@register('GetApplianceBackupByMoid')
def GetApplianceBackupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceBackupByMoid(body=body, **kwargs)

@register('GetApplianceBackupMonitorList')
def GetApplianceBackupMonitorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceBackupMonitorList(body=body, **kwargs)

@register('GetApplianceBackupMonitorByMoid')
def GetApplianceBackupMonitorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceBackupMonitorByMoid(body=body, **kwargs)

@register('GetApplianceBackupPolicyList')
def GetApplianceBackupPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceBackupPolicyList(body=body, **kwargs)

@register('GetApplianceBackupPolicyByMoid')
def GetApplianceBackupPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceBackupPolicyByMoid(body=body, **kwargs)

@register('GetApplianceBackupRotateDataList')
def GetApplianceBackupRotateDataList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceBackupRotateDataList(body=body, **kwargs)

@register('GetApplianceBackupRotateDataByMoid')
def GetApplianceBackupRotateDataByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceBackupRotateDataByMoid(body=body, **kwargs)

@register('GetApplianceCertificateSettingList')
def GetApplianceCertificateSettingList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceCertificateSettingList(body=body, **kwargs)

@register('GetApplianceCertificateSettingByMoid')
def GetApplianceCertificateSettingByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceCertificateSettingByMoid(body=body, **kwargs)

@register('GetApplianceClusterInfoList')
def GetApplianceClusterInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceClusterInfoList(body=body, **kwargs)

@register('GetApplianceClusterInfoByMoid')
def GetApplianceClusterInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceClusterInfoByMoid(body=body, **kwargs)

@register('GetApplianceClusterInstallList')
def GetApplianceClusterInstallList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceClusterInstallList(body=body, **kwargs)

@register('GetApplianceClusterInstallByMoid')
def GetApplianceClusterInstallByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceClusterInstallByMoid(body=body, **kwargs)

@register('GetApplianceClusterReplaceNodeList')
def GetApplianceClusterReplaceNodeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceClusterReplaceNodeList(body=body, **kwargs)

@register('GetApplianceClusterReplaceNodeByMoid')
def GetApplianceClusterReplaceNodeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceClusterReplaceNodeByMoid(body=body, **kwargs)

@register('GetApplianceClusterWorkerNodeList')
def GetApplianceClusterWorkerNodeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceClusterWorkerNodeList(body=body, **kwargs)

@register('GetApplianceClusterWorkerNodeByMoid')
def GetApplianceClusterWorkerNodeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceClusterWorkerNodeByMoid(body=body, **kwargs)

@register('GetApplianceDataExportPolicyList')
def GetApplianceDataExportPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceDataExportPolicyList(body=body, **kwargs)

@register('GetApplianceDataExportPolicyByMoid')
def GetApplianceDataExportPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceDataExportPolicyByMoid(body=body, **kwargs)

@register('GetApplianceDeviceCertificateList')
def GetApplianceDeviceCertificateList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceDeviceCertificateList(body=body, **kwargs)

@register('GetApplianceDeviceCertificateByMoid')
def GetApplianceDeviceCertificateByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceDeviceCertificateByMoid(body=body, **kwargs)

@register('GetApplianceDeviceClaimList')
def GetApplianceDeviceClaimList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceDeviceClaimList(body=body, **kwargs)

@register('GetApplianceDeviceClaimByMoid')
def GetApplianceDeviceClaimByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceDeviceClaimByMoid(body=body, **kwargs)

@register('GetApplianceDeviceClusterInstallList')
def GetApplianceDeviceClusterInstallList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceDeviceClusterInstallList(body=body, **kwargs)

@register('GetApplianceDeviceClusterInstallByMoid')
def GetApplianceDeviceClusterInstallByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceDeviceClusterInstallByMoid(body=body, **kwargs)

@register('GetApplianceDeviceStateList')
def GetApplianceDeviceStateList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceDeviceStateList(body=body, **kwargs)

@register('GetApplianceDeviceStateByMoid')
def GetApplianceDeviceStateByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceDeviceStateByMoid(body=body, **kwargs)

@register('GetApplianceDeviceUpgradePolicyList')
def GetApplianceDeviceUpgradePolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceDeviceUpgradePolicyList(body=body, **kwargs)

@register('GetApplianceDeviceUpgradePolicyByMoid')
def GetApplianceDeviceUpgradePolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceDeviceUpgradePolicyByMoid(body=body, **kwargs)

@register('GetApplianceDiagSettingList')
def GetApplianceDiagSettingList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceDiagSettingList(body=body, **kwargs)

@register('GetApplianceDiagSettingByMoid')
def GetApplianceDiagSettingByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceDiagSettingByMoid(body=body, **kwargs)

@register('GetApplianceExternalSyslogSettingList')
def GetApplianceExternalSyslogSettingList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceExternalSyslogSettingList(body=body, **kwargs)

@register('GetApplianceExternalSyslogSettingByMoid')
def GetApplianceExternalSyslogSettingByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceExternalSyslogSettingByMoid(body=body, **kwargs)

@register('GetApplianceFileGatewayList')
def GetApplianceFileGatewayList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceFileGatewayList(body=body, **kwargs)

@register('GetApplianceFileGatewayByMoid')
def GetApplianceFileGatewayByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceFileGatewayByMoid(body=body, **kwargs)

@register('GetApplianceFileSystemOpStatusList')
def GetApplianceFileSystemOpStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceFileSystemOpStatusList(body=body, **kwargs)

@register('GetApplianceFileSystemOpStatusByMoid')
def GetApplianceFileSystemOpStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceFileSystemOpStatusByMoid(body=body, **kwargs)

@register('GetApplianceFileSystemStatusList')
def GetApplianceFileSystemStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceFileSystemStatusList(body=body, **kwargs)

@register('GetApplianceFileSystemStatusByMoid')
def GetApplianceFileSystemStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceFileSystemStatusByMoid(body=body, **kwargs)

@register('GetApplianceGroupOpStatusList')
def GetApplianceGroupOpStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceGroupOpStatusList(body=body, **kwargs)

@register('GetApplianceGroupOpStatusByMoid')
def GetApplianceGroupOpStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceGroupOpStatusByMoid(body=body, **kwargs)

@register('GetApplianceGroupStatusList')
def GetApplianceGroupStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceGroupStatusList(body=body, **kwargs)

@register('GetApplianceGroupStatusByMoid')
def GetApplianceGroupStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceGroupStatusByMoid(body=body, **kwargs)

@register('GetApplianceImageBundleList')
def GetApplianceImageBundleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceImageBundleList(body=body, **kwargs)

@register('GetApplianceImageBundleByMoid')
def GetApplianceImageBundleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceImageBundleByMoid(body=body, **kwargs)

@register('GetApplianceMetaManifestList')
def GetApplianceMetaManifestList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceMetaManifestList(body=body, **kwargs)

@register('GetApplianceMetaManifestByMoid')
def GetApplianceMetaManifestByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceMetaManifestByMoid(body=body, **kwargs)

@register('GetApplianceMetricsConfigList')
def GetApplianceMetricsConfigList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceMetricsConfigList(body=body, **kwargs)

@register('GetApplianceMetricsConfigByMoid')
def GetApplianceMetricsConfigByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceMetricsConfigByMoid(body=body, **kwargs)

@register('GetApplianceNetworkLinkStatusList')
def GetApplianceNetworkLinkStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceNetworkLinkStatusList(body=body, **kwargs)

@register('GetApplianceNetworkLinkStatusByMoid')
def GetApplianceNetworkLinkStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceNetworkLinkStatusByMoid(body=body, **kwargs)

@register('GetApplianceNodeInfoList')
def GetApplianceNodeInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceNodeInfoList(body=body, **kwargs)

@register('GetApplianceNodeInfoByMoid')
def GetApplianceNodeInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceNodeInfoByMoid(body=body, **kwargs)

@register('GetApplianceNodeOpStatusList')
def GetApplianceNodeOpStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceNodeOpStatusList(body=body, **kwargs)

@register('GetApplianceNodeOpStatusByMoid')
def GetApplianceNodeOpStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceNodeOpStatusByMoid(body=body, **kwargs)

@register('GetApplianceNodeStatusList')
def GetApplianceNodeStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceNodeStatusList(body=body, **kwargs)

@register('GetApplianceNodeStatusByMoid')
def GetApplianceNodeStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceNodeStatusByMoid(body=body, **kwargs)

@register('GetApplianceReleaseNoteList')
def GetApplianceReleaseNoteList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceReleaseNoteList(body=body, **kwargs)

@register('GetApplianceReleaseNoteByMoid')
def GetApplianceReleaseNoteByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceReleaseNoteByMoid(body=body, **kwargs)

@register('GetApplianceRemoteFileImportList')
def GetApplianceRemoteFileImportList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceRemoteFileImportList(body=body, **kwargs)

@register('GetApplianceRemoteFileImportByMoid')
def GetApplianceRemoteFileImportByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceRemoteFileImportByMoid(body=body, **kwargs)

@register('GetApplianceRestoreList')
def GetApplianceRestoreList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceRestoreList(body=body, **kwargs)

@register('GetApplianceRestoreByMoid')
def GetApplianceRestoreByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceRestoreByMoid(body=body, **kwargs)

@register('GetApplianceSetupInfoList')
def GetApplianceSetupInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceSetupInfoList(body=body, **kwargs)

@register('GetApplianceSetupInfoByMoid')
def GetApplianceSetupInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceSetupInfoByMoid(body=body, **kwargs)

@register('GetApplianceSystemInfoList')
def GetApplianceSystemInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceSystemInfoList(body=body, **kwargs)

@register('GetApplianceSystemInfoByMoid')
def GetApplianceSystemInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceSystemInfoByMoid(body=body, **kwargs)

@register('GetApplianceSystemOpStatusList')
def GetApplianceSystemOpStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceSystemOpStatusList(body=body, **kwargs)

@register('GetApplianceSystemOpStatusByMoid')
def GetApplianceSystemOpStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceSystemOpStatusByMoid(body=body, **kwargs)

@register('GetApplianceSystemStatusList')
def GetApplianceSystemStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceSystemStatusList(body=body, **kwargs)

@register('GetApplianceSystemStatusByMoid')
def GetApplianceSystemStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceSystemStatusByMoid(body=body, **kwargs)

@register('GetApplianceUpgradeList')
def GetApplianceUpgradeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceUpgradeList(body=body, **kwargs)

@register('GetApplianceUpgradeByMoid')
def GetApplianceUpgradeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceUpgradeByMoid(body=body, **kwargs)

@register('GetApplianceUpgradePolicyList')
def GetApplianceUpgradePolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceUpgradePolicyList(body=body, **kwargs)

@register('GetApplianceUpgradePolicyByMoid')
def GetApplianceUpgradePolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceUpgradePolicyByMoid(body=body, **kwargs)

@register('GetApplianceUpgradeTrackerList')
def GetApplianceUpgradeTrackerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceUpgradeTrackerList(body=body, **kwargs)

@register('GetApplianceUpgradeTrackerByMoid')
def GetApplianceUpgradeTrackerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetApplianceUpgradeTrackerByMoid(body=body, **kwargs)

@register('GetAssetClusterMemberList')
def GetAssetClusterMemberList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetClusterMemberList(body=body, **kwargs)

@register('GetAssetClusterMemberByMoid')
def GetAssetClusterMemberByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetClusterMemberByMoid(body=body, **kwargs)

@register('GetAssetDeploymentList')
def GetAssetDeploymentList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetDeploymentList(body=body, **kwargs)

@register('GetAssetDeploymentByMoid')
def GetAssetDeploymentByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetDeploymentByMoid(body=body, **kwargs)

@register('GetAssetDeploymentDeviceList')
def GetAssetDeploymentDeviceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetDeploymentDeviceList(body=body, **kwargs)

@register('GetAssetDeploymentDeviceByMoid')
def GetAssetDeploymentDeviceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetDeploymentDeviceByMoid(body=body, **kwargs)

@register('GetAssetDeviceConfigurationList')
def GetAssetDeviceConfigurationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetDeviceConfigurationList(body=body, **kwargs)

@register('GetAssetDeviceConfigurationByMoid')
def GetAssetDeviceConfigurationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetDeviceConfigurationByMoid(body=body, **kwargs)

@register('GetAssetDeviceConnectorManagerList')
def GetAssetDeviceConnectorManagerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetDeviceConnectorManagerList(body=body, **kwargs)

@register('GetAssetDeviceConnectorManagerByMoid')
def GetAssetDeviceConnectorManagerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetDeviceConnectorManagerByMoid(body=body, **kwargs)

@register('GetAssetDeviceContractInformationList')
def GetAssetDeviceContractInformationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetDeviceContractInformationList(body=body, **kwargs)

@register('GetAssetDeviceContractInformationByMoid')
def GetAssetDeviceContractInformationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetDeviceContractInformationByMoid(body=body, **kwargs)

@register('GetAssetDeviceRegistrationList')
def GetAssetDeviceRegistrationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetDeviceRegistrationList(body=body, **kwargs)

@register('GetAssetDeviceRegistrationByMoid')
def GetAssetDeviceRegistrationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetDeviceRegistrationByMoid(body=body, **kwargs)

@register('GetAssetSubscriptionList')
def GetAssetSubscriptionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetSubscriptionList(body=body, **kwargs)

@register('GetAssetSubscriptionByMoid')
def GetAssetSubscriptionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetSubscriptionByMoid(body=body, **kwargs)

@register('GetAssetSubscriptionAccountList')
def GetAssetSubscriptionAccountList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetSubscriptionAccountList(body=body, **kwargs)

@register('GetAssetSubscriptionAccountByMoid')
def GetAssetSubscriptionAccountByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetSubscriptionAccountByMoid(body=body, **kwargs)

@register('GetAssetSubscriptionDeviceContractInformationList')
def GetAssetSubscriptionDeviceContractInformationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetSubscriptionDeviceContractInformationList(body=body, **kwargs)

@register('GetAssetSubscriptionDeviceContractInformationByMoid')
def GetAssetSubscriptionDeviceContractInformationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetSubscriptionDeviceContractInformationByMoid(body=body, **kwargs)

@register('GetAssetTargetList')
def GetAssetTargetList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetTargetList(body=body, **kwargs)

@register('GetAssetTargetByMoid')
def GetAssetTargetByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetAssetTargetByMoid(body=body, **kwargs)

@register('GetBiosBootDeviceList')
def GetBiosBootDeviceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBiosBootDeviceList(body=body, **kwargs)

@register('GetBiosBootDeviceByMoid')
def GetBiosBootDeviceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBiosBootDeviceByMoid(body=body, **kwargs)

@register('GetBiosBootModeList')
def GetBiosBootModeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBiosBootModeList(body=body, **kwargs)

@register('GetBiosBootModeByMoid')
def GetBiosBootModeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBiosBootModeByMoid(body=body, **kwargs)

@register('GetBiosPolicyList')
def GetBiosPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBiosPolicyList(body=body, **kwargs)

@register('GetBiosPolicyByMoid')
def GetBiosPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBiosPolicyByMoid(body=body, **kwargs)

@register('GetBiosSystemBootOrderList')
def GetBiosSystemBootOrderList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBiosSystemBootOrderList(body=body, **kwargs)

@register('GetBiosSystemBootOrderByMoid')
def GetBiosSystemBootOrderByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBiosSystemBootOrderByMoid(body=body, **kwargs)

@register('GetBiosTokenSettingsList')
def GetBiosTokenSettingsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBiosTokenSettingsList(body=body, **kwargs)

@register('GetBiosTokenSettingsByMoid')
def GetBiosTokenSettingsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBiosTokenSettingsByMoid(body=body, **kwargs)

@register('GetBiosUnitList')
def GetBiosUnitList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBiosUnitList(body=body, **kwargs)

@register('GetBiosUnitByMoid')
def GetBiosUnitByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBiosUnitByMoid(body=body, **kwargs)

@register('GetBiosVfSelectMemoryRasConfigurationList')
def GetBiosVfSelectMemoryRasConfigurationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBiosVfSelectMemoryRasConfigurationList(body=body, **kwargs)

@register('GetBiosVfSelectMemoryRasConfigurationByMoid')
def GetBiosVfSelectMemoryRasConfigurationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBiosVfSelectMemoryRasConfigurationByMoid(body=body, **kwargs)

@register('GetBootCddDeviceList')
def GetBootCddDeviceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootCddDeviceList(body=body, **kwargs)

@register('GetBootCddDeviceByMoid')
def GetBootCddDeviceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootCddDeviceByMoid(body=body, **kwargs)

@register('GetBootDeviceBootModeList')
def GetBootDeviceBootModeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootDeviceBootModeList(body=body, **kwargs)

@register('GetBootDeviceBootModeByMoid')
def GetBootDeviceBootModeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootDeviceBootModeByMoid(body=body, **kwargs)

@register('GetBootDeviceBootSecurityList')
def GetBootDeviceBootSecurityList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootDeviceBootSecurityList(body=body, **kwargs)

@register('GetBootDeviceBootSecurityByMoid')
def GetBootDeviceBootSecurityByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootDeviceBootSecurityByMoid(body=body, **kwargs)

@register('GetBootHddDeviceList')
def GetBootHddDeviceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootHddDeviceList(body=body, **kwargs)

@register('GetBootHddDeviceByMoid')
def GetBootHddDeviceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootHddDeviceByMoid(body=body, **kwargs)

@register('GetBootIscsiDeviceList')
def GetBootIscsiDeviceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootIscsiDeviceList(body=body, **kwargs)

@register('GetBootIscsiDeviceByMoid')
def GetBootIscsiDeviceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootIscsiDeviceByMoid(body=body, **kwargs)

@register('GetBootNvmeDeviceList')
def GetBootNvmeDeviceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootNvmeDeviceList(body=body, **kwargs)

@register('GetBootNvmeDeviceByMoid')
def GetBootNvmeDeviceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootNvmeDeviceByMoid(body=body, **kwargs)

@register('GetBootPchStorageDeviceList')
def GetBootPchStorageDeviceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootPchStorageDeviceList(body=body, **kwargs)

@register('GetBootPchStorageDeviceByMoid')
def GetBootPchStorageDeviceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootPchStorageDeviceByMoid(body=body, **kwargs)

@register('GetBootPrecisionPolicyList')
def GetBootPrecisionPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootPrecisionPolicyList(body=body, **kwargs)

@register('GetBootPrecisionPolicyByMoid')
def GetBootPrecisionPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootPrecisionPolicyByMoid(body=body, **kwargs)

@register('GetBootPxeDeviceList')
def GetBootPxeDeviceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootPxeDeviceList(body=body, **kwargs)

@register('GetBootPxeDeviceByMoid')
def GetBootPxeDeviceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootPxeDeviceByMoid(body=body, **kwargs)

@register('GetBootSanDeviceList')
def GetBootSanDeviceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootSanDeviceList(body=body, **kwargs)

@register('GetBootSanDeviceByMoid')
def GetBootSanDeviceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootSanDeviceByMoid(body=body, **kwargs)

@register('GetBootSdDeviceList')
def GetBootSdDeviceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootSdDeviceList(body=body, **kwargs)

@register('GetBootSdDeviceByMoid')
def GetBootSdDeviceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootSdDeviceByMoid(body=body, **kwargs)

@register('GetBootUefiShellDeviceList')
def GetBootUefiShellDeviceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootUefiShellDeviceList(body=body, **kwargs)

@register('GetBootUefiShellDeviceByMoid')
def GetBootUefiShellDeviceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootUefiShellDeviceByMoid(body=body, **kwargs)

@register('GetBootUsbDeviceList')
def GetBootUsbDeviceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootUsbDeviceList(body=body, **kwargs)

@register('GetBootUsbDeviceByMoid')
def GetBootUsbDeviceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootUsbDeviceByMoid(body=body, **kwargs)

@register('GetBootVmediaDeviceList')
def GetBootVmediaDeviceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootVmediaDeviceList(body=body, **kwargs)

@register('GetBootVmediaDeviceByMoid')
def GetBootVmediaDeviceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBootVmediaDeviceByMoid(body=body, **kwargs)

@register('GetBulkExportList')
def GetBulkExportList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBulkExportList(body=body, **kwargs)

@register('GetBulkExportByMoid')
def GetBulkExportByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBulkExportByMoid(body=body, **kwargs)

@register('GetBulkExportedItemList')
def GetBulkExportedItemList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBulkExportedItemList(body=body, **kwargs)

@register('GetBulkExportedItemByMoid')
def GetBulkExportedItemByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBulkExportedItemByMoid(body=body, **kwargs)

@register('GetBulkMoClonerList')
def GetBulkMoClonerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBulkMoClonerList(body=body, **kwargs)

@register('GetBulkMoClonerByMoid')
def GetBulkMoClonerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBulkMoClonerByMoid(body=body, **kwargs)

@register('GetBulkMoDeepClonerList')
def GetBulkMoDeepClonerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBulkMoDeepClonerList(body=body, **kwargs)

@register('GetBulkMoDeepClonerByMoid')
def GetBulkMoDeepClonerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBulkMoDeepClonerByMoid(body=body, **kwargs)

@register('GetBulkMoMergerList')
def GetBulkMoMergerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBulkMoMergerList(body=body, **kwargs)

@register('GetBulkMoMergerByMoid')
def GetBulkMoMergerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBulkMoMergerByMoid(body=body, **kwargs)

@register('GetBulkRequestList')
def GetBulkRequestList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBulkRequestList(body=body, **kwargs)

@register('GetBulkRequestByMoid')
def GetBulkRequestByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBulkRequestByMoid(body=body, **kwargs)

@register('GetBulkResultList')
def GetBulkResultList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBulkResultList(body=body, **kwargs)

@register('GetBulkResultByMoid')
def GetBulkResultByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBulkResultByMoid(body=body, **kwargs)

@register('GetBulkSubRequestObjList')
def GetBulkSubRequestObjList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBulkSubRequestObjList(body=body, **kwargs)

@register('GetBulkSubRequestObjByMoid')
def GetBulkSubRequestObjByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetBulkSubRequestObjByMoid(body=body, **kwargs)

@register('GetCapabilityActionsMetaDataList')
def GetCapabilityActionsMetaDataList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityActionsMetaDataList(body=body, **kwargs)

@register('GetCapabilityActionsMetaDataByMoid')
def GetCapabilityActionsMetaDataByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityActionsMetaDataByMoid(body=body, **kwargs)

@register('GetCapabilityAdapterDeprecatedDefList')
def GetCapabilityAdapterDeprecatedDefList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityAdapterDeprecatedDefList(body=body, **kwargs)

@register('GetCapabilityAdapterDeprecatedDefByMoid')
def GetCapabilityAdapterDeprecatedDefByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityAdapterDeprecatedDefByMoid(body=body, **kwargs)

@register('GetCapabilityAdapterFirmwareRequirementList')
def GetCapabilityAdapterFirmwareRequirementList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityAdapterFirmwareRequirementList(body=body, **kwargs)

@register('GetCapabilityAdapterFirmwareRequirementByMoid')
def GetCapabilityAdapterFirmwareRequirementByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityAdapterFirmwareRequirementByMoid(body=body, **kwargs)

@register('GetCapabilityAdapterUnitDescriptorList')
def GetCapabilityAdapterUnitDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityAdapterUnitDescriptorList(body=body, **kwargs)

@register('GetCapabilityAdapterUnitDescriptorByMoid')
def GetCapabilityAdapterUnitDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityAdapterUnitDescriptorByMoid(body=body, **kwargs)

@register('GetCapabilityAdapterUpdateConstraintMetaList')
def GetCapabilityAdapterUpdateConstraintMetaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityAdapterUpdateConstraintMetaList(body=body, **kwargs)

@register('GetCapabilityAdapterUpdateConstraintMetaByMoid')
def GetCapabilityAdapterUpdateConstraintMetaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityAdapterUpdateConstraintMetaByMoid(body=body, **kwargs)

@register('GetCapabilityAdapterUpgradeSupportMetaList')
def GetCapabilityAdapterUpgradeSupportMetaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityAdapterUpgradeSupportMetaList(body=body, **kwargs)

@register('GetCapabilityAdapterUpgradeSupportMetaByMoid')
def GetCapabilityAdapterUpgradeSupportMetaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityAdapterUpgradeSupportMetaByMoid(body=body, **kwargs)

@register('GetCapabilityCatalogList')
def GetCapabilityCatalogList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityCatalogList(body=body, **kwargs)

@register('GetCapabilityCatalogByMoid')
def GetCapabilityCatalogByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityCatalogByMoid(body=body, **kwargs)

@register('GetCapabilityChassisDescriptorList')
def GetCapabilityChassisDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityChassisDescriptorList(body=body, **kwargs)

@register('GetCapabilityChassisDescriptorByMoid')
def GetCapabilityChassisDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityChassisDescriptorByMoid(body=body, **kwargs)

@register('GetCapabilityChassisManufacturingDefList')
def GetCapabilityChassisManufacturingDefList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityChassisManufacturingDefList(body=body, **kwargs)

@register('GetCapabilityChassisManufacturingDefByMoid')
def GetCapabilityChassisManufacturingDefByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityChassisManufacturingDefByMoid(body=body, **kwargs)

@register('GetCapabilityChassisUpgradeSupportMetaList')
def GetCapabilityChassisUpgradeSupportMetaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityChassisUpgradeSupportMetaList(body=body, **kwargs)

@register('GetCapabilityChassisUpgradeSupportMetaByMoid')
def GetCapabilityChassisUpgradeSupportMetaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityChassisUpgradeSupportMetaByMoid(body=body, **kwargs)

@register('GetCapabilityCimcFirmwareDescriptorList')
def GetCapabilityCimcFirmwareDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityCimcFirmwareDescriptorList(body=body, **kwargs)

@register('GetCapabilityCimcFirmwareDescriptorByMoid')
def GetCapabilityCimcFirmwareDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityCimcFirmwareDescriptorByMoid(body=body, **kwargs)

@register('GetCapabilityCpuEndpointDescriptorList')
def GetCapabilityCpuEndpointDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityCpuEndpointDescriptorList(body=body, **kwargs)

@register('GetCapabilityCpuEndpointDescriptorByMoid')
def GetCapabilityCpuEndpointDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityCpuEndpointDescriptorByMoid(body=body, **kwargs)

@register('GetCapabilityDimmsEndpointDescriptorList')
def GetCapabilityDimmsEndpointDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityDimmsEndpointDescriptorList(body=body, **kwargs)

@register('GetCapabilityDimmsEndpointDescriptorByMoid')
def GetCapabilityDimmsEndpointDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityDimmsEndpointDescriptorByMoid(body=body, **kwargs)

@register('GetCapabilityDomainPolicyRequirementList')
def GetCapabilityDomainPolicyRequirementList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityDomainPolicyRequirementList(body=body, **kwargs)

@register('GetCapabilityDomainPolicyRequirementByMoid')
def GetCapabilityDomainPolicyRequirementByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityDomainPolicyRequirementByMoid(body=body, **kwargs)

@register('GetCapabilityDrivesEndpointDescriptorList')
def GetCapabilityDrivesEndpointDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityDrivesEndpointDescriptorList(body=body, **kwargs)

@register('GetCapabilityDrivesEndpointDescriptorByMoid')
def GetCapabilityDrivesEndpointDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityDrivesEndpointDescriptorByMoid(body=body, **kwargs)

@register('GetCapabilityEquipmentPhysicalDefList')
def GetCapabilityEquipmentPhysicalDefList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityEquipmentPhysicalDefList(body=body, **kwargs)

@register('GetCapabilityEquipmentPhysicalDefByMoid')
def GetCapabilityEquipmentPhysicalDefByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityEquipmentPhysicalDefByMoid(body=body, **kwargs)

@register('GetCapabilityEquipmentSlotArrayList')
def GetCapabilityEquipmentSlotArrayList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityEquipmentSlotArrayList(body=body, **kwargs)

@register('GetCapabilityEquipmentSlotArrayByMoid')
def GetCapabilityEquipmentSlotArrayByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityEquipmentSlotArrayByMoid(body=body, **kwargs)

@register('GetCapabilityFanModuleDescriptorList')
def GetCapabilityFanModuleDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityFanModuleDescriptorList(body=body, **kwargs)

@register('GetCapabilityFanModuleDescriptorByMoid')
def GetCapabilityFanModuleDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityFanModuleDescriptorByMoid(body=body, **kwargs)

@register('GetCapabilityFanModuleManufacturingDefList')
def GetCapabilityFanModuleManufacturingDefList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityFanModuleManufacturingDefList(body=body, **kwargs)

@register('GetCapabilityFanModuleManufacturingDefByMoid')
def GetCapabilityFanModuleManufacturingDefByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityFanModuleManufacturingDefByMoid(body=body, **kwargs)

@register('GetCapabilityFexCapabilityDefList')
def GetCapabilityFexCapabilityDefList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityFexCapabilityDefList(body=body, **kwargs)

@register('GetCapabilityFexCapabilityDefByMoid')
def GetCapabilityFexCapabilityDefByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityFexCapabilityDefByMoid(body=body, **kwargs)

@register('GetCapabilityFexDescriptorList')
def GetCapabilityFexDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityFexDescriptorList(body=body, **kwargs)

@register('GetCapabilityFexDescriptorByMoid')
def GetCapabilityFexDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityFexDescriptorByMoid(body=body, **kwargs)

@register('GetCapabilityFexManufacturingDefList')
def GetCapabilityFexManufacturingDefList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityFexManufacturingDefList(body=body, **kwargs)

@register('GetCapabilityFexManufacturingDefByMoid')
def GetCapabilityFexManufacturingDefByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityFexManufacturingDefByMoid(body=body, **kwargs)

@register('GetCapabilityFexSupportMetaList')
def GetCapabilityFexSupportMetaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityFexSupportMetaList(body=body, **kwargs)

@register('GetCapabilityFexSupportMetaByMoid')
def GetCapabilityFexSupportMetaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityFexSupportMetaByMoid(body=body, **kwargs)

@register('GetCapabilityGpuEndpointDescriptorList')
def GetCapabilityGpuEndpointDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityGpuEndpointDescriptorList(body=body, **kwargs)

@register('GetCapabilityGpuEndpointDescriptorByMoid')
def GetCapabilityGpuEndpointDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityGpuEndpointDescriptorByMoid(body=body, **kwargs)

@register('GetCapabilityHsuIsoFileSupportMetaList')
def GetCapabilityHsuIsoFileSupportMetaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityHsuIsoFileSupportMetaList(body=body, **kwargs)

@register('GetCapabilityHsuIsoFileSupportMetaByMoid')
def GetCapabilityHsuIsoFileSupportMetaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityHsuIsoFileSupportMetaByMoid(body=body, **kwargs)

@register('GetCapabilityIoCardCapabilityDefList')
def GetCapabilityIoCardCapabilityDefList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityIoCardCapabilityDefList(body=body, **kwargs)

@register('GetCapabilityIoCardCapabilityDefByMoid')
def GetCapabilityIoCardCapabilityDefByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityIoCardCapabilityDefByMoid(body=body, **kwargs)

@register('GetCapabilityIoCardDescriptorList')
def GetCapabilityIoCardDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityIoCardDescriptorList(body=body, **kwargs)

@register('GetCapabilityIoCardDescriptorByMoid')
def GetCapabilityIoCardDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityIoCardDescriptorByMoid(body=body, **kwargs)

@register('GetCapabilityIoCardManufacturingDefList')
def GetCapabilityIoCardManufacturingDefList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityIoCardManufacturingDefList(body=body, **kwargs)

@register('GetCapabilityIoCardManufacturingDefByMoid')
def GetCapabilityIoCardManufacturingDefByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityIoCardManufacturingDefByMoid(body=body, **kwargs)

@register('GetCapabilityIomUpgradeSupportMetaList')
def GetCapabilityIomUpgradeSupportMetaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityIomUpgradeSupportMetaList(body=body, **kwargs)

@register('GetCapabilityIomUpgradeSupportMetaByMoid')
def GetCapabilityIomUpgradeSupportMetaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityIomUpgradeSupportMetaByMoid(body=body, **kwargs)

@register('GetCapabilityPortGroupAggregationDefList')
def GetCapabilityPortGroupAggregationDefList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityPortGroupAggregationDefList(body=body, **kwargs)

@register('GetCapabilityPortGroupAggregationDefByMoid')
def GetCapabilityPortGroupAggregationDefByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityPortGroupAggregationDefByMoid(body=body, **kwargs)

@register('GetCapabilityProcessorUnitUpdateConstraintMetaList')
def GetCapabilityProcessorUnitUpdateConstraintMetaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityProcessorUnitUpdateConstraintMetaList(body=body, **kwargs)

@register('GetCapabilityProcessorUnitUpdateConstraintMetaByMoid')
def GetCapabilityProcessorUnitUpdateConstraintMetaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityProcessorUnitUpdateConstraintMetaByMoid(body=body, **kwargs)

@register('GetCapabilityPsuDescriptorList')
def GetCapabilityPsuDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityPsuDescriptorList(body=body, **kwargs)

@register('GetCapabilityPsuDescriptorByMoid')
def GetCapabilityPsuDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityPsuDescriptorByMoid(body=body, **kwargs)

@register('GetCapabilityPsuManufacturingDefList')
def GetCapabilityPsuManufacturingDefList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityPsuManufacturingDefList(body=body, **kwargs)

@register('GetCapabilityPsuManufacturingDefByMoid')
def GetCapabilityPsuManufacturingDefByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityPsuManufacturingDefByMoid(body=body, **kwargs)

@register('GetCapabilityServerActionsMetaList')
def GetCapabilityServerActionsMetaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityServerActionsMetaList(body=body, **kwargs)

@register('GetCapabilityServerActionsMetaByMoid')
def GetCapabilityServerActionsMetaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityServerActionsMetaByMoid(body=body, **kwargs)

@register('GetCapabilityServerDescriptorList')
def GetCapabilityServerDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityServerDescriptorList(body=body, **kwargs)

@register('GetCapabilityServerDescriptorByMoid')
def GetCapabilityServerDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityServerDescriptorByMoid(body=body, **kwargs)

@register('GetCapabilityServerModelsCapabilityDefList')
def GetCapabilityServerModelsCapabilityDefList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityServerModelsCapabilityDefList(body=body, **kwargs)

@register('GetCapabilityServerModelsCapabilityDefByMoid')
def GetCapabilityServerModelsCapabilityDefByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityServerModelsCapabilityDefByMoid(body=body, **kwargs)

@register('GetCapabilityServerSchemaDescriptorList')
def GetCapabilityServerSchemaDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityServerSchemaDescriptorList(body=body, **kwargs)

@register('GetCapabilityServerSchemaDescriptorByMoid')
def GetCapabilityServerSchemaDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityServerSchemaDescriptorByMoid(body=body, **kwargs)

@register('GetCapabilityServerUpgradeSupportMetaList')
def GetCapabilityServerUpgradeSupportMetaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityServerUpgradeSupportMetaList(body=body, **kwargs)

@register('GetCapabilityServerUpgradeSupportMetaByMoid')
def GetCapabilityServerUpgradeSupportMetaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityServerUpgradeSupportMetaByMoid(body=body, **kwargs)

@register('GetCapabilitySiocModuleCapabilityDefList')
def GetCapabilitySiocModuleCapabilityDefList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilitySiocModuleCapabilityDefList(body=body, **kwargs)

@register('GetCapabilitySiocModuleCapabilityDefByMoid')
def GetCapabilitySiocModuleCapabilityDefByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilitySiocModuleCapabilityDefByMoid(body=body, **kwargs)

@register('GetCapabilitySiocModuleDescriptorList')
def GetCapabilitySiocModuleDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilitySiocModuleDescriptorList(body=body, **kwargs)

@register('GetCapabilitySiocModuleDescriptorByMoid')
def GetCapabilitySiocModuleDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilitySiocModuleDescriptorByMoid(body=body, **kwargs)

@register('GetCapabilitySiocModuleManufacturingDefList')
def GetCapabilitySiocModuleManufacturingDefList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilitySiocModuleManufacturingDefList(body=body, **kwargs)

@register('GetCapabilitySiocModuleManufacturingDefByMoid')
def GetCapabilitySiocModuleManufacturingDefByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilitySiocModuleManufacturingDefByMoid(body=body, **kwargs)

@register('GetCapabilityStorageControllerUpdateConstraintMetaList')
def GetCapabilityStorageControllerUpdateConstraintMetaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityStorageControllerUpdateConstraintMetaList(body=body, **kwargs)

@register('GetCapabilityStorageControllerUpdateConstraintMetaByMoid')
def GetCapabilityStorageControllerUpdateConstraintMetaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityStorageControllerUpdateConstraintMetaByMoid(body=body, **kwargs)

@register('GetCapabilityStorageControllersMetaDataList')
def GetCapabilityStorageControllersMetaDataList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityStorageControllersMetaDataList(body=body, **kwargs)

@register('GetCapabilityStorageControllersMetaDataByMoid')
def GetCapabilityStorageControllersMetaDataByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityStorageControllersMetaDataByMoid(body=body, **kwargs)

@register('GetCapabilitySwitchCapabilityList')
def GetCapabilitySwitchCapabilityList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilitySwitchCapabilityList(body=body, **kwargs)

@register('GetCapabilitySwitchCapabilityByMoid')
def GetCapabilitySwitchCapabilityByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilitySwitchCapabilityByMoid(body=body, **kwargs)

@register('GetCapabilitySwitchDescriptorList')
def GetCapabilitySwitchDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilitySwitchDescriptorList(body=body, **kwargs)

@register('GetCapabilitySwitchDescriptorByMoid')
def GetCapabilitySwitchDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilitySwitchDescriptorByMoid(body=body, **kwargs)

@register('GetCapabilitySwitchEquipmentInfoList')
def GetCapabilitySwitchEquipmentInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilitySwitchEquipmentInfoList(body=body, **kwargs)

@register('GetCapabilitySwitchEquipmentInfoByMoid')
def GetCapabilitySwitchEquipmentInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilitySwitchEquipmentInfoByMoid(body=body, **kwargs)

@register('GetCapabilitySwitchManufacturingDefList')
def GetCapabilitySwitchManufacturingDefList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilitySwitchManufacturingDefList(body=body, **kwargs)

@register('GetCapabilitySwitchManufacturingDefByMoid')
def GetCapabilitySwitchManufacturingDefByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilitySwitchManufacturingDefByMoid(body=body, **kwargs)

@register('GetCapabilityTemplateCatalogList')
def GetCapabilityTemplateCatalogList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityTemplateCatalogList(body=body, **kwargs)

@register('GetCapabilityTemplateCatalogByMoid')
def GetCapabilityTemplateCatalogByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityTemplateCatalogByMoid(body=body, **kwargs)

@register('GetCapabilityUpdateOrderMetaList')
def GetCapabilityUpdateOrderMetaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityUpdateOrderMetaList(body=body, **kwargs)

@register('GetCapabilityUpdateOrderMetaByMoid')
def GetCapabilityUpdateOrderMetaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityUpdateOrderMetaByMoid(body=body, **kwargs)

@register('GetCapabilityVicDescriptorList')
def GetCapabilityVicDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityVicDescriptorList(body=body, **kwargs)

@register('GetCapabilityVicDescriptorByMoid')
def GetCapabilityVicDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCapabilityVicDescriptorByMoid(body=body, **kwargs)

@register('GetCatalystsdwanConfigGroupList')
def GetCatalystsdwanConfigGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCatalystsdwanConfigGroupList(body=body, **kwargs)

@register('GetCatalystsdwanConfigGroupByMoid')
def GetCatalystsdwanConfigGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCatalystsdwanConfigGroupByMoid(body=body, **kwargs)

@register('GetCatalystsdwanPolicyGroupList')
def GetCatalystsdwanPolicyGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCatalystsdwanPolicyGroupList(body=body, **kwargs)

@register('GetCatalystsdwanPolicyGroupByMoid')
def GetCatalystsdwanPolicyGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCatalystsdwanPolicyGroupByMoid(body=body, **kwargs)

@register('GetCatalystsdwanVedgeDeviceList')
def GetCatalystsdwanVedgeDeviceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCatalystsdwanVedgeDeviceList(body=body, **kwargs)

@register('GetCatalystsdwanVedgeDeviceByMoid')
def GetCatalystsdwanVedgeDeviceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCatalystsdwanVedgeDeviceByMoid(body=body, **kwargs)

@register('GetCertificatemanagementPolicyList')
def GetCertificatemanagementPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCertificatemanagementPolicyList(body=body, **kwargs)

@register('GetCertificatemanagementPolicyByMoid')
def GetCertificatemanagementPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCertificatemanagementPolicyByMoid(body=body, **kwargs)

@register('GetCertificatemanagementPolicyInventoryList')
def GetCertificatemanagementPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCertificatemanagementPolicyInventoryList(body=body, **kwargs)

@register('GetCertificatemanagementPolicyInventoryByMoid')
def GetCertificatemanagementPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCertificatemanagementPolicyInventoryByMoid(body=body, **kwargs)

@register('GetChangelogItemList')
def GetChangelogItemList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetChangelogItemList(body=body, **kwargs)

@register('GetChangelogItemByMoid')
def GetChangelogItemByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetChangelogItemByMoid(body=body, **kwargs)

@register('GetChassisConfigChangeDetailList')
def GetChassisConfigChangeDetailList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetChassisConfigChangeDetailList(body=body, **kwargs)

@register('GetChassisConfigChangeDetailByMoid')
def GetChassisConfigChangeDetailByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetChassisConfigChangeDetailByMoid(body=body, **kwargs)

@register('GetChassisConfigImportList')
def GetChassisConfigImportList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetChassisConfigImportList(body=body, **kwargs)

@register('GetChassisConfigImportByMoid')
def GetChassisConfigImportByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetChassisConfigImportByMoid(body=body, **kwargs)

@register('GetChassisConfigResultList')
def GetChassisConfigResultList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetChassisConfigResultList(body=body, **kwargs)

@register('GetChassisConfigResultByMoid')
def GetChassisConfigResultByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetChassisConfigResultByMoid(body=body, **kwargs)

@register('GetChassisConfigResultEntryList')
def GetChassisConfigResultEntryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetChassisConfigResultEntryList(body=body, **kwargs)

@register('GetChassisConfigResultEntryByMoid')
def GetChassisConfigResultEntryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetChassisConfigResultEntryByMoid(body=body, **kwargs)

@register('GetChassisIomProfileList')
def GetChassisIomProfileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetChassisIomProfileList(body=body, **kwargs)

@register('GetChassisIomProfileByMoid')
def GetChassisIomProfileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetChassisIomProfileByMoid(body=body, **kwargs)

@register('GetChassisProfileList')
def GetChassisProfileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetChassisProfileList(body=body, **kwargs)

@register('GetChassisProfileByMoid')
def GetChassisProfileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetChassisProfileByMoid(body=body, **kwargs)

@register('GetChassisProfileTemplateList')
def GetChassisProfileTemplateList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetChassisProfileTemplateList(body=body, **kwargs)

@register('GetChassisProfileTemplateByMoid')
def GetChassisProfileTemplateByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetChassisProfileTemplateByMoid(body=body, **kwargs)

@register('GetCloudTfcAgentpoolList')
def GetCloudTfcAgentpoolList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCloudTfcAgentpoolList(body=body, **kwargs)

@register('GetCloudTfcAgentpoolByMoid')
def GetCloudTfcAgentpoolByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCloudTfcAgentpoolByMoid(body=body, **kwargs)

@register('GetCloudTfcOrganizationList')
def GetCloudTfcOrganizationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCloudTfcOrganizationList(body=body, **kwargs)

@register('GetCloudTfcOrganizationByMoid')
def GetCloudTfcOrganizationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCloudTfcOrganizationByMoid(body=body, **kwargs)

@register('GetCloudTfcWorkspaceList')
def GetCloudTfcWorkspaceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCloudTfcWorkspaceList(body=body, **kwargs)

@register('GetCloudTfcWorkspaceByMoid')
def GetCloudTfcWorkspaceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCloudTfcWorkspaceByMoid(body=body, **kwargs)

@register('GetCommHttpProxyPolicyList')
def GetCommHttpProxyPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCommHttpProxyPolicyList(body=body, **kwargs)

@register('GetCommHttpProxyPolicyByMoid')
def GetCommHttpProxyPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCommHttpProxyPolicyByMoid(body=body, **kwargs)

@register('GetComputeBladeList')
def GetComputeBladeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeBladeList(body=body, **kwargs)

@register('GetComputeBladeByMoid')
def GetComputeBladeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeBladeByMoid(body=body, **kwargs)

@register('GetComputeBladeIdentityList')
def GetComputeBladeIdentityList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeBladeIdentityList(body=body, **kwargs)

@register('GetComputeBladeIdentityByMoid')
def GetComputeBladeIdentityByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeBladeIdentityByMoid(body=body, **kwargs)

@register('GetComputeBoardList')
def GetComputeBoardList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeBoardList(body=body, **kwargs)

@register('GetComputeBoardByMoid')
def GetComputeBoardByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeBoardByMoid(body=body, **kwargs)

@register('GetComputeDownloadStatusList')
def GetComputeDownloadStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeDownloadStatusList(body=body, **kwargs)

@register('GetComputeDownloadStatusByMoid')
def GetComputeDownloadStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeDownloadStatusByMoid(body=body, **kwargs)

@register('GetComputeHostUtilityOperationList')
def GetComputeHostUtilityOperationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeHostUtilityOperationList(body=body, **kwargs)

@register('GetComputeHostUtilityOperationByMoid')
def GetComputeHostUtilityOperationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeHostUtilityOperationByMoid(body=body, **kwargs)

@register('GetComputeMappingList')
def GetComputeMappingList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeMappingList(body=body, **kwargs)

@register('GetComputeMappingByMoid')
def GetComputeMappingByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeMappingByMoid(body=body, **kwargs)

@register('GetComputePersonalityList')
def GetComputePersonalityList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputePersonalityList(body=body, **kwargs)

@register('GetComputePersonalityByMoid')
def GetComputePersonalityByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputePersonalityByMoid(body=body, **kwargs)

@register('GetComputePhysicalSummaryList')
def GetComputePhysicalSummaryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputePhysicalSummaryList(body=body, **kwargs)

@register('GetComputePhysicalSummaryByMoid')
def GetComputePhysicalSummaryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputePhysicalSummaryByMoid(body=body, **kwargs)

@register('GetComputeRackUnitList')
def GetComputeRackUnitList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeRackUnitList(body=body, **kwargs)

@register('GetComputeRackUnitByMoid')
def GetComputeRackUnitByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeRackUnitByMoid(body=body, **kwargs)

@register('GetComputeRackUnitIdentityList')
def GetComputeRackUnitIdentityList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeRackUnitIdentityList(body=body, **kwargs)

@register('GetComputeRackUnitIdentityByMoid')
def GetComputeRackUnitIdentityByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeRackUnitIdentityByMoid(body=body, **kwargs)

@register('GetComputeScrubPolicyList')
def GetComputeScrubPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeScrubPolicyList(body=body, **kwargs)

@register('GetComputeScrubPolicyByMoid')
def GetComputeScrubPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeScrubPolicyByMoid(body=body, **kwargs)

@register('GetComputeServerIdPoolList')
def GetComputeServerIdPoolList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeServerIdPoolList(body=body, **kwargs)

@register('GetComputeServerIdPoolByMoid')
def GetComputeServerIdPoolByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeServerIdPoolByMoid(body=body, **kwargs)

@register('GetComputeServerPowerPolicyList')
def GetComputeServerPowerPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeServerPowerPolicyList(body=body, **kwargs)

@register('GetComputeServerPowerPolicyByMoid')
def GetComputeServerPowerPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeServerPowerPolicyByMoid(body=body, **kwargs)

@register('GetComputeServerSettingList')
def GetComputeServerSettingList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeServerSettingList(body=body, **kwargs)

@register('GetComputeServerSettingByMoid')
def GetComputeServerSettingByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeServerSettingByMoid(body=body, **kwargs)

@register('GetComputeVmediaList')
def GetComputeVmediaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeVmediaList(body=body, **kwargs)

@register('GetComputeVmediaByMoid')
def GetComputeVmediaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetComputeVmediaByMoid(body=body, **kwargs)

@register('GetCondAlarmList')
def GetCondAlarmList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCondAlarmList(body=body, **kwargs)

@register('GetCondAlarmByMoid')
def GetCondAlarmByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCondAlarmByMoid(body=body, **kwargs)

@register('GetCondAlarmAggregationList')
def GetCondAlarmAggregationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCondAlarmAggregationList(body=body, **kwargs)

@register('GetCondAlarmAggregationByMoid')
def GetCondAlarmAggregationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCondAlarmAggregationByMoid(body=body, **kwargs)

@register('GetCondAlarmClassificationList')
def GetCondAlarmClassificationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCondAlarmClassificationList(body=body, **kwargs)

@register('GetCondAlarmClassificationByMoid')
def GetCondAlarmClassificationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCondAlarmClassificationByMoid(body=body, **kwargs)

@register('GetCondAlarmDefinitionList')
def GetCondAlarmDefinitionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCondAlarmDefinitionList(body=body, **kwargs)

@register('GetCondAlarmDefinitionByMoid')
def GetCondAlarmDefinitionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCondAlarmDefinitionByMoid(body=body, **kwargs)

@register('GetCondAlarmSuppressionList')
def GetCondAlarmSuppressionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCondAlarmSuppressionList(body=body, **kwargs)

@register('GetCondAlarmSuppressionByMoid')
def GetCondAlarmSuppressionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCondAlarmSuppressionByMoid(body=body, **kwargs)

@register('GetCondHclStatusList')
def GetCondHclStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCondHclStatusList(body=body, **kwargs)

@register('GetCondHclStatusByMoid')
def GetCondHclStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCondHclStatusByMoid(body=body, **kwargs)

@register('GetCondHclStatusDetailList')
def GetCondHclStatusDetailList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCondHclStatusDetailList(body=body, **kwargs)

@register('GetCondHclStatusDetailByMoid')
def GetCondHclStatusDetailByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCondHclStatusDetailByMoid(body=body, **kwargs)

@register('GetCondHclStatusJobList')
def GetCondHclStatusJobList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCondHclStatusJobList(body=body, **kwargs)

@register('GetCondHclStatusJobByMoid')
def GetCondHclStatusJobByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCondHclStatusJobByMoid(body=body, **kwargs)

@register('GetConnectorpackConnectorPackUpgradeList')
def GetConnectorpackConnectorPackUpgradeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetConnectorpackConnectorPackUpgradeList(body=body, **kwargs)

@register('GetConnectorpackConnectorPackUpgradeByMoid')
def GetConnectorpackConnectorPackUpgradeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetConnectorpackConnectorPackUpgradeByMoid(body=body, **kwargs)

@register('GetConnectorpackUpgradeImpactList')
def GetConnectorpackUpgradeImpactList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetConnectorpackUpgradeImpactList(body=body, **kwargs)

@register('GetConnectorpackUpgradeImpactByMoid')
def GetConnectorpackUpgradeImpactByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetConnectorpackUpgradeImpactByMoid(body=body, **kwargs)

@register('GetConsoleConsoleConfigList')
def GetConsoleConsoleConfigList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetConsoleConsoleConfigList(body=body, **kwargs)

@register('GetConsoleConsoleConfigByMoid')
def GetConsoleConsoleConfigByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetConsoleConsoleConfigByMoid(body=body, **kwargs)

@register('GetConvergedinfraAdapterComplianceDetailsList')
def GetConvergedinfraAdapterComplianceDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetConvergedinfraAdapterComplianceDetailsList(body=body, **kwargs)

@register('GetConvergedinfraAdapterComplianceDetailsByMoid')
def GetConvergedinfraAdapterComplianceDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetConvergedinfraAdapterComplianceDetailsByMoid(body=body, **kwargs)

@register('GetConvergedinfraPodList')
def GetConvergedinfraPodList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetConvergedinfraPodList(body=body, **kwargs)

@register('GetConvergedinfraPodByMoid')
def GetConvergedinfraPodByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetConvergedinfraPodByMoid(body=body, **kwargs)

@register('GetConvergedinfraPodComplianceInfoList')
def GetConvergedinfraPodComplianceInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetConvergedinfraPodComplianceInfoList(body=body, **kwargs)

@register('GetConvergedinfraPodComplianceInfoByMoid')
def GetConvergedinfraPodComplianceInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetConvergedinfraPodComplianceInfoByMoid(body=body, **kwargs)

@register('GetConvergedinfraServerComplianceDetailsList')
def GetConvergedinfraServerComplianceDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetConvergedinfraServerComplianceDetailsList(body=body, **kwargs)

@register('GetConvergedinfraServerComplianceDetailsByMoid')
def GetConvergedinfraServerComplianceDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetConvergedinfraServerComplianceDetailsByMoid(body=body, **kwargs)

@register('GetConvergedinfraStorageComplianceDetailsList')
def GetConvergedinfraStorageComplianceDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetConvergedinfraStorageComplianceDetailsList(body=body, **kwargs)

@register('GetConvergedinfraStorageComplianceDetailsByMoid')
def GetConvergedinfraStorageComplianceDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetConvergedinfraStorageComplianceDetailsByMoid(body=body, **kwargs)

@register('GetConvergedinfraSwitchComplianceDetailsList')
def GetConvergedinfraSwitchComplianceDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetConvergedinfraSwitchComplianceDetailsList(body=body, **kwargs)

@register('GetConvergedinfraSwitchComplianceDetailsByMoid')
def GetConvergedinfraSwitchComplianceDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetConvergedinfraSwitchComplianceDetailsByMoid(body=body, **kwargs)

@register('GetCrdCustomResourceList')
def GetCrdCustomResourceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCrdCustomResourceList(body=body, **kwargs)

@register('GetCrdCustomResourceByMoid')
def GetCrdCustomResourceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetCrdCustomResourceByMoid(body=body, **kwargs)

@register('GetDeviceconnectorPolicyList')
def GetDeviceconnectorPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDeviceconnectorPolicyList(body=body, **kwargs)

@register('GetDeviceconnectorPolicyByMoid')
def GetDeviceconnectorPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDeviceconnectorPolicyByMoid(body=body, **kwargs)

@register('GetDnacDeviceList')
def GetDnacDeviceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDnacDeviceList(body=body, **kwargs)

@register('GetDnacDeviceByMoid')
def GetDnacDeviceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDnacDeviceByMoid(body=body, **kwargs)

@register('GetDnacDeviceInterfaceList')
def GetDnacDeviceInterfaceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDnacDeviceInterfaceList(body=body, **kwargs)

@register('GetDnacDeviceInterfaceByMoid')
def GetDnacDeviceInterfaceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDnacDeviceInterfaceByMoid(body=body, **kwargs)

@register('GetDnacExternalBorderNodeList')
def GetDnacExternalBorderNodeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDnacExternalBorderNodeList(body=body, **kwargs)

@register('GetDnacExternalBorderNodeByMoid')
def GetDnacExternalBorderNodeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDnacExternalBorderNodeByMoid(body=body, **kwargs)

@register('GetDnacExternalBorderNodeInterfaceList')
def GetDnacExternalBorderNodeInterfaceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDnacExternalBorderNodeInterfaceList(body=body, **kwargs)

@register('GetDnacExternalBorderNodeInterfaceByMoid')
def GetDnacExternalBorderNodeInterfaceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDnacExternalBorderNodeInterfaceByMoid(body=body, **kwargs)

@register('GetDnacFabricSiteList')
def GetDnacFabricSiteList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDnacFabricSiteList(body=body, **kwargs)

@register('GetDnacFabricSiteByMoid')
def GetDnacFabricSiteByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDnacFabricSiteByMoid(body=body, **kwargs)

@register('GetDnacSiteList')
def GetDnacSiteList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDnacSiteList(body=body, **kwargs)

@register('GetDnacSiteByMoid')
def GetDnacSiteByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDnacSiteByMoid(body=body, **kwargs)

@register('GetDnacSiteIpPoolList')
def GetDnacSiteIpPoolList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDnacSiteIpPoolList(body=body, **kwargs)

@register('GetDnacSiteIpPoolByMoid')
def GetDnacSiteIpPoolByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDnacSiteIpPoolByMoid(body=body, **kwargs)

@register('GetDnacTemplateList')
def GetDnacTemplateList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDnacTemplateList(body=body, **kwargs)

@register('GetDnacTemplateByMoid')
def GetDnacTemplateByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDnacTemplateByMoid(body=body, **kwargs)

@register('GetDnacTransitList')
def GetDnacTransitList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDnacTransitList(body=body, **kwargs)

@register('GetDnacTransitByMoid')
def GetDnacTransitByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDnacTransitByMoid(body=body, **kwargs)

@register('GetDnacVirtualNetworkFabricSiteList')
def GetDnacVirtualNetworkFabricSiteList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDnacVirtualNetworkFabricSiteList(body=body, **kwargs)

@register('GetDnacVirtualNetworkFabricSiteByMoid')
def GetDnacVirtualNetworkFabricSiteByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetDnacVirtualNetworkFabricSiteByMoid(body=body, **kwargs)

@register('GetEquipmentChassisList')
def GetEquipmentChassisList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentChassisList(body=body, **kwargs)

@register('GetEquipmentChassisByMoid')
def GetEquipmentChassisByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentChassisByMoid(body=body, **kwargs)

@register('GetEquipmentChassisIdPoolList')
def GetEquipmentChassisIdPoolList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentChassisIdPoolList(body=body, **kwargs)

@register('GetEquipmentChassisIdPoolByMoid')
def GetEquipmentChassisIdPoolByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentChassisIdPoolByMoid(body=body, **kwargs)

@register('GetEquipmentChassisIdentityList')
def GetEquipmentChassisIdentityList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentChassisIdentityList(body=body, **kwargs)

@register('GetEquipmentChassisIdentityByMoid')
def GetEquipmentChassisIdentityByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentChassisIdentityByMoid(body=body, **kwargs)

@register('GetEquipmentChassisOperationList')
def GetEquipmentChassisOperationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentChassisOperationList(body=body, **kwargs)

@register('GetEquipmentChassisOperationByMoid')
def GetEquipmentChassisOperationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentChassisOperationByMoid(body=body, **kwargs)

@register('GetEquipmentDeviceSummaryList')
def GetEquipmentDeviceSummaryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentDeviceSummaryList(body=body, **kwargs)

@register('GetEquipmentDeviceSummaryByMoid')
def GetEquipmentDeviceSummaryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentDeviceSummaryByMoid(body=body, **kwargs)

@register('GetEquipmentEnclosureElementList')
def GetEquipmentEnclosureElementList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentEnclosureElementList(body=body, **kwargs)

@register('GetEquipmentEnclosureElementByMoid')
def GetEquipmentEnclosureElementByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentEnclosureElementByMoid(body=body, **kwargs)

@register('GetEquipmentEndPointLogList')
def GetEquipmentEndPointLogList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentEndPointLogList(body=body, **kwargs)

@register('GetEquipmentEndPointLogByMoid')
def GetEquipmentEndPointLogByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentEndPointLogByMoid(body=body, **kwargs)

@register('GetEquipmentExpanderModuleList')
def GetEquipmentExpanderModuleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentExpanderModuleList(body=body, **kwargs)

@register('GetEquipmentExpanderModuleByMoid')
def GetEquipmentExpanderModuleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentExpanderModuleByMoid(body=body, **kwargs)

@register('GetEquipmentFanList')
def GetEquipmentFanList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentFanList(body=body, **kwargs)

@register('GetEquipmentFanByMoid')
def GetEquipmentFanByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentFanByMoid(body=body, **kwargs)

@register('GetEquipmentFanControlList')
def GetEquipmentFanControlList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentFanControlList(body=body, **kwargs)

@register('GetEquipmentFanControlByMoid')
def GetEquipmentFanControlByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentFanControlByMoid(body=body, **kwargs)

@register('GetEquipmentFanModuleList')
def GetEquipmentFanModuleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentFanModuleList(body=body, **kwargs)

@register('GetEquipmentFanModuleByMoid')
def GetEquipmentFanModuleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentFanModuleByMoid(body=body, **kwargs)

@register('GetEquipmentFexList')
def GetEquipmentFexList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentFexList(body=body, **kwargs)

@register('GetEquipmentFexByMoid')
def GetEquipmentFexByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentFexByMoid(body=body, **kwargs)

@register('GetEquipmentFexIdentityList')
def GetEquipmentFexIdentityList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentFexIdentityList(body=body, **kwargs)

@register('GetEquipmentFexIdentityByMoid')
def GetEquipmentFexIdentityByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentFexIdentityByMoid(body=body, **kwargs)

@register('GetEquipmentFexOperationList')
def GetEquipmentFexOperationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentFexOperationList(body=body, **kwargs)

@register('GetEquipmentFexOperationByMoid')
def GetEquipmentFexOperationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentFexOperationByMoid(body=body, **kwargs)

@register('GetEquipmentFruList')
def GetEquipmentFruList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentFruList(body=body, **kwargs)

@register('GetEquipmentFruByMoid')
def GetEquipmentFruByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentFruByMoid(body=body, **kwargs)

@register('GetEquipmentHybridDriveSlotList')
def GetEquipmentHybridDriveSlotList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentHybridDriveSlotList(body=body, **kwargs)

@register('GetEquipmentHybridDriveSlotByMoid')
def GetEquipmentHybridDriveSlotByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentHybridDriveSlotByMoid(body=body, **kwargs)

@register('GetEquipmentIoCardList')
def GetEquipmentIoCardList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentIoCardList(body=body, **kwargs)

@register('GetEquipmentIoCardByMoid')
def GetEquipmentIoCardByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentIoCardByMoid(body=body, **kwargs)

@register('GetEquipmentIoCardOperationList')
def GetEquipmentIoCardOperationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentIoCardOperationList(body=body, **kwargs)

@register('GetEquipmentIoCardOperationByMoid')
def GetEquipmentIoCardOperationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentIoCardOperationByMoid(body=body, **kwargs)

@register('GetEquipmentIoExpanderList')
def GetEquipmentIoExpanderList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentIoExpanderList(body=body, **kwargs)

@register('GetEquipmentIoExpanderByMoid')
def GetEquipmentIoExpanderByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentIoExpanderByMoid(body=body, **kwargs)

@register('GetEquipmentLocatorLedList')
def GetEquipmentLocatorLedList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentLocatorLedList(body=body, **kwargs)

@register('GetEquipmentLocatorLedByMoid')
def GetEquipmentLocatorLedByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentLocatorLedByMoid(body=body, **kwargs)

@register('GetEquipmentLogDownloadList')
def GetEquipmentLogDownloadList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentLogDownloadList(body=body, **kwargs)

@register('GetEquipmentLogDownloadByMoid')
def GetEquipmentLogDownloadByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentLogDownloadByMoid(body=body, **kwargs)

@register('GetEquipmentPsuList')
def GetEquipmentPsuList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentPsuList(body=body, **kwargs)

@register('GetEquipmentPsuByMoid')
def GetEquipmentPsuByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentPsuByMoid(body=body, **kwargs)

@register('GetEquipmentPsuControlList')
def GetEquipmentPsuControlList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentPsuControlList(body=body, **kwargs)

@register('GetEquipmentPsuControlByMoid')
def GetEquipmentPsuControlByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentPsuControlByMoid(body=body, **kwargs)

@register('GetEquipmentRackEnclosureList')
def GetEquipmentRackEnclosureList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentRackEnclosureList(body=body, **kwargs)

@register('GetEquipmentRackEnclosureByMoid')
def GetEquipmentRackEnclosureByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentRackEnclosureByMoid(body=body, **kwargs)

@register('GetEquipmentRackEnclosureSlotList')
def GetEquipmentRackEnclosureSlotList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentRackEnclosureSlotList(body=body, **kwargs)

@register('GetEquipmentRackEnclosureSlotByMoid')
def GetEquipmentRackEnclosureSlotByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentRackEnclosureSlotByMoid(body=body, **kwargs)

@register('GetEquipmentSensorList')
def GetEquipmentSensorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentSensorList(body=body, **kwargs)

@register('GetEquipmentSensorByMoid')
def GetEquipmentSensorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentSensorByMoid(body=body, **kwargs)

@register('GetEquipmentSharedIoModuleList')
def GetEquipmentSharedIoModuleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentSharedIoModuleList(body=body, **kwargs)

@register('GetEquipmentSharedIoModuleByMoid')
def GetEquipmentSharedIoModuleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentSharedIoModuleByMoid(body=body, **kwargs)

@register('GetEquipmentSwitchCardList')
def GetEquipmentSwitchCardList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentSwitchCardList(body=body, **kwargs)

@register('GetEquipmentSwitchCardByMoid')
def GetEquipmentSwitchCardByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentSwitchCardByMoid(body=body, **kwargs)

@register('GetEquipmentSwitchOperationList')
def GetEquipmentSwitchOperationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentSwitchOperationList(body=body, **kwargs)

@register('GetEquipmentSwitchOperationByMoid')
def GetEquipmentSwitchOperationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentSwitchOperationByMoid(body=body, **kwargs)

@register('GetEquipmentSystemIoControllerList')
def GetEquipmentSystemIoControllerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentSystemIoControllerList(body=body, **kwargs)

@register('GetEquipmentSystemIoControllerByMoid')
def GetEquipmentSystemIoControllerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentSystemIoControllerByMoid(body=body, **kwargs)

@register('GetEquipmentTpmList')
def GetEquipmentTpmList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentTpmList(body=body, **kwargs)

@register('GetEquipmentTpmByMoid')
def GetEquipmentTpmByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentTpmByMoid(body=body, **kwargs)

@register('GetEquipmentTransceiverList')
def GetEquipmentTransceiverList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentTransceiverList(body=body, **kwargs)

@register('GetEquipmentTransceiverByMoid')
def GetEquipmentTransceiverByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEquipmentTransceiverByMoid(body=body, **kwargs)

@register('GetEtherHostPortList')
def GetEtherHostPortList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEtherHostPortList(body=body, **kwargs)

@register('GetEtherHostPortByMoid')
def GetEtherHostPortByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEtherHostPortByMoid(body=body, **kwargs)

@register('GetEtherNetworkPortList')
def GetEtherNetworkPortList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEtherNetworkPortList(body=body, **kwargs)

@register('GetEtherNetworkPortByMoid')
def GetEtherNetworkPortByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEtherNetworkPortByMoid(body=body, **kwargs)

@register('GetEtherPhysicalPortList')
def GetEtherPhysicalPortList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEtherPhysicalPortList(body=body, **kwargs)

@register('GetEtherPhysicalPortByMoid')
def GetEtherPhysicalPortByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEtherPhysicalPortByMoid(body=body, **kwargs)

@register('GetEtherPortChannelList')
def GetEtherPortChannelList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEtherPortChannelList(body=body, **kwargs)

@register('GetEtherPortChannelByMoid')
def GetEtherPortChannelByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetEtherPortChannelByMoid(body=body, **kwargs)

@register('GetExternalsiteAuthorizationList')
def GetExternalsiteAuthorizationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetExternalsiteAuthorizationList(body=body, **kwargs)

@register('GetExternalsiteAuthorizationByMoid')
def GetExternalsiteAuthorizationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetExternalsiteAuthorizationByMoid(body=body, **kwargs)

@register('GetFabricAppliancePcRoleList')
def GetFabricAppliancePcRoleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricAppliancePcRoleList(body=body, **kwargs)

@register('GetFabricAppliancePcRoleByMoid')
def GetFabricAppliancePcRoleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricAppliancePcRoleByMoid(body=body, **kwargs)

@register('GetFabricApplianceRoleList')
def GetFabricApplianceRoleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricApplianceRoleList(body=body, **kwargs)

@register('GetFabricApplianceRoleByMoid')
def GetFabricApplianceRoleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricApplianceRoleByMoid(body=body, **kwargs)

@register('GetFabricConfigChangeDetailList')
def GetFabricConfigChangeDetailList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricConfigChangeDetailList(body=body, **kwargs)

@register('GetFabricConfigChangeDetailByMoid')
def GetFabricConfigChangeDetailByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricConfigChangeDetailByMoid(body=body, **kwargs)

@register('GetFabricConfigResultList')
def GetFabricConfigResultList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricConfigResultList(body=body, **kwargs)

@register('GetFabricConfigResultByMoid')
def GetFabricConfigResultByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricConfigResultByMoid(body=body, **kwargs)

@register('GetFabricConfigResultEntryList')
def GetFabricConfigResultEntryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricConfigResultEntryList(body=body, **kwargs)

@register('GetFabricConfigResultEntryByMoid')
def GetFabricConfigResultEntryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricConfigResultEntryByMoid(body=body, **kwargs)

@register('GetFabricElementIdentityList')
def GetFabricElementIdentityList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricElementIdentityList(body=body, **kwargs)

@register('GetFabricElementIdentityByMoid')
def GetFabricElementIdentityByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricElementIdentityByMoid(body=body, **kwargs)

@register('GetFabricEthNetworkControlPolicyList')
def GetFabricEthNetworkControlPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricEthNetworkControlPolicyList(body=body, **kwargs)

@register('GetFabricEthNetworkControlPolicyByMoid')
def GetFabricEthNetworkControlPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricEthNetworkControlPolicyByMoid(body=body, **kwargs)

@register('GetFabricEthNetworkControlPolicyInventoryList')
def GetFabricEthNetworkControlPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricEthNetworkControlPolicyInventoryList(body=body, **kwargs)

@register('GetFabricEthNetworkControlPolicyInventoryByMoid')
def GetFabricEthNetworkControlPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricEthNetworkControlPolicyInventoryByMoid(body=body, **kwargs)

@register('GetFabricEthNetworkGroupPolicyList')
def GetFabricEthNetworkGroupPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricEthNetworkGroupPolicyList(body=body, **kwargs)

@register('GetFabricEthNetworkGroupPolicyByMoid')
def GetFabricEthNetworkGroupPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricEthNetworkGroupPolicyByMoid(body=body, **kwargs)

@register('GetFabricEthNetworkGroupPolicyInventoryList')
def GetFabricEthNetworkGroupPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricEthNetworkGroupPolicyInventoryList(body=body, **kwargs)

@register('GetFabricEthNetworkGroupPolicyInventoryByMoid')
def GetFabricEthNetworkGroupPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricEthNetworkGroupPolicyInventoryByMoid(body=body, **kwargs)

@register('GetFabricEthNetworkPolicyList')
def GetFabricEthNetworkPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricEthNetworkPolicyList(body=body, **kwargs)

@register('GetFabricEthNetworkPolicyByMoid')
def GetFabricEthNetworkPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricEthNetworkPolicyByMoid(body=body, **kwargs)

@register('GetFabricFcNetworkPolicyList')
def GetFabricFcNetworkPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricFcNetworkPolicyList(body=body, **kwargs)

@register('GetFabricFcNetworkPolicyByMoid')
def GetFabricFcNetworkPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricFcNetworkPolicyByMoid(body=body, **kwargs)

@register('GetFabricFcStorageRoleList')
def GetFabricFcStorageRoleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricFcStorageRoleList(body=body, **kwargs)

@register('GetFabricFcStorageRoleByMoid')
def GetFabricFcStorageRoleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricFcStorageRoleByMoid(body=body, **kwargs)

@register('GetFabricFcUplinkPcRoleList')
def GetFabricFcUplinkPcRoleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricFcUplinkPcRoleList(body=body, **kwargs)

@register('GetFabricFcUplinkPcRoleByMoid')
def GetFabricFcUplinkPcRoleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricFcUplinkPcRoleByMoid(body=body, **kwargs)

@register('GetFabricFcUplinkRoleList')
def GetFabricFcUplinkRoleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricFcUplinkRoleList(body=body, **kwargs)

@register('GetFabricFcUplinkRoleByMoid')
def GetFabricFcUplinkRoleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricFcUplinkRoleByMoid(body=body, **kwargs)

@register('GetFabricFcZonePolicyList')
def GetFabricFcZonePolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricFcZonePolicyList(body=body, **kwargs)

@register('GetFabricFcZonePolicyByMoid')
def GetFabricFcZonePolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricFcZonePolicyByMoid(body=body, **kwargs)

@register('GetFabricFcoeUplinkPcRoleList')
def GetFabricFcoeUplinkPcRoleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricFcoeUplinkPcRoleList(body=body, **kwargs)

@register('GetFabricFcoeUplinkPcRoleByMoid')
def GetFabricFcoeUplinkPcRoleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricFcoeUplinkPcRoleByMoid(body=body, **kwargs)

@register('GetFabricFcoeUplinkRoleList')
def GetFabricFcoeUplinkRoleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricFcoeUplinkRoleList(body=body, **kwargs)

@register('GetFabricFcoeUplinkRoleByMoid')
def GetFabricFcoeUplinkRoleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricFcoeUplinkRoleByMoid(body=body, **kwargs)

@register('GetFabricFlowControlPolicyList')
def GetFabricFlowControlPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricFlowControlPolicyList(body=body, **kwargs)

@register('GetFabricFlowControlPolicyByMoid')
def GetFabricFlowControlPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricFlowControlPolicyByMoid(body=body, **kwargs)

@register('GetFabricLanPinGroupList')
def GetFabricLanPinGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricLanPinGroupList(body=body, **kwargs)

@register('GetFabricLanPinGroupByMoid')
def GetFabricLanPinGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricLanPinGroupByMoid(body=body, **kwargs)

@register('GetFabricLinkAggregationPolicyList')
def GetFabricLinkAggregationPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricLinkAggregationPolicyList(body=body, **kwargs)

@register('GetFabricLinkAggregationPolicyByMoid')
def GetFabricLinkAggregationPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricLinkAggregationPolicyByMoid(body=body, **kwargs)

@register('GetFabricLinkControlPolicyList')
def GetFabricLinkControlPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricLinkControlPolicyList(body=body, **kwargs)

@register('GetFabricLinkControlPolicyByMoid')
def GetFabricLinkControlPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricLinkControlPolicyByMoid(body=body, **kwargs)

@register('GetFabricMacSecPolicyList')
def GetFabricMacSecPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricMacSecPolicyList(body=body, **kwargs)

@register('GetFabricMacSecPolicyByMoid')
def GetFabricMacSecPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricMacSecPolicyByMoid(body=body, **kwargs)

@register('GetFabricMulticastPolicyList')
def GetFabricMulticastPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricMulticastPolicyList(body=body, **kwargs)

@register('GetFabricMulticastPolicyByMoid')
def GetFabricMulticastPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricMulticastPolicyByMoid(body=body, **kwargs)

@register('GetFabricPcMemberList')
def GetFabricPcMemberList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricPcMemberList(body=body, **kwargs)

@register('GetFabricPcMemberByMoid')
def GetFabricPcMemberByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricPcMemberByMoid(body=body, **kwargs)

@register('GetFabricPcOperationList')
def GetFabricPcOperationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricPcOperationList(body=body, **kwargs)

@register('GetFabricPcOperationByMoid')
def GetFabricPcOperationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricPcOperationByMoid(body=body, **kwargs)

@register('GetFabricPortModeList')
def GetFabricPortModeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricPortModeList(body=body, **kwargs)

@register('GetFabricPortModeByMoid')
def GetFabricPortModeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricPortModeByMoid(body=body, **kwargs)

@register('GetFabricPortOperationList')
def GetFabricPortOperationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricPortOperationList(body=body, **kwargs)

@register('GetFabricPortOperationByMoid')
def GetFabricPortOperationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricPortOperationByMoid(body=body, **kwargs)

@register('GetFabricPortPolicyList')
def GetFabricPortPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricPortPolicyList(body=body, **kwargs)

@register('GetFabricPortPolicyByMoid')
def GetFabricPortPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricPortPolicyByMoid(body=body, **kwargs)

@register('GetFabricSanPinGroupList')
def GetFabricSanPinGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSanPinGroupList(body=body, **kwargs)

@register('GetFabricSanPinGroupByMoid')
def GetFabricSanPinGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSanPinGroupByMoid(body=body, **kwargs)

@register('GetFabricServerRoleList')
def GetFabricServerRoleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricServerRoleList(body=body, **kwargs)

@register('GetFabricServerRoleByMoid')
def GetFabricServerRoleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricServerRoleByMoid(body=body, **kwargs)

@register('GetFabricSpanDestEthPortList')
def GetFabricSpanDestEthPortList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSpanDestEthPortList(body=body, **kwargs)

@register('GetFabricSpanDestEthPortByMoid')
def GetFabricSpanDestEthPortByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSpanDestEthPortByMoid(body=body, **kwargs)

@register('GetFabricSpanSessionList')
def GetFabricSpanSessionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSpanSessionList(body=body, **kwargs)

@register('GetFabricSpanSessionByMoid')
def GetFabricSpanSessionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSpanSessionByMoid(body=body, **kwargs)

@register('GetFabricSpanSourceEthPortList')
def GetFabricSpanSourceEthPortList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSpanSourceEthPortList(body=body, **kwargs)

@register('GetFabricSpanSourceEthPortByMoid')
def GetFabricSpanSourceEthPortByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSpanSourceEthPortByMoid(body=body, **kwargs)

@register('GetFabricSpanSourceEthPortChannelList')
def GetFabricSpanSourceEthPortChannelList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSpanSourceEthPortChannelList(body=body, **kwargs)

@register('GetFabricSpanSourceEthPortChannelByMoid')
def GetFabricSpanSourceEthPortChannelByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSpanSourceEthPortChannelByMoid(body=body, **kwargs)

@register('GetFabricSpanSourceVlanList')
def GetFabricSpanSourceVlanList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSpanSourceVlanList(body=body, **kwargs)

@register('GetFabricSpanSourceVlanByMoid')
def GetFabricSpanSourceVlanByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSpanSourceVlanByMoid(body=body, **kwargs)

@register('GetFabricSpanSourceVnicEthIfList')
def GetFabricSpanSourceVnicEthIfList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSpanSourceVnicEthIfList(body=body, **kwargs)

@register('GetFabricSpanSourceVnicEthIfByMoid')
def GetFabricSpanSourceVnicEthIfByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSpanSourceVnicEthIfByMoid(body=body, **kwargs)

@register('GetFabricSwitchClusterProfileList')
def GetFabricSwitchClusterProfileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSwitchClusterProfileList(body=body, **kwargs)

@register('GetFabricSwitchClusterProfileByMoid')
def GetFabricSwitchClusterProfileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSwitchClusterProfileByMoid(body=body, **kwargs)

@register('GetFabricSwitchClusterProfileTemplateList')
def GetFabricSwitchClusterProfileTemplateList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSwitchClusterProfileTemplateList(body=body, **kwargs)

@register('GetFabricSwitchClusterProfileTemplateByMoid')
def GetFabricSwitchClusterProfileTemplateByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSwitchClusterProfileTemplateByMoid(body=body, **kwargs)

@register('GetFabricSwitchControlPolicyList')
def GetFabricSwitchControlPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSwitchControlPolicyList(body=body, **kwargs)

@register('GetFabricSwitchControlPolicyByMoid')
def GetFabricSwitchControlPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSwitchControlPolicyByMoid(body=body, **kwargs)

@register('GetFabricSwitchProfileList')
def GetFabricSwitchProfileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSwitchProfileList(body=body, **kwargs)

@register('GetFabricSwitchProfileByMoid')
def GetFabricSwitchProfileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSwitchProfileByMoid(body=body, **kwargs)

@register('GetFabricSwitchProfileTemplateList')
def GetFabricSwitchProfileTemplateList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSwitchProfileTemplateList(body=body, **kwargs)

@register('GetFabricSwitchProfileTemplateByMoid')
def GetFabricSwitchProfileTemplateByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSwitchProfileTemplateByMoid(body=body, **kwargs)

@register('GetFabricSystemQosPolicyList')
def GetFabricSystemQosPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSystemQosPolicyList(body=body, **kwargs)

@register('GetFabricSystemQosPolicyByMoid')
def GetFabricSystemQosPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricSystemQosPolicyByMoid(body=body, **kwargs)

@register('GetFabricUplinkPcRoleList')
def GetFabricUplinkPcRoleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricUplinkPcRoleList(body=body, **kwargs)

@register('GetFabricUplinkPcRoleByMoid')
def GetFabricUplinkPcRoleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricUplinkPcRoleByMoid(body=body, **kwargs)

@register('GetFabricUplinkRoleList')
def GetFabricUplinkRoleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricUplinkRoleList(body=body, **kwargs)

@register('GetFabricUplinkRoleByMoid')
def GetFabricUplinkRoleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricUplinkRoleByMoid(body=body, **kwargs)

@register('GetFabricVlanList')
def GetFabricVlanList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricVlanList(body=body, **kwargs)

@register('GetFabricVlanByMoid')
def GetFabricVlanByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricVlanByMoid(body=body, **kwargs)

@register('GetFabricVlanInventoryList')
def GetFabricVlanInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricVlanInventoryList(body=body, **kwargs)

@register('GetFabricVlanInventoryByMoid')
def GetFabricVlanInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricVlanInventoryByMoid(body=body, **kwargs)

@register('GetFabricVlanSetList')
def GetFabricVlanSetList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricVlanSetList(body=body, **kwargs)

@register('GetFabricVlanSetByMoid')
def GetFabricVlanSetByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricVlanSetByMoid(body=body, **kwargs)

@register('GetFabricVsanList')
def GetFabricVsanList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricVsanList(body=body, **kwargs)

@register('GetFabricVsanByMoid')
def GetFabricVsanByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricVsanByMoid(body=body, **kwargs)

@register('GetFabricVsanInventoryList')
def GetFabricVsanInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricVsanInventoryList(body=body, **kwargs)

@register('GetFabricVsanInventoryByMoid')
def GetFabricVsanInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFabricVsanInventoryByMoid(body=body, **kwargs)

@register('GetFaultInstanceList')
def GetFaultInstanceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFaultInstanceList(body=body, **kwargs)

@register('GetFaultInstanceByMoid')
def GetFaultInstanceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFaultInstanceByMoid(body=body, **kwargs)

@register('GetFcNeighborList')
def GetFcNeighborList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFcNeighborList(body=body, **kwargs)

@register('GetFcNeighborByMoid')
def GetFcNeighborByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFcNeighborByMoid(body=body, **kwargs)

@register('GetFcPhysicalPortList')
def GetFcPhysicalPortList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFcPhysicalPortList(body=body, **kwargs)

@register('GetFcPhysicalPortByMoid')
def GetFcPhysicalPortByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFcPhysicalPortByMoid(body=body, **kwargs)

@register('GetFcPortChannelList')
def GetFcPortChannelList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFcPortChannelList(body=body, **kwargs)

@register('GetFcPortChannelByMoid')
def GetFcPortChannelByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFcPortChannelByMoid(body=body, **kwargs)

@register('GetFcpoolFcBlockList')
def GetFcpoolFcBlockList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFcpoolFcBlockList(body=body, **kwargs)

@register('GetFcpoolFcBlockByMoid')
def GetFcpoolFcBlockByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFcpoolFcBlockByMoid(body=body, **kwargs)

@register('GetFcpoolLeaseList')
def GetFcpoolLeaseList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFcpoolLeaseList(body=body, **kwargs)

@register('GetFcpoolLeaseByMoid')
def GetFcpoolLeaseByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFcpoolLeaseByMoid(body=body, **kwargs)

@register('GetFcpoolPoolList')
def GetFcpoolPoolList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFcpoolPoolList(body=body, **kwargs)

@register('GetFcpoolPoolByMoid')
def GetFcpoolPoolByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFcpoolPoolByMoid(body=body, **kwargs)

@register('GetFcpoolPoolMemberList')
def GetFcpoolPoolMemberList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFcpoolPoolMemberList(body=body, **kwargs)

@register('GetFcpoolPoolMemberByMoid')
def GetFcpoolPoolMemberByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFcpoolPoolMemberByMoid(body=body, **kwargs)

@register('GetFcpoolReservationList')
def GetFcpoolReservationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFcpoolReservationList(body=body, **kwargs)

@register('GetFcpoolReservationByMoid')
def GetFcpoolReservationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFcpoolReservationByMoid(body=body, **kwargs)

@register('GetFcpoolUniverseList')
def GetFcpoolUniverseList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFcpoolUniverseList(body=body, **kwargs)

@register('GetFcpoolUniverseByMoid')
def GetFcpoolUniverseByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFcpoolUniverseByMoid(body=body, **kwargs)

@register('GetFirmwareBiosDescriptorList')
def GetFirmwareBiosDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareBiosDescriptorList(body=body, **kwargs)

@register('GetFirmwareBiosDescriptorByMoid')
def GetFirmwareBiosDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareBiosDescriptorByMoid(body=body, **kwargs)

@register('GetFirmwareBoardControllerDescriptorList')
def GetFirmwareBoardControllerDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareBoardControllerDescriptorList(body=body, **kwargs)

@register('GetFirmwareBoardControllerDescriptorByMoid')
def GetFirmwareBoardControllerDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareBoardControllerDescriptorByMoid(body=body, **kwargs)

@register('GetFirmwareChassisUpgradeList')
def GetFirmwareChassisUpgradeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareChassisUpgradeList(body=body, **kwargs)

@register('GetFirmwareChassisUpgradeByMoid')
def GetFirmwareChassisUpgradeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareChassisUpgradeByMoid(body=body, **kwargs)

@register('GetFirmwareCimcDescriptorList')
def GetFirmwareCimcDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareCimcDescriptorList(body=body, **kwargs)

@register('GetFirmwareCimcDescriptorByMoid')
def GetFirmwareCimcDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareCimcDescriptorByMoid(body=body, **kwargs)

@register('GetFirmwareDimmDescriptorList')
def GetFirmwareDimmDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareDimmDescriptorList(body=body, **kwargs)

@register('GetFirmwareDimmDescriptorByMoid')
def GetFirmwareDimmDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareDimmDescriptorByMoid(body=body, **kwargs)

@register('GetFirmwareDistributableList')
def GetFirmwareDistributableList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareDistributableList(body=body, **kwargs)

@register('GetFirmwareDistributableByMoid')
def GetFirmwareDistributableByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareDistributableByMoid(body=body, **kwargs)

@register('GetFirmwareDistributableMetaList')
def GetFirmwareDistributableMetaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareDistributableMetaList(body=body, **kwargs)

@register('GetFirmwareDistributableMetaByMoid')
def GetFirmwareDistributableMetaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareDistributableMetaByMoid(body=body, **kwargs)

@register('GetFirmwareDriveDescriptorList')
def GetFirmwareDriveDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareDriveDescriptorList(body=body, **kwargs)

@register('GetFirmwareDriveDescriptorByMoid')
def GetFirmwareDriveDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareDriveDescriptorByMoid(body=body, **kwargs)

@register('GetFirmwareDriverDistributableList')
def GetFirmwareDriverDistributableList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareDriverDistributableList(body=body, **kwargs)

@register('GetFirmwareDriverDistributableByMoid')
def GetFirmwareDriverDistributableByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareDriverDistributableByMoid(body=body, **kwargs)

@register('GetFirmwareEulaList')
def GetFirmwareEulaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareEulaList(body=body, **kwargs)

@register('GetFirmwareEulaByMoid')
def GetFirmwareEulaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareEulaByMoid(body=body, **kwargs)

@register('GetFirmwareFirmwareSummaryList')
def GetFirmwareFirmwareSummaryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareFirmwareSummaryList(body=body, **kwargs)

@register('GetFirmwareFirmwareSummaryByMoid')
def GetFirmwareFirmwareSummaryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareFirmwareSummaryByMoid(body=body, **kwargs)

@register('GetFirmwareGpuDescriptorList')
def GetFirmwareGpuDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareGpuDescriptorList(body=body, **kwargs)

@register('GetFirmwareGpuDescriptorByMoid')
def GetFirmwareGpuDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareGpuDescriptorByMoid(body=body, **kwargs)

@register('GetFirmwareHbaDescriptorList')
def GetFirmwareHbaDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareHbaDescriptorList(body=body, **kwargs)

@register('GetFirmwareHbaDescriptorByMoid')
def GetFirmwareHbaDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareHbaDescriptorByMoid(body=body, **kwargs)

@register('GetFirmwareIomDescriptorList')
def GetFirmwareIomDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareIomDescriptorList(body=body, **kwargs)

@register('GetFirmwareIomDescriptorByMoid')
def GetFirmwareIomDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareIomDescriptorByMoid(body=body, **kwargs)

@register('GetFirmwareMswitchDescriptorList')
def GetFirmwareMswitchDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareMswitchDescriptorList(body=body, **kwargs)

@register('GetFirmwareMswitchDescriptorByMoid')
def GetFirmwareMswitchDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareMswitchDescriptorByMoid(body=body, **kwargs)

@register('GetFirmwareNxosDescriptorList')
def GetFirmwareNxosDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareNxosDescriptorList(body=body, **kwargs)

@register('GetFirmwareNxosDescriptorByMoid')
def GetFirmwareNxosDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareNxosDescriptorByMoid(body=body, **kwargs)

@register('GetFirmwarePcieDescriptorList')
def GetFirmwarePcieDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwarePcieDescriptorList(body=body, **kwargs)

@register('GetFirmwarePcieDescriptorByMoid')
def GetFirmwarePcieDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwarePcieDescriptorByMoid(body=body, **kwargs)

@register('GetFirmwarePolicyList')
def GetFirmwarePolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwarePolicyList(body=body, **kwargs)

@register('GetFirmwarePolicyByMoid')
def GetFirmwarePolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwarePolicyByMoid(body=body, **kwargs)

@register('GetFirmwarePsuDescriptorList')
def GetFirmwarePsuDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwarePsuDescriptorList(body=body, **kwargs)

@register('GetFirmwarePsuDescriptorByMoid')
def GetFirmwarePsuDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwarePsuDescriptorByMoid(body=body, **kwargs)

@register('GetFirmwareRunningFirmwareList')
def GetFirmwareRunningFirmwareList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareRunningFirmwareList(body=body, **kwargs)

@register('GetFirmwareRunningFirmwareByMoid')
def GetFirmwareRunningFirmwareByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareRunningFirmwareByMoid(body=body, **kwargs)

@register('GetFirmwareSasExpanderDescriptorList')
def GetFirmwareSasExpanderDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareSasExpanderDescriptorList(body=body, **kwargs)

@register('GetFirmwareSasExpanderDescriptorByMoid')
def GetFirmwareSasExpanderDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareSasExpanderDescriptorByMoid(body=body, **kwargs)

@register('GetFirmwareServerConfigurationUtilityDistributableList')
def GetFirmwareServerConfigurationUtilityDistributableList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareServerConfigurationUtilityDistributableList(body=body, **kwargs)

@register('GetFirmwareServerConfigurationUtilityDistributableByMoid')
def GetFirmwareServerConfigurationUtilityDistributableByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareServerConfigurationUtilityDistributableByMoid(body=body, **kwargs)

@register('GetFirmwareStorageControllerDescriptorList')
def GetFirmwareStorageControllerDescriptorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareStorageControllerDescriptorList(body=body, **kwargs)

@register('GetFirmwareStorageControllerDescriptorByMoid')
def GetFirmwareStorageControllerDescriptorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareStorageControllerDescriptorByMoid(body=body, **kwargs)

@register('GetFirmwareSwitchUpgradeList')
def GetFirmwareSwitchUpgradeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareSwitchUpgradeList(body=body, **kwargs)

@register('GetFirmwareSwitchUpgradeByMoid')
def GetFirmwareSwitchUpgradeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareSwitchUpgradeByMoid(body=body, **kwargs)

@register('GetFirmwareUnsupportedVersionUpgradeList')
def GetFirmwareUnsupportedVersionUpgradeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareUnsupportedVersionUpgradeList(body=body, **kwargs)

@register('GetFirmwareUnsupportedVersionUpgradeByMoid')
def GetFirmwareUnsupportedVersionUpgradeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareUnsupportedVersionUpgradeByMoid(body=body, **kwargs)

@register('GetFirmwareUpgradeList')
def GetFirmwareUpgradeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareUpgradeList(body=body, **kwargs)

@register('GetFirmwareUpgradeByMoid')
def GetFirmwareUpgradeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareUpgradeByMoid(body=body, **kwargs)

@register('GetFirmwareUpgradeImpactStatusList')
def GetFirmwareUpgradeImpactStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareUpgradeImpactStatusList(body=body, **kwargs)

@register('GetFirmwareUpgradeImpactStatusByMoid')
def GetFirmwareUpgradeImpactStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareUpgradeImpactStatusByMoid(body=body, **kwargs)

@register('GetFirmwareUpgradeStatusList')
def GetFirmwareUpgradeStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareUpgradeStatusList(body=body, **kwargs)

@register('GetFirmwareUpgradeStatusByMoid')
def GetFirmwareUpgradeStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFirmwareUpgradeStatusByMoid(body=body, **kwargs)

@register('GetFmcDeviceList')
def GetFmcDeviceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFmcDeviceList(body=body, **kwargs)

@register('GetFmcDeviceByMoid')
def GetFmcDeviceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFmcDeviceByMoid(body=body, **kwargs)

@register('GetFmcDeviceHaPairList')
def GetFmcDeviceHaPairList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFmcDeviceHaPairList(body=body, **kwargs)

@register('GetFmcDeviceHaPairByMoid')
def GetFmcDeviceHaPairByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFmcDeviceHaPairByMoid(body=body, **kwargs)

@register('GetFmcDomainList')
def GetFmcDomainList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFmcDomainList(body=body, **kwargs)

@register('GetFmcDomainByMoid')
def GetFmcDomainByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFmcDomainByMoid(body=body, **kwargs)

@register('GetFmcPhysicalInterfaceList')
def GetFmcPhysicalInterfaceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFmcPhysicalInterfaceList(body=body, **kwargs)

@register('GetFmcPhysicalInterfaceByMoid')
def GetFmcPhysicalInterfaceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFmcPhysicalInterfaceByMoid(body=body, **kwargs)

@register('GetForecastCatalogList')
def GetForecastCatalogList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetForecastCatalogList(body=body, **kwargs)

@register('GetForecastCatalogByMoid')
def GetForecastCatalogByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetForecastCatalogByMoid(body=body, **kwargs)

@register('GetForecastDefinitionList')
def GetForecastDefinitionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetForecastDefinitionList(body=body, **kwargs)

@register('GetForecastDefinitionByMoid')
def GetForecastDefinitionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetForecastDefinitionByMoid(body=body, **kwargs)

@register('GetForecastInstanceList')
def GetForecastInstanceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetForecastInstanceList(body=body, **kwargs)

@register('GetForecastInstanceByMoid')
def GetForecastInstanceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetForecastInstanceByMoid(body=body, **kwargs)

@register('GetFunctionsFunctionList')
def GetFunctionsFunctionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFunctionsFunctionList(body=body, **kwargs)

@register('GetFunctionsFunctionByMoid')
def GetFunctionsFunctionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFunctionsFunctionByMoid(body=body, **kwargs)

@register('GetFunctionsFunctionVersionList')
def GetFunctionsFunctionVersionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFunctionsFunctionVersionList(body=body, **kwargs)

@register('GetFunctionsFunctionVersionByMoid')
def GetFunctionsFunctionVersionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFunctionsFunctionVersionByMoid(body=body, **kwargs)

@register('GetFunctionsRuntimeList')
def GetFunctionsRuntimeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFunctionsRuntimeList(body=body, **kwargs)

@register('GetFunctionsRuntimeByMoid')
def GetFunctionsRuntimeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFunctionsRuntimeByMoid(body=body, **kwargs)

@register('GetFunctionsUploadList')
def GetFunctionsUploadList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFunctionsUploadList(body=body, **kwargs)

@register('GetFunctionsUploadByMoid')
def GetFunctionsUploadByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetFunctionsUploadByMoid(body=body, **kwargs)

@register('GetGraphicsCardList')
def GetGraphicsCardList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetGraphicsCardList(body=body, **kwargs)

@register('GetGraphicsCardByMoid')
def GetGraphicsCardByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetGraphicsCardByMoid(body=body, **kwargs)

@register('GetGraphicsControllerList')
def GetGraphicsControllerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetGraphicsControllerList(body=body, **kwargs)

@register('GetGraphicsControllerByMoid')
def GetGraphicsControllerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetGraphicsControllerByMoid(body=body, **kwargs)

@register('GetHciAlarmList')
def GetHciAlarmList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHciAlarmList(body=body, **kwargs)

@register('GetHciAlarmByMoid')
def GetHciAlarmByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHciAlarmByMoid(body=body, **kwargs)

@register('GetHciClusterList')
def GetHciClusterList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHciClusterList(body=body, **kwargs)

@register('GetHciClusterByMoid')
def GetHciClusterByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHciClusterByMoid(body=body, **kwargs)

@register('GetHciComplianceList')
def GetHciComplianceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHciComplianceList(body=body, **kwargs)

@register('GetHciComplianceByMoid')
def GetHciComplianceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHciComplianceByMoid(body=body, **kwargs)

@register('GetHciDiskList')
def GetHciDiskList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHciDiskList(body=body, **kwargs)

@register('GetHciDiskByMoid')
def GetHciDiskByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHciDiskByMoid(body=body, **kwargs)

@register('GetHciDomainManagerList')
def GetHciDomainManagerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHciDomainManagerList(body=body, **kwargs)

@register('GetHciDomainManagerByMoid')
def GetHciDomainManagerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHciDomainManagerByMoid(body=body, **kwargs)

@register('GetHciEntitlementList')
def GetHciEntitlementList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHciEntitlementList(body=body, **kwargs)

@register('GetHciEntitlementByMoid')
def GetHciEntitlementByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHciEntitlementByMoid(body=body, **kwargs)

@register('GetHciGpuList')
def GetHciGpuList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHciGpuList(body=body, **kwargs)

@register('GetHciGpuByMoid')
def GetHciGpuByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHciGpuByMoid(body=body, **kwargs)

@register('GetHciLicenseList')
def GetHciLicenseList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHciLicenseList(body=body, **kwargs)

@register('GetHciLicenseByMoid')
def GetHciLicenseByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHciLicenseByMoid(body=body, **kwargs)

@register('GetHciNodeList')
def GetHciNodeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHciNodeList(body=body, **kwargs)

@register('GetHciNodeByMoid')
def GetHciNodeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHciNodeByMoid(body=body, **kwargs)

@register('GetHciViolationList')
def GetHciViolationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHciViolationList(body=body, **kwargs)

@register('GetHciViolationByMoid')
def GetHciViolationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHciViolationByMoid(body=body, **kwargs)

@register('GetHclDriverImageList')
def GetHclDriverImageList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHclDriverImageList(body=body, **kwargs)

@register('GetHclDriverImageByMoid')
def GetHclDriverImageByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHclDriverImageByMoid(body=body, **kwargs)

@register('GetHclExemptedCatalogList')
def GetHclExemptedCatalogList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHclExemptedCatalogList(body=body, **kwargs)

@register('GetHclExemptedCatalogByMoid')
def GetHclExemptedCatalogByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHclExemptedCatalogByMoid(body=body, **kwargs)

@register('GetHclHwCatalogInfoList')
def GetHclHwCatalogInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHclHwCatalogInfoList(body=body, **kwargs)

@register('GetHclHwCatalogInfoByMoid')
def GetHclHwCatalogInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHclHwCatalogInfoByMoid(body=body, **kwargs)

@register('GetHclHyperflexSoftwareCompatibilityInfoList')
def GetHclHyperflexSoftwareCompatibilityInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHclHyperflexSoftwareCompatibilityInfoList(body=body, **kwargs)

@register('GetHclHyperflexSoftwareCompatibilityInfoByMoid')
def GetHclHyperflexSoftwareCompatibilityInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHclHyperflexSoftwareCompatibilityInfoByMoid(body=body, **kwargs)

@register('GetHclOperatingSystemList')
def GetHclOperatingSystemList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHclOperatingSystemList(body=body, **kwargs)

@register('GetHclOperatingSystemByMoid')
def GetHclOperatingSystemByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHclOperatingSystemByMoid(body=body, **kwargs)

@register('GetHclOperatingSystemVendorList')
def GetHclOperatingSystemVendorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHclOperatingSystemVendorList(body=body, **kwargs)

@register('GetHclOperatingSystemVendorByMoid')
def GetHclOperatingSystemVendorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHclOperatingSystemVendorByMoid(body=body, **kwargs)

@register('GetHclServerHwCatalogInfoList')
def GetHclServerHwCatalogInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHclServerHwCatalogInfoList(body=body, **kwargs)

@register('GetHclServerHwCatalogInfoByMoid')
def GetHclServerHwCatalogInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHclServerHwCatalogInfoByMoid(body=body, **kwargs)

@register('GetHyperflexAlarmList')
def GetHyperflexAlarmList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexAlarmList(body=body, **kwargs)

@register('GetHyperflexAlarmByMoid')
def GetHyperflexAlarmByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexAlarmByMoid(body=body, **kwargs)

@register('GetHyperflexAppCatalogList')
def GetHyperflexAppCatalogList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexAppCatalogList(body=body, **kwargs)

@register('GetHyperflexAppCatalogByMoid')
def GetHyperflexAppCatalogByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexAppCatalogByMoid(body=body, **kwargs)

@register('GetHyperflexAutoSupportPolicyList')
def GetHyperflexAutoSupportPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexAutoSupportPolicyList(body=body, **kwargs)

@register('GetHyperflexAutoSupportPolicyByMoid')
def GetHyperflexAutoSupportPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexAutoSupportPolicyByMoid(body=body, **kwargs)

@register('GetHyperflexBackupClusterList')
def GetHyperflexBackupClusterList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexBackupClusterList(body=body, **kwargs)

@register('GetHyperflexBackupClusterByMoid')
def GetHyperflexBackupClusterByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexBackupClusterByMoid(body=body, **kwargs)

@register('GetHyperflexCapabilityInfoList')
def GetHyperflexCapabilityInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexCapabilityInfoList(body=body, **kwargs)

@register('GetHyperflexCapabilityInfoByMoid')
def GetHyperflexCapabilityInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexCapabilityInfoByMoid(body=body, **kwargs)

@register('GetHyperflexClusterList')
def GetHyperflexClusterList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexClusterList(body=body, **kwargs)

@register('GetHyperflexClusterByMoid')
def GetHyperflexClusterByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexClusterByMoid(body=body, **kwargs)

@register('GetHyperflexClusterBackupPolicyList')
def GetHyperflexClusterBackupPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexClusterBackupPolicyList(body=body, **kwargs)

@register('GetHyperflexClusterBackupPolicyByMoid')
def GetHyperflexClusterBackupPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexClusterBackupPolicyByMoid(body=body, **kwargs)

@register('GetHyperflexClusterBackupPolicyDeploymentList')
def GetHyperflexClusterBackupPolicyDeploymentList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexClusterBackupPolicyDeploymentList(body=body, **kwargs)

@register('GetHyperflexClusterBackupPolicyDeploymentByMoid')
def GetHyperflexClusterBackupPolicyDeploymentByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexClusterBackupPolicyDeploymentByMoid(body=body, **kwargs)

@register('GetHyperflexClusterBackupPolicyInventoryList')
def GetHyperflexClusterBackupPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexClusterBackupPolicyInventoryList(body=body, **kwargs)

@register('GetHyperflexClusterBackupPolicyInventoryByMoid')
def GetHyperflexClusterBackupPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexClusterBackupPolicyInventoryByMoid(body=body, **kwargs)

@register('GetHyperflexClusterHealthCheckExecutionSnapshotList')
def GetHyperflexClusterHealthCheckExecutionSnapshotList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexClusterHealthCheckExecutionSnapshotList(body=body, **kwargs)

@register('GetHyperflexClusterHealthCheckExecutionSnapshotByMoid')
def GetHyperflexClusterHealthCheckExecutionSnapshotByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexClusterHealthCheckExecutionSnapshotByMoid(body=body, **kwargs)

@register('GetHyperflexClusterNetworkPolicyList')
def GetHyperflexClusterNetworkPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexClusterNetworkPolicyList(body=body, **kwargs)

@register('GetHyperflexClusterNetworkPolicyByMoid')
def GetHyperflexClusterNetworkPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexClusterNetworkPolicyByMoid(body=body, **kwargs)

@register('GetHyperflexClusterProfileList')
def GetHyperflexClusterProfileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexClusterProfileList(body=body, **kwargs)

@register('GetHyperflexClusterProfileByMoid')
def GetHyperflexClusterProfileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexClusterProfileByMoid(body=body, **kwargs)

@register('GetHyperflexClusterReplicationNetworkPolicyList')
def GetHyperflexClusterReplicationNetworkPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexClusterReplicationNetworkPolicyList(body=body, **kwargs)

@register('GetHyperflexClusterReplicationNetworkPolicyByMoid')
def GetHyperflexClusterReplicationNetworkPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexClusterReplicationNetworkPolicyByMoid(body=body, **kwargs)

@register('GetHyperflexClusterReplicationNetworkPolicyDeploymentList')
def GetHyperflexClusterReplicationNetworkPolicyDeploymentList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexClusterReplicationNetworkPolicyDeploymentList(body=body, **kwargs)

@register('GetHyperflexClusterReplicationNetworkPolicyDeploymentByMoid')
def GetHyperflexClusterReplicationNetworkPolicyDeploymentByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexClusterReplicationNetworkPolicyDeploymentByMoid(body=body, **kwargs)

@register('GetHyperflexClusterStoragePolicyList')
def GetHyperflexClusterStoragePolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexClusterStoragePolicyList(body=body, **kwargs)

@register('GetHyperflexClusterStoragePolicyByMoid')
def GetHyperflexClusterStoragePolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexClusterStoragePolicyByMoid(body=body, **kwargs)

@register('GetHyperflexConfigResultList')
def GetHyperflexConfigResultList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexConfigResultList(body=body, **kwargs)

@register('GetHyperflexConfigResultByMoid')
def GetHyperflexConfigResultByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexConfigResultByMoid(body=body, **kwargs)

@register('GetHyperflexConfigResultEntryList')
def GetHyperflexConfigResultEntryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexConfigResultEntryList(body=body, **kwargs)

@register('GetHyperflexConfigResultEntryByMoid')
def GetHyperflexConfigResultEntryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexConfigResultEntryByMoid(body=body, **kwargs)

@register('GetHyperflexDataProtectionPeerList')
def GetHyperflexDataProtectionPeerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexDataProtectionPeerList(body=body, **kwargs)

@register('GetHyperflexDataProtectionPeerByMoid')
def GetHyperflexDataProtectionPeerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexDataProtectionPeerByMoid(body=body, **kwargs)

@register('GetHyperflexDatastoreStatisticList')
def GetHyperflexDatastoreStatisticList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexDatastoreStatisticList(body=body, **kwargs)

@register('GetHyperflexDatastoreStatisticByMoid')
def GetHyperflexDatastoreStatisticByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexDatastoreStatisticByMoid(body=body, **kwargs)

@register('GetHyperflexDevicePackageDownloadStateList')
def GetHyperflexDevicePackageDownloadStateList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexDevicePackageDownloadStateList(body=body, **kwargs)

@register('GetHyperflexDevicePackageDownloadStateByMoid')
def GetHyperflexDevicePackageDownloadStateByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexDevicePackageDownloadStateByMoid(body=body, **kwargs)

@register('GetHyperflexDriveList')
def GetHyperflexDriveList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexDriveList(body=body, **kwargs)

@register('GetHyperflexDriveByMoid')
def GetHyperflexDriveByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexDriveByMoid(body=body, **kwargs)

@register('GetHyperflexEncryptionList')
def GetHyperflexEncryptionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexEncryptionList(body=body, **kwargs)

@register('GetHyperflexEncryptionByMoid')
def GetHyperflexEncryptionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexEncryptionByMoid(body=body, **kwargs)

@register('GetHyperflexExtFcStoragePolicyList')
def GetHyperflexExtFcStoragePolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexExtFcStoragePolicyList(body=body, **kwargs)

@register('GetHyperflexExtFcStoragePolicyByMoid')
def GetHyperflexExtFcStoragePolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexExtFcStoragePolicyByMoid(body=body, **kwargs)

@register('GetHyperflexExtIscsiStoragePolicyList')
def GetHyperflexExtIscsiStoragePolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexExtIscsiStoragePolicyList(body=body, **kwargs)

@register('GetHyperflexExtIscsiStoragePolicyByMoid')
def GetHyperflexExtIscsiStoragePolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexExtIscsiStoragePolicyByMoid(body=body, **kwargs)

@register('GetHyperflexFeatureLimitExternalList')
def GetHyperflexFeatureLimitExternalList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexFeatureLimitExternalList(body=body, **kwargs)

@register('GetHyperflexFeatureLimitExternalByMoid')
def GetHyperflexFeatureLimitExternalByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexFeatureLimitExternalByMoid(body=body, **kwargs)

@register('GetHyperflexFeatureLimitInternalList')
def GetHyperflexFeatureLimitInternalList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexFeatureLimitInternalList(body=body, **kwargs)

@register('GetHyperflexFeatureLimitInternalByMoid')
def GetHyperflexFeatureLimitInternalByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexFeatureLimitInternalByMoid(body=body, **kwargs)

@register('GetHyperflexHealthList')
def GetHyperflexHealthList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexHealthList(body=body, **kwargs)

@register('GetHyperflexHealthByMoid')
def GetHyperflexHealthByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexHealthByMoid(body=body, **kwargs)

@register('GetHyperflexHealthCheckDefinitionList')
def GetHyperflexHealthCheckDefinitionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexHealthCheckDefinitionList(body=body, **kwargs)

@register('GetHyperflexHealthCheckDefinitionByMoid')
def GetHyperflexHealthCheckDefinitionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexHealthCheckDefinitionByMoid(body=body, **kwargs)

@register('GetHyperflexHealthCheckExecutionList')
def GetHyperflexHealthCheckExecutionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexHealthCheckExecutionList(body=body, **kwargs)

@register('GetHyperflexHealthCheckExecutionByMoid')
def GetHyperflexHealthCheckExecutionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexHealthCheckExecutionByMoid(body=body, **kwargs)

@register('GetHyperflexHealthCheckExecutionSnapshotList')
def GetHyperflexHealthCheckExecutionSnapshotList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexHealthCheckExecutionSnapshotList(body=body, **kwargs)

@register('GetHyperflexHealthCheckExecutionSnapshotByMoid')
def GetHyperflexHealthCheckExecutionSnapshotByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexHealthCheckExecutionSnapshotByMoid(body=body, **kwargs)

@register('GetHyperflexHealthCheckPackageChecksumList')
def GetHyperflexHealthCheckPackageChecksumList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexHealthCheckPackageChecksumList(body=body, **kwargs)

@register('GetHyperflexHealthCheckPackageChecksumByMoid')
def GetHyperflexHealthCheckPackageChecksumByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexHealthCheckPackageChecksumByMoid(body=body, **kwargs)

@register('GetHyperflexHealthCheckSchedulePolicyList')
def GetHyperflexHealthCheckSchedulePolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexHealthCheckSchedulePolicyList(body=body, **kwargs)

@register('GetHyperflexHealthCheckSchedulePolicyByMoid')
def GetHyperflexHealthCheckSchedulePolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexHealthCheckSchedulePolicyByMoid(body=body, **kwargs)

@register('GetHyperflexHwCatalogList')
def GetHyperflexHwCatalogList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexHwCatalogList(body=body, **kwargs)

@register('GetHyperflexHwCatalogByMoid')
def GetHyperflexHwCatalogByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexHwCatalogByMoid(body=body, **kwargs)

@register('GetHyperflexHxdpVersionList')
def GetHyperflexHxdpVersionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexHxdpVersionList(body=body, **kwargs)

@register('GetHyperflexHxdpVersionByMoid')
def GetHyperflexHxdpVersionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexHxdpVersionByMoid(body=body, **kwargs)

@register('GetHyperflexHypervisorHostList')
def GetHyperflexHypervisorHostList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexHypervisorHostList(body=body, **kwargs)

@register('GetHyperflexHypervisorHostByMoid')
def GetHyperflexHypervisorHostByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexHypervisorHostByMoid(body=body, **kwargs)

@register('GetHyperflexHypervisorVirtualMachineList')
def GetHyperflexHypervisorVirtualMachineList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexHypervisorVirtualMachineList(body=body, **kwargs)

@register('GetHyperflexHypervisorVirtualMachineByMoid')
def GetHyperflexHypervisorVirtualMachineByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexHypervisorVirtualMachineByMoid(body=body, **kwargs)

@register('GetHyperflexInitiatorGroupList')
def GetHyperflexInitiatorGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexInitiatorGroupList(body=body, **kwargs)

@register('GetHyperflexInitiatorGroupByMoid')
def GetHyperflexInitiatorGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexInitiatorGroupByMoid(body=body, **kwargs)

@register('GetHyperflexIscsiNetworkList')
def GetHyperflexIscsiNetworkList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexIscsiNetworkList(body=body, **kwargs)

@register('GetHyperflexIscsiNetworkByMoid')
def GetHyperflexIscsiNetworkByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexIscsiNetworkByMoid(body=body, **kwargs)

@register('GetHyperflexKeyEncryptionKeyList')
def GetHyperflexKeyEncryptionKeyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexKeyEncryptionKeyList(body=body, **kwargs)

@register('GetHyperflexKeyEncryptionKeyByMoid')
def GetHyperflexKeyEncryptionKeyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexKeyEncryptionKeyByMoid(body=body, **kwargs)

@register('GetHyperflexLicenseList')
def GetHyperflexLicenseList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexLicenseList(body=body, **kwargs)

@register('GetHyperflexLicenseByMoid')
def GetHyperflexLicenseByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexLicenseByMoid(body=body, **kwargs)

@register('GetHyperflexLocalCredentialPolicyList')
def GetHyperflexLocalCredentialPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexLocalCredentialPolicyList(body=body, **kwargs)

@register('GetHyperflexLocalCredentialPolicyByMoid')
def GetHyperflexLocalCredentialPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexLocalCredentialPolicyByMoid(body=body, **kwargs)

@register('GetHyperflexLunList')
def GetHyperflexLunList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexLunList(body=body, **kwargs)

@register('GetHyperflexLunByMoid')
def GetHyperflexLunByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexLunByMoid(body=body, **kwargs)

@register('GetHyperflexNodeList')
def GetHyperflexNodeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexNodeList(body=body, **kwargs)

@register('GetHyperflexNodeByMoid')
def GetHyperflexNodeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexNodeByMoid(body=body, **kwargs)

@register('GetHyperflexNodeConfigPolicyList')
def GetHyperflexNodeConfigPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexNodeConfigPolicyList(body=body, **kwargs)

@register('GetHyperflexNodeConfigPolicyByMoid')
def GetHyperflexNodeConfigPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexNodeConfigPolicyByMoid(body=body, **kwargs)

@register('GetHyperflexNodeProfileList')
def GetHyperflexNodeProfileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexNodeProfileList(body=body, **kwargs)

@register('GetHyperflexNodeProfileByMoid')
def GetHyperflexNodeProfileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexNodeProfileByMoid(body=body, **kwargs)

@register('GetHyperflexProtectedClusterList')
def GetHyperflexProtectedClusterList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexProtectedClusterList(body=body, **kwargs)

@register('GetHyperflexProtectedClusterByMoid')
def GetHyperflexProtectedClusterByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexProtectedClusterByMoid(body=body, **kwargs)

@register('GetHyperflexProxySettingPolicyList')
def GetHyperflexProxySettingPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexProxySettingPolicyList(body=body, **kwargs)

@register('GetHyperflexProxySettingPolicyByMoid')
def GetHyperflexProxySettingPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexProxySettingPolicyByMoid(body=body, **kwargs)

@register('GetHyperflexReduceReSyncList')
def GetHyperflexReduceReSyncList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexReduceReSyncList(body=body, **kwargs)

@register('GetHyperflexReduceReSyncByMoid')
def GetHyperflexReduceReSyncByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexReduceReSyncByMoid(body=body, **kwargs)

@register('GetHyperflexServerFirmwareVersionList')
def GetHyperflexServerFirmwareVersionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexServerFirmwareVersionList(body=body, **kwargs)

@register('GetHyperflexServerFirmwareVersionByMoid')
def GetHyperflexServerFirmwareVersionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexServerFirmwareVersionByMoid(body=body, **kwargs)

@register('GetHyperflexServerFirmwareVersionEntryList')
def GetHyperflexServerFirmwareVersionEntryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexServerFirmwareVersionEntryList(body=body, **kwargs)

@register('GetHyperflexServerFirmwareVersionEntryByMoid')
def GetHyperflexServerFirmwareVersionEntryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexServerFirmwareVersionEntryByMoid(body=body, **kwargs)

@register('GetHyperflexServerModelList')
def GetHyperflexServerModelList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexServerModelList(body=body, **kwargs)

@register('GetHyperflexServerModelByMoid')
def GetHyperflexServerModelByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexServerModelByMoid(body=body, **kwargs)

@register('GetHyperflexServiceAuthTokenList')
def GetHyperflexServiceAuthTokenList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexServiceAuthTokenList(body=body, **kwargs)

@register('GetHyperflexServiceAuthTokenByMoid')
def GetHyperflexServiceAuthTokenByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexServiceAuthTokenByMoid(body=body, **kwargs)

@register('GetHyperflexSoftwareDistributionComponentList')
def GetHyperflexSoftwareDistributionComponentList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexSoftwareDistributionComponentList(body=body, **kwargs)

@register('GetHyperflexSoftwareDistributionComponentByMoid')
def GetHyperflexSoftwareDistributionComponentByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexSoftwareDistributionComponentByMoid(body=body, **kwargs)

@register('GetHyperflexSoftwareDistributionEntryList')
def GetHyperflexSoftwareDistributionEntryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexSoftwareDistributionEntryList(body=body, **kwargs)

@register('GetHyperflexSoftwareDistributionEntryByMoid')
def GetHyperflexSoftwareDistributionEntryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexSoftwareDistributionEntryByMoid(body=body, **kwargs)

@register('GetHyperflexSoftwareDistributionVersionList')
def GetHyperflexSoftwareDistributionVersionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexSoftwareDistributionVersionList(body=body, **kwargs)

@register('GetHyperflexSoftwareDistributionVersionByMoid')
def GetHyperflexSoftwareDistributionVersionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexSoftwareDistributionVersionByMoid(body=body, **kwargs)

@register('GetHyperflexSoftwareVersionPolicyList')
def GetHyperflexSoftwareVersionPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexSoftwareVersionPolicyList(body=body, **kwargs)

@register('GetHyperflexSoftwareVersionPolicyByMoid')
def GetHyperflexSoftwareVersionPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexSoftwareVersionPolicyByMoid(body=body, **kwargs)

@register('GetHyperflexStartReduceReSyncList')
def GetHyperflexStartReduceReSyncList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexStartReduceReSyncList(body=body, **kwargs)

@register('GetHyperflexStartReduceReSyncByMoid')
def GetHyperflexStartReduceReSyncByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexStartReduceReSyncByMoid(body=body, **kwargs)

@register('GetHyperflexStorageContainerList')
def GetHyperflexStorageContainerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexStorageContainerList(body=body, **kwargs)

@register('GetHyperflexStorageContainerByMoid')
def GetHyperflexStorageContainerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexStorageContainerByMoid(body=body, **kwargs)

@register('GetHyperflexSysConfigPolicyList')
def GetHyperflexSysConfigPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexSysConfigPolicyList(body=body, **kwargs)

@register('GetHyperflexSysConfigPolicyByMoid')
def GetHyperflexSysConfigPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexSysConfigPolicyByMoid(body=body, **kwargs)

@register('GetHyperflexTargetList')
def GetHyperflexTargetList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexTargetList(body=body, **kwargs)

@register('GetHyperflexTargetByMoid')
def GetHyperflexTargetByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexTargetByMoid(body=body, **kwargs)

@register('GetHyperflexUcsmConfigPolicyList')
def GetHyperflexUcsmConfigPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexUcsmConfigPolicyList(body=body, **kwargs)

@register('GetHyperflexUcsmConfigPolicyByMoid')
def GetHyperflexUcsmConfigPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexUcsmConfigPolicyByMoid(body=body, **kwargs)

@register('GetHyperflexVcenterConfigPolicyList')
def GetHyperflexVcenterConfigPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexVcenterConfigPolicyList(body=body, **kwargs)

@register('GetHyperflexVcenterConfigPolicyByMoid')
def GetHyperflexVcenterConfigPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexVcenterConfigPolicyByMoid(body=body, **kwargs)

@register('GetHyperflexVmBackupInfoList')
def GetHyperflexVmBackupInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexVmBackupInfoList(body=body, **kwargs)

@register('GetHyperflexVmBackupInfoByMoid')
def GetHyperflexVmBackupInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexVmBackupInfoByMoid(body=body, **kwargs)

@register('GetHyperflexVmImportOperationList')
def GetHyperflexVmImportOperationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexVmImportOperationList(body=body, **kwargs)

@register('GetHyperflexVmImportOperationByMoid')
def GetHyperflexVmImportOperationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexVmImportOperationByMoid(body=body, **kwargs)

@register('GetHyperflexVmRestoreOperationList')
def GetHyperflexVmRestoreOperationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexVmRestoreOperationList(body=body, **kwargs)

@register('GetHyperflexVmRestoreOperationByMoid')
def GetHyperflexVmRestoreOperationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexVmRestoreOperationByMoid(body=body, **kwargs)

@register('GetHyperflexVmSnapshotInfoList')
def GetHyperflexVmSnapshotInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexVmSnapshotInfoList(body=body, **kwargs)

@register('GetHyperflexVmSnapshotInfoByMoid')
def GetHyperflexVmSnapshotInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexVmSnapshotInfoByMoid(body=body, **kwargs)

@register('GetHyperflexVolumeList')
def GetHyperflexVolumeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexVolumeList(body=body, **kwargs)

@register('GetHyperflexVolumeByMoid')
def GetHyperflexVolumeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexVolumeByMoid(body=body, **kwargs)

@register('GetHyperflexWitnessConfigurationList')
def GetHyperflexWitnessConfigurationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexWitnessConfigurationList(body=body, **kwargs)

@register('GetHyperflexWitnessConfigurationByMoid')
def GetHyperflexWitnessConfigurationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetHyperflexWitnessConfigurationByMoid(body=body, **kwargs)

@register('GetIaasConnectorPackList')
def GetIaasConnectorPackList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasConnectorPackList(body=body, **kwargs)

@register('GetIaasConnectorPackByMoid')
def GetIaasConnectorPackByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasConnectorPackByMoid(body=body, **kwargs)

@register('GetIaasCustomTaskInfoList')
def GetIaasCustomTaskInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasCustomTaskInfoList(body=body, **kwargs)

@register('GetIaasCustomTaskInfoByMoid')
def GetIaasCustomTaskInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasCustomTaskInfoByMoid(body=body, **kwargs)

@register('GetIaasDeviceStatusList')
def GetIaasDeviceStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasDeviceStatusList(body=body, **kwargs)

@register('GetIaasDeviceStatusByMoid')
def GetIaasDeviceStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasDeviceStatusByMoid(body=body, **kwargs)

@register('GetIaasDiagnosticMessagesList')
def GetIaasDiagnosticMessagesList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasDiagnosticMessagesList(body=body, **kwargs)

@register('GetIaasDiagnosticMessagesByMoid')
def GetIaasDiagnosticMessagesByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasDiagnosticMessagesByMoid(body=body, **kwargs)

@register('GetIaasLicenseInfoList')
def GetIaasLicenseInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasLicenseInfoList(body=body, **kwargs)

@register('GetIaasLicenseInfoByMoid')
def GetIaasLicenseInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasLicenseInfoByMoid(body=body, **kwargs)

@register('GetIaasMostRunTasksList')
def GetIaasMostRunTasksList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasMostRunTasksList(body=body, **kwargs)

@register('GetIaasMostRunTasksByMoid')
def GetIaasMostRunTasksByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasMostRunTasksByMoid(body=body, **kwargs)

@register('GetIaasServiceRequestList')
def GetIaasServiceRequestList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasServiceRequestList(body=body, **kwargs)

@register('GetIaasServiceRequestByMoid')
def GetIaasServiceRequestByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasServiceRequestByMoid(body=body, **kwargs)

@register('GetIaasSystemTaskInfoList')
def GetIaasSystemTaskInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasSystemTaskInfoList(body=body, **kwargs)

@register('GetIaasSystemTaskInfoByMoid')
def GetIaasSystemTaskInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasSystemTaskInfoByMoid(body=body, **kwargs)

@register('GetIaasUcsdInfoList')
def GetIaasUcsdInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasUcsdInfoList(body=body, **kwargs)

@register('GetIaasUcsdInfoByMoid')
def GetIaasUcsdInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasUcsdInfoByMoid(body=body, **kwargs)

@register('GetIaasUcsdManagedInfraList')
def GetIaasUcsdManagedInfraList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasUcsdManagedInfraList(body=body, **kwargs)

@register('GetIaasUcsdManagedInfraByMoid')
def GetIaasUcsdManagedInfraByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasUcsdManagedInfraByMoid(body=body, **kwargs)

@register('GetIaasUcsdMessagesList')
def GetIaasUcsdMessagesList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasUcsdMessagesList(body=body, **kwargs)

@register('GetIaasUcsdMessagesByMoid')
def GetIaasUcsdMessagesByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIaasUcsdMessagesByMoid(body=body, **kwargs)

@register('GetIamAccountList')
def GetIamAccountList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamAccountList(body=body, **kwargs)

@register('GetIamAccountByMoid')
def GetIamAccountByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamAccountByMoid(body=body, **kwargs)

@register('GetIamAccountExperienceList')
def GetIamAccountExperienceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamAccountExperienceList(body=body, **kwargs)

@register('GetIamAccountExperienceByMoid')
def GetIamAccountExperienceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamAccountExperienceByMoid(body=body, **kwargs)

@register('GetIamApiKeyList')
def GetIamApiKeyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamApiKeyList(body=body, **kwargs)

@register('GetIamApiKeyByMoid')
def GetIamApiKeyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamApiKeyByMoid(body=body, **kwargs)

@register('GetIamAppRegistrationList')
def GetIamAppRegistrationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamAppRegistrationList(body=body, **kwargs)

@register('GetIamAppRegistrationByMoid')
def GetIamAppRegistrationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamAppRegistrationByMoid(body=body, **kwargs)

@register('GetIamBannerMessageList')
def GetIamBannerMessageList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamBannerMessageList(body=body, **kwargs)

@register('GetIamBannerMessageByMoid')
def GetIamBannerMessageByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamBannerMessageByMoid(body=body, **kwargs)

@register('GetIamCertificateList')
def GetIamCertificateList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamCertificateList(body=body, **kwargs)

@register('GetIamCertificateByMoid')
def GetIamCertificateByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamCertificateByMoid(body=body, **kwargs)

@register('GetIamCertificateRequestList')
def GetIamCertificateRequestList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamCertificateRequestList(body=body, **kwargs)

@register('GetIamCertificateRequestByMoid')
def GetIamCertificateRequestByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamCertificateRequestByMoid(body=body, **kwargs)

@register('GetIamDomainGroupList')
def GetIamDomainGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamDomainGroupList(body=body, **kwargs)

@register('GetIamDomainGroupByMoid')
def GetIamDomainGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamDomainGroupByMoid(body=body, **kwargs)

@register('GetIamDomainNameInfoList')
def GetIamDomainNameInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamDomainNameInfoList(body=body, **kwargs)

@register('GetIamDomainNameInfoByMoid')
def GetIamDomainNameInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamDomainNameInfoByMoid(body=body, **kwargs)

@register('GetIamEndPointPrivilegeList')
def GetIamEndPointPrivilegeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamEndPointPrivilegeList(body=body, **kwargs)

@register('GetIamEndPointPrivilegeByMoid')
def GetIamEndPointPrivilegeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamEndPointPrivilegeByMoid(body=body, **kwargs)

@register('GetIamEndPointRoleList')
def GetIamEndPointRoleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamEndPointRoleList(body=body, **kwargs)

@register('GetIamEndPointRoleByMoid')
def GetIamEndPointRoleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamEndPointRoleByMoid(body=body, **kwargs)

@register('GetIamEndPointUserList')
def GetIamEndPointUserList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamEndPointUserList(body=body, **kwargs)

@register('GetIamEndPointUserByMoid')
def GetIamEndPointUserByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamEndPointUserByMoid(body=body, **kwargs)

@register('GetIamEndPointUserInventoryList')
def GetIamEndPointUserInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamEndPointUserInventoryList(body=body, **kwargs)

@register('GetIamEndPointUserInventoryByMoid')
def GetIamEndPointUserInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamEndPointUserInventoryByMoid(body=body, **kwargs)

@register('GetIamEndPointUserPolicyList')
def GetIamEndPointUserPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamEndPointUserPolicyList(body=body, **kwargs)

@register('GetIamEndPointUserPolicyByMoid')
def GetIamEndPointUserPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamEndPointUserPolicyByMoid(body=body, **kwargs)

@register('GetIamEndPointUserPolicyInventoryList')
def GetIamEndPointUserPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamEndPointUserPolicyInventoryList(body=body, **kwargs)

@register('GetIamEndPointUserPolicyInventoryByMoid')
def GetIamEndPointUserPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamEndPointUserPolicyInventoryByMoid(body=body, **kwargs)

@register('GetIamEndPointUserRoleList')
def GetIamEndPointUserRoleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamEndPointUserRoleList(body=body, **kwargs)

@register('GetIamEndPointUserRoleByMoid')
def GetIamEndPointUserRoleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamEndPointUserRoleByMoid(body=body, **kwargs)

@register('GetIamEndPointUserRoleInventoryList')
def GetIamEndPointUserRoleInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamEndPointUserRoleInventoryList(body=body, **kwargs)

@register('GetIamEndPointUserRoleInventoryByMoid')
def GetIamEndPointUserRoleInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamEndPointUserRoleInventoryByMoid(body=body, **kwargs)

@register('GetIamIdpList')
def GetIamIdpList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamIdpList(body=body, **kwargs)

@register('GetIamIdpByMoid')
def GetIamIdpByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamIdpByMoid(body=body, **kwargs)

@register('GetIamIdpReferenceList')
def GetIamIdpReferenceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamIdpReferenceList(body=body, **kwargs)

@register('GetIamIdpReferenceByMoid')
def GetIamIdpReferenceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamIdpReferenceByMoid(body=body, **kwargs)

@register('GetIamIpAccessManagementList')
def GetIamIpAccessManagementList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamIpAccessManagementList(body=body, **kwargs)

@register('GetIamIpAccessManagementByMoid')
def GetIamIpAccessManagementByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamIpAccessManagementByMoid(body=body, **kwargs)

@register('GetIamIpAddressList')
def GetIamIpAddressList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamIpAddressList(body=body, **kwargs)

@register('GetIamIpAddressByMoid')
def GetIamIpAddressByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamIpAddressByMoid(body=body, **kwargs)

@register('GetIamLdapConfigParamsList')
def GetIamLdapConfigParamsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamLdapConfigParamsList(body=body, **kwargs)

@register('GetIamLdapConfigParamsByMoid')
def GetIamLdapConfigParamsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamLdapConfigParamsByMoid(body=body, **kwargs)

@register('GetIamLdapGroupList')
def GetIamLdapGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamLdapGroupList(body=body, **kwargs)

@register('GetIamLdapGroupByMoid')
def GetIamLdapGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamLdapGroupByMoid(body=body, **kwargs)

@register('GetIamLdapPolicyList')
def GetIamLdapPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamLdapPolicyList(body=body, **kwargs)

@register('GetIamLdapPolicyByMoid')
def GetIamLdapPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamLdapPolicyByMoid(body=body, **kwargs)

@register('GetIamLdapProviderList')
def GetIamLdapProviderList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamLdapProviderList(body=body, **kwargs)

@register('GetIamLdapProviderByMoid')
def GetIamLdapProviderByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamLdapProviderByMoid(body=body, **kwargs)

@register('GetIamLocalUserPasswordList')
def GetIamLocalUserPasswordList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamLocalUserPasswordList(body=body, **kwargs)

@register('GetIamLocalUserPasswordByMoid')
def GetIamLocalUserPasswordByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamLocalUserPasswordByMoid(body=body, **kwargs)

@register('GetIamLocalUserPasswordPolicyList')
def GetIamLocalUserPasswordPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamLocalUserPasswordPolicyList(body=body, **kwargs)

@register('GetIamLocalUserPasswordPolicyByMoid')
def GetIamLocalUserPasswordPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamLocalUserPasswordPolicyByMoid(body=body, **kwargs)

@register('GetIamOAuthTokenList')
def GetIamOAuthTokenList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamOAuthTokenList(body=body, **kwargs)

@register('GetIamOAuthTokenByMoid')
def GetIamOAuthTokenByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamOAuthTokenByMoid(body=body, **kwargs)

@register('GetIamPermissionList')
def GetIamPermissionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamPermissionList(body=body, **kwargs)

@register('GetIamPermissionByMoid')
def GetIamPermissionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamPermissionByMoid(body=body, **kwargs)

@register('GetIamPrivateKeySpecList')
def GetIamPrivateKeySpecList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamPrivateKeySpecList(body=body, **kwargs)

@register('GetIamPrivateKeySpecByMoid')
def GetIamPrivateKeySpecByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamPrivateKeySpecByMoid(body=body, **kwargs)

@register('GetIamPrivilegeList')
def GetIamPrivilegeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamPrivilegeList(body=body, **kwargs)

@register('GetIamPrivilegeByMoid')
def GetIamPrivilegeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamPrivilegeByMoid(body=body, **kwargs)

@register('GetIamPrivilegeSetList')
def GetIamPrivilegeSetList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamPrivilegeSetList(body=body, **kwargs)

@register('GetIamPrivilegeSetByMoid')
def GetIamPrivilegeSetByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamPrivilegeSetByMoid(body=body, **kwargs)

@register('GetIamQualifierList')
def GetIamQualifierList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamQualifierList(body=body, **kwargs)

@register('GetIamQualifierByMoid')
def GetIamQualifierByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamQualifierByMoid(body=body, **kwargs)

@register('GetIamResourceLimitsList')
def GetIamResourceLimitsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamResourceLimitsList(body=body, **kwargs)

@register('GetIamResourceLimitsByMoid')
def GetIamResourceLimitsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamResourceLimitsByMoid(body=body, **kwargs)

@register('GetIamResourcePermissionList')
def GetIamResourcePermissionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamResourcePermissionList(body=body, **kwargs)

@register('GetIamResourcePermissionByMoid')
def GetIamResourcePermissionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamResourcePermissionByMoid(body=body, **kwargs)

@register('GetIamResourceRolesList')
def GetIamResourceRolesList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamResourceRolesList(body=body, **kwargs)

@register('GetIamResourceRolesByMoid')
def GetIamResourceRolesByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamResourceRolesByMoid(body=body, **kwargs)

@register('GetIamRoleList')
def GetIamRoleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamRoleList(body=body, **kwargs)

@register('GetIamRoleByMoid')
def GetIamRoleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamRoleByMoid(body=body, **kwargs)

@register('GetIamSecurityHolderList')
def GetIamSecurityHolderList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamSecurityHolderList(body=body, **kwargs)

@register('GetIamSecurityHolderByMoid')
def GetIamSecurityHolderByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamSecurityHolderByMoid(body=body, **kwargs)

@register('GetIamServiceProviderList')
def GetIamServiceProviderList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamServiceProviderList(body=body, **kwargs)

@register('GetIamServiceProviderByMoid')
def GetIamServiceProviderByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamServiceProviderByMoid(body=body, **kwargs)

@register('GetIamSessionList')
def GetIamSessionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamSessionList(body=body, **kwargs)

@register('GetIamSessionByMoid')
def GetIamSessionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamSessionByMoid(body=body, **kwargs)

@register('GetIamSessionLimitsList')
def GetIamSessionLimitsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamSessionLimitsList(body=body, **kwargs)

@register('GetIamSessionLimitsByMoid')
def GetIamSessionLimitsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamSessionLimitsByMoid(body=body, **kwargs)

@register('GetIamSharingRuleList')
def GetIamSharingRuleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamSharingRuleList(body=body, **kwargs)

@register('GetIamSharingRuleByMoid')
def GetIamSharingRuleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamSharingRuleByMoid(body=body, **kwargs)

@register('GetIamSystemList')
def GetIamSystemList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamSystemList(body=body, **kwargs)

@register('GetIamSystemByMoid')
def GetIamSystemByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamSystemByMoid(body=body, **kwargs)

@register('GetIamTestIdpConfigurationList')
def GetIamTestIdpConfigurationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamTestIdpConfigurationList(body=body, **kwargs)

@register('GetIamTestIdpConfigurationByMoid')
def GetIamTestIdpConfigurationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamTestIdpConfigurationByMoid(body=body, **kwargs)

@register('GetIamTrustPointList')
def GetIamTrustPointList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamTrustPointList(body=body, **kwargs)

@register('GetIamTrustPointByMoid')
def GetIamTrustPointByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamTrustPointByMoid(body=body, **kwargs)

@register('GetIamUserList')
def GetIamUserList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamUserList(body=body, **kwargs)

@register('GetIamUserByMoid')
def GetIamUserByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamUserByMoid(body=body, **kwargs)

@register('GetIamUserGroupList')
def GetIamUserGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamUserGroupList(body=body, **kwargs)

@register('GetIamUserGroupByMoid')
def GetIamUserGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamUserGroupByMoid(body=body, **kwargs)

@register('GetIamUserPreferenceList')
def GetIamUserPreferenceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamUserPreferenceList(body=body, **kwargs)

@register('GetIamUserPreferenceByMoid')
def GetIamUserPreferenceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamUserPreferenceByMoid(body=body, **kwargs)

@register('GetIamUserSettingList')
def GetIamUserSettingList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamUserSettingList(body=body, **kwargs)

@register('GetIamUserSettingByMoid')
def GetIamUserSettingByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIamUserSettingByMoid(body=body, **kwargs)

@register('GetInventoryDeviceInfoList')
def GetInventoryDeviceInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetInventoryDeviceInfoList(body=body, **kwargs)

@register('GetInventoryDeviceInfoByMoid')
def GetInventoryDeviceInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetInventoryDeviceInfoByMoid(body=body, **kwargs)

@register('GetInventoryDnMoBindingList')
def GetInventoryDnMoBindingList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetInventoryDnMoBindingList(body=body, **kwargs)

@register('GetInventoryDnMoBindingByMoid')
def GetInventoryDnMoBindingByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetInventoryDnMoBindingByMoid(body=body, **kwargs)

@register('GetInventoryGenericInventoryList')
def GetInventoryGenericInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetInventoryGenericInventoryList(body=body, **kwargs)

@register('GetInventoryGenericInventoryByMoid')
def GetInventoryGenericInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetInventoryGenericInventoryByMoid(body=body, **kwargs)

@register('GetInventoryGenericInventoryHolderList')
def GetInventoryGenericInventoryHolderList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetInventoryGenericInventoryHolderList(body=body, **kwargs)

@register('GetInventoryGenericInventoryHolderByMoid')
def GetInventoryGenericInventoryHolderByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetInventoryGenericInventoryHolderByMoid(body=body, **kwargs)

@register('GetIpmioverlanPolicyList')
def GetIpmioverlanPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIpmioverlanPolicyList(body=body, **kwargs)

@register('GetIpmioverlanPolicyByMoid')
def GetIpmioverlanPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIpmioverlanPolicyByMoid(body=body, **kwargs)

@register('GetIpmioverlanPolicyInventoryList')
def GetIpmioverlanPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIpmioverlanPolicyInventoryList(body=body, **kwargs)

@register('GetIpmioverlanPolicyInventoryByMoid')
def GetIpmioverlanPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIpmioverlanPolicyInventoryByMoid(body=body, **kwargs)

@register('GetIppoolBlockLeaseList')
def GetIppoolBlockLeaseList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIppoolBlockLeaseList(body=body, **kwargs)

@register('GetIppoolBlockLeaseByMoid')
def GetIppoolBlockLeaseByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIppoolBlockLeaseByMoid(body=body, **kwargs)

@register('GetIppoolIpLeaseList')
def GetIppoolIpLeaseList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIppoolIpLeaseList(body=body, **kwargs)

@register('GetIppoolIpLeaseByMoid')
def GetIppoolIpLeaseByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIppoolIpLeaseByMoid(body=body, **kwargs)

@register('GetIppoolPoolList')
def GetIppoolPoolList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIppoolPoolList(body=body, **kwargs)

@register('GetIppoolPoolByMoid')
def GetIppoolPoolByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIppoolPoolByMoid(body=body, **kwargs)

@register('GetIppoolPoolMemberList')
def GetIppoolPoolMemberList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIppoolPoolMemberList(body=body, **kwargs)

@register('GetIppoolPoolMemberByMoid')
def GetIppoolPoolMemberByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIppoolPoolMemberByMoid(body=body, **kwargs)

@register('GetIppoolReservationList')
def GetIppoolReservationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIppoolReservationList(body=body, **kwargs)

@register('GetIppoolReservationByMoid')
def GetIppoolReservationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIppoolReservationByMoid(body=body, **kwargs)

@register('GetIppoolShadowBlockList')
def GetIppoolShadowBlockList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIppoolShadowBlockList(body=body, **kwargs)

@register('GetIppoolShadowBlockByMoid')
def GetIppoolShadowBlockByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIppoolShadowBlockByMoid(body=body, **kwargs)

@register('GetIppoolShadowPoolList')
def GetIppoolShadowPoolList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIppoolShadowPoolList(body=body, **kwargs)

@register('GetIppoolShadowPoolByMoid')
def GetIppoolShadowPoolByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIppoolShadowPoolByMoid(body=body, **kwargs)

@register('GetIppoolUniverseList')
def GetIppoolUniverseList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIppoolUniverseList(body=body, **kwargs)

@register('GetIppoolUniverseByMoid')
def GetIppoolUniverseByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIppoolUniverseByMoid(body=body, **kwargs)

@register('GetIqnpoolBlockList')
def GetIqnpoolBlockList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIqnpoolBlockList(body=body, **kwargs)

@register('GetIqnpoolBlockByMoid')
def GetIqnpoolBlockByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIqnpoolBlockByMoid(body=body, **kwargs)

@register('GetIqnpoolLeaseList')
def GetIqnpoolLeaseList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIqnpoolLeaseList(body=body, **kwargs)

@register('GetIqnpoolLeaseByMoid')
def GetIqnpoolLeaseByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIqnpoolLeaseByMoid(body=body, **kwargs)

@register('GetIqnpoolPoolList')
def GetIqnpoolPoolList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIqnpoolPoolList(body=body, **kwargs)

@register('GetIqnpoolPoolByMoid')
def GetIqnpoolPoolByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIqnpoolPoolByMoid(body=body, **kwargs)

@register('GetIqnpoolPoolMemberList')
def GetIqnpoolPoolMemberList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIqnpoolPoolMemberList(body=body, **kwargs)

@register('GetIqnpoolPoolMemberByMoid')
def GetIqnpoolPoolMemberByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIqnpoolPoolMemberByMoid(body=body, **kwargs)

@register('GetIqnpoolReservationList')
def GetIqnpoolReservationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIqnpoolReservationList(body=body, **kwargs)

@register('GetIqnpoolReservationByMoid')
def GetIqnpoolReservationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIqnpoolReservationByMoid(body=body, **kwargs)

@register('GetIqnpoolUniverseList')
def GetIqnpoolUniverseList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIqnpoolUniverseList(body=body, **kwargs)

@register('GetIqnpoolUniverseByMoid')
def GetIqnpoolUniverseByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIqnpoolUniverseByMoid(body=body, **kwargs)

@register('GetIwotenantMaintenanceNotificationList')
def GetIwotenantMaintenanceNotificationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIwotenantMaintenanceNotificationList(body=body, **kwargs)

@register('GetIwotenantMaintenanceNotificationByMoid')
def GetIwotenantMaintenanceNotificationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIwotenantMaintenanceNotificationByMoid(body=body, **kwargs)

@register('GetIwotenantMigrateList')
def GetIwotenantMigrateList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIwotenantMigrateList(body=body, **kwargs)

@register('GetIwotenantMigrateByMoid')
def GetIwotenantMigrateByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIwotenantMigrateByMoid(body=body, **kwargs)

@register('GetIwotenantTenantCustomizationList')
def GetIwotenantTenantCustomizationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIwotenantTenantCustomizationList(body=body, **kwargs)

@register('GetIwotenantTenantCustomizationByMoid')
def GetIwotenantTenantCustomizationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIwotenantTenantCustomizationByMoid(body=body, **kwargs)

@register('GetIwotenantTenantStatusList')
def GetIwotenantTenantStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIwotenantTenantStatusList(body=body, **kwargs)

@register('GetIwotenantTenantStatusByMoid')
def GetIwotenantTenantStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetIwotenantTenantStatusByMoid(body=body, **kwargs)

@register('GetKubernetesAciCniApicList')
def GetKubernetesAciCniApicList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesAciCniApicList(body=body, **kwargs)

@register('GetKubernetesAciCniApicByMoid')
def GetKubernetesAciCniApicByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesAciCniApicByMoid(body=body, **kwargs)

@register('GetKubernetesAciCniProfileList')
def GetKubernetesAciCniProfileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesAciCniProfileList(body=body, **kwargs)

@register('GetKubernetesAciCniProfileByMoid')
def GetKubernetesAciCniProfileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesAciCniProfileByMoid(body=body, **kwargs)

@register('GetKubernetesAciCniTenantClusterAllocationList')
def GetKubernetesAciCniTenantClusterAllocationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesAciCniTenantClusterAllocationList(body=body, **kwargs)

@register('GetKubernetesAciCniTenantClusterAllocationByMoid')
def GetKubernetesAciCniTenantClusterAllocationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesAciCniTenantClusterAllocationByMoid(body=body, **kwargs)

@register('GetKubernetesAddonDefinitionList')
def GetKubernetesAddonDefinitionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesAddonDefinitionList(body=body, **kwargs)

@register('GetKubernetesAddonDefinitionByMoid')
def GetKubernetesAddonDefinitionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesAddonDefinitionByMoid(body=body, **kwargs)

@register('GetKubernetesAddonPolicyList')
def GetKubernetesAddonPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesAddonPolicyList(body=body, **kwargs)

@register('GetKubernetesAddonPolicyByMoid')
def GetKubernetesAddonPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesAddonPolicyByMoid(body=body, **kwargs)

@register('GetKubernetesAddonRepositoryList')
def GetKubernetesAddonRepositoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesAddonRepositoryList(body=body, **kwargs)

@register('GetKubernetesAddonRepositoryByMoid')
def GetKubernetesAddonRepositoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesAddonRepositoryByMoid(body=body, **kwargs)

@register('GetKubernetesBaremetalNodeProfileList')
def GetKubernetesBaremetalNodeProfileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesBaremetalNodeProfileList(body=body, **kwargs)

@register('GetKubernetesBaremetalNodeProfileByMoid')
def GetKubernetesBaremetalNodeProfileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesBaremetalNodeProfileByMoid(body=body, **kwargs)

@register('GetKubernetesCatalogList')
def GetKubernetesCatalogList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesCatalogList(body=body, **kwargs)

@register('GetKubernetesCatalogByMoid')
def GetKubernetesCatalogByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesCatalogByMoid(body=body, **kwargs)

@register('GetKubernetesClusterList')
def GetKubernetesClusterList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesClusterList(body=body, **kwargs)

@register('GetKubernetesClusterByMoid')
def GetKubernetesClusterByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesClusterByMoid(body=body, **kwargs)

@register('GetKubernetesClusterAddonProfileList')
def GetKubernetesClusterAddonProfileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesClusterAddonProfileList(body=body, **kwargs)

@register('GetKubernetesClusterAddonProfileByMoid')
def GetKubernetesClusterAddonProfileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesClusterAddonProfileByMoid(body=body, **kwargs)

@register('GetKubernetesClusterProfileList')
def GetKubernetesClusterProfileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesClusterProfileList(body=body, **kwargs)

@register('GetKubernetesClusterProfileByMoid')
def GetKubernetesClusterProfileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesClusterProfileByMoid(body=body, **kwargs)

@register('GetKubernetesConfigResultList')
def GetKubernetesConfigResultList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesConfigResultList(body=body, **kwargs)

@register('GetKubernetesConfigResultByMoid')
def GetKubernetesConfigResultByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesConfigResultByMoid(body=body, **kwargs)

@register('GetKubernetesConfigResultEntryList')
def GetKubernetesConfigResultEntryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesConfigResultEntryList(body=body, **kwargs)

@register('GetKubernetesConfigResultEntryByMoid')
def GetKubernetesConfigResultEntryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesConfigResultEntryByMoid(body=body, **kwargs)

@register('GetKubernetesContainerRuntimePolicyList')
def GetKubernetesContainerRuntimePolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesContainerRuntimePolicyList(body=body, **kwargs)

@register('GetKubernetesContainerRuntimePolicyByMoid')
def GetKubernetesContainerRuntimePolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesContainerRuntimePolicyByMoid(body=body, **kwargs)

@register('GetKubernetesDaemonSetList')
def GetKubernetesDaemonSetList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesDaemonSetList(body=body, **kwargs)

@register('GetKubernetesDaemonSetByMoid')
def GetKubernetesDaemonSetByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesDaemonSetByMoid(body=body, **kwargs)

@register('GetKubernetesDeploymentList')
def GetKubernetesDeploymentList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesDeploymentList(body=body, **kwargs)

@register('GetKubernetesDeploymentByMoid')
def GetKubernetesDeploymentByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesDeploymentByMoid(body=body, **kwargs)

@register('GetKubernetesHttpProxyPolicyList')
def GetKubernetesHttpProxyPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesHttpProxyPolicyList(body=body, **kwargs)

@register('GetKubernetesHttpProxyPolicyByMoid')
def GetKubernetesHttpProxyPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesHttpProxyPolicyByMoid(body=body, **kwargs)

@register('GetKubernetesIngressList')
def GetKubernetesIngressList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesIngressList(body=body, **kwargs)

@register('GetKubernetesIngressByMoid')
def GetKubernetesIngressByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesIngressByMoid(body=body, **kwargs)

@register('GetKubernetesNetworkPolicyList')
def GetKubernetesNetworkPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesNetworkPolicyList(body=body, **kwargs)

@register('GetKubernetesNetworkPolicyByMoid')
def GetKubernetesNetworkPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesNetworkPolicyByMoid(body=body, **kwargs)

@register('GetKubernetesNodeList')
def GetKubernetesNodeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesNodeList(body=body, **kwargs)

@register('GetKubernetesNodeByMoid')
def GetKubernetesNodeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesNodeByMoid(body=body, **kwargs)

@register('GetKubernetesNodeGroupProfileList')
def GetKubernetesNodeGroupProfileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesNodeGroupProfileList(body=body, **kwargs)

@register('GetKubernetesNodeGroupProfileByMoid')
def GetKubernetesNodeGroupProfileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesNodeGroupProfileByMoid(body=body, **kwargs)

@register('GetKubernetesNvidiaGpuProductList')
def GetKubernetesNvidiaGpuProductList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesNvidiaGpuProductList(body=body, **kwargs)

@register('GetKubernetesNvidiaGpuProductByMoid')
def GetKubernetesNvidiaGpuProductByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesNvidiaGpuProductByMoid(body=body, **kwargs)

@register('GetKubernetesPodList')
def GetKubernetesPodList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesPodList(body=body, **kwargs)

@register('GetKubernetesPodByMoid')
def GetKubernetesPodByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesPodByMoid(body=body, **kwargs)

@register('GetKubernetesServiceList')
def GetKubernetesServiceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesServiceList(body=body, **kwargs)

@register('GetKubernetesServiceByMoid')
def GetKubernetesServiceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesServiceByMoid(body=body, **kwargs)

@register('GetKubernetesStatefulSetList')
def GetKubernetesStatefulSetList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesStatefulSetList(body=body, **kwargs)

@register('GetKubernetesStatefulSetByMoid')
def GetKubernetesStatefulSetByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesStatefulSetByMoid(body=body, **kwargs)

@register('GetKubernetesSysConfigPolicyList')
def GetKubernetesSysConfigPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesSysConfigPolicyList(body=body, **kwargs)

@register('GetKubernetesSysConfigPolicyByMoid')
def GetKubernetesSysConfigPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesSysConfigPolicyByMoid(body=body, **kwargs)

@register('GetKubernetesTrustedRegistriesPolicyList')
def GetKubernetesTrustedRegistriesPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesTrustedRegistriesPolicyList(body=body, **kwargs)

@register('GetKubernetesTrustedRegistriesPolicyByMoid')
def GetKubernetesTrustedRegistriesPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesTrustedRegistriesPolicyByMoid(body=body, **kwargs)

@register('GetKubernetesVersionList')
def GetKubernetesVersionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesVersionList(body=body, **kwargs)

@register('GetKubernetesVersionByMoid')
def GetKubernetesVersionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesVersionByMoid(body=body, **kwargs)

@register('GetKubernetesVersionPolicyList')
def GetKubernetesVersionPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesVersionPolicyList(body=body, **kwargs)

@register('GetKubernetesVersionPolicyByMoid')
def GetKubernetesVersionPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesVersionPolicyByMoid(body=body, **kwargs)

@register('GetKubernetesVirtualMachineInfraConfigPolicyList')
def GetKubernetesVirtualMachineInfraConfigPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesVirtualMachineInfraConfigPolicyList(body=body, **kwargs)

@register('GetKubernetesVirtualMachineInfraConfigPolicyByMoid')
def GetKubernetesVirtualMachineInfraConfigPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesVirtualMachineInfraConfigPolicyByMoid(body=body, **kwargs)

@register('GetKubernetesVirtualMachineInfrastructureProviderList')
def GetKubernetesVirtualMachineInfrastructureProviderList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesVirtualMachineInfrastructureProviderList(body=body, **kwargs)

@register('GetKubernetesVirtualMachineInfrastructureProviderByMoid')
def GetKubernetesVirtualMachineInfrastructureProviderByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesVirtualMachineInfrastructureProviderByMoid(body=body, **kwargs)

@register('GetKubernetesVirtualMachineInstanceTypeList')
def GetKubernetesVirtualMachineInstanceTypeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesVirtualMachineInstanceTypeList(body=body, **kwargs)

@register('GetKubernetesVirtualMachineInstanceTypeByMoid')
def GetKubernetesVirtualMachineInstanceTypeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesVirtualMachineInstanceTypeByMoid(body=body, **kwargs)

@register('GetKubernetesVirtualMachineNodeProfileList')
def GetKubernetesVirtualMachineNodeProfileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesVirtualMachineNodeProfileList(body=body, **kwargs)

@register('GetKubernetesVirtualMachineNodeProfileByMoid')
def GetKubernetesVirtualMachineNodeProfileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKubernetesVirtualMachineNodeProfileByMoid(body=body, **kwargs)

@register('GetKvmPolicyList')
def GetKvmPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKvmPolicyList(body=body, **kwargs)

@register('GetKvmPolicyByMoid')
def GetKvmPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKvmPolicyByMoid(body=body, **kwargs)

@register('GetKvmPolicyInventoryList')
def GetKvmPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKvmPolicyInventoryList(body=body, **kwargs)

@register('GetKvmPolicyInventoryByMoid')
def GetKvmPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKvmPolicyInventoryByMoid(body=body, **kwargs)

@register('GetKvmSessionList')
def GetKvmSessionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKvmSessionList(body=body, **kwargs)

@register('GetKvmSessionByMoid')
def GetKvmSessionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKvmSessionByMoid(body=body, **kwargs)

@register('GetKvmTunnelList')
def GetKvmTunnelList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKvmTunnelList(body=body, **kwargs)

@register('GetKvmTunnelByMoid')
def GetKvmTunnelByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKvmTunnelByMoid(body=body, **kwargs)

@register('GetKvmTunneledKvmPolicyList')
def GetKvmTunneledKvmPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKvmTunneledKvmPolicyList(body=body, **kwargs)

@register('GetKvmTunneledKvmPolicyByMoid')
def GetKvmTunneledKvmPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetKvmTunneledKvmPolicyByMoid(body=body, **kwargs)

@register('GetLicenseAccountLicenseDataList')
def GetLicenseAccountLicenseDataList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseAccountLicenseDataList(body=body, **kwargs)

@register('GetLicenseAccountLicenseDataByMoid')
def GetLicenseAccountLicenseDataByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseAccountLicenseDataByMoid(body=body, **kwargs)

@register('GetLicenseCustomerOpList')
def GetLicenseCustomerOpList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseCustomerOpList(body=body, **kwargs)

@register('GetLicenseCustomerOpByMoid')
def GetLicenseCustomerOpByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseCustomerOpByMoid(body=body, **kwargs)

@register('GetLicenseErpCustomerOpList')
def GetLicenseErpCustomerOpList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseErpCustomerOpList(body=body, **kwargs)

@register('GetLicenseErpCustomerOpByMoid')
def GetLicenseErpCustomerOpByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseErpCustomerOpByMoid(body=body, **kwargs)

@register('GetLicenseErpLicenseCountList')
def GetLicenseErpLicenseCountList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseErpLicenseCountList(body=body, **kwargs)

@register('GetLicenseErpLicenseCountByMoid')
def GetLicenseErpLicenseCountByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseErpLicenseCountByMoid(body=body, **kwargs)

@register('GetLicenseIksCustomerOpList')
def GetLicenseIksCustomerOpList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseIksCustomerOpList(body=body, **kwargs)

@register('GetLicenseIksCustomerOpByMoid')
def GetLicenseIksCustomerOpByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseIksCustomerOpByMoid(body=body, **kwargs)

@register('GetLicenseIksLicenseCountList')
def GetLicenseIksLicenseCountList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseIksLicenseCountList(body=body, **kwargs)

@register('GetLicenseIksLicenseCountByMoid')
def GetLicenseIksLicenseCountByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseIksLicenseCountByMoid(body=body, **kwargs)

@register('GetLicenseIncCustomerOpList')
def GetLicenseIncCustomerOpList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseIncCustomerOpList(body=body, **kwargs)

@register('GetLicenseIncCustomerOpByMoid')
def GetLicenseIncCustomerOpByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseIncCustomerOpByMoid(body=body, **kwargs)

@register('GetLicenseIncLicenseCountList')
def GetLicenseIncLicenseCountList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseIncLicenseCountList(body=body, **kwargs)

@register('GetLicenseIncLicenseCountByMoid')
def GetLicenseIncLicenseCountByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseIncLicenseCountByMoid(body=body, **kwargs)

@register('GetLicenseIwoCustomerOpList')
def GetLicenseIwoCustomerOpList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseIwoCustomerOpList(body=body, **kwargs)

@register('GetLicenseIwoCustomerOpByMoid')
def GetLicenseIwoCustomerOpByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseIwoCustomerOpByMoid(body=body, **kwargs)

@register('GetLicenseIwoLicenseCountList')
def GetLicenseIwoLicenseCountList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseIwoLicenseCountList(body=body, **kwargs)

@register('GetLicenseIwoLicenseCountByMoid')
def GetLicenseIwoLicenseCountByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseIwoLicenseCountByMoid(body=body, **kwargs)

@register('GetLicenseLicenseInfoList')
def GetLicenseLicenseInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseLicenseInfoList(body=body, **kwargs)

@register('GetLicenseLicenseInfoByMoid')
def GetLicenseLicenseInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseLicenseInfoByMoid(body=body, **kwargs)

@register('GetLicenseLicenseInfoViewList')
def GetLicenseLicenseInfoViewList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseLicenseInfoViewList(body=body, **kwargs)

@register('GetLicenseLicenseInfoViewByMoid')
def GetLicenseLicenseInfoViewByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseLicenseInfoViewByMoid(body=body, **kwargs)

@register('GetLicenseLicenseRegistrationStatusList')
def GetLicenseLicenseRegistrationStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseLicenseRegistrationStatusList(body=body, **kwargs)

@register('GetLicenseLicenseRegistrationStatusByMoid')
def GetLicenseLicenseRegistrationStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseLicenseRegistrationStatusByMoid(body=body, **kwargs)

@register('GetLicenseLicenseReservationOpList')
def GetLicenseLicenseReservationOpList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseLicenseReservationOpList(body=body, **kwargs)

@register('GetLicenseLicenseReservationOpByMoid')
def GetLicenseLicenseReservationOpByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseLicenseReservationOpByMoid(body=body, **kwargs)

@register('GetLicenseSmartlicenseTokenList')
def GetLicenseSmartlicenseTokenList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseSmartlicenseTokenList(body=body, **kwargs)

@register('GetLicenseSmartlicenseTokenByMoid')
def GetLicenseSmartlicenseTokenByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLicenseSmartlicenseTokenByMoid(body=body, **kwargs)

@register('GetLsServiceProfileList')
def GetLsServiceProfileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLsServiceProfileList(body=body, **kwargs)

@register('GetLsServiceProfileByMoid')
def GetLsServiceProfileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetLsServiceProfileByMoid(body=body, **kwargs)

@register('GetMacpoolIdBlockList')
def GetMacpoolIdBlockList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMacpoolIdBlockList(body=body, **kwargs)

@register('GetMacpoolIdBlockByMoid')
def GetMacpoolIdBlockByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMacpoolIdBlockByMoid(body=body, **kwargs)

@register('GetMacpoolLeaseList')
def GetMacpoolLeaseList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMacpoolLeaseList(body=body, **kwargs)

@register('GetMacpoolLeaseByMoid')
def GetMacpoolLeaseByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMacpoolLeaseByMoid(body=body, **kwargs)

@register('GetMacpoolPoolList')
def GetMacpoolPoolList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMacpoolPoolList(body=body, **kwargs)

@register('GetMacpoolPoolByMoid')
def GetMacpoolPoolByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMacpoolPoolByMoid(body=body, **kwargs)

@register('GetMacpoolPoolMemberList')
def GetMacpoolPoolMemberList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMacpoolPoolMemberList(body=body, **kwargs)

@register('GetMacpoolPoolMemberByMoid')
def GetMacpoolPoolMemberByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMacpoolPoolMemberByMoid(body=body, **kwargs)

@register('GetMacpoolReservationList')
def GetMacpoolReservationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMacpoolReservationList(body=body, **kwargs)

@register('GetMacpoolReservationByMoid')
def GetMacpoolReservationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMacpoolReservationByMoid(body=body, **kwargs)

@register('GetMacpoolUniverseList')
def GetMacpoolUniverseList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMacpoolUniverseList(body=body, **kwargs)

@register('GetMacpoolUniverseByMoid')
def GetMacpoolUniverseByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMacpoolUniverseByMoid(body=body, **kwargs)

@register('GetManagementControllerList')
def GetManagementControllerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetManagementControllerList(body=body, **kwargs)

@register('GetManagementControllerByMoid')
def GetManagementControllerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetManagementControllerByMoid(body=body, **kwargs)

@register('GetManagementEntityList')
def GetManagementEntityList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetManagementEntityList(body=body, **kwargs)

@register('GetManagementEntityByMoid')
def GetManagementEntityByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetManagementEntityByMoid(body=body, **kwargs)

@register('GetManagementInterfaceList')
def GetManagementInterfaceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetManagementInterfaceList(body=body, **kwargs)

@register('GetManagementInterfaceByMoid')
def GetManagementInterfaceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetManagementInterfaceByMoid(body=body, **kwargs)

@register('GetMarketplaceUseCaseList')
def GetMarketplaceUseCaseList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMarketplaceUseCaseList(body=body, **kwargs)

@register('GetMarketplaceUseCaseByMoid')
def GetMarketplaceUseCaseByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMarketplaceUseCaseByMoid(body=body, **kwargs)

@register('GetMarketplaceUseCaseVersionList')
def GetMarketplaceUseCaseVersionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMarketplaceUseCaseVersionList(body=body, **kwargs)

@register('GetMarketplaceUseCaseVersionByMoid')
def GetMarketplaceUseCaseVersionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMarketplaceUseCaseVersionByMoid(body=body, **kwargs)

@register('GetMemoryArrayList')
def GetMemoryArrayList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryArrayList(body=body, **kwargs)

@register('GetMemoryArrayByMoid')
def GetMemoryArrayByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryArrayByMoid(body=body, **kwargs)

@register('GetMemoryPersistentMemoryConfigResultList')
def GetMemoryPersistentMemoryConfigResultList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryPersistentMemoryConfigResultList(body=body, **kwargs)

@register('GetMemoryPersistentMemoryConfigResultByMoid')
def GetMemoryPersistentMemoryConfigResultByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryPersistentMemoryConfigResultByMoid(body=body, **kwargs)

@register('GetMemoryPersistentMemoryConfigurationList')
def GetMemoryPersistentMemoryConfigurationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryPersistentMemoryConfigurationList(body=body, **kwargs)

@register('GetMemoryPersistentMemoryConfigurationByMoid')
def GetMemoryPersistentMemoryConfigurationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryPersistentMemoryConfigurationByMoid(body=body, **kwargs)

@register('GetMemoryPersistentMemoryNamespaceList')
def GetMemoryPersistentMemoryNamespaceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryPersistentMemoryNamespaceList(body=body, **kwargs)

@register('GetMemoryPersistentMemoryNamespaceByMoid')
def GetMemoryPersistentMemoryNamespaceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryPersistentMemoryNamespaceByMoid(body=body, **kwargs)

@register('GetMemoryPersistentMemoryNamespaceConfigResultList')
def GetMemoryPersistentMemoryNamespaceConfigResultList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryPersistentMemoryNamespaceConfigResultList(body=body, **kwargs)

@register('GetMemoryPersistentMemoryNamespaceConfigResultByMoid')
def GetMemoryPersistentMemoryNamespaceConfigResultByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryPersistentMemoryNamespaceConfigResultByMoid(body=body, **kwargs)

@register('GetMemoryPersistentMemoryPolicyList')
def GetMemoryPersistentMemoryPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryPersistentMemoryPolicyList(body=body, **kwargs)

@register('GetMemoryPersistentMemoryPolicyByMoid')
def GetMemoryPersistentMemoryPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryPersistentMemoryPolicyByMoid(body=body, **kwargs)

@register('GetMemoryPersistentMemoryRegionList')
def GetMemoryPersistentMemoryRegionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryPersistentMemoryRegionList(body=body, **kwargs)

@register('GetMemoryPersistentMemoryRegionByMoid')
def GetMemoryPersistentMemoryRegionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryPersistentMemoryRegionByMoid(body=body, **kwargs)

@register('GetMemoryPersistentMemoryUnitList')
def GetMemoryPersistentMemoryUnitList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryPersistentMemoryUnitList(body=body, **kwargs)

@register('GetMemoryPersistentMemoryUnitByMoid')
def GetMemoryPersistentMemoryUnitByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryPersistentMemoryUnitByMoid(body=body, **kwargs)

@register('GetMemoryPolicyList')
def GetMemoryPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryPolicyList(body=body, **kwargs)

@register('GetMemoryPolicyByMoid')
def GetMemoryPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryPolicyByMoid(body=body, **kwargs)

@register('GetMemoryPolicyInventoryList')
def GetMemoryPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryPolicyInventoryList(body=body, **kwargs)

@register('GetMemoryPolicyInventoryByMoid')
def GetMemoryPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryPolicyInventoryByMoid(body=body, **kwargs)

@register('GetMemoryUnitList')
def GetMemoryUnitList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryUnitList(body=body, **kwargs)

@register('GetMemoryUnitByMoid')
def GetMemoryUnitByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMemoryUnitByMoid(body=body, **kwargs)

@register('GetMerakiDeviceList')
def GetMerakiDeviceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMerakiDeviceList(body=body, **kwargs)

@register('GetMerakiDeviceByMoid')
def GetMerakiDeviceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMerakiDeviceByMoid(body=body, **kwargs)

@register('GetMerakiNetworkList')
def GetMerakiNetworkList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMerakiNetworkList(body=body, **kwargs)

@register('GetMerakiNetworkByMoid')
def GetMerakiNetworkByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMerakiNetworkByMoid(body=body, **kwargs)

@register('GetMerakiOrganizationList')
def GetMerakiOrganizationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMerakiOrganizationList(body=body, **kwargs)

@register('GetMerakiOrganizationByMoid')
def GetMerakiOrganizationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMerakiOrganizationByMoid(body=body, **kwargs)

@register('GetMerakiPortProfileList')
def GetMerakiPortProfileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMerakiPortProfileList(body=body, **kwargs)

@register('GetMerakiPortProfileByMoid')
def GetMerakiPortProfileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMerakiPortProfileByMoid(body=body, **kwargs)

@register('GetMerakiTagList')
def GetMerakiTagList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMerakiTagList(body=body, **kwargs)

@register('GetMerakiTagByMoid')
def GetMerakiTagByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMerakiTagByMoid(body=body, **kwargs)

@register('GetMetaDefinitionList')
def GetMetaDefinitionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMetaDefinitionList(body=body, **kwargs)

@register('GetMetaDefinitionByMoid')
def GetMetaDefinitionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMetaDefinitionByMoid(body=body, **kwargs)

@register('GetMetricsConfigurationList')
def GetMetricsConfigurationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMetricsConfigurationList(body=body, **kwargs)

@register('GetMetricsConfigurationByMoid')
def GetMetricsConfigurationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMetricsConfigurationByMoid(body=body, **kwargs)

@register('GetMetricsMetricsExplorationList')
def GetMetricsMetricsExplorationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMetricsMetricsExplorationList(body=body, **kwargs)

@register('GetMetricsMetricsExplorationByMoid')
def GetMetricsMetricsExplorationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMetricsMetricsExplorationByMoid(body=body, **kwargs)

@register('GetMetricsResourceConfigurationList')
def GetMetricsResourceConfigurationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMetricsResourceConfigurationList(body=body, **kwargs)

@register('GetMetricsResourceConfigurationByMoid')
def GetMetricsResourceConfigurationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMetricsResourceConfigurationByMoid(body=body, **kwargs)

@register('GetMonitoringHealthStatusList')
def GetMonitoringHealthStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMonitoringHealthStatusList(body=body, **kwargs)

@register('GetMonitoringHealthStatusByMoid')
def GetMonitoringHealthStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetMonitoringHealthStatusByMoid(body=body, **kwargs)

@register('GetNetworkDiscoveredNeighborList')
def GetNetworkDiscoveredNeighborList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkDiscoveredNeighborList(body=body, **kwargs)

@register('GetNetworkDiscoveredNeighborByMoid')
def GetNetworkDiscoveredNeighborByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkDiscoveredNeighborByMoid(body=body, **kwargs)

@register('GetNetworkDnsList')
def GetNetworkDnsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkDnsList(body=body, **kwargs)

@register('GetNetworkDnsByMoid')
def GetNetworkDnsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkDnsByMoid(body=body, **kwargs)

@register('GetNetworkElementList')
def GetNetworkElementList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkElementList(body=body, **kwargs)

@register('GetNetworkElementByMoid')
def GetNetworkElementByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkElementByMoid(body=body, **kwargs)

@register('GetNetworkElementSummaryList')
def GetNetworkElementSummaryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkElementSummaryList(body=body, **kwargs)

@register('GetNetworkElementSummaryByMoid')
def GetNetworkElementSummaryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkElementSummaryByMoid(body=body, **kwargs)

@register('GetNetworkFcZoneInfoList')
def GetNetworkFcZoneInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkFcZoneInfoList(body=body, **kwargs)

@register('GetNetworkFcZoneInfoByMoid')
def GetNetworkFcZoneInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkFcZoneInfoByMoid(body=body, **kwargs)

@register('GetNetworkFeatureControlList')
def GetNetworkFeatureControlList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkFeatureControlList(body=body, **kwargs)

@register('GetNetworkFeatureControlByMoid')
def GetNetworkFeatureControlByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkFeatureControlByMoid(body=body, **kwargs)

@register('GetNetworkInterfaceListList')
def GetNetworkInterfaceListList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkInterfaceListList(body=body, **kwargs)

@register('GetNetworkInterfaceListByMoid')
def GetNetworkInterfaceListByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkInterfaceListByMoid(body=body, **kwargs)

@register('GetNetworkLicenseFileList')
def GetNetworkLicenseFileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkLicenseFileList(body=body, **kwargs)

@register('GetNetworkLicenseFileByMoid')
def GetNetworkLicenseFileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkLicenseFileByMoid(body=body, **kwargs)

@register('GetNetworkSupervisorCardList')
def GetNetworkSupervisorCardList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkSupervisorCardList(body=body, **kwargs)

@register('GetNetworkSupervisorCardByMoid')
def GetNetworkSupervisorCardByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkSupervisorCardByMoid(body=body, **kwargs)

@register('GetNetworkTelemetryCheckList')
def GetNetworkTelemetryCheckList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkTelemetryCheckList(body=body, **kwargs)

@register('GetNetworkTelemetryCheckByMoid')
def GetNetworkTelemetryCheckByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkTelemetryCheckByMoid(body=body, **kwargs)

@register('GetNetworkVethernetList')
def GetNetworkVethernetList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkVethernetList(body=body, **kwargs)

@register('GetNetworkVethernetByMoid')
def GetNetworkVethernetByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkVethernetByMoid(body=body, **kwargs)

@register('GetNetworkVfcList')
def GetNetworkVfcList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkVfcList(body=body, **kwargs)

@register('GetNetworkVfcByMoid')
def GetNetworkVfcByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkVfcByMoid(body=body, **kwargs)

@register('GetNetworkVlanPortInfoList')
def GetNetworkVlanPortInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkVlanPortInfoList(body=body, **kwargs)

@register('GetNetworkVlanPortInfoByMoid')
def GetNetworkVlanPortInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkVlanPortInfoByMoid(body=body, **kwargs)

@register('GetNetworkVpcDomainList')
def GetNetworkVpcDomainList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkVpcDomainList(body=body, **kwargs)

@register('GetNetworkVpcDomainByMoid')
def GetNetworkVpcDomainByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkVpcDomainByMoid(body=body, **kwargs)

@register('GetNetworkVpcMemberList')
def GetNetworkVpcMemberList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkVpcMemberList(body=body, **kwargs)

@register('GetNetworkVpcMemberByMoid')
def GetNetworkVpcMemberByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkVpcMemberByMoid(body=body, **kwargs)

@register('GetNetworkVpcPeerList')
def GetNetworkVpcPeerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkVpcPeerList(body=body, **kwargs)

@register('GetNetworkVpcPeerByMoid')
def GetNetworkVpcPeerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkVpcPeerByMoid(body=body, **kwargs)

@register('GetNetworkVrfList')
def GetNetworkVrfList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkVrfList(body=body, **kwargs)

@register('GetNetworkVrfByMoid')
def GetNetworkVrfByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkVrfByMoid(body=body, **kwargs)

@register('GetNetworkconfigPolicyList')
def GetNetworkconfigPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkconfigPolicyList(body=body, **kwargs)

@register('GetNetworkconfigPolicyByMoid')
def GetNetworkconfigPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkconfigPolicyByMoid(body=body, **kwargs)

@register('GetNetworkconfigPolicyInventoryList')
def GetNetworkconfigPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkconfigPolicyInventoryList(body=body, **kwargs)

@register('GetNetworkconfigPolicyInventoryByMoid')
def GetNetworkconfigPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNetworkconfigPolicyInventoryByMoid(body=body, **kwargs)

@register('GetNiaapiApicCcoPostList')
def GetNiaapiApicCcoPostList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiApicCcoPostList(body=body, **kwargs)

@register('GetNiaapiApicCcoPostByMoid')
def GetNiaapiApicCcoPostByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiApicCcoPostByMoid(body=body, **kwargs)

@register('GetNiaapiApicFieldNoticeList')
def GetNiaapiApicFieldNoticeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiApicFieldNoticeList(body=body, **kwargs)

@register('GetNiaapiApicFieldNoticeByMoid')
def GetNiaapiApicFieldNoticeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiApicFieldNoticeByMoid(body=body, **kwargs)

@register('GetNiaapiApicHweolList')
def GetNiaapiApicHweolList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiApicHweolList(body=body, **kwargs)

@register('GetNiaapiApicHweolByMoid')
def GetNiaapiApicHweolByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiApicHweolByMoid(body=body, **kwargs)

@register('GetNiaapiApicLatestMaintainedReleaseList')
def GetNiaapiApicLatestMaintainedReleaseList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiApicLatestMaintainedReleaseList(body=body, **kwargs)

@register('GetNiaapiApicLatestMaintainedReleaseByMoid')
def GetNiaapiApicLatestMaintainedReleaseByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiApicLatestMaintainedReleaseByMoid(body=body, **kwargs)

@register('GetNiaapiApicReleaseRecommendList')
def GetNiaapiApicReleaseRecommendList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiApicReleaseRecommendList(body=body, **kwargs)

@register('GetNiaapiApicReleaseRecommendByMoid')
def GetNiaapiApicReleaseRecommendByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiApicReleaseRecommendByMoid(body=body, **kwargs)

@register('GetNiaapiApicSweolList')
def GetNiaapiApicSweolList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiApicSweolList(body=body, **kwargs)

@register('GetNiaapiApicSweolByMoid')
def GetNiaapiApicSweolByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiApicSweolByMoid(body=body, **kwargs)

@register('GetNiaapiDcnmCcoPostList')
def GetNiaapiDcnmCcoPostList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiDcnmCcoPostList(body=body, **kwargs)

@register('GetNiaapiDcnmCcoPostByMoid')
def GetNiaapiDcnmCcoPostByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiDcnmCcoPostByMoid(body=body, **kwargs)

@register('GetNiaapiDcnmFieldNoticeList')
def GetNiaapiDcnmFieldNoticeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiDcnmFieldNoticeList(body=body, **kwargs)

@register('GetNiaapiDcnmFieldNoticeByMoid')
def GetNiaapiDcnmFieldNoticeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiDcnmFieldNoticeByMoid(body=body, **kwargs)

@register('GetNiaapiDcnmHweolList')
def GetNiaapiDcnmHweolList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiDcnmHweolList(body=body, **kwargs)

@register('GetNiaapiDcnmHweolByMoid')
def GetNiaapiDcnmHweolByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiDcnmHweolByMoid(body=body, **kwargs)

@register('GetNiaapiDcnmLatestMaintainedReleaseList')
def GetNiaapiDcnmLatestMaintainedReleaseList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiDcnmLatestMaintainedReleaseList(body=body, **kwargs)

@register('GetNiaapiDcnmLatestMaintainedReleaseByMoid')
def GetNiaapiDcnmLatestMaintainedReleaseByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiDcnmLatestMaintainedReleaseByMoid(body=body, **kwargs)

@register('GetNiaapiDcnmReleaseRecommendList')
def GetNiaapiDcnmReleaseRecommendList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiDcnmReleaseRecommendList(body=body, **kwargs)

@register('GetNiaapiDcnmReleaseRecommendByMoid')
def GetNiaapiDcnmReleaseRecommendByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiDcnmReleaseRecommendByMoid(body=body, **kwargs)

@register('GetNiaapiDcnmSweolList')
def GetNiaapiDcnmSweolList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiDcnmSweolList(body=body, **kwargs)

@register('GetNiaapiDcnmSweolByMoid')
def GetNiaapiDcnmSweolByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiDcnmSweolByMoid(body=body, **kwargs)

@register('GetNiaapiFileDownloaderList')
def GetNiaapiFileDownloaderList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiFileDownloaderList(body=body, **kwargs)

@register('GetNiaapiFileDownloaderByMoid')
def GetNiaapiFileDownloaderByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiFileDownloaderByMoid(body=body, **kwargs)

@register('GetNiaapiNiaMetadataList')
def GetNiaapiNiaMetadataList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiNiaMetadataList(body=body, **kwargs)

@register('GetNiaapiNiaMetadataByMoid')
def GetNiaapiNiaMetadataByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiNiaMetadataByMoid(body=body, **kwargs)

@register('GetNiaapiNibFileDownloaderList')
def GetNiaapiNibFileDownloaderList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiNibFileDownloaderList(body=body, **kwargs)

@register('GetNiaapiNibFileDownloaderByMoid')
def GetNiaapiNibFileDownloaderByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiNibFileDownloaderByMoid(body=body, **kwargs)

@register('GetNiaapiNibMetadataList')
def GetNiaapiNibMetadataList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiNibMetadataList(body=body, **kwargs)

@register('GetNiaapiNibMetadataByMoid')
def GetNiaapiNibMetadataByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiNibMetadataByMoid(body=body, **kwargs)

@register('GetNiaapiPuvScriptDownloaderList')
def GetNiaapiPuvScriptDownloaderList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiPuvScriptDownloaderList(body=body, **kwargs)

@register('GetNiaapiPuvScriptDownloaderByMoid')
def GetNiaapiPuvScriptDownloaderByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiPuvScriptDownloaderByMoid(body=body, **kwargs)

@register('GetNiaapiSnValidatorMetadataList')
def GetNiaapiSnValidatorMetadataList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiSnValidatorMetadataList(body=body, **kwargs)

@register('GetNiaapiSnValidatorMetadataByMoid')
def GetNiaapiSnValidatorMetadataByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiSnValidatorMetadataByMoid(body=body, **kwargs)

@register('GetNiaapiUpgradeAssistFileList')
def GetNiaapiUpgradeAssistFileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiUpgradeAssistFileList(body=body, **kwargs)

@register('GetNiaapiUpgradeAssistFileByMoid')
def GetNiaapiUpgradeAssistFileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiUpgradeAssistFileByMoid(body=body, **kwargs)

@register('GetNiaapiVersionRegexList')
def GetNiaapiVersionRegexList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiVersionRegexList(body=body, **kwargs)

@register('GetNiaapiVersionRegexByMoid')
def GetNiaapiVersionRegexByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiaapiVersionRegexByMoid(body=body, **kwargs)

@register('GetNiatelemetryAaaLdapProviderDetailsList')
def GetNiatelemetryAaaLdapProviderDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryAaaLdapProviderDetailsList(body=body, **kwargs)

@register('GetNiatelemetryAaaLdapProviderDetailsByMoid')
def GetNiatelemetryAaaLdapProviderDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryAaaLdapProviderDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryAaaRadiusProviderDetailsList')
def GetNiatelemetryAaaRadiusProviderDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryAaaRadiusProviderDetailsList(body=body, **kwargs)

@register('GetNiatelemetryAaaRadiusProviderDetailsByMoid')
def GetNiatelemetryAaaRadiusProviderDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryAaaRadiusProviderDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryAaaTacacsProviderDetailsList')
def GetNiatelemetryAaaTacacsProviderDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryAaaTacacsProviderDetailsList(body=body, **kwargs)

@register('GetNiatelemetryAaaTacacsProviderDetailsByMoid')
def GetNiatelemetryAaaTacacsProviderDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryAaaTacacsProviderDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicAppPluginDetailsList')
def GetNiatelemetryApicAppPluginDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicAppPluginDetailsList(body=body, **kwargs)

@register('GetNiatelemetryApicAppPluginDetailsByMoid')
def GetNiatelemetryApicAppPluginDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicAppPluginDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicCoreFileDetailsList')
def GetNiatelemetryApicCoreFileDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicCoreFileDetailsList(body=body, **kwargs)

@register('GetNiatelemetryApicCoreFileDetailsByMoid')
def GetNiatelemetryApicCoreFileDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicCoreFileDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicDbgexpRsExportDestList')
def GetNiatelemetryApicDbgexpRsExportDestList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicDbgexpRsExportDestList(body=body, **kwargs)

@register('GetNiatelemetryApicDbgexpRsExportDestByMoid')
def GetNiatelemetryApicDbgexpRsExportDestByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicDbgexpRsExportDestByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicDbgexpRsTsSchedulerList')
def GetNiatelemetryApicDbgexpRsTsSchedulerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicDbgexpRsTsSchedulerList(body=body, **kwargs)

@register('GetNiatelemetryApicDbgexpRsTsSchedulerByMoid')
def GetNiatelemetryApicDbgexpRsTsSchedulerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicDbgexpRsTsSchedulerByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicFanDetailsList')
def GetNiatelemetryApicFanDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicFanDetailsList(body=body, **kwargs)

@register('GetNiatelemetryApicFanDetailsByMoid')
def GetNiatelemetryApicFanDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicFanDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicFexDetailsList')
def GetNiatelemetryApicFexDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicFexDetailsList(body=body, **kwargs)

@register('GetNiatelemetryApicFexDetailsByMoid')
def GetNiatelemetryApicFexDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicFexDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicFlashDetailsList')
def GetNiatelemetryApicFlashDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicFlashDetailsList(body=body, **kwargs)

@register('GetNiatelemetryApicFlashDetailsByMoid')
def GetNiatelemetryApicFlashDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicFlashDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicNtpAuthList')
def GetNiatelemetryApicNtpAuthList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicNtpAuthList(body=body, **kwargs)

@register('GetNiatelemetryApicNtpAuthByMoid')
def GetNiatelemetryApicNtpAuthByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicNtpAuthByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicPerformanceDataList')
def GetNiatelemetryApicPerformanceDataList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicPerformanceDataList(body=body, **kwargs)

@register('GetNiatelemetryApicPerformanceDataByMoid')
def GetNiatelemetryApicPerformanceDataByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicPerformanceDataByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicPodDataList')
def GetNiatelemetryApicPodDataList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicPodDataList(body=body, **kwargs)

@register('GetNiatelemetryApicPodDataByMoid')
def GetNiatelemetryApicPodDataByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicPodDataByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicPsuDetailsList')
def GetNiatelemetryApicPsuDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicPsuDetailsList(body=body, **kwargs)

@register('GetNiatelemetryApicPsuDetailsByMoid')
def GetNiatelemetryApicPsuDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicPsuDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicRealmDetailsList')
def GetNiatelemetryApicRealmDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicRealmDetailsList(body=body, **kwargs)

@register('GetNiatelemetryApicRealmDetailsByMoid')
def GetNiatelemetryApicRealmDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicRealmDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicSnmpClientGrpDetailsList')
def GetNiatelemetryApicSnmpClientGrpDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicSnmpClientGrpDetailsList(body=body, **kwargs)

@register('GetNiatelemetryApicSnmpClientGrpDetailsByMoid')
def GetNiatelemetryApicSnmpClientGrpDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicSnmpClientGrpDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicSnmpCommunityAccessDetailsList')
def GetNiatelemetryApicSnmpCommunityAccessDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicSnmpCommunityAccessDetailsList(body=body, **kwargs)

@register('GetNiatelemetryApicSnmpCommunityAccessDetailsByMoid')
def GetNiatelemetryApicSnmpCommunityAccessDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicSnmpCommunityAccessDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicSnmpCommunityDetailsList')
def GetNiatelemetryApicSnmpCommunityDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicSnmpCommunityDetailsList(body=body, **kwargs)

@register('GetNiatelemetryApicSnmpCommunityDetailsByMoid')
def GetNiatelemetryApicSnmpCommunityDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicSnmpCommunityDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicSnmpTrapDetailsList')
def GetNiatelemetryApicSnmpTrapDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicSnmpTrapDetailsList(body=body, **kwargs)

@register('GetNiatelemetryApicSnmpTrapDetailsByMoid')
def GetNiatelemetryApicSnmpTrapDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicSnmpTrapDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicSnmpTrapFwdServerDetailsList')
def GetNiatelemetryApicSnmpTrapFwdServerDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicSnmpTrapFwdServerDetailsList(body=body, **kwargs)

@register('GetNiatelemetryApicSnmpTrapFwdServerDetailsByMoid')
def GetNiatelemetryApicSnmpTrapFwdServerDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicSnmpTrapFwdServerDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicSnmpVersionThreeDetailsList')
def GetNiatelemetryApicSnmpVersionThreeDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicSnmpVersionThreeDetailsList(body=body, **kwargs)

@register('GetNiatelemetryApicSnmpVersionThreeDetailsByMoid')
def GetNiatelemetryApicSnmpVersionThreeDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicSnmpVersionThreeDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicSysLogGrpList')
def GetNiatelemetryApicSysLogGrpList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicSysLogGrpList(body=body, **kwargs)

@register('GetNiatelemetryApicSysLogGrpByMoid')
def GetNiatelemetryApicSysLogGrpByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicSysLogGrpByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicSysLogSrcList')
def GetNiatelemetryApicSysLogSrcList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicSysLogSrcList(body=body, **kwargs)

@register('GetNiatelemetryApicSysLogSrcByMoid')
def GetNiatelemetryApicSysLogSrcByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicSysLogSrcByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicTransceiverDetailsList')
def GetNiatelemetryApicTransceiverDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicTransceiverDetailsList(body=body, **kwargs)

@register('GetNiatelemetryApicTransceiverDetailsByMoid')
def GetNiatelemetryApicTransceiverDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicTransceiverDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicUiPageCountsList')
def GetNiatelemetryApicUiPageCountsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicUiPageCountsList(body=body, **kwargs)

@register('GetNiatelemetryApicUiPageCountsByMoid')
def GetNiatelemetryApicUiPageCountsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicUiPageCountsByMoid(body=body, **kwargs)

@register('GetNiatelemetryApicVisionList')
def GetNiatelemetryApicVisionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicVisionList(body=body, **kwargs)

@register('GetNiatelemetryApicVisionByMoid')
def GetNiatelemetryApicVisionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryApicVisionByMoid(body=body, **kwargs)

@register('GetNiatelemetryAppDetailsList')
def GetNiatelemetryAppDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryAppDetailsList(body=body, **kwargs)

@register('GetNiatelemetryAppDetailsByMoid')
def GetNiatelemetryAppDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryAppDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryCloudDetailsList')
def GetNiatelemetryCloudDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryCloudDetailsList(body=body, **kwargs)

@register('GetNiatelemetryCloudDetailsByMoid')
def GetNiatelemetryCloudDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryCloudDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryCommonPoliciesList')
def GetNiatelemetryCommonPoliciesList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryCommonPoliciesList(body=body, **kwargs)

@register('GetNiatelemetryCommonPoliciesByMoid')
def GetNiatelemetryCommonPoliciesByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryCommonPoliciesByMoid(body=body, **kwargs)

@register('GetNiatelemetryDcnmFanDetailsList')
def GetNiatelemetryDcnmFanDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryDcnmFanDetailsList(body=body, **kwargs)

@register('GetNiatelemetryDcnmFanDetailsByMoid')
def GetNiatelemetryDcnmFanDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryDcnmFanDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryDcnmFexDetailsList')
def GetNiatelemetryDcnmFexDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryDcnmFexDetailsList(body=body, **kwargs)

@register('GetNiatelemetryDcnmFexDetailsByMoid')
def GetNiatelemetryDcnmFexDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryDcnmFexDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryDcnmModuleDetailsList')
def GetNiatelemetryDcnmModuleDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryDcnmModuleDetailsList(body=body, **kwargs)

@register('GetNiatelemetryDcnmModuleDetailsByMoid')
def GetNiatelemetryDcnmModuleDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryDcnmModuleDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryDcnmPsuDetailsList')
def GetNiatelemetryDcnmPsuDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryDcnmPsuDetailsList(body=body, **kwargs)

@register('GetNiatelemetryDcnmPsuDetailsByMoid')
def GetNiatelemetryDcnmPsuDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryDcnmPsuDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryDcnmTransceiverDetailsList')
def GetNiatelemetryDcnmTransceiverDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryDcnmTransceiverDetailsList(body=body, **kwargs)

@register('GetNiatelemetryDcnmTransceiverDetailsByMoid')
def GetNiatelemetryDcnmTransceiverDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryDcnmTransceiverDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryDomInfoObjectList')
def GetNiatelemetryDomInfoObjectList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryDomInfoObjectList(body=body, **kwargs)

@register('GetNiatelemetryDomInfoObjectByMoid')
def GetNiatelemetryDomInfoObjectByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryDomInfoObjectByMoid(body=body, **kwargs)

@register('GetNiatelemetryDomThresInfoObjectList')
def GetNiatelemetryDomThresInfoObjectList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryDomThresInfoObjectList(body=body, **kwargs)

@register('GetNiatelemetryDomThresInfoObjectByMoid')
def GetNiatelemetryDomThresInfoObjectByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryDomThresInfoObjectByMoid(body=body, **kwargs)

@register('GetNiatelemetryEpgList')
def GetNiatelemetryEpgList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryEpgList(body=body, **kwargs)

@register('GetNiatelemetryEpgByMoid')
def GetNiatelemetryEpgByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryEpgByMoid(body=body, **kwargs)

@register('GetNiatelemetryFabricModuleDetailsList')
def GetNiatelemetryFabricModuleDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryFabricModuleDetailsList(body=body, **kwargs)

@register('GetNiatelemetryFabricModuleDetailsByMoid')
def GetNiatelemetryFabricModuleDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryFabricModuleDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryFabricNodeControlDetailsList')
def GetNiatelemetryFabricNodeControlDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryFabricNodeControlDetailsList(body=body, **kwargs)

@register('GetNiatelemetryFabricNodeControlDetailsByMoid')
def GetNiatelemetryFabricNodeControlDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryFabricNodeControlDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryFabricPodProfileList')
def GetNiatelemetryFabricPodProfileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryFabricPodProfileList(body=body, **kwargs)

@register('GetNiatelemetryFabricPodProfileByMoid')
def GetNiatelemetryFabricPodProfileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryFabricPodProfileByMoid(body=body, **kwargs)

@register('GetNiatelemetryFabricPodSsList')
def GetNiatelemetryFabricPodSsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryFabricPodSsList(body=body, **kwargs)

@register('GetNiatelemetryFabricPodSsByMoid')
def GetNiatelemetryFabricPodSsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryFabricPodSsByMoid(body=body, **kwargs)

@register('GetNiatelemetryFaultList')
def GetNiatelemetryFaultList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryFaultList(body=body, **kwargs)

@register('GetNiatelemetryFaultByMoid')
def GetNiatelemetryFaultByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryFaultByMoid(body=body, **kwargs)

@register('GetNiatelemetryHcloudDetailsList')
def GetNiatelemetryHcloudDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryHcloudDetailsList(body=body, **kwargs)

@register('GetNiatelemetryHcloudDetailsByMoid')
def GetNiatelemetryHcloudDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryHcloudDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryHealthInsightsDataList')
def GetNiatelemetryHealthInsightsDataList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryHealthInsightsDataList(body=body, **kwargs)

@register('GetNiatelemetryHealthInsightsDataByMoid')
def GetNiatelemetryHealthInsightsDataByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryHealthInsightsDataByMoid(body=body, **kwargs)

@register('GetNiatelemetryHttpsAclContractDetailsList')
def GetNiatelemetryHttpsAclContractDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryHttpsAclContractDetailsList(body=body, **kwargs)

@register('GetNiatelemetryHttpsAclContractDetailsByMoid')
def GetNiatelemetryHttpsAclContractDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryHttpsAclContractDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryHttpsAclContractFilterMapList')
def GetNiatelemetryHttpsAclContractFilterMapList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryHttpsAclContractFilterMapList(body=body, **kwargs)

@register('GetNiatelemetryHttpsAclContractFilterMapByMoid')
def GetNiatelemetryHttpsAclContractFilterMapByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryHttpsAclContractFilterMapByMoid(body=body, **kwargs)

@register('GetNiatelemetryHttpsAclEpgContractMapList')
def GetNiatelemetryHttpsAclEpgContractMapList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryHttpsAclEpgContractMapList(body=body, **kwargs)

@register('GetNiatelemetryHttpsAclEpgContractMapByMoid')
def GetNiatelemetryHttpsAclEpgContractMapByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryHttpsAclEpgContractMapByMoid(body=body, **kwargs)

@register('GetNiatelemetryHttpsAclEpgDetailsList')
def GetNiatelemetryHttpsAclEpgDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryHttpsAclEpgDetailsList(body=body, **kwargs)

@register('GetNiatelemetryHttpsAclEpgDetailsByMoid')
def GetNiatelemetryHttpsAclEpgDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryHttpsAclEpgDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryHttpsAclFilterDetailsList')
def GetNiatelemetryHttpsAclFilterDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryHttpsAclFilterDetailsList(body=body, **kwargs)

@register('GetNiatelemetryHttpsAclFilterDetailsByMoid')
def GetNiatelemetryHttpsAclFilterDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryHttpsAclFilterDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryInsightGroupDetailsList')
def GetNiatelemetryInsightGroupDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryInsightGroupDetailsList(body=body, **kwargs)

@register('GetNiatelemetryInsightGroupDetailsByMoid')
def GetNiatelemetryInsightGroupDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryInsightGroupDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryLcList')
def GetNiatelemetryLcList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryLcList(body=body, **kwargs)

@register('GetNiatelemetryLcByMoid')
def GetNiatelemetryLcByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryLcByMoid(body=body, **kwargs)

@register('GetNiatelemetryLeafPolGrpDetailsList')
def GetNiatelemetryLeafPolGrpDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryLeafPolGrpDetailsList(body=body, **kwargs)

@register('GetNiatelemetryLeafPolGrpDetailsByMoid')
def GetNiatelemetryLeafPolGrpDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryLeafPolGrpDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryMdsNeighborsList')
def GetNiatelemetryMdsNeighborsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryMdsNeighborsList(body=body, **kwargs)

@register('GetNiatelemetryMdsNeighborsByMoid')
def GetNiatelemetryMdsNeighborsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryMdsNeighborsByMoid(body=body, **kwargs)

@register('GetNiatelemetryMsoContractDetailsList')
def GetNiatelemetryMsoContractDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryMsoContractDetailsList(body=body, **kwargs)

@register('GetNiatelemetryMsoContractDetailsByMoid')
def GetNiatelemetryMsoContractDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryMsoContractDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryMsoEpgDetailsList')
def GetNiatelemetryMsoEpgDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryMsoEpgDetailsList(body=body, **kwargs)

@register('GetNiatelemetryMsoEpgDetailsByMoid')
def GetNiatelemetryMsoEpgDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryMsoEpgDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryMsoSchemaDetailsList')
def GetNiatelemetryMsoSchemaDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryMsoSchemaDetailsList(body=body, **kwargs)

@register('GetNiatelemetryMsoSchemaDetailsByMoid')
def GetNiatelemetryMsoSchemaDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryMsoSchemaDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryMsoSiteDetailsList')
def GetNiatelemetryMsoSiteDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryMsoSiteDetailsList(body=body, **kwargs)

@register('GetNiatelemetryMsoSiteDetailsByMoid')
def GetNiatelemetryMsoSiteDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryMsoSiteDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryMsoTenantDetailsList')
def GetNiatelemetryMsoTenantDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryMsoTenantDetailsList(body=body, **kwargs)

@register('GetNiatelemetryMsoTenantDetailsByMoid')
def GetNiatelemetryMsoTenantDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryMsoTenantDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryNexusCloudAccountList')
def GetNiatelemetryNexusCloudAccountList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNexusCloudAccountList(body=body, **kwargs)

@register('GetNiatelemetryNexusCloudAccountByMoid')
def GetNiatelemetryNexusCloudAccountByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNexusCloudAccountByMoid(body=body, **kwargs)

@register('GetNiatelemetryNexusCloudSiteList')
def GetNiatelemetryNexusCloudSiteList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNexusCloudSiteList(body=body, **kwargs)

@register('GetNiatelemetryNexusCloudSiteByMoid')
def GetNiatelemetryNexusCloudSiteByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNexusCloudSiteByMoid(body=body, **kwargs)

@register('GetNiatelemetryNexusDashboardControllerDetailsList')
def GetNiatelemetryNexusDashboardControllerDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNexusDashboardControllerDetailsList(body=body, **kwargs)

@register('GetNiatelemetryNexusDashboardControllerDetailsByMoid')
def GetNiatelemetryNexusDashboardControllerDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNexusDashboardControllerDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryNexusDashboardDetailsList')
def GetNiatelemetryNexusDashboardDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNexusDashboardDetailsList(body=body, **kwargs)

@register('GetNiatelemetryNexusDashboardDetailsByMoid')
def GetNiatelemetryNexusDashboardDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNexusDashboardDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryNexusDashboardMemoryDetailsList')
def GetNiatelemetryNexusDashboardMemoryDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNexusDashboardMemoryDetailsList(body=body, **kwargs)

@register('GetNiatelemetryNexusDashboardMemoryDetailsByMoid')
def GetNiatelemetryNexusDashboardMemoryDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNexusDashboardMemoryDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryNexusDashboardsList')
def GetNiatelemetryNexusDashboardsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNexusDashboardsList(body=body, **kwargs)

@register('GetNiatelemetryNexusDashboardsByMoid')
def GetNiatelemetryNexusDashboardsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNexusDashboardsByMoid(body=body, **kwargs)

@register('GetNiatelemetryNiaFeatureUsageList')
def GetNiatelemetryNiaFeatureUsageList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNiaFeatureUsageList(body=body, **kwargs)

@register('GetNiatelemetryNiaFeatureUsageByMoid')
def GetNiatelemetryNiaFeatureUsageByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNiaFeatureUsageByMoid(body=body, **kwargs)

@register('GetNiatelemetryNiaInventoryList')
def GetNiatelemetryNiaInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNiaInventoryList(body=body, **kwargs)

@register('GetNiatelemetryNiaInventoryByMoid')
def GetNiatelemetryNiaInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNiaInventoryByMoid(body=body, **kwargs)

@register('GetNiatelemetryNiaInventoryDcnmList')
def GetNiatelemetryNiaInventoryDcnmList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNiaInventoryDcnmList(body=body, **kwargs)

@register('GetNiatelemetryNiaInventoryDcnmByMoid')
def GetNiatelemetryNiaInventoryDcnmByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNiaInventoryDcnmByMoid(body=body, **kwargs)

@register('GetNiatelemetryNiaInventoryFabricList')
def GetNiatelemetryNiaInventoryFabricList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNiaInventoryFabricList(body=body, **kwargs)

@register('GetNiatelemetryNiaInventoryFabricByMoid')
def GetNiatelemetryNiaInventoryFabricByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNiaInventoryFabricByMoid(body=body, **kwargs)

@register('GetNiatelemetryNiaLicenseStateList')
def GetNiatelemetryNiaLicenseStateList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNiaLicenseStateList(body=body, **kwargs)

@register('GetNiatelemetryNiaLicenseStateByMoid')
def GetNiatelemetryNiaLicenseStateByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNiaLicenseStateByMoid(body=body, **kwargs)

@register('GetNiatelemetryNiccList')
def GetNiatelemetryNiccList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNiccList(body=body, **kwargs)

@register('GetNiatelemetryNiccByMoid')
def GetNiatelemetryNiccByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryNiccByMoid(body=body, **kwargs)

@register('GetNiatelemetryPasswordStrengthCheckList')
def GetNiatelemetryPasswordStrengthCheckList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryPasswordStrengthCheckList(body=body, **kwargs)

@register('GetNiatelemetryPasswordStrengthCheckByMoid')
def GetNiatelemetryPasswordStrengthCheckByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryPasswordStrengthCheckByMoid(body=body, **kwargs)

@register('GetNiatelemetryPodCommPoliciesList')
def GetNiatelemetryPodCommPoliciesList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryPodCommPoliciesList(body=body, **kwargs)

@register('GetNiatelemetryPodCommPoliciesByMoid')
def GetNiatelemetryPodCommPoliciesByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryPodCommPoliciesByMoid(body=body, **kwargs)

@register('GetNiatelemetryPodSnmpPoliciesList')
def GetNiatelemetryPodSnmpPoliciesList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryPodSnmpPoliciesList(body=body, **kwargs)

@register('GetNiatelemetryPodSnmpPoliciesByMoid')
def GetNiatelemetryPodSnmpPoliciesByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryPodSnmpPoliciesByMoid(body=body, **kwargs)

@register('GetNiatelemetryPodTimeServerPoliciesList')
def GetNiatelemetryPodTimeServerPoliciesList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryPodTimeServerPoliciesList(body=body, **kwargs)

@register('GetNiatelemetryPodTimeServerPoliciesByMoid')
def GetNiatelemetryPodTimeServerPoliciesByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryPodTimeServerPoliciesByMoid(body=body, **kwargs)

@register('GetNiatelemetrySiteInventoryList')
def GetNiatelemetrySiteInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetrySiteInventoryList(body=body, **kwargs)

@register('GetNiatelemetrySiteInventoryByMoid')
def GetNiatelemetrySiteInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetrySiteInventoryByMoid(body=body, **kwargs)

@register('GetNiatelemetrySnmpSrcList')
def GetNiatelemetrySnmpSrcList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetrySnmpSrcList(body=body, **kwargs)

@register('GetNiatelemetrySnmpSrcByMoid')
def GetNiatelemetrySnmpSrcByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetrySnmpSrcByMoid(body=body, **kwargs)

@register('GetNiatelemetrySpinePolGrpDetailsList')
def GetNiatelemetrySpinePolGrpDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetrySpinePolGrpDetailsList(body=body, **kwargs)

@register('GetNiatelemetrySpinePolGrpDetailsByMoid')
def GetNiatelemetrySpinePolGrpDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetrySpinePolGrpDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetrySshVersionTwoList')
def GetNiatelemetrySshVersionTwoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetrySshVersionTwoList(body=body, **kwargs)

@register('GetNiatelemetrySshVersionTwoByMoid')
def GetNiatelemetrySshVersionTwoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetrySshVersionTwoByMoid(body=body, **kwargs)

@register('GetNiatelemetrySupervisorModuleDetailsList')
def GetNiatelemetrySupervisorModuleDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetrySupervisorModuleDetailsList(body=body, **kwargs)

@register('GetNiatelemetrySupervisorModuleDetailsByMoid')
def GetNiatelemetrySupervisorModuleDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetrySupervisorModuleDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetrySyslogRemoteDestList')
def GetNiatelemetrySyslogRemoteDestList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetrySyslogRemoteDestList(body=body, **kwargs)

@register('GetNiatelemetrySyslogRemoteDestByMoid')
def GetNiatelemetrySyslogRemoteDestByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetrySyslogRemoteDestByMoid(body=body, **kwargs)

@register('GetNiatelemetrySyslogSysMsgList')
def GetNiatelemetrySyslogSysMsgList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetrySyslogSysMsgList(body=body, **kwargs)

@register('GetNiatelemetrySyslogSysMsgByMoid')
def GetNiatelemetrySyslogSysMsgByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetrySyslogSysMsgByMoid(body=body, **kwargs)

@register('GetNiatelemetrySyslogSysMsgFacFilterList')
def GetNiatelemetrySyslogSysMsgFacFilterList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetrySyslogSysMsgFacFilterList(body=body, **kwargs)

@register('GetNiatelemetrySyslogSysMsgFacFilterByMoid')
def GetNiatelemetrySyslogSysMsgFacFilterByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetrySyslogSysMsgFacFilterByMoid(body=body, **kwargs)

@register('GetNiatelemetrySystemControllerDetailsList')
def GetNiatelemetrySystemControllerDetailsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetrySystemControllerDetailsList(body=body, **kwargs)

@register('GetNiatelemetrySystemControllerDetailsByMoid')
def GetNiatelemetrySystemControllerDetailsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetrySystemControllerDetailsByMoid(body=body, **kwargs)

@register('GetNiatelemetryTenantList')
def GetNiatelemetryTenantList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryTenantList(body=body, **kwargs)

@register('GetNiatelemetryTenantByMoid')
def GetNiatelemetryTenantByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNiatelemetryTenantByMoid(body=body, **kwargs)

@register('GetNotificationAccountSubscriptionList')
def GetNotificationAccountSubscriptionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNotificationAccountSubscriptionList(body=body, **kwargs)

@register('GetNotificationAccountSubscriptionByMoid')
def GetNotificationAccountSubscriptionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNotificationAccountSubscriptionByMoid(body=body, **kwargs)

@register('GetNtpNtpServerList')
def GetNtpNtpServerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNtpNtpServerList(body=body, **kwargs)

@register('GetNtpNtpServerByMoid')
def GetNtpNtpServerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNtpNtpServerByMoid(body=body, **kwargs)

@register('GetNtpPolicyList')
def GetNtpPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNtpPolicyList(body=body, **kwargs)

@register('GetNtpPolicyByMoid')
def GetNtpPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetNtpPolicyByMoid(body=body, **kwargs)

@register('GetOauthAccessTokenList')
def GetOauthAccessTokenList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOauthAccessTokenList(body=body, **kwargs)

@register('GetOauthAccessTokenByMoid')
def GetOauthAccessTokenByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOauthAccessTokenByMoid(body=body, **kwargs)

@register('GetOauthAuthorizationList')
def GetOauthAuthorizationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOauthAuthorizationList(body=body, **kwargs)

@register('GetOauthAuthorizationByMoid')
def GetOauthAuthorizationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOauthAuthorizationByMoid(body=body, **kwargs)

@register('GetOpenapiApiMethodMetaList')
def GetOpenapiApiMethodMetaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOpenapiApiMethodMetaList(body=body, **kwargs)

@register('GetOpenapiApiMethodMetaByMoid')
def GetOpenapiApiMethodMetaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOpenapiApiMethodMetaByMoid(body=body, **kwargs)

@register('GetOpenapiOpenApiSpecificationList')
def GetOpenapiOpenApiSpecificationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOpenapiOpenApiSpecificationList(body=body, **kwargs)

@register('GetOpenapiOpenApiSpecificationByMoid')
def GetOpenapiOpenApiSpecificationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOpenapiOpenApiSpecificationByMoid(body=body, **kwargs)

@register('GetOpenapiProcessFileList')
def GetOpenapiProcessFileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOpenapiProcessFileList(body=body, **kwargs)

@register('GetOpenapiProcessFileByMoid')
def GetOpenapiProcessFileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOpenapiProcessFileByMoid(body=body, **kwargs)

@register('GetOpenapiTaskGenerationRequestList')
def GetOpenapiTaskGenerationRequestList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOpenapiTaskGenerationRequestList(body=body, **kwargs)

@register('GetOpenapiTaskGenerationRequestByMoid')
def GetOpenapiTaskGenerationRequestByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOpenapiTaskGenerationRequestByMoid(body=body, **kwargs)

@register('GetOpenapiTaskGenerationResultList')
def GetOpenapiTaskGenerationResultList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOpenapiTaskGenerationResultList(body=body, **kwargs)

@register('GetOpenapiTaskGenerationResultByMoid')
def GetOpenapiTaskGenerationResultByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOpenapiTaskGenerationResultByMoid(body=body, **kwargs)

@register('GetOprsDeploymentList')
def GetOprsDeploymentList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOprsDeploymentList(body=body, **kwargs)

@register('GetOprsDeploymentByMoid')
def GetOprsDeploymentByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOprsDeploymentByMoid(body=body, **kwargs)

@register('GetOprsSyncTargetListMessageList')
def GetOprsSyncTargetListMessageList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOprsSyncTargetListMessageList(body=body, **kwargs)

@register('GetOprsSyncTargetListMessageByMoid')
def GetOprsSyncTargetListMessageByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOprsSyncTargetListMessageByMoid(body=body, **kwargs)

@register('GetOrganizationOrganizationList')
def GetOrganizationOrganizationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOrganizationOrganizationList(body=body, **kwargs)

@register('GetOrganizationOrganizationByMoid')
def GetOrganizationOrganizationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOrganizationOrganizationByMoid(body=body, **kwargs)

@register('GetOsBulkInstallInfoList')
def GetOsBulkInstallInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOsBulkInstallInfoList(body=body, **kwargs)

@register('GetOsBulkInstallInfoByMoid')
def GetOsBulkInstallInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOsBulkInstallInfoByMoid(body=body, **kwargs)

@register('GetOsCatalogList')
def GetOsCatalogList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOsCatalogList(body=body, **kwargs)

@register('GetOsCatalogByMoid')
def GetOsCatalogByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOsCatalogByMoid(body=body, **kwargs)

@register('GetOsConfigurationFileList')
def GetOsConfigurationFileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOsConfigurationFileList(body=body, **kwargs)

@register('GetOsConfigurationFileByMoid')
def GetOsConfigurationFileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOsConfigurationFileByMoid(body=body, **kwargs)

@register('GetOsDistributionList')
def GetOsDistributionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOsDistributionList(body=body, **kwargs)

@register('GetOsDistributionByMoid')
def GetOsDistributionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOsDistributionByMoid(body=body, **kwargs)

@register('GetOsInstallList')
def GetOsInstallList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOsInstallList(body=body, **kwargs)

@register('GetOsInstallByMoid')
def GetOsInstallByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOsInstallByMoid(body=body, **kwargs)

@register('GetOsSupportedVersionList')
def GetOsSupportedVersionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOsSupportedVersionList(body=body, **kwargs)

@register('GetOsSupportedVersionByMoid')
def GetOsSupportedVersionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOsSupportedVersionByMoid(body=body, **kwargs)

@register('GetOsValidRemoteTargetList')
def GetOsValidRemoteTargetList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOsValidRemoteTargetList(body=body, **kwargs)

@register('GetOsValidRemoteTargetByMoid')
def GetOsValidRemoteTargetByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetOsValidRemoteTargetByMoid(body=body, **kwargs)

@register('GetPartnerintegrationDcLogsList')
def GetPartnerintegrationDcLogsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPartnerintegrationDcLogsList(body=body, **kwargs)

@register('GetPartnerintegrationDcLogsByMoid')
def GetPartnerintegrationDcLogsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPartnerintegrationDcLogsByMoid(body=body, **kwargs)

@register('GetPartnerintegrationDeviceConnectorList')
def GetPartnerintegrationDeviceConnectorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPartnerintegrationDeviceConnectorList(body=body, **kwargs)

@register('GetPartnerintegrationDeviceConnectorByMoid')
def GetPartnerintegrationDeviceConnectorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPartnerintegrationDeviceConnectorByMoid(body=body, **kwargs)

@register('GetPartnerintegrationDocIssuesList')
def GetPartnerintegrationDocIssuesList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPartnerintegrationDocIssuesList(body=body, **kwargs)

@register('GetPartnerintegrationDocIssuesByMoid')
def GetPartnerintegrationDocIssuesByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPartnerintegrationDocIssuesByMoid(body=body, **kwargs)

@register('GetPartnerintegrationEtlList')
def GetPartnerintegrationEtlList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPartnerintegrationEtlList(body=body, **kwargs)

@register('GetPartnerintegrationEtlByMoid')
def GetPartnerintegrationEtlByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPartnerintegrationEtlByMoid(body=body, **kwargs)

@register('GetPartnerintegrationFileList')
def GetPartnerintegrationFileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPartnerintegrationFileList(body=body, **kwargs)

@register('GetPartnerintegrationFileByMoid')
def GetPartnerintegrationFileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPartnerintegrationFileByMoid(body=body, **kwargs)

@register('GetPartnerintegrationInventoryList')
def GetPartnerintegrationInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPartnerintegrationInventoryList(body=body, **kwargs)

@register('GetPartnerintegrationInventoryByMoid')
def GetPartnerintegrationInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPartnerintegrationInventoryByMoid(body=body, **kwargs)

@register('GetPartnerintegrationLogsList')
def GetPartnerintegrationLogsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPartnerintegrationLogsList(body=body, **kwargs)

@register('GetPartnerintegrationLogsByMoid')
def GetPartnerintegrationLogsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPartnerintegrationLogsByMoid(body=body, **kwargs)

@register('GetPartnerintegrationMetricsList')
def GetPartnerintegrationMetricsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPartnerintegrationMetricsList(body=body, **kwargs)

@register('GetPartnerintegrationMetricsByMoid')
def GetPartnerintegrationMetricsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPartnerintegrationMetricsByMoid(body=body, **kwargs)

@register('GetPartnerintegrationModelList')
def GetPartnerintegrationModelList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPartnerintegrationModelList(body=body, **kwargs)

@register('GetPartnerintegrationModelByMoid')
def GetPartnerintegrationModelByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPartnerintegrationModelByMoid(body=body, **kwargs)

@register('GetPciCoprocessorCardList')
def GetPciCoprocessorCardList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPciCoprocessorCardList(body=body, **kwargs)

@register('GetPciCoprocessorCardByMoid')
def GetPciCoprocessorCardByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPciCoprocessorCardByMoid(body=body, **kwargs)

@register('GetPciDeviceList')
def GetPciDeviceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPciDeviceList(body=body, **kwargs)

@register('GetPciDeviceByMoid')
def GetPciDeviceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPciDeviceByMoid(body=body, **kwargs)

@register('GetPciLinkList')
def GetPciLinkList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPciLinkList(body=body, **kwargs)

@register('GetPciLinkByMoid')
def GetPciLinkByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPciLinkByMoid(body=body, **kwargs)

@register('GetPciNodeList')
def GetPciNodeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPciNodeList(body=body, **kwargs)

@register('GetPciNodeByMoid')
def GetPciNodeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPciNodeByMoid(body=body, **kwargs)

@register('GetPciSwitchList')
def GetPciSwitchList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPciSwitchList(body=body, **kwargs)

@register('GetPciSwitchByMoid')
def GetPciSwitchByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPciSwitchByMoid(body=body, **kwargs)

@register('GetPortGroupList')
def GetPortGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPortGroupList(body=body, **kwargs)

@register('GetPortGroupByMoid')
def GetPortGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPortGroupByMoid(body=body, **kwargs)

@register('GetPortMacBindingList')
def GetPortMacBindingList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPortMacBindingList(body=body, **kwargs)

@register('GetPortMacBindingByMoid')
def GetPortMacBindingByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPortMacBindingByMoid(body=body, **kwargs)

@register('GetPortSubGroupList')
def GetPortSubGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPortSubGroupList(body=body, **kwargs)

@register('GetPortSubGroupByMoid')
def GetPortSubGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPortSubGroupByMoid(body=body, **kwargs)

@register('GetPowerControlStateList')
def GetPowerControlStateList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPowerControlStateList(body=body, **kwargs)

@register('GetPowerControlStateByMoid')
def GetPowerControlStateByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPowerControlStateByMoid(body=body, **kwargs)

@register('GetPowerPolicyList')
def GetPowerPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPowerPolicyList(body=body, **kwargs)

@register('GetPowerPolicyByMoid')
def GetPowerPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPowerPolicyByMoid(body=body, **kwargs)

@register('GetPowerPolicyInventoryList')
def GetPowerPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPowerPolicyInventoryList(body=body, **kwargs)

@register('GetPowerPolicyInventoryByMoid')
def GetPowerPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetPowerPolicyInventoryByMoid(body=body, **kwargs)

@register('GetProcessorUnitList')
def GetProcessorUnitList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetProcessorUnitList(body=body, **kwargs)

@register('GetProcessorUnitByMoid')
def GetProcessorUnitByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetProcessorUnitByMoid(body=body, **kwargs)

@register('GetRackUnitPersonalityList')
def GetRackUnitPersonalityList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRackUnitPersonalityList(body=body, **kwargs)

@register('GetRackUnitPersonalityByMoid')
def GetRackUnitPersonalityByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRackUnitPersonalityByMoid(body=body, **kwargs)

@register('GetRecommendationCapacityRunwayList')
def GetRecommendationCapacityRunwayList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecommendationCapacityRunwayList(body=body, **kwargs)

@register('GetRecommendationCapacityRunwayByMoid')
def GetRecommendationCapacityRunwayByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecommendationCapacityRunwayByMoid(body=body, **kwargs)

@register('GetRecommendationClusterExpansionList')
def GetRecommendationClusterExpansionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecommendationClusterExpansionList(body=body, **kwargs)

@register('GetRecommendationClusterExpansionByMoid')
def GetRecommendationClusterExpansionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecommendationClusterExpansionByMoid(body=body, **kwargs)

@register('GetRecommendationHardwareExpansionRequestList')
def GetRecommendationHardwareExpansionRequestList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecommendationHardwareExpansionRequestList(body=body, **kwargs)

@register('GetRecommendationHardwareExpansionRequestByMoid')
def GetRecommendationHardwareExpansionRequestByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecommendationHardwareExpansionRequestByMoid(body=body, **kwargs)

@register('GetRecommendationHardwareExpansionRequestItemList')
def GetRecommendationHardwareExpansionRequestItemList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecommendationHardwareExpansionRequestItemList(body=body, **kwargs)

@register('GetRecommendationHardwareExpansionRequestItemByMoid')
def GetRecommendationHardwareExpansionRequestItemByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecommendationHardwareExpansionRequestItemByMoid(body=body, **kwargs)

@register('GetRecommendationPhysicalItemList')
def GetRecommendationPhysicalItemList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecommendationPhysicalItemList(body=body, **kwargs)

@register('GetRecommendationPhysicalItemByMoid')
def GetRecommendationPhysicalItemByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecommendationPhysicalItemByMoid(body=body, **kwargs)

@register('GetRecommendationPurchaseOrderEstimateList')
def GetRecommendationPurchaseOrderEstimateList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecommendationPurchaseOrderEstimateList(body=body, **kwargs)

@register('GetRecommendationPurchaseOrderEstimateByMoid')
def GetRecommendationPurchaseOrderEstimateByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecommendationPurchaseOrderEstimateByMoid(body=body, **kwargs)

@register('GetRecommendationPurchaseOrderListList')
def GetRecommendationPurchaseOrderListList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecommendationPurchaseOrderListList(body=body, **kwargs)

@register('GetRecommendationPurchaseOrderListByMoid')
def GetRecommendationPurchaseOrderListByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecommendationPurchaseOrderListByMoid(body=body, **kwargs)

@register('GetRecommendationSoftwareItemList')
def GetRecommendationSoftwareItemList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecommendationSoftwareItemList(body=body, **kwargs)

@register('GetRecommendationSoftwareItemByMoid')
def GetRecommendationSoftwareItemByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecommendationSoftwareItemByMoid(body=body, **kwargs)

@register('GetRecoveryBackupConfigPolicyList')
def GetRecoveryBackupConfigPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecoveryBackupConfigPolicyList(body=body, **kwargs)

@register('GetRecoveryBackupConfigPolicyByMoid')
def GetRecoveryBackupConfigPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecoveryBackupConfigPolicyByMoid(body=body, **kwargs)

@register('GetRecoveryBackupProfileList')
def GetRecoveryBackupProfileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecoveryBackupProfileList(body=body, **kwargs)

@register('GetRecoveryBackupProfileByMoid')
def GetRecoveryBackupProfileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecoveryBackupProfileByMoid(body=body, **kwargs)

@register('GetRecoveryConfigResultList')
def GetRecoveryConfigResultList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecoveryConfigResultList(body=body, **kwargs)

@register('GetRecoveryConfigResultByMoid')
def GetRecoveryConfigResultByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecoveryConfigResultByMoid(body=body, **kwargs)

@register('GetRecoveryConfigResultEntryList')
def GetRecoveryConfigResultEntryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecoveryConfigResultEntryList(body=body, **kwargs)

@register('GetRecoveryConfigResultEntryByMoid')
def GetRecoveryConfigResultEntryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecoveryConfigResultEntryByMoid(body=body, **kwargs)

@register('GetRecoveryOnDemandBackupList')
def GetRecoveryOnDemandBackupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecoveryOnDemandBackupList(body=body, **kwargs)

@register('GetRecoveryOnDemandBackupByMoid')
def GetRecoveryOnDemandBackupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecoveryOnDemandBackupByMoid(body=body, **kwargs)

@register('GetRecoveryRestoreList')
def GetRecoveryRestoreList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecoveryRestoreList(body=body, **kwargs)

@register('GetRecoveryRestoreByMoid')
def GetRecoveryRestoreByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecoveryRestoreByMoid(body=body, **kwargs)

@register('GetRecoveryScheduleConfigPolicyList')
def GetRecoveryScheduleConfigPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecoveryScheduleConfigPolicyList(body=body, **kwargs)

@register('GetRecoveryScheduleConfigPolicyByMoid')
def GetRecoveryScheduleConfigPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetRecoveryScheduleConfigPolicyByMoid(body=body, **kwargs)

@register('GetResourceGroupList')
def GetResourceGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourceGroupList(body=body, **kwargs)

@register('GetResourceGroupByMoid')
def GetResourceGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourceGroupByMoid(body=body, **kwargs)

@register('GetResourceGroupMemberList')
def GetResourceGroupMemberList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourceGroupMemberList(body=body, **kwargs)

@register('GetResourceGroupMemberByMoid')
def GetResourceGroupMemberByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourceGroupMemberByMoid(body=body, **kwargs)

@register('GetResourceLicenseResourceCountList')
def GetResourceLicenseResourceCountList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourceLicenseResourceCountList(body=body, **kwargs)

@register('GetResourceLicenseResourceCountByMoid')
def GetResourceLicenseResourceCountByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourceLicenseResourceCountByMoid(body=body, **kwargs)

@register('GetResourceMembershipList')
def GetResourceMembershipList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourceMembershipList(body=body, **kwargs)

@register('GetResourceMembershipByMoid')
def GetResourceMembershipByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourceMembershipByMoid(body=body, **kwargs)

@register('GetResourceMembershipHolderList')
def GetResourceMembershipHolderList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourceMembershipHolderList(body=body, **kwargs)

@register('GetResourceMembershipHolderByMoid')
def GetResourceMembershipHolderByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourceMembershipHolderByMoid(body=body, **kwargs)

@register('GetResourceReservationList')
def GetResourceReservationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourceReservationList(body=body, **kwargs)

@register('GetResourceReservationByMoid')
def GetResourceReservationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourceReservationByMoid(body=body, **kwargs)

@register('GetResourceSelectionCriteriaList')
def GetResourceSelectionCriteriaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourceSelectionCriteriaList(body=body, **kwargs)

@register('GetResourceSelectionCriteriaByMoid')
def GetResourceSelectionCriteriaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourceSelectionCriteriaByMoid(body=body, **kwargs)

@register('GetResourceSharedResourcesInfoHolderList')
def GetResourceSharedResourcesInfoHolderList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourceSharedResourcesInfoHolderList(body=body, **kwargs)

@register('GetResourceSharedResourcesInfoHolderByMoid')
def GetResourceSharedResourcesInfoHolderByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourceSharedResourcesInfoHolderByMoid(body=body, **kwargs)

@register('GetResourcepoolLeaseList')
def GetResourcepoolLeaseList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourcepoolLeaseList(body=body, **kwargs)

@register('GetResourcepoolLeaseByMoid')
def GetResourcepoolLeaseByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourcepoolLeaseByMoid(body=body, **kwargs)

@register('GetResourcepoolLeaseResourceList')
def GetResourcepoolLeaseResourceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourcepoolLeaseResourceList(body=body, **kwargs)

@register('GetResourcepoolLeaseResourceByMoid')
def GetResourcepoolLeaseResourceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourcepoolLeaseResourceByMoid(body=body, **kwargs)

@register('GetResourcepoolMembershipReservationList')
def GetResourcepoolMembershipReservationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourcepoolMembershipReservationList(body=body, **kwargs)

@register('GetResourcepoolMembershipReservationByMoid')
def GetResourcepoolMembershipReservationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourcepoolMembershipReservationByMoid(body=body, **kwargs)

@register('GetResourcepoolPoolList')
def GetResourcepoolPoolList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourcepoolPoolList(body=body, **kwargs)

@register('GetResourcepoolPoolByMoid')
def GetResourcepoolPoolByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourcepoolPoolByMoid(body=body, **kwargs)

@register('GetResourcepoolPoolMemberList')
def GetResourcepoolPoolMemberList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourcepoolPoolMemberList(body=body, **kwargs)

@register('GetResourcepoolPoolMemberByMoid')
def GetResourcepoolPoolMemberByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourcepoolPoolMemberByMoid(body=body, **kwargs)

@register('GetResourcepoolQualificationPolicyList')
def GetResourcepoolQualificationPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourcepoolQualificationPolicyList(body=body, **kwargs)

@register('GetResourcepoolQualificationPolicyByMoid')
def GetResourcepoolQualificationPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourcepoolQualificationPolicyByMoid(body=body, **kwargs)

@register('GetResourcepoolUniverseList')
def GetResourcepoolUniverseList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourcepoolUniverseList(body=body, **kwargs)

@register('GetResourcepoolUniverseByMoid')
def GetResourcepoolUniverseByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetResourcepoolUniverseByMoid(body=body, **kwargs)

@register('GetSchedulerTaskResultList')
def GetSchedulerTaskResultList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSchedulerTaskResultList(body=body, **kwargs)

@register('GetSchedulerTaskResultByMoid')
def GetSchedulerTaskResultByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSchedulerTaskResultByMoid(body=body, **kwargs)

@register('GetSchedulerTaskScheduleList')
def GetSchedulerTaskScheduleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSchedulerTaskScheduleList(body=body, **kwargs)

@register('GetSchedulerTaskScheduleByMoid')
def GetSchedulerTaskScheduleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSchedulerTaskScheduleByMoid(body=body, **kwargs)

@register('GetSdaaciConnectionList')
def GetSdaaciConnectionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSdaaciConnectionList(body=body, **kwargs)

@register('GetSdaaciConnectionByMoid')
def GetSdaaciConnectionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSdaaciConnectionByMoid(body=body, **kwargs)

@register('GetSdaaciConnectionDetailList')
def GetSdaaciConnectionDetailList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSdaaciConnectionDetailList(body=body, **kwargs)

@register('GetSdaaciConnectionDetailByMoid')
def GetSdaaciConnectionDetailByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSdaaciConnectionDetailByMoid(body=body, **kwargs)

@register('GetSdcardPolicyList')
def GetSdcardPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSdcardPolicyList(body=body, **kwargs)

@register('GetSdcardPolicyByMoid')
def GetSdcardPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSdcardPolicyByMoid(body=body, **kwargs)

@register('GetSdcardPolicyInventoryList')
def GetSdcardPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSdcardPolicyInventoryList(body=body, **kwargs)

@register('GetSdcardPolicyInventoryByMoid')
def GetSdcardPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSdcardPolicyInventoryByMoid(body=body, **kwargs)

@register('GetSearchSearchItemList')
def GetSearchSearchItemList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSearchSearchItemList(body=body, **kwargs)

@register('GetSearchSearchItemByMoid')
def GetSearchSearchItemByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSearchSearchItemByMoid(body=body, **kwargs)

@register('GetSearchTagItemList')
def GetSearchTagItemList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSearchTagItemList(body=body, **kwargs)

@register('GetSearchTagItemByMoid')
def GetSearchTagItemByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSearchTagItemByMoid(body=body, **kwargs)

@register('GetSecurityUnitList')
def GetSecurityUnitList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSecurityUnitList(body=body, **kwargs)

@register('GetSecurityUnitByMoid')
def GetSecurityUnitByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSecurityUnitByMoid(body=body, **kwargs)

@register('GetServerConfigChangeDetailList')
def GetServerConfigChangeDetailList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServerConfigChangeDetailList(body=body, **kwargs)

@register('GetServerConfigChangeDetailByMoid')
def GetServerConfigChangeDetailByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServerConfigChangeDetailByMoid(body=body, **kwargs)

@register('GetServerConfigImportList')
def GetServerConfigImportList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServerConfigImportList(body=body, **kwargs)

@register('GetServerConfigImportByMoid')
def GetServerConfigImportByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServerConfigImportByMoid(body=body, **kwargs)

@register('GetServerConfigResultList')
def GetServerConfigResultList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServerConfigResultList(body=body, **kwargs)

@register('GetServerConfigResultByMoid')
def GetServerConfigResultByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServerConfigResultByMoid(body=body, **kwargs)

@register('GetServerConfigResultEntryList')
def GetServerConfigResultEntryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServerConfigResultEntryList(body=body, **kwargs)

@register('GetServerConfigResultEntryByMoid')
def GetServerConfigResultEntryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServerConfigResultEntryByMoid(body=body, **kwargs)

@register('GetServerDisruptionList')
def GetServerDisruptionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServerDisruptionList(body=body, **kwargs)

@register('GetServerDisruptionByMoid')
def GetServerDisruptionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServerDisruptionByMoid(body=body, **kwargs)

@register('GetServerProfileList')
def GetServerProfileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServerProfileList(body=body, **kwargs)

@register('GetServerProfileByMoid')
def GetServerProfileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServerProfileByMoid(body=body, **kwargs)

@register('GetServerProfileTemplateList')
def GetServerProfileTemplateList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServerProfileTemplateList(body=body, **kwargs)

@register('GetServerProfileTemplateByMoid')
def GetServerProfileTemplateByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServerProfileTemplateByMoid(body=body, **kwargs)

@register('GetServicenowChangeRequestList')
def GetServicenowChangeRequestList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServicenowChangeRequestList(body=body, **kwargs)

@register('GetServicenowChangeRequestByMoid')
def GetServicenowChangeRequestByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServicenowChangeRequestByMoid(body=body, **kwargs)

@register('GetServicenowChangeRequestDocList')
def GetServicenowChangeRequestDocList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServicenowChangeRequestDocList(body=body, **kwargs)

@register('GetServicenowChangeRequestDocByMoid')
def GetServicenowChangeRequestDocByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServicenowChangeRequestDocByMoid(body=body, **kwargs)

@register('GetServicenowIncidentList')
def GetServicenowIncidentList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServicenowIncidentList(body=body, **kwargs)

@register('GetServicenowIncidentByMoid')
def GetServicenowIncidentByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServicenowIncidentByMoid(body=body, **kwargs)

@register('GetServicenowIncidentDocList')
def GetServicenowIncidentDocList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServicenowIncidentDocList(body=body, **kwargs)

@register('GetServicenowIncidentDocByMoid')
def GetServicenowIncidentDocByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetServicenowIncidentDocByMoid(body=body, **kwargs)

@register('GetSmtpPolicyList')
def GetSmtpPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSmtpPolicyList(body=body, **kwargs)

@register('GetSmtpPolicyByMoid')
def GetSmtpPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSmtpPolicyByMoid(body=body, **kwargs)

@register('GetSmtpPolicyTestList')
def GetSmtpPolicyTestList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSmtpPolicyTestList(body=body, **kwargs)

@register('GetSmtpPolicyTestByMoid')
def GetSmtpPolicyTestByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSmtpPolicyTestByMoid(body=body, **kwargs)

@register('GetSnmpPolicyList')
def GetSnmpPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSnmpPolicyList(body=body, **kwargs)

@register('GetSnmpPolicyByMoid')
def GetSnmpPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSnmpPolicyByMoid(body=body, **kwargs)

@register('GetSnmpPolicyInventoryList')
def GetSnmpPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSnmpPolicyInventoryList(body=body, **kwargs)

@register('GetSnmpPolicyInventoryByMoid')
def GetSnmpPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSnmpPolicyInventoryByMoid(body=body, **kwargs)

@register('GetSoftwareApplianceDistributableList')
def GetSoftwareApplianceDistributableList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareApplianceDistributableList(body=body, **kwargs)

@register('GetSoftwareApplianceDistributableByMoid')
def GetSoftwareApplianceDistributableByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareApplianceDistributableByMoid(body=body, **kwargs)

@register('GetSoftwareDownloadHistoryList')
def GetSoftwareDownloadHistoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareDownloadHistoryList(body=body, **kwargs)

@register('GetSoftwareDownloadHistoryByMoid')
def GetSoftwareDownloadHistoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareDownloadHistoryByMoid(body=body, **kwargs)

@register('GetSoftwareHciBundleDistributableList')
def GetSoftwareHciBundleDistributableList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareHciBundleDistributableList(body=body, **kwargs)

@register('GetSoftwareHciBundleDistributableByMoid')
def GetSoftwareHciBundleDistributableByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareHciBundleDistributableByMoid(body=body, **kwargs)

@register('GetSoftwareHciDistributableList')
def GetSoftwareHciDistributableList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareHciDistributableList(body=body, **kwargs)

@register('GetSoftwareHciDistributableByMoid')
def GetSoftwareHciDistributableByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareHciDistributableByMoid(body=body, **kwargs)

@register('GetSoftwareHclMetaList')
def GetSoftwareHclMetaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareHclMetaList(body=body, **kwargs)

@register('GetSoftwareHclMetaByMoid')
def GetSoftwareHclMetaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareHclMetaByMoid(body=body, **kwargs)

@register('GetSoftwareHyperflexBundleDistributableList')
def GetSoftwareHyperflexBundleDistributableList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareHyperflexBundleDistributableList(body=body, **kwargs)

@register('GetSoftwareHyperflexBundleDistributableByMoid')
def GetSoftwareHyperflexBundleDistributableByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareHyperflexBundleDistributableByMoid(body=body, **kwargs)

@register('GetSoftwareHyperflexDistributableList')
def GetSoftwareHyperflexDistributableList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareHyperflexDistributableList(body=body, **kwargs)

@register('GetSoftwareHyperflexDistributableByMoid')
def GetSoftwareHyperflexDistributableByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareHyperflexDistributableByMoid(body=body, **kwargs)

@register('GetSoftwareIksBundleDistributableList')
def GetSoftwareIksBundleDistributableList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareIksBundleDistributableList(body=body, **kwargs)

@register('GetSoftwareIksBundleDistributableByMoid')
def GetSoftwareIksBundleDistributableByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareIksBundleDistributableByMoid(body=body, **kwargs)

@register('GetSoftwareReleaseMetaList')
def GetSoftwareReleaseMetaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareReleaseMetaList(body=body, **kwargs)

@register('GetSoftwareReleaseMetaByMoid')
def GetSoftwareReleaseMetaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareReleaseMetaByMoid(body=body, **kwargs)

@register('GetSoftwareSolutionDistributableList')
def GetSoftwareSolutionDistributableList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareSolutionDistributableList(body=body, **kwargs)

@register('GetSoftwareSolutionDistributableByMoid')
def GetSoftwareSolutionDistributableByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareSolutionDistributableByMoid(body=body, **kwargs)

@register('GetSoftwareUcsdBundleDistributableList')
def GetSoftwareUcsdBundleDistributableList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareUcsdBundleDistributableList(body=body, **kwargs)

@register('GetSoftwareUcsdBundleDistributableByMoid')
def GetSoftwareUcsdBundleDistributableByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareUcsdBundleDistributableByMoid(body=body, **kwargs)

@register('GetSoftwareUcsdDistributableList')
def GetSoftwareUcsdDistributableList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareUcsdDistributableList(body=body, **kwargs)

@register('GetSoftwareUcsdDistributableByMoid')
def GetSoftwareUcsdDistributableByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwareUcsdDistributableByMoid(body=body, **kwargs)

@register('GetSoftwarerepositoryAuthorizationList')
def GetSoftwarerepositoryAuthorizationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwarerepositoryAuthorizationList(body=body, **kwargs)

@register('GetSoftwarerepositoryAuthorizationByMoid')
def GetSoftwarerepositoryAuthorizationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwarerepositoryAuthorizationByMoid(body=body, **kwargs)

@register('GetSoftwarerepositoryCachedImageList')
def GetSoftwarerepositoryCachedImageList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwarerepositoryCachedImageList(body=body, **kwargs)

@register('GetSoftwarerepositoryCachedImageByMoid')
def GetSoftwarerepositoryCachedImageByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwarerepositoryCachedImageByMoid(body=body, **kwargs)

@register('GetSoftwarerepositoryCatalogList')
def GetSoftwarerepositoryCatalogList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwarerepositoryCatalogList(body=body, **kwargs)

@register('GetSoftwarerepositoryCatalogByMoid')
def GetSoftwarerepositoryCatalogByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwarerepositoryCatalogByMoid(body=body, **kwargs)

@register('GetSoftwarerepositoryCategoryMapperList')
def GetSoftwarerepositoryCategoryMapperList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwarerepositoryCategoryMapperList(body=body, **kwargs)

@register('GetSoftwarerepositoryCategoryMapperByMoid')
def GetSoftwarerepositoryCategoryMapperByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwarerepositoryCategoryMapperByMoid(body=body, **kwargs)

@register('GetSoftwarerepositoryCategoryMapperModelList')
def GetSoftwarerepositoryCategoryMapperModelList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwarerepositoryCategoryMapperModelList(body=body, **kwargs)

@register('GetSoftwarerepositoryCategoryMapperModelByMoid')
def GetSoftwarerepositoryCategoryMapperModelByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwarerepositoryCategoryMapperModelByMoid(body=body, **kwargs)

@register('GetSoftwarerepositoryCategorySupportConstraintList')
def GetSoftwarerepositoryCategorySupportConstraintList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwarerepositoryCategorySupportConstraintList(body=body, **kwargs)

@register('GetSoftwarerepositoryCategorySupportConstraintByMoid')
def GetSoftwarerepositoryCategorySupportConstraintByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwarerepositoryCategorySupportConstraintByMoid(body=body, **kwargs)

@register('GetSoftwarerepositoryCategoryUnsupportedModelsList')
def GetSoftwarerepositoryCategoryUnsupportedModelsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwarerepositoryCategoryUnsupportedModelsList(body=body, **kwargs)

@register('GetSoftwarerepositoryCategoryUnsupportedModelsByMoid')
def GetSoftwarerepositoryCategoryUnsupportedModelsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwarerepositoryCategoryUnsupportedModelsByMoid(body=body, **kwargs)

@register('GetSoftwarerepositoryDownloadSpecList')
def GetSoftwarerepositoryDownloadSpecList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwarerepositoryDownloadSpecList(body=body, **kwargs)

@register('GetSoftwarerepositoryDownloadSpecByMoid')
def GetSoftwarerepositoryDownloadSpecByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwarerepositoryDownloadSpecByMoid(body=body, **kwargs)

@register('GetSoftwarerepositoryOperatingSystemFileList')
def GetSoftwarerepositoryOperatingSystemFileList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwarerepositoryOperatingSystemFileList(body=body, **kwargs)

@register('GetSoftwarerepositoryOperatingSystemFileByMoid')
def GetSoftwarerepositoryOperatingSystemFileByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwarerepositoryOperatingSystemFileByMoid(body=body, **kwargs)

@register('GetSoftwarerepositoryReleaseList')
def GetSoftwarerepositoryReleaseList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwarerepositoryReleaseList(body=body, **kwargs)

@register('GetSoftwarerepositoryReleaseByMoid')
def GetSoftwarerepositoryReleaseByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSoftwarerepositoryReleaseByMoid(body=body, **kwargs)

@register('GetSolPolicyList')
def GetSolPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSolPolicyList(body=body, **kwargs)

@register('GetSolPolicyByMoid')
def GetSolPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSolPolicyByMoid(body=body, **kwargs)

@register('GetSolPolicyInventoryList')
def GetSolPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSolPolicyInventoryList(body=body, **kwargs)

@register('GetSolPolicyInventoryByMoid')
def GetSolPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSolPolicyInventoryByMoid(body=body, **kwargs)

@register('GetSshPolicyList')
def GetSshPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSshPolicyList(body=body, **kwargs)

@register('GetSshPolicyByMoid')
def GetSshPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSshPolicyByMoid(body=body, **kwargs)

@register('GetSshPolicyInventoryList')
def GetSshPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSshPolicyInventoryList(body=body, **kwargs)

@register('GetSshPolicyInventoryByMoid')
def GetSshPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSshPolicyInventoryByMoid(body=body, **kwargs)

@register('GetStorageBatteryBackupUnitList')
def GetStorageBatteryBackupUnitList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageBatteryBackupUnitList(body=body, **kwargs)

@register('GetStorageBatteryBackupUnitByMoid')
def GetStorageBatteryBackupUnitByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageBatteryBackupUnitByMoid(body=body, **kwargs)

@register('GetStorageControllerList')
def GetStorageControllerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageControllerList(body=body, **kwargs)

@register('GetStorageControllerByMoid')
def GetStorageControllerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageControllerByMoid(body=body, **kwargs)

@register('GetStorageControllerDriveList')
def GetStorageControllerDriveList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageControllerDriveList(body=body, **kwargs)

@register('GetStorageControllerDriveByMoid')
def GetStorageControllerDriveByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageControllerDriveByMoid(body=body, **kwargs)

@register('GetStorageDiskGroupList')
def GetStorageDiskGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageDiskGroupList(body=body, **kwargs)

@register('GetStorageDiskGroupByMoid')
def GetStorageDiskGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageDiskGroupByMoid(body=body, **kwargs)

@register('GetStorageDiskSlotList')
def GetStorageDiskSlotList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageDiskSlotList(body=body, **kwargs)

@register('GetStorageDiskSlotByMoid')
def GetStorageDiskSlotByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageDiskSlotByMoid(body=body, **kwargs)

@register('GetStorageDriveGroupList')
def GetStorageDriveGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageDriveGroupList(body=body, **kwargs)

@register('GetStorageDriveGroupByMoid')
def GetStorageDriveGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageDriveGroupByMoid(body=body, **kwargs)

@register('GetStorageDriveSecurityPolicyList')
def GetStorageDriveSecurityPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageDriveSecurityPolicyList(body=body, **kwargs)

@register('GetStorageDriveSecurityPolicyByMoid')
def GetStorageDriveSecurityPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageDriveSecurityPolicyByMoid(body=body, **kwargs)

@register('GetStorageEnclosureList')
def GetStorageEnclosureList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageEnclosureList(body=body, **kwargs)

@register('GetStorageEnclosureByMoid')
def GetStorageEnclosureByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageEnclosureByMoid(body=body, **kwargs)

@register('GetStorageEnclosureDiskList')
def GetStorageEnclosureDiskList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageEnclosureDiskList(body=body, **kwargs)

@register('GetStorageEnclosureDiskByMoid')
def GetStorageEnclosureDiskByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageEnclosureDiskByMoid(body=body, **kwargs)

@register('GetStorageEnclosureDiskSlotEpList')
def GetStorageEnclosureDiskSlotEpList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageEnclosureDiskSlotEpList(body=body, **kwargs)

@register('GetStorageEnclosureDiskSlotEpByMoid')
def GetStorageEnclosureDiskSlotEpByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageEnclosureDiskSlotEpByMoid(body=body, **kwargs)

@register('GetStorageFileItemList')
def GetStorageFileItemList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageFileItemList(body=body, **kwargs)

@register('GetStorageFileItemByMoid')
def GetStorageFileItemByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageFileItemByMoid(body=body, **kwargs)

@register('GetStorageFlexFlashControllerList')
def GetStorageFlexFlashControllerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageFlexFlashControllerList(body=body, **kwargs)

@register('GetStorageFlexFlashControllerByMoid')
def GetStorageFlexFlashControllerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageFlexFlashControllerByMoid(body=body, **kwargs)

@register('GetStorageFlexFlashControllerPropsList')
def GetStorageFlexFlashControllerPropsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageFlexFlashControllerPropsList(body=body, **kwargs)

@register('GetStorageFlexFlashControllerPropsByMoid')
def GetStorageFlexFlashControllerPropsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageFlexFlashControllerPropsByMoid(body=body, **kwargs)

@register('GetStorageFlexFlashPhysicalDriveList')
def GetStorageFlexFlashPhysicalDriveList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageFlexFlashPhysicalDriveList(body=body, **kwargs)

@register('GetStorageFlexFlashPhysicalDriveByMoid')
def GetStorageFlexFlashPhysicalDriveByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageFlexFlashPhysicalDriveByMoid(body=body, **kwargs)

@register('GetStorageFlexFlashVirtualDriveList')
def GetStorageFlexFlashVirtualDriveList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageFlexFlashVirtualDriveList(body=body, **kwargs)

@register('GetStorageFlexFlashVirtualDriveByMoid')
def GetStorageFlexFlashVirtualDriveByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageFlexFlashVirtualDriveByMoid(body=body, **kwargs)

@register('GetStorageFlexUtilControllerList')
def GetStorageFlexUtilControllerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageFlexUtilControllerList(body=body, **kwargs)

@register('GetStorageFlexUtilControllerByMoid')
def GetStorageFlexUtilControllerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageFlexUtilControllerByMoid(body=body, **kwargs)

@register('GetStorageFlexUtilPhysicalDriveList')
def GetStorageFlexUtilPhysicalDriveList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageFlexUtilPhysicalDriveList(body=body, **kwargs)

@register('GetStorageFlexUtilPhysicalDriveByMoid')
def GetStorageFlexUtilPhysicalDriveByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageFlexUtilPhysicalDriveByMoid(body=body, **kwargs)

@register('GetStorageFlexUtilVirtualDriveList')
def GetStorageFlexUtilVirtualDriveList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageFlexUtilVirtualDriveList(body=body, **kwargs)

@register('GetStorageFlexUtilVirtualDriveByMoid')
def GetStorageFlexUtilVirtualDriveByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageFlexUtilVirtualDriveByMoid(body=body, **kwargs)

@register('GetStorageHitachiArrayList')
def GetStorageHitachiArrayList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiArrayList(body=body, **kwargs)

@register('GetStorageHitachiArrayByMoid')
def GetStorageHitachiArrayByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiArrayByMoid(body=body, **kwargs)

@register('GetStorageHitachiControllerList')
def GetStorageHitachiControllerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiControllerList(body=body, **kwargs)

@register('GetStorageHitachiControllerByMoid')
def GetStorageHitachiControllerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiControllerByMoid(body=body, **kwargs)

@register('GetStorageHitachiDiskList')
def GetStorageHitachiDiskList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiDiskList(body=body, **kwargs)

@register('GetStorageHitachiDiskByMoid')
def GetStorageHitachiDiskByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiDiskByMoid(body=body, **kwargs)

@register('GetStorageHitachiExternalParityGroupList')
def GetStorageHitachiExternalParityGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiExternalParityGroupList(body=body, **kwargs)

@register('GetStorageHitachiExternalParityGroupByMoid')
def GetStorageHitachiExternalParityGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiExternalParityGroupByMoid(body=body, **kwargs)

@register('GetStorageHitachiExternalPathGroupList')
def GetStorageHitachiExternalPathGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiExternalPathGroupList(body=body, **kwargs)

@register('GetStorageHitachiExternalPathGroupByMoid')
def GetStorageHitachiExternalPathGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiExternalPathGroupByMoid(body=body, **kwargs)

@register('GetStorageHitachiExternalStorageLunList')
def GetStorageHitachiExternalStorageLunList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiExternalStorageLunList(body=body, **kwargs)

@register('GetStorageHitachiExternalStorageLunByMoid')
def GetStorageHitachiExternalStorageLunByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiExternalStorageLunByMoid(body=body, **kwargs)

@register('GetStorageHitachiExternalStoragePortList')
def GetStorageHitachiExternalStoragePortList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiExternalStoragePortList(body=body, **kwargs)

@register('GetStorageHitachiExternalStoragePortByMoid')
def GetStorageHitachiExternalStoragePortByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiExternalStoragePortByMoid(body=body, **kwargs)

@register('GetStorageHitachiHostList')
def GetStorageHitachiHostList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiHostList(body=body, **kwargs)

@register('GetStorageHitachiHostByMoid')
def GetStorageHitachiHostByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiHostByMoid(body=body, **kwargs)

@register('GetStorageHitachiHostLunList')
def GetStorageHitachiHostLunList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiHostLunList(body=body, **kwargs)

@register('GetStorageHitachiHostLunByMoid')
def GetStorageHitachiHostLunByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiHostLunByMoid(body=body, **kwargs)

@register('GetStorageHitachiNvmSubsystemList')
def GetStorageHitachiNvmSubsystemList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiNvmSubsystemList(body=body, **kwargs)

@register('GetStorageHitachiNvmSubsystemByMoid')
def GetStorageHitachiNvmSubsystemByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiNvmSubsystemByMoid(body=body, **kwargs)

@register('GetStorageHitachiParityGroupList')
def GetStorageHitachiParityGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiParityGroupList(body=body, **kwargs)

@register('GetStorageHitachiParityGroupByMoid')
def GetStorageHitachiParityGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiParityGroupByMoid(body=body, **kwargs)

@register('GetStorageHitachiPoolList')
def GetStorageHitachiPoolList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiPoolList(body=body, **kwargs)

@register('GetStorageHitachiPoolByMoid')
def GetStorageHitachiPoolByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiPoolByMoid(body=body, **kwargs)

@register('GetStorageHitachiPortList')
def GetStorageHitachiPortList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiPortList(body=body, **kwargs)

@register('GetStorageHitachiPortByMoid')
def GetStorageHitachiPortByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiPortByMoid(body=body, **kwargs)

@register('GetStorageHitachiRemoteCopyPairGadList')
def GetStorageHitachiRemoteCopyPairGadList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiRemoteCopyPairGadList(body=body, **kwargs)

@register('GetStorageHitachiRemoteCopyPairGadByMoid')
def GetStorageHitachiRemoteCopyPairGadByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiRemoteCopyPairGadByMoid(body=body, **kwargs)

@register('GetStorageHitachiRemoteCopyPairTcList')
def GetStorageHitachiRemoteCopyPairTcList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiRemoteCopyPairTcList(body=body, **kwargs)

@register('GetStorageHitachiRemoteCopyPairTcByMoid')
def GetStorageHitachiRemoteCopyPairTcByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiRemoteCopyPairTcByMoid(body=body, **kwargs)

@register('GetStorageHitachiRemoteCopyPairUrList')
def GetStorageHitachiRemoteCopyPairUrList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiRemoteCopyPairUrList(body=body, **kwargs)

@register('GetStorageHitachiRemoteCopyPairUrByMoid')
def GetStorageHitachiRemoteCopyPairUrByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiRemoteCopyPairUrByMoid(body=body, **kwargs)

@register('GetStorageHitachiRemoteReplicationList')
def GetStorageHitachiRemoteReplicationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiRemoteReplicationList(body=body, **kwargs)

@register('GetStorageHitachiRemoteReplicationByMoid')
def GetStorageHitachiRemoteReplicationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiRemoteReplicationByMoid(body=body, **kwargs)

@register('GetStorageHitachiSnapshotList')
def GetStorageHitachiSnapshotList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiSnapshotList(body=body, **kwargs)

@register('GetStorageHitachiSnapshotByMoid')
def GetStorageHitachiSnapshotByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiSnapshotByMoid(body=body, **kwargs)

@register('GetStorageHitachiVolumeList')
def GetStorageHitachiVolumeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiVolumeList(body=body, **kwargs)

@register('GetStorageHitachiVolumeByMoid')
def GetStorageHitachiVolumeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiVolumeByMoid(body=body, **kwargs)

@register('GetStorageHitachiVolumeMigrationPairList')
def GetStorageHitachiVolumeMigrationPairList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiVolumeMigrationPairList(body=body, **kwargs)

@register('GetStorageHitachiVolumeMigrationPairByMoid')
def GetStorageHitachiVolumeMigrationPairByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHitachiVolumeMigrationPairByMoid(body=body, **kwargs)

@register('GetStorageHyperFlexStorageContainerList')
def GetStorageHyperFlexStorageContainerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHyperFlexStorageContainerList(body=body, **kwargs)

@register('GetStorageHyperFlexStorageContainerByMoid')
def GetStorageHyperFlexStorageContainerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHyperFlexStorageContainerByMoid(body=body, **kwargs)

@register('GetStorageHyperFlexVolumeList')
def GetStorageHyperFlexVolumeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHyperFlexVolumeList(body=body, **kwargs)

@register('GetStorageHyperFlexVolumeByMoid')
def GetStorageHyperFlexVolumeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageHyperFlexVolumeByMoid(body=body, **kwargs)

@register('GetStorageItemList')
def GetStorageItemList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageItemList(body=body, **kwargs)

@register('GetStorageItemByMoid')
def GetStorageItemByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageItemByMoid(body=body, **kwargs)

@register('GetStorageKnoxSecureDriveConfigurationList')
def GetStorageKnoxSecureDriveConfigurationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageKnoxSecureDriveConfigurationList(body=body, **kwargs)

@register('GetStorageKnoxSecureDriveConfigurationByMoid')
def GetStorageKnoxSecureDriveConfigurationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageKnoxSecureDriveConfigurationByMoid(body=body, **kwargs)

@register('GetStorageNetAppAggregateList')
def GetStorageNetAppAggregateList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppAggregateList(body=body, **kwargs)

@register('GetStorageNetAppAggregateByMoid')
def GetStorageNetAppAggregateByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppAggregateByMoid(body=body, **kwargs)

@register('GetStorageNetAppAggregateEventList')
def GetStorageNetAppAggregateEventList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppAggregateEventList(body=body, **kwargs)

@register('GetStorageNetAppAggregateEventByMoid')
def GetStorageNetAppAggregateEventByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppAggregateEventByMoid(body=body, **kwargs)

@register('GetStorageNetAppBaseDiskList')
def GetStorageNetAppBaseDiskList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppBaseDiskList(body=body, **kwargs)

@register('GetStorageNetAppBaseDiskByMoid')
def GetStorageNetAppBaseDiskByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppBaseDiskByMoid(body=body, **kwargs)

@register('GetStorageNetAppCifsServiceList')
def GetStorageNetAppCifsServiceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppCifsServiceList(body=body, **kwargs)

@register('GetStorageNetAppCifsServiceByMoid')
def GetStorageNetAppCifsServiceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppCifsServiceByMoid(body=body, **kwargs)

@register('GetStorageNetAppCifsShareList')
def GetStorageNetAppCifsShareList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppCifsShareList(body=body, **kwargs)

@register('GetStorageNetAppCifsShareByMoid')
def GetStorageNetAppCifsShareByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppCifsShareByMoid(body=body, **kwargs)

@register('GetStorageNetAppCloudTargetList')
def GetStorageNetAppCloudTargetList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppCloudTargetList(body=body, **kwargs)

@register('GetStorageNetAppCloudTargetByMoid')
def GetStorageNetAppCloudTargetByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppCloudTargetByMoid(body=body, **kwargs)

@register('GetStorageNetAppClusterList')
def GetStorageNetAppClusterList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppClusterList(body=body, **kwargs)

@register('GetStorageNetAppClusterByMoid')
def GetStorageNetAppClusterByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppClusterByMoid(body=body, **kwargs)

@register('GetStorageNetAppClusterEventList')
def GetStorageNetAppClusterEventList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppClusterEventList(body=body, **kwargs)

@register('GetStorageNetAppClusterEventByMoid')
def GetStorageNetAppClusterEventByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppClusterEventByMoid(body=body, **kwargs)

@register('GetStorageNetAppClusterSnapMirrorPolicyList')
def GetStorageNetAppClusterSnapMirrorPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppClusterSnapMirrorPolicyList(body=body, **kwargs)

@register('GetStorageNetAppClusterSnapMirrorPolicyByMoid')
def GetStorageNetAppClusterSnapMirrorPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppClusterSnapMirrorPolicyByMoid(body=body, **kwargs)

@register('GetStorageNetAppClusterSnapshotPolicyList')
def GetStorageNetAppClusterSnapshotPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppClusterSnapshotPolicyList(body=body, **kwargs)

@register('GetStorageNetAppClusterSnapshotPolicyByMoid')
def GetStorageNetAppClusterSnapshotPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppClusterSnapshotPolicyByMoid(body=body, **kwargs)

@register('GetStorageNetAppDataIpInterfaceList')
def GetStorageNetAppDataIpInterfaceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppDataIpInterfaceList(body=body, **kwargs)

@register('GetStorageNetAppDataIpInterfaceByMoid')
def GetStorageNetAppDataIpInterfaceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppDataIpInterfaceByMoid(body=body, **kwargs)

@register('GetStorageNetAppDataIpInterfaceEventList')
def GetStorageNetAppDataIpInterfaceEventList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppDataIpInterfaceEventList(body=body, **kwargs)

@register('GetStorageNetAppDataIpInterfaceEventByMoid')
def GetStorageNetAppDataIpInterfaceEventByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppDataIpInterfaceEventByMoid(body=body, **kwargs)

@register('GetStorageNetAppDiskEventList')
def GetStorageNetAppDiskEventList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppDiskEventList(body=body, **kwargs)

@register('GetStorageNetAppDiskEventByMoid')
def GetStorageNetAppDiskEventByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppDiskEventByMoid(body=body, **kwargs)

@register('GetStorageNetAppEthernetPortList')
def GetStorageNetAppEthernetPortList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppEthernetPortList(body=body, **kwargs)

@register('GetStorageNetAppEthernetPortByMoid')
def GetStorageNetAppEthernetPortByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppEthernetPortByMoid(body=body, **kwargs)

@register('GetStorageNetAppEthernetPortEventList')
def GetStorageNetAppEthernetPortEventList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppEthernetPortEventList(body=body, **kwargs)

@register('GetStorageNetAppEthernetPortEventByMoid')
def GetStorageNetAppEthernetPortEventByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppEthernetPortEventByMoid(body=body, **kwargs)

@register('GetStorageNetAppExportPolicyList')
def GetStorageNetAppExportPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppExportPolicyList(body=body, **kwargs)

@register('GetStorageNetAppExportPolicyByMoid')
def GetStorageNetAppExportPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppExportPolicyByMoid(body=body, **kwargs)

@register('GetStorageNetAppFcInterfaceList')
def GetStorageNetAppFcInterfaceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppFcInterfaceList(body=body, **kwargs)

@register('GetStorageNetAppFcInterfaceByMoid')
def GetStorageNetAppFcInterfaceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppFcInterfaceByMoid(body=body, **kwargs)

@register('GetStorageNetAppFcInterfaceEventList')
def GetStorageNetAppFcInterfaceEventList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppFcInterfaceEventList(body=body, **kwargs)

@register('GetStorageNetAppFcInterfaceEventByMoid')
def GetStorageNetAppFcInterfaceEventByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppFcInterfaceEventByMoid(body=body, **kwargs)

@register('GetStorageNetAppFcPortList')
def GetStorageNetAppFcPortList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppFcPortList(body=body, **kwargs)

@register('GetStorageNetAppFcPortByMoid')
def GetStorageNetAppFcPortByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppFcPortByMoid(body=body, **kwargs)

@register('GetStorageNetAppFcPortEventList')
def GetStorageNetAppFcPortEventList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppFcPortEventList(body=body, **kwargs)

@register('GetStorageNetAppFcPortEventByMoid')
def GetStorageNetAppFcPortEventByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppFcPortEventByMoid(body=body, **kwargs)

@register('GetStorageNetAppInitiatorGroupList')
def GetStorageNetAppInitiatorGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppInitiatorGroupList(body=body, **kwargs)

@register('GetStorageNetAppInitiatorGroupByMoid')
def GetStorageNetAppInitiatorGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppInitiatorGroupByMoid(body=body, **kwargs)

@register('GetStorageNetAppIpInterfaceList')
def GetStorageNetAppIpInterfaceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppIpInterfaceList(body=body, **kwargs)

@register('GetStorageNetAppIpInterfaceByMoid')
def GetStorageNetAppIpInterfaceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppIpInterfaceByMoid(body=body, **kwargs)

@register('GetStorageNetAppIpInterfaceEventList')
def GetStorageNetAppIpInterfaceEventList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppIpInterfaceEventList(body=body, **kwargs)

@register('GetStorageNetAppIpInterfaceEventByMoid')
def GetStorageNetAppIpInterfaceEventByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppIpInterfaceEventByMoid(body=body, **kwargs)

@register('GetStorageNetAppIscsiServiceList')
def GetStorageNetAppIscsiServiceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppIscsiServiceList(body=body, **kwargs)

@register('GetStorageNetAppIscsiServiceByMoid')
def GetStorageNetAppIscsiServiceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppIscsiServiceByMoid(body=body, **kwargs)

@register('GetStorageNetAppLicenseList')
def GetStorageNetAppLicenseList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppLicenseList(body=body, **kwargs)

@register('GetStorageNetAppLicenseByMoid')
def GetStorageNetAppLicenseByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppLicenseByMoid(body=body, **kwargs)

@register('GetStorageNetAppLunList')
def GetStorageNetAppLunList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppLunList(body=body, **kwargs)

@register('GetStorageNetAppLunByMoid')
def GetStorageNetAppLunByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppLunByMoid(body=body, **kwargs)

@register('GetStorageNetAppLunEventList')
def GetStorageNetAppLunEventList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppLunEventList(body=body, **kwargs)

@register('GetStorageNetAppLunEventByMoid')
def GetStorageNetAppLunEventByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppLunEventByMoid(body=body, **kwargs)

@register('GetStorageNetAppLunMapList')
def GetStorageNetAppLunMapList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppLunMapList(body=body, **kwargs)

@register('GetStorageNetAppLunMapByMoid')
def GetStorageNetAppLunMapByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppLunMapByMoid(body=body, **kwargs)

@register('GetStorageNetAppNamespaceList')
def GetStorageNetAppNamespaceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppNamespaceList(body=body, **kwargs)

@register('GetStorageNetAppNamespaceByMoid')
def GetStorageNetAppNamespaceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppNamespaceByMoid(body=body, **kwargs)

@register('GetStorageNetAppNfsClientList')
def GetStorageNetAppNfsClientList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppNfsClientList(body=body, **kwargs)

@register('GetStorageNetAppNfsClientByMoid')
def GetStorageNetAppNfsClientByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppNfsClientByMoid(body=body, **kwargs)

@register('GetStorageNetAppNfsServiceList')
def GetStorageNetAppNfsServiceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppNfsServiceList(body=body, **kwargs)

@register('GetStorageNetAppNfsServiceByMoid')
def GetStorageNetAppNfsServiceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppNfsServiceByMoid(body=body, **kwargs)

@register('GetStorageNetAppNodeList')
def GetStorageNetAppNodeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppNodeList(body=body, **kwargs)

@register('GetStorageNetAppNodeByMoid')
def GetStorageNetAppNodeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppNodeByMoid(body=body, **kwargs)

@register('GetStorageNetAppNodeCdpNeighborList')
def GetStorageNetAppNodeCdpNeighborList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppNodeCdpNeighborList(body=body, **kwargs)

@register('GetStorageNetAppNodeCdpNeighborByMoid')
def GetStorageNetAppNodeCdpNeighborByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppNodeCdpNeighborByMoid(body=body, **kwargs)

@register('GetStorageNetAppNodeEventList')
def GetStorageNetAppNodeEventList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppNodeEventList(body=body, **kwargs)

@register('GetStorageNetAppNodeEventByMoid')
def GetStorageNetAppNodeEventByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppNodeEventByMoid(body=body, **kwargs)

@register('GetStorageNetAppNonDataIpInterfaceList')
def GetStorageNetAppNonDataIpInterfaceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppNonDataIpInterfaceList(body=body, **kwargs)

@register('GetStorageNetAppNonDataIpInterfaceByMoid')
def GetStorageNetAppNonDataIpInterfaceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppNonDataIpInterfaceByMoid(body=body, **kwargs)

@register('GetStorageNetAppNonDataIpInterfaceEventList')
def GetStorageNetAppNonDataIpInterfaceEventList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppNonDataIpInterfaceEventList(body=body, **kwargs)

@register('GetStorageNetAppNonDataIpInterfaceEventByMoid')
def GetStorageNetAppNonDataIpInterfaceEventByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppNonDataIpInterfaceEventByMoid(body=body, **kwargs)

@register('GetStorageNetAppNtpServerList')
def GetStorageNetAppNtpServerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppNtpServerList(body=body, **kwargs)

@register('GetStorageNetAppNtpServerByMoid')
def GetStorageNetAppNtpServerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppNtpServerByMoid(body=body, **kwargs)

@register('GetStorageNetAppQtreeList')
def GetStorageNetAppQtreeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppQtreeList(body=body, **kwargs)

@register('GetStorageNetAppQtreeByMoid')
def GetStorageNetAppQtreeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppQtreeByMoid(body=body, **kwargs)

@register('GetStorageNetAppScheduleList')
def GetStorageNetAppScheduleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppScheduleList(body=body, **kwargs)

@register('GetStorageNetAppScheduleByMoid')
def GetStorageNetAppScheduleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppScheduleByMoid(body=body, **kwargs)

@register('GetStorageNetAppSensorList')
def GetStorageNetAppSensorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppSensorList(body=body, **kwargs)

@register('GetStorageNetAppSensorByMoid')
def GetStorageNetAppSensorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppSensorByMoid(body=body, **kwargs)

@register('GetStorageNetAppSnapMirrorRelationshipList')
def GetStorageNetAppSnapMirrorRelationshipList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppSnapMirrorRelationshipList(body=body, **kwargs)

@register('GetStorageNetAppSnapMirrorRelationshipByMoid')
def GetStorageNetAppSnapMirrorRelationshipByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppSnapMirrorRelationshipByMoid(body=body, **kwargs)

@register('GetStorageNetAppStorageVmList')
def GetStorageNetAppStorageVmList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppStorageVmList(body=body, **kwargs)

@register('GetStorageNetAppStorageVmByMoid')
def GetStorageNetAppStorageVmByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppStorageVmByMoid(body=body, **kwargs)

@register('GetStorageNetAppSvmEventList')
def GetStorageNetAppSvmEventList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppSvmEventList(body=body, **kwargs)

@register('GetStorageNetAppSvmEventByMoid')
def GetStorageNetAppSvmEventByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppSvmEventByMoid(body=body, **kwargs)

@register('GetStorageNetAppSvmSnapMirrorPolicyList')
def GetStorageNetAppSvmSnapMirrorPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppSvmSnapMirrorPolicyList(body=body, **kwargs)

@register('GetStorageNetAppSvmSnapMirrorPolicyByMoid')
def GetStorageNetAppSvmSnapMirrorPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppSvmSnapMirrorPolicyByMoid(body=body, **kwargs)

@register('GetStorageNetAppSvmSnapshotPolicyList')
def GetStorageNetAppSvmSnapshotPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppSvmSnapshotPolicyList(body=body, **kwargs)

@register('GetStorageNetAppSvmSnapshotPolicyByMoid')
def GetStorageNetAppSvmSnapshotPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppSvmSnapshotPolicyByMoid(body=body, **kwargs)

@register('GetStorageNetAppVolumeList')
def GetStorageNetAppVolumeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppVolumeList(body=body, **kwargs)

@register('GetStorageNetAppVolumeByMoid')
def GetStorageNetAppVolumeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppVolumeByMoid(body=body, **kwargs)

@register('GetStorageNetAppVolumeEventList')
def GetStorageNetAppVolumeEventList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppVolumeEventList(body=body, **kwargs)

@register('GetStorageNetAppVolumeEventByMoid')
def GetStorageNetAppVolumeEventByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppVolumeEventByMoid(body=body, **kwargs)

@register('GetStorageNetAppVolumeSnapshotList')
def GetStorageNetAppVolumeSnapshotList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppVolumeSnapshotList(body=body, **kwargs)

@register('GetStorageNetAppVolumeSnapshotByMoid')
def GetStorageNetAppVolumeSnapshotByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNetAppVolumeSnapshotByMoid(body=body, **kwargs)

@register('GetStorageNvmeRaidConfigurationList')
def GetStorageNvmeRaidConfigurationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNvmeRaidConfigurationList(body=body, **kwargs)

@register('GetStorageNvmeRaidConfigurationByMoid')
def GetStorageNvmeRaidConfigurationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageNvmeRaidConfigurationByMoid(body=body, **kwargs)

@register('GetStoragePhysicalDiskList')
def GetStoragePhysicalDiskList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePhysicalDiskList(body=body, **kwargs)

@register('GetStoragePhysicalDiskByMoid')
def GetStoragePhysicalDiskByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePhysicalDiskByMoid(body=body, **kwargs)

@register('GetStoragePhysicalDiskExtensionList')
def GetStoragePhysicalDiskExtensionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePhysicalDiskExtensionList(body=body, **kwargs)

@register('GetStoragePhysicalDiskExtensionByMoid')
def GetStoragePhysicalDiskExtensionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePhysicalDiskExtensionByMoid(body=body, **kwargs)

@register('GetStoragePhysicalDiskUsageList')
def GetStoragePhysicalDiskUsageList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePhysicalDiskUsageList(body=body, **kwargs)

@register('GetStoragePhysicalDiskUsageByMoid')
def GetStoragePhysicalDiskUsageByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePhysicalDiskUsageByMoid(body=body, **kwargs)

@register('GetStoragePureArrayList')
def GetStoragePureArrayList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureArrayList(body=body, **kwargs)

@register('GetStoragePureArrayByMoid')
def GetStoragePureArrayByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureArrayByMoid(body=body, **kwargs)

@register('GetStoragePureArrayAlertsList')
def GetStoragePureArrayAlertsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureArrayAlertsList(body=body, **kwargs)

@register('GetStoragePureArrayAlertsByMoid')
def GetStoragePureArrayAlertsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureArrayAlertsByMoid(body=body, **kwargs)

@register('GetStoragePureControllerList')
def GetStoragePureControllerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureControllerList(body=body, **kwargs)

@register('GetStoragePureControllerByMoid')
def GetStoragePureControllerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureControllerByMoid(body=body, **kwargs)

@register('GetStoragePureDiskList')
def GetStoragePureDiskList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureDiskList(body=body, **kwargs)

@register('GetStoragePureDiskByMoid')
def GetStoragePureDiskByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureDiskByMoid(body=body, **kwargs)

@register('GetStoragePureHostList')
def GetStoragePureHostList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureHostList(body=body, **kwargs)

@register('GetStoragePureHostByMoid')
def GetStoragePureHostByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureHostByMoid(body=body, **kwargs)

@register('GetStoragePureHostGroupList')
def GetStoragePureHostGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureHostGroupList(body=body, **kwargs)

@register('GetStoragePureHostGroupByMoid')
def GetStoragePureHostGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureHostGroupByMoid(body=body, **kwargs)

@register('GetStoragePureHostLunList')
def GetStoragePureHostLunList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureHostLunList(body=body, **kwargs)

@register('GetStoragePureHostLunByMoid')
def GetStoragePureHostLunByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureHostLunByMoid(body=body, **kwargs)

@register('GetStoragePurePortList')
def GetStoragePurePortList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePurePortList(body=body, **kwargs)

@register('GetStoragePurePortByMoid')
def GetStoragePurePortByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePurePortByMoid(body=body, **kwargs)

@register('GetStoragePureProtectionGroupList')
def GetStoragePureProtectionGroupList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureProtectionGroupList(body=body, **kwargs)

@register('GetStoragePureProtectionGroupByMoid')
def GetStoragePureProtectionGroupByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureProtectionGroupByMoid(body=body, **kwargs)

@register('GetStoragePureProtectionGroupSnapshotList')
def GetStoragePureProtectionGroupSnapshotList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureProtectionGroupSnapshotList(body=body, **kwargs)

@register('GetStoragePureProtectionGroupSnapshotByMoid')
def GetStoragePureProtectionGroupSnapshotByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureProtectionGroupSnapshotByMoid(body=body, **kwargs)

@register('GetStoragePureReplicationScheduleList')
def GetStoragePureReplicationScheduleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureReplicationScheduleList(body=body, **kwargs)

@register('GetStoragePureReplicationScheduleByMoid')
def GetStoragePureReplicationScheduleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureReplicationScheduleByMoid(body=body, **kwargs)

@register('GetStoragePureSnapshotScheduleList')
def GetStoragePureSnapshotScheduleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureSnapshotScheduleList(body=body, **kwargs)

@register('GetStoragePureSnapshotScheduleByMoid')
def GetStoragePureSnapshotScheduleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureSnapshotScheduleByMoid(body=body, **kwargs)

@register('GetStoragePureTargetArrayList')
def GetStoragePureTargetArrayList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureTargetArrayList(body=body, **kwargs)

@register('GetStoragePureTargetArrayByMoid')
def GetStoragePureTargetArrayByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureTargetArrayByMoid(body=body, **kwargs)

@register('GetStoragePureVolumeList')
def GetStoragePureVolumeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureVolumeList(body=body, **kwargs)

@register('GetStoragePureVolumeByMoid')
def GetStoragePureVolumeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureVolumeByMoid(body=body, **kwargs)

@register('GetStoragePureVolumeSnapshotList')
def GetStoragePureVolumeSnapshotList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureVolumeSnapshotList(body=body, **kwargs)

@register('GetStoragePureVolumeSnapshotByMoid')
def GetStoragePureVolumeSnapshotByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStoragePureVolumeSnapshotByMoid(body=body, **kwargs)

@register('GetStorageSasExpanderList')
def GetStorageSasExpanderList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageSasExpanderList(body=body, **kwargs)

@register('GetStorageSasExpanderByMoid')
def GetStorageSasExpanderByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageSasExpanderByMoid(body=body, **kwargs)

@register('GetStorageSasPortList')
def GetStorageSasPortList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageSasPortList(body=body, **kwargs)

@register('GetStorageSasPortByMoid')
def GetStorageSasPortByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageSasPortByMoid(body=body, **kwargs)

@register('GetStorageSpanList')
def GetStorageSpanList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageSpanList(body=body, **kwargs)

@register('GetStorageSpanByMoid')
def GetStorageSpanByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageSpanByMoid(body=body, **kwargs)

@register('GetStorageStoragePolicyList')
def GetStorageStoragePolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageStoragePolicyList(body=body, **kwargs)

@register('GetStorageStoragePolicyByMoid')
def GetStorageStoragePolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageStoragePolicyByMoid(body=body, **kwargs)

@register('GetStorageVdMemberEpList')
def GetStorageVdMemberEpList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageVdMemberEpList(body=body, **kwargs)

@register('GetStorageVdMemberEpByMoid')
def GetStorageVdMemberEpByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageVdMemberEpByMoid(body=body, **kwargs)

@register('GetStorageVirtualDriveList')
def GetStorageVirtualDriveList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageVirtualDriveList(body=body, **kwargs)

@register('GetStorageVirtualDriveByMoid')
def GetStorageVirtualDriveByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageVirtualDriveByMoid(body=body, **kwargs)

@register('GetStorageVirtualDriveContainerList')
def GetStorageVirtualDriveContainerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageVirtualDriveContainerList(body=body, **kwargs)

@register('GetStorageVirtualDriveContainerByMoid')
def GetStorageVirtualDriveContainerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageVirtualDriveContainerByMoid(body=body, **kwargs)

@register('GetStorageVirtualDriveExtensionList')
def GetStorageVirtualDriveExtensionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageVirtualDriveExtensionList(body=body, **kwargs)

@register('GetStorageVirtualDriveExtensionByMoid')
def GetStorageVirtualDriveExtensionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageVirtualDriveExtensionByMoid(body=body, **kwargs)

@register('GetStorageVirtualDriveIdentityList')
def GetStorageVirtualDriveIdentityList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageVirtualDriveIdentityList(body=body, **kwargs)

@register('GetStorageVirtualDriveIdentityByMoid')
def GetStorageVirtualDriveIdentityByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetStorageVirtualDriveIdentityByMoid(body=body, **kwargs)

@register('GetSyslogPolicyList')
def GetSyslogPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSyslogPolicyList(body=body, **kwargs)

@register('GetSyslogPolicyByMoid')
def GetSyslogPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSyslogPolicyByMoid(body=body, **kwargs)

@register('GetSyslogPolicyInventoryList')
def GetSyslogPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSyslogPolicyInventoryList(body=body, **kwargs)

@register('GetSyslogPolicyInventoryByMoid')
def GetSyslogPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetSyslogPolicyInventoryByMoid(body=body, **kwargs)

@register('GetTamAdvisoryCountList')
def GetTamAdvisoryCountList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTamAdvisoryCountList(body=body, **kwargs)

@register('GetTamAdvisoryCountByMoid')
def GetTamAdvisoryCountByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTamAdvisoryCountByMoid(body=body, **kwargs)

@register('GetTamAdvisoryDefinitionList')
def GetTamAdvisoryDefinitionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTamAdvisoryDefinitionList(body=body, **kwargs)

@register('GetTamAdvisoryDefinitionByMoid')
def GetTamAdvisoryDefinitionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTamAdvisoryDefinitionByMoid(body=body, **kwargs)

@register('GetTamAdvisoryInfoList')
def GetTamAdvisoryInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTamAdvisoryInfoList(body=body, **kwargs)

@register('GetTamAdvisoryInfoByMoid')
def GetTamAdvisoryInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTamAdvisoryInfoByMoid(body=body, **kwargs)

@register('GetTamAdvisoryInstanceList')
def GetTamAdvisoryInstanceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTamAdvisoryInstanceList(body=body, **kwargs)

@register('GetTamAdvisoryInstanceByMoid')
def GetTamAdvisoryInstanceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTamAdvisoryInstanceByMoid(body=body, **kwargs)

@register('GetTamSecurityAdvisoryList')
def GetTamSecurityAdvisoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTamSecurityAdvisoryList(body=body, **kwargs)

@register('GetTamSecurityAdvisoryByMoid')
def GetTamSecurityAdvisoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTamSecurityAdvisoryByMoid(body=body, **kwargs)

@register('GetTaskWorkflowActionList')
def GetTaskWorkflowActionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTaskWorkflowActionList(body=body, **kwargs)

@register('GetTaskWorkflowActionByMoid')
def GetTaskWorkflowActionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTaskWorkflowActionByMoid(body=body, **kwargs)

@register('GetTechsupportmanagementCollectionControlPolicyList')
def GetTechsupportmanagementCollectionControlPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTechsupportmanagementCollectionControlPolicyList(body=body, **kwargs)

@register('GetTechsupportmanagementCollectionControlPolicyByMoid')
def GetTechsupportmanagementCollectionControlPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTechsupportmanagementCollectionControlPolicyByMoid(body=body, **kwargs)

@register('GetTechsupportmanagementDownloadList')
def GetTechsupportmanagementDownloadList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTechsupportmanagementDownloadList(body=body, **kwargs)

@register('GetTechsupportmanagementDownloadByMoid')
def GetTechsupportmanagementDownloadByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTechsupportmanagementDownloadByMoid(body=body, **kwargs)

@register('GetTechsupportmanagementEndPointList')
def GetTechsupportmanagementEndPointList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTechsupportmanagementEndPointList(body=body, **kwargs)

@register('GetTechsupportmanagementEndPointByMoid')
def GetTechsupportmanagementEndPointByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTechsupportmanagementEndPointByMoid(body=body, **kwargs)

@register('GetTechsupportmanagementTechSupportBundleList')
def GetTechsupportmanagementTechSupportBundleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTechsupportmanagementTechSupportBundleList(body=body, **kwargs)

@register('GetTechsupportmanagementTechSupportBundleByMoid')
def GetTechsupportmanagementTechSupportBundleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTechsupportmanagementTechSupportBundleByMoid(body=body, **kwargs)

@register('GetTechsupportmanagementTechSupportStatusList')
def GetTechsupportmanagementTechSupportStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTechsupportmanagementTechSupportStatusList(body=body, **kwargs)

@register('GetTechsupportmanagementTechSupportStatusByMoid')
def GetTechsupportmanagementTechSupportStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTechsupportmanagementTechSupportStatusByMoid(body=body, **kwargs)

@register('GetTerminalAuditLogList')
def GetTerminalAuditLogList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTerminalAuditLogList(body=body, **kwargs)

@register('GetTerminalAuditLogByMoid')
def GetTerminalAuditLogByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTerminalAuditLogByMoid(body=body, **kwargs)

@register('GetThermalPolicyList')
def GetThermalPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetThermalPolicyList(body=body, **kwargs)

@register('GetThermalPolicyByMoid')
def GetThermalPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetThermalPolicyByMoid(body=body, **kwargs)

@register('GetThermalPolicyInventoryList')
def GetThermalPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetThermalPolicyInventoryList(body=body, **kwargs)

@register('GetThermalPolicyInventoryByMoid')
def GetThermalPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetThermalPolicyInventoryByMoid(body=body, **kwargs)

@register('GetTopSystemList')
def GetTopSystemList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTopSystemList(body=body, **kwargs)

@register('GetTopSystemByMoid')
def GetTopSystemByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetTopSystemByMoid(body=body, **kwargs)

@register('GetUcsdBackupInfoList')
def GetUcsdBackupInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetUcsdBackupInfoList(body=body, **kwargs)

@register('GetUcsdBackupInfoByMoid')
def GetUcsdBackupInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetUcsdBackupInfoByMoid(body=body, **kwargs)

@register('GetUuidpoolBlockList')
def GetUuidpoolBlockList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetUuidpoolBlockList(body=body, **kwargs)

@register('GetUuidpoolBlockByMoid')
def GetUuidpoolBlockByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetUuidpoolBlockByMoid(body=body, **kwargs)

@register('GetUuidpoolPoolList')
def GetUuidpoolPoolList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetUuidpoolPoolList(body=body, **kwargs)

@register('GetUuidpoolPoolByMoid')
def GetUuidpoolPoolByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetUuidpoolPoolByMoid(body=body, **kwargs)

@register('GetUuidpoolPoolMemberList')
def GetUuidpoolPoolMemberList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetUuidpoolPoolMemberList(body=body, **kwargs)

@register('GetUuidpoolPoolMemberByMoid')
def GetUuidpoolPoolMemberByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetUuidpoolPoolMemberByMoid(body=body, **kwargs)

@register('GetUuidpoolReservationList')
def GetUuidpoolReservationList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetUuidpoolReservationList(body=body, **kwargs)

@register('GetUuidpoolReservationByMoid')
def GetUuidpoolReservationByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetUuidpoolReservationByMoid(body=body, **kwargs)

@register('GetUuidpoolUniverseList')
def GetUuidpoolUniverseList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetUuidpoolUniverseList(body=body, **kwargs)

@register('GetUuidpoolUniverseByMoid')
def GetUuidpoolUniverseByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetUuidpoolUniverseByMoid(body=body, **kwargs)

@register('GetUuidpoolUuidLeaseList')
def GetUuidpoolUuidLeaseList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetUuidpoolUuidLeaseList(body=body, **kwargs)

@register('GetUuidpoolUuidLeaseByMoid')
def GetUuidpoolUuidLeaseByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetUuidpoolUuidLeaseByMoid(body=body, **kwargs)

@register('GetViewHealthStatusList')
def GetViewHealthStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetViewHealthStatusList(body=body, **kwargs)

@register('GetViewHealthStatusByMoid')
def GetViewHealthStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetViewHealthStatusByMoid(body=body, **kwargs)

@register('GetViewServerList')
def GetViewServerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetViewServerList(body=body, **kwargs)

@register('GetViewServerByMoid')
def GetViewServerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetViewServerByMoid(body=body, **kwargs)

@register('GetVirtualizationEsxiConsoleList')
def GetVirtualizationEsxiConsoleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationEsxiConsoleList(body=body, **kwargs)

@register('GetVirtualizationEsxiConsoleByMoid')
def GetVirtualizationEsxiConsoleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationEsxiConsoleByMoid(body=body, **kwargs)

@register('GetVirtualizationHostList')
def GetVirtualizationHostList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationHostList(body=body, **kwargs)

@register('GetVirtualizationHostByMoid')
def GetVirtualizationHostByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationHostByMoid(body=body, **kwargs)

@register('GetVirtualizationVirtualMachineList')
def GetVirtualizationVirtualMachineList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVirtualMachineList(body=body, **kwargs)

@register('GetVirtualizationVirtualMachineByMoid')
def GetVirtualizationVirtualMachineByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVirtualMachineByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwareClusterList')
def GetVirtualizationVmwareClusterList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareClusterList(body=body, **kwargs)

@register('GetVirtualizationVmwareClusterByMoid')
def GetVirtualizationVmwareClusterByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareClusterByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwareDatacenterList')
def GetVirtualizationVmwareDatacenterList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareDatacenterList(body=body, **kwargs)

@register('GetVirtualizationVmwareDatacenterByMoid')
def GetVirtualizationVmwareDatacenterByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareDatacenterByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwareDatastoreList')
def GetVirtualizationVmwareDatastoreList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareDatastoreList(body=body, **kwargs)

@register('GetVirtualizationVmwareDatastoreByMoid')
def GetVirtualizationVmwareDatastoreByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareDatastoreByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwareDatastoreClusterList')
def GetVirtualizationVmwareDatastoreClusterList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareDatastoreClusterList(body=body, **kwargs)

@register('GetVirtualizationVmwareDatastoreClusterByMoid')
def GetVirtualizationVmwareDatastoreClusterByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareDatastoreClusterByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwareDistributedNetworkList')
def GetVirtualizationVmwareDistributedNetworkList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareDistributedNetworkList(body=body, **kwargs)

@register('GetVirtualizationVmwareDistributedNetworkByMoid')
def GetVirtualizationVmwareDistributedNetworkByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareDistributedNetworkByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwareDistributedSwitchList')
def GetVirtualizationVmwareDistributedSwitchList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareDistributedSwitchList(body=body, **kwargs)

@register('GetVirtualizationVmwareDistributedSwitchByMoid')
def GetVirtualizationVmwareDistributedSwitchByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareDistributedSwitchByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwareFolderList')
def GetVirtualizationVmwareFolderList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareFolderList(body=body, **kwargs)

@register('GetVirtualizationVmwareFolderByMoid')
def GetVirtualizationVmwareFolderByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareFolderByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwareHostList')
def GetVirtualizationVmwareHostList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareHostList(body=body, **kwargs)

@register('GetVirtualizationVmwareHostByMoid')
def GetVirtualizationVmwareHostByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareHostByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwareHostGpuList')
def GetVirtualizationVmwareHostGpuList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareHostGpuList(body=body, **kwargs)

@register('GetVirtualizationVmwareHostGpuByMoid')
def GetVirtualizationVmwareHostGpuByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareHostGpuByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwareKernelNetworkList')
def GetVirtualizationVmwareKernelNetworkList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareKernelNetworkList(body=body, **kwargs)

@register('GetVirtualizationVmwareKernelNetworkByMoid')
def GetVirtualizationVmwareKernelNetworkByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareKernelNetworkByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwareNetworkList')
def GetVirtualizationVmwareNetworkList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareNetworkList(body=body, **kwargs)

@register('GetVirtualizationVmwareNetworkByMoid')
def GetVirtualizationVmwareNetworkByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareNetworkByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwarePhysicalNetworkInterfaceList')
def GetVirtualizationVmwarePhysicalNetworkInterfaceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwarePhysicalNetworkInterfaceList(body=body, **kwargs)

@register('GetVirtualizationVmwarePhysicalNetworkInterfaceByMoid')
def GetVirtualizationVmwarePhysicalNetworkInterfaceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwarePhysicalNetworkInterfaceByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwareProactiveHaList')
def GetVirtualizationVmwareProactiveHaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareProactiveHaList(body=body, **kwargs)

@register('GetVirtualizationVmwareProactiveHaByMoid')
def GetVirtualizationVmwareProactiveHaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareProactiveHaByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwareUplinkPortList')
def GetVirtualizationVmwareUplinkPortList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareUplinkPortList(body=body, **kwargs)

@register('GetVirtualizationVmwareUplinkPortByMoid')
def GetVirtualizationVmwareUplinkPortByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareUplinkPortByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwareVcenterList')
def GetVirtualizationVmwareVcenterList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareVcenterList(body=body, **kwargs)

@register('GetVirtualizationVmwareVcenterByMoid')
def GetVirtualizationVmwareVcenterByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareVcenterByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwareVirtualDiskList')
def GetVirtualizationVmwareVirtualDiskList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareVirtualDiskList(body=body, **kwargs)

@register('GetVirtualizationVmwareVirtualDiskByMoid')
def GetVirtualizationVmwareVirtualDiskByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareVirtualDiskByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwareVirtualMachineList')
def GetVirtualizationVmwareVirtualMachineList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareVirtualMachineList(body=body, **kwargs)

@register('GetVirtualizationVmwareVirtualMachineByMoid')
def GetVirtualizationVmwareVirtualMachineByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareVirtualMachineByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwareVirtualMachineGpuList')
def GetVirtualizationVmwareVirtualMachineGpuList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareVirtualMachineGpuList(body=body, **kwargs)

@register('GetVirtualizationVmwareVirtualMachineGpuByMoid')
def GetVirtualizationVmwareVirtualMachineGpuByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareVirtualMachineGpuByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwareVirtualMachineSnapshotList')
def GetVirtualizationVmwareVirtualMachineSnapshotList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareVirtualMachineSnapshotList(body=body, **kwargs)

@register('GetVirtualizationVmwareVirtualMachineSnapshotByMoid')
def GetVirtualizationVmwareVirtualMachineSnapshotByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareVirtualMachineSnapshotByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwareVirtualNetworkInterfaceList')
def GetVirtualizationVmwareVirtualNetworkInterfaceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareVirtualNetworkInterfaceList(body=body, **kwargs)

@register('GetVirtualizationVmwareVirtualNetworkInterfaceByMoid')
def GetVirtualizationVmwareVirtualNetworkInterfaceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareVirtualNetworkInterfaceByMoid(body=body, **kwargs)

@register('GetVirtualizationVmwareVirtualSwitchList')
def GetVirtualizationVmwareVirtualSwitchList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareVirtualSwitchList(body=body, **kwargs)

@register('GetVirtualizationVmwareVirtualSwitchByMoid')
def GetVirtualizationVmwareVirtualSwitchByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVirtualizationVmwareVirtualSwitchByMoid(body=body, **kwargs)

@register('GetVmediaPolicyList')
def GetVmediaPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVmediaPolicyList(body=body, **kwargs)

@register('GetVmediaPolicyByMoid')
def GetVmediaPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVmediaPolicyByMoid(body=body, **kwargs)

@register('GetVmediaPolicyInventoryList')
def GetVmediaPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVmediaPolicyInventoryList(body=body, **kwargs)

@register('GetVmediaPolicyInventoryByMoid')
def GetVmediaPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVmediaPolicyInventoryByMoid(body=body, **kwargs)

@register('GetVmrcConsoleList')
def GetVmrcConsoleList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVmrcConsoleList(body=body, **kwargs)

@register('GetVmrcConsoleByMoid')
def GetVmrcConsoleByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVmrcConsoleByMoid(body=body, **kwargs)

@register('GetVnicEthAdapterPolicyList')
def GetVnicEthAdapterPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicEthAdapterPolicyList(body=body, **kwargs)

@register('GetVnicEthAdapterPolicyByMoid')
def GetVnicEthAdapterPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicEthAdapterPolicyByMoid(body=body, **kwargs)

@register('GetVnicEthAdapterPolicyInventoryList')
def GetVnicEthAdapterPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicEthAdapterPolicyInventoryList(body=body, **kwargs)

@register('GetVnicEthAdapterPolicyInventoryByMoid')
def GetVnicEthAdapterPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicEthAdapterPolicyInventoryByMoid(body=body, **kwargs)

@register('GetVnicEthIfList')
def GetVnicEthIfList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicEthIfList(body=body, **kwargs)

@register('GetVnicEthIfByMoid')
def GetVnicEthIfByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicEthIfByMoid(body=body, **kwargs)

@register('GetVnicEthIfInventoryList')
def GetVnicEthIfInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicEthIfInventoryList(body=body, **kwargs)

@register('GetVnicEthIfInventoryByMoid')
def GetVnicEthIfInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicEthIfInventoryByMoid(body=body, **kwargs)

@register('GetVnicEthNetworkPolicyList')
def GetVnicEthNetworkPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicEthNetworkPolicyList(body=body, **kwargs)

@register('GetVnicEthNetworkPolicyByMoid')
def GetVnicEthNetworkPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicEthNetworkPolicyByMoid(body=body, **kwargs)

@register('GetVnicEthNetworkPolicyInventoryList')
def GetVnicEthNetworkPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicEthNetworkPolicyInventoryList(body=body, **kwargs)

@register('GetVnicEthNetworkPolicyInventoryByMoid')
def GetVnicEthNetworkPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicEthNetworkPolicyInventoryByMoid(body=body, **kwargs)

@register('GetVnicEthQosPolicyList')
def GetVnicEthQosPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicEthQosPolicyList(body=body, **kwargs)

@register('GetVnicEthQosPolicyByMoid')
def GetVnicEthQosPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicEthQosPolicyByMoid(body=body, **kwargs)

@register('GetVnicEthQosPolicyInventoryList')
def GetVnicEthQosPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicEthQosPolicyInventoryList(body=body, **kwargs)

@register('GetVnicEthQosPolicyInventoryByMoid')
def GetVnicEthQosPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicEthQosPolicyInventoryByMoid(body=body, **kwargs)

@register('GetVnicEthVethInventoryList')
def GetVnicEthVethInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicEthVethInventoryList(body=body, **kwargs)

@register('GetVnicEthVethInventoryByMoid')
def GetVnicEthVethInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicEthVethInventoryByMoid(body=body, **kwargs)

@register('GetVnicEthVnicInventoryList')
def GetVnicEthVnicInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicEthVnicInventoryList(body=body, **kwargs)

@register('GetVnicEthVnicInventoryByMoid')
def GetVnicEthVnicInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicEthVnicInventoryByMoid(body=body, **kwargs)

@register('GetVnicFcAdapterPolicyList')
def GetVnicFcAdapterPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicFcAdapterPolicyList(body=body, **kwargs)

@register('GetVnicFcAdapterPolicyByMoid')
def GetVnicFcAdapterPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicFcAdapterPolicyByMoid(body=body, **kwargs)

@register('GetVnicFcAdapterPolicyInventoryList')
def GetVnicFcAdapterPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicFcAdapterPolicyInventoryList(body=body, **kwargs)

@register('GetVnicFcAdapterPolicyInventoryByMoid')
def GetVnicFcAdapterPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicFcAdapterPolicyInventoryByMoid(body=body, **kwargs)

@register('GetVnicFcIfList')
def GetVnicFcIfList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicFcIfList(body=body, **kwargs)

@register('GetVnicFcIfByMoid')
def GetVnicFcIfByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicFcIfByMoid(body=body, **kwargs)

@register('GetVnicFcIfInventoryList')
def GetVnicFcIfInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicFcIfInventoryList(body=body, **kwargs)

@register('GetVnicFcIfInventoryByMoid')
def GetVnicFcIfInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicFcIfInventoryByMoid(body=body, **kwargs)

@register('GetVnicFcNetworkPolicyList')
def GetVnicFcNetworkPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicFcNetworkPolicyList(body=body, **kwargs)

@register('GetVnicFcNetworkPolicyByMoid')
def GetVnicFcNetworkPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicFcNetworkPolicyByMoid(body=body, **kwargs)

@register('GetVnicFcNetworkPolicyInventoryList')
def GetVnicFcNetworkPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicFcNetworkPolicyInventoryList(body=body, **kwargs)

@register('GetVnicFcNetworkPolicyInventoryByMoid')
def GetVnicFcNetworkPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicFcNetworkPolicyInventoryByMoid(body=body, **kwargs)

@register('GetVnicFcQosPolicyList')
def GetVnicFcQosPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicFcQosPolicyList(body=body, **kwargs)

@register('GetVnicFcQosPolicyByMoid')
def GetVnicFcQosPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicFcQosPolicyByMoid(body=body, **kwargs)

@register('GetVnicFcQosPolicyInventoryList')
def GetVnicFcQosPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicFcQosPolicyInventoryList(body=body, **kwargs)

@register('GetVnicFcQosPolicyInventoryByMoid')
def GetVnicFcQosPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicFcQosPolicyInventoryByMoid(body=body, **kwargs)

@register('GetVnicFcVethInventoryList')
def GetVnicFcVethInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicFcVethInventoryList(body=body, **kwargs)

@register('GetVnicFcVethInventoryByMoid')
def GetVnicFcVethInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicFcVethInventoryByMoid(body=body, **kwargs)

@register('GetVnicFcVhbaPolicyInventoryList')
def GetVnicFcVhbaPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicFcVhbaPolicyInventoryList(body=body, **kwargs)

@register('GetVnicFcVhbaPolicyInventoryByMoid')
def GetVnicFcVhbaPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicFcVhbaPolicyInventoryByMoid(body=body, **kwargs)

@register('GetVnicIscsiAdapterPolicyList')
def GetVnicIscsiAdapterPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicIscsiAdapterPolicyList(body=body, **kwargs)

@register('GetVnicIscsiAdapterPolicyByMoid')
def GetVnicIscsiAdapterPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicIscsiAdapterPolicyByMoid(body=body, **kwargs)

@register('GetVnicIscsiAdapterPolicyInventoryList')
def GetVnicIscsiAdapterPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicIscsiAdapterPolicyInventoryList(body=body, **kwargs)

@register('GetVnicIscsiAdapterPolicyInventoryByMoid')
def GetVnicIscsiAdapterPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicIscsiAdapterPolicyInventoryByMoid(body=body, **kwargs)

@register('GetVnicIscsiBootPolicyList')
def GetVnicIscsiBootPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicIscsiBootPolicyList(body=body, **kwargs)

@register('GetVnicIscsiBootPolicyByMoid')
def GetVnicIscsiBootPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicIscsiBootPolicyByMoid(body=body, **kwargs)

@register('GetVnicIscsiBootPolicyInventoryList')
def GetVnicIscsiBootPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicIscsiBootPolicyInventoryList(body=body, **kwargs)

@register('GetVnicIscsiBootPolicyInventoryByMoid')
def GetVnicIscsiBootPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicIscsiBootPolicyInventoryByMoid(body=body, **kwargs)

@register('GetVnicIscsiStaticTargetPolicyList')
def GetVnicIscsiStaticTargetPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicIscsiStaticTargetPolicyList(body=body, **kwargs)

@register('GetVnicIscsiStaticTargetPolicyByMoid')
def GetVnicIscsiStaticTargetPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicIscsiStaticTargetPolicyByMoid(body=body, **kwargs)

@register('GetVnicIscsiStaticTargetPolicyInventoryList')
def GetVnicIscsiStaticTargetPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicIscsiStaticTargetPolicyInventoryList(body=body, **kwargs)

@register('GetVnicIscsiStaticTargetPolicyInventoryByMoid')
def GetVnicIscsiStaticTargetPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicIscsiStaticTargetPolicyInventoryByMoid(body=body, **kwargs)

@register('GetVnicLanConnectivityPolicyList')
def GetVnicLanConnectivityPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicLanConnectivityPolicyList(body=body, **kwargs)

@register('GetVnicLanConnectivityPolicyByMoid')
def GetVnicLanConnectivityPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicLanConnectivityPolicyByMoid(body=body, **kwargs)

@register('GetVnicLanConnectivityPolicyInventoryList')
def GetVnicLanConnectivityPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicLanConnectivityPolicyInventoryList(body=body, **kwargs)

@register('GetVnicLanConnectivityPolicyInventoryByMoid')
def GetVnicLanConnectivityPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicLanConnectivityPolicyInventoryByMoid(body=body, **kwargs)

@register('GetVnicLanSettingsList')
def GetVnicLanSettingsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicLanSettingsList(body=body, **kwargs)

@register('GetVnicLanSettingsByMoid')
def GetVnicLanSettingsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicLanSettingsByMoid(body=body, **kwargs)

@register('GetVnicLcpStatusList')
def GetVnicLcpStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicLcpStatusList(body=body, **kwargs)

@register('GetVnicLcpStatusByMoid')
def GetVnicLcpStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicLcpStatusByMoid(body=body, **kwargs)

@register('GetVnicSanConnectivityPolicyList')
def GetVnicSanConnectivityPolicyList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicSanConnectivityPolicyList(body=body, **kwargs)

@register('GetVnicSanConnectivityPolicyByMoid')
def GetVnicSanConnectivityPolicyByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicSanConnectivityPolicyByMoid(body=body, **kwargs)

@register('GetVnicSanConnectivityPolicyInventoryList')
def GetVnicSanConnectivityPolicyInventoryList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicSanConnectivityPolicyInventoryList(body=body, **kwargs)

@register('GetVnicSanConnectivityPolicyInventoryByMoid')
def GetVnicSanConnectivityPolicyInventoryByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicSanConnectivityPolicyInventoryByMoid(body=body, **kwargs)

@register('GetVnicSanSettingsList')
def GetVnicSanSettingsList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicSanSettingsList(body=body, **kwargs)

@register('GetVnicSanSettingsByMoid')
def GetVnicSanSettingsByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicSanSettingsByMoid(body=body, **kwargs)

@register('GetVnicScpStatusList')
def GetVnicScpStatusList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicScpStatusList(body=body, **kwargs)

@register('GetVnicScpStatusByMoid')
def GetVnicScpStatusByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicScpStatusByMoid(body=body, **kwargs)

@register('GetVnicVhbaTemplateList')
def GetVnicVhbaTemplateList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicVhbaTemplateList(body=body, **kwargs)

@register('GetVnicVhbaTemplateByMoid')
def GetVnicVhbaTemplateByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicVhbaTemplateByMoid(body=body, **kwargs)

@register('GetVnicVnicTemplateList')
def GetVnicVnicTemplateList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicVnicTemplateList(body=body, **kwargs)

@register('GetVnicVnicTemplateByMoid')
def GetVnicVnicTemplateByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVnicVnicTemplateByMoid(body=body, **kwargs)

@register('GetVrfVrfList')
def GetVrfVrfList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVrfVrfList(body=body, **kwargs)

@register('GetVrfVrfByMoid')
def GetVrfVrfByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetVrfVrfByMoid(body=body, **kwargs)

@register('GetWebhookEndpointList')
def GetWebhookEndpointList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWebhookEndpointList(body=body, **kwargs)

@register('GetWebhookEndpointByMoid')
def GetWebhookEndpointByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWebhookEndpointByMoid(body=body, **kwargs)

@register('GetWebhookSchemaList')
def GetWebhookSchemaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWebhookSchemaList(body=body, **kwargs)

@register('GetWebhookSchemaByMoid')
def GetWebhookSchemaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWebhookSchemaByMoid(body=body, **kwargs)

@register('GetWorkflowAnsibleBatchExecutorList')
def GetWorkflowAnsibleBatchExecutorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowAnsibleBatchExecutorList(body=body, **kwargs)

@register('GetWorkflowAnsibleBatchExecutorByMoid')
def GetWorkflowAnsibleBatchExecutorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowAnsibleBatchExecutorByMoid(body=body, **kwargs)

@register('GetWorkflowBatchApiExecutorList')
def GetWorkflowBatchApiExecutorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowBatchApiExecutorList(body=body, **kwargs)

@register('GetWorkflowBatchApiExecutorByMoid')
def GetWorkflowBatchApiExecutorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowBatchApiExecutorByMoid(body=body, **kwargs)

@register('GetWorkflowCatalogList')
def GetWorkflowCatalogList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowCatalogList(body=body, **kwargs)

@register('GetWorkflowCatalogByMoid')
def GetWorkflowCatalogByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowCatalogByMoid(body=body, **kwargs)

@register('GetWorkflowCatalogItemDefinitionList')
def GetWorkflowCatalogItemDefinitionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowCatalogItemDefinitionList(body=body, **kwargs)

@register('GetWorkflowCatalogItemDefinitionByMoid')
def GetWorkflowCatalogItemDefinitionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowCatalogItemDefinitionByMoid(body=body, **kwargs)

@register('GetWorkflowCatalogServiceRequestList')
def GetWorkflowCatalogServiceRequestList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowCatalogServiceRequestList(body=body, **kwargs)

@register('GetWorkflowCatalogServiceRequestByMoid')
def GetWorkflowCatalogServiceRequestByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowCatalogServiceRequestByMoid(body=body, **kwargs)

@register('GetWorkflowCustomDataTypeDefinitionList')
def GetWorkflowCustomDataTypeDefinitionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowCustomDataTypeDefinitionList(body=body, **kwargs)

@register('GetWorkflowCustomDataTypeDefinitionByMoid')
def GetWorkflowCustomDataTypeDefinitionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowCustomDataTypeDefinitionByMoid(body=body, **kwargs)

@register('GetWorkflowErrorResponseHandlerList')
def GetWorkflowErrorResponseHandlerList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowErrorResponseHandlerList(body=body, **kwargs)

@register('GetWorkflowErrorResponseHandlerByMoid')
def GetWorkflowErrorResponseHandlerByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowErrorResponseHandlerByMoid(body=body, **kwargs)

@register('GetWorkflowPowerShellBatchApiExecutorList')
def GetWorkflowPowerShellBatchApiExecutorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowPowerShellBatchApiExecutorList(body=body, **kwargs)

@register('GetWorkflowPowerShellBatchApiExecutorByMoid')
def GetWorkflowPowerShellBatchApiExecutorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowPowerShellBatchApiExecutorByMoid(body=body, **kwargs)

@register('GetWorkflowRollbackWorkflowList')
def GetWorkflowRollbackWorkflowList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowRollbackWorkflowList(body=body, **kwargs)

@register('GetWorkflowRollbackWorkflowByMoid')
def GetWorkflowRollbackWorkflowByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowRollbackWorkflowByMoid(body=body, **kwargs)

@register('GetWorkflowServiceItemActionDefinitionList')
def GetWorkflowServiceItemActionDefinitionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowServiceItemActionDefinitionList(body=body, **kwargs)

@register('GetWorkflowServiceItemActionDefinitionByMoid')
def GetWorkflowServiceItemActionDefinitionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowServiceItemActionDefinitionByMoid(body=body, **kwargs)

@register('GetWorkflowServiceItemActionInstanceList')
def GetWorkflowServiceItemActionInstanceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowServiceItemActionInstanceList(body=body, **kwargs)

@register('GetWorkflowServiceItemActionInstanceByMoid')
def GetWorkflowServiceItemActionInstanceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowServiceItemActionInstanceByMoid(body=body, **kwargs)

@register('GetWorkflowServiceItemAttributeList')
def GetWorkflowServiceItemAttributeList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowServiceItemAttributeList(body=body, **kwargs)

@register('GetWorkflowServiceItemAttributeByMoid')
def GetWorkflowServiceItemAttributeByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowServiceItemAttributeByMoid(body=body, **kwargs)

@register('GetWorkflowServiceItemDefinitionList')
def GetWorkflowServiceItemDefinitionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowServiceItemDefinitionList(body=body, **kwargs)

@register('GetWorkflowServiceItemDefinitionByMoid')
def GetWorkflowServiceItemDefinitionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowServiceItemDefinitionByMoid(body=body, **kwargs)

@register('GetWorkflowServiceItemHealthCheckDefinitionList')
def GetWorkflowServiceItemHealthCheckDefinitionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowServiceItemHealthCheckDefinitionList(body=body, **kwargs)

@register('GetWorkflowServiceItemHealthCheckDefinitionByMoid')
def GetWorkflowServiceItemHealthCheckDefinitionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowServiceItemHealthCheckDefinitionByMoid(body=body, **kwargs)

@register('GetWorkflowServiceItemHealthCheckExecutionList')
def GetWorkflowServiceItemHealthCheckExecutionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowServiceItemHealthCheckExecutionList(body=body, **kwargs)

@register('GetWorkflowServiceItemHealthCheckExecutionByMoid')
def GetWorkflowServiceItemHealthCheckExecutionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowServiceItemHealthCheckExecutionByMoid(body=body, **kwargs)

@register('GetWorkflowServiceItemInstanceList')
def GetWorkflowServiceItemInstanceList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowServiceItemInstanceList(body=body, **kwargs)

@register('GetWorkflowServiceItemInstanceByMoid')
def GetWorkflowServiceItemInstanceByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowServiceItemInstanceByMoid(body=body, **kwargs)

@register('GetWorkflowServiceItemOutputList')
def GetWorkflowServiceItemOutputList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowServiceItemOutputList(body=body, **kwargs)

@register('GetWorkflowServiceItemOutputByMoid')
def GetWorkflowServiceItemOutputByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowServiceItemOutputByMoid(body=body, **kwargs)

@register('GetWorkflowSshBatchExecutorList')
def GetWorkflowSshBatchExecutorList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowSshBatchExecutorList(body=body, **kwargs)

@register('GetWorkflowSshBatchExecutorByMoid')
def GetWorkflowSshBatchExecutorByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowSshBatchExecutorByMoid(body=body, **kwargs)

@register('GetWorkflowTaskDebugLogList')
def GetWorkflowTaskDebugLogList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowTaskDebugLogList(body=body, **kwargs)

@register('GetWorkflowTaskDebugLogByMoid')
def GetWorkflowTaskDebugLogByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowTaskDebugLogByMoid(body=body, **kwargs)

@register('GetWorkflowTaskDefinitionList')
def GetWorkflowTaskDefinitionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowTaskDefinitionList(body=body, **kwargs)

@register('GetWorkflowTaskDefinitionByMoid')
def GetWorkflowTaskDefinitionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowTaskDefinitionByMoid(body=body, **kwargs)

@register('GetWorkflowTaskInfoList')
def GetWorkflowTaskInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowTaskInfoList(body=body, **kwargs)

@register('GetWorkflowTaskInfoByMoid')
def GetWorkflowTaskInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowTaskInfoByMoid(body=body, **kwargs)

@register('GetWorkflowTaskMetadataList')
def GetWorkflowTaskMetadataList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowTaskMetadataList(body=body, **kwargs)

@register('GetWorkflowTaskMetadataByMoid')
def GetWorkflowTaskMetadataByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowTaskMetadataByMoid(body=body, **kwargs)

@register('GetWorkflowTemplateFunctionMetaList')
def GetWorkflowTemplateFunctionMetaList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowTemplateFunctionMetaList(body=body, **kwargs)

@register('GetWorkflowTemplateFunctionMetaByMoid')
def GetWorkflowTemplateFunctionMetaByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowTemplateFunctionMetaByMoid(body=body, **kwargs)

@register('GetWorkflowUiDisplayMetadataList')
def GetWorkflowUiDisplayMetadataList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowUiDisplayMetadataList(body=body, **kwargs)

@register('GetWorkflowUiDisplayMetadataByMoid')
def GetWorkflowUiDisplayMetadataByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowUiDisplayMetadataByMoid(body=body, **kwargs)

@register('GetWorkflowVariableList')
def GetWorkflowVariableList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowVariableList(body=body, **kwargs)

@register('GetWorkflowVariableByMoid')
def GetWorkflowVariableByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowVariableByMoid(body=body, **kwargs)

@register('GetWorkflowWorkflowDefinitionList')
def GetWorkflowWorkflowDefinitionList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowWorkflowDefinitionList(body=body, **kwargs)

@register('GetWorkflowWorkflowDefinitionByMoid')
def GetWorkflowWorkflowDefinitionByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowWorkflowDefinitionByMoid(body=body, **kwargs)

@register('GetWorkflowWorkflowInfoList')
def GetWorkflowWorkflowInfoList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowWorkflowInfoList(body=body, **kwargs)

@register('GetWorkflowWorkflowInfoByMoid')
def GetWorkflowWorkflowInfoByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowWorkflowInfoByMoid(body=body, **kwargs)

@register('GetWorkflowWorkflowMetadataList')
def GetWorkflowWorkflowMetadataList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowWorkflowMetadataList(body=body, **kwargs)

@register('GetWorkflowWorkflowMetadataByMoid')
def GetWorkflowWorkflowMetadataByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkflowWorkflowMetadataByMoid(body=body, **kwargs)

@register('GetWorkspaceFolderList')
def GetWorkspaceFolderList(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkspaceFolderList(body=body, **kwargs)

@register('GetWorkspaceFolderByMoid')
def GetWorkspaceFolderByMoid(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return IntersightClient().GetWorkspaceFolderByMoid(body=body, **kwargs)
