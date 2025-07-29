from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeSpecNetworkV1PlatformGET")


@_attrs_define
class NodeSpecNetworkV1PlatformGET:
    """Node Network config. Inband represents cluster internal network information, OOB represents user-accessible network
    information

        Attributes:
            gateway (Union[Unset, str]): IPv4 node gateway address
            gatewayv6 (Union[Unset, str]): IPv6 node gateway address
            subnet (Union[Unset, str]): IPv4 node subnet address
            subnetv6 (Union[Unset, str]): IPv6 node subnet address
            vlan_id (Union[Unset, int]): Node vlan ID
    """

    gateway: Union[Unset, str] = UNSET
    gatewayv6: Union[Unset, str] = UNSET
    subnet: Union[Unset, str] = UNSET
    subnetv6: Union[Unset, str] = UNSET
    vlan_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gateway = self.gateway

        gatewayv6 = self.gatewayv6

        subnet = self.subnet

        subnetv6 = self.subnetv6

        vlan_id = self.vlan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if gatewayv6 is not UNSET:
            field_dict["gatewayv6"] = gatewayv6
        if subnet is not UNSET:
            field_dict["subnet"] = subnet
        if subnetv6 is not UNSET:
            field_dict["subnetv6"] = subnetv6
        if vlan_id is not UNSET:
            field_dict["vlanID"] = vlan_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gateway = d.pop("gateway", UNSET)

        gatewayv6 = d.pop("gatewayv6", UNSET)

        subnet = d.pop("subnet", UNSET)

        subnetv6 = d.pop("subnetv6", UNSET)

        vlan_id = d.pop("vlanID", UNSET)

        node_spec_network_v1_platform_get = cls(
            gateway=gateway,
            gatewayv6=gatewayv6,
            subnet=subnet,
            subnetv6=subnetv6,
            vlan_id=vlan_id,
        )

        node_spec_network_v1_platform_get.additional_properties = d
        return node_spec_network_v1_platform_get

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
