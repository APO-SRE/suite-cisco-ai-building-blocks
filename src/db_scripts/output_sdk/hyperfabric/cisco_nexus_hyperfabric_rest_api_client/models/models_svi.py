from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSvi")


@_attrs_define
class ModelsSvi:
    """Svi encapsulates properties of a Switch Virtual Interface (SVI). A Svi is a Layer3 interface for a VLAN on a given
    switch. NOTES:  * Svi is used to link a Vrf to a Vlan. Svi also acts as a gateway for the   hosts connected to the
    Vlan.  * Svi can be a static-anycast-gateway. In this mode, Svi is not bound to   a specific node. Instead, it gets
    mapped to all nodes where Vlan

        Attributes:
            enabled (Union[Unset, bool]): Indicates if the SVI is in enabled state or not.
            ipv_4_addresses (Union[Unset, list[str]]): IPv4 addresses of SVI. The service supports up to 1 IPv4 address, and
                address must be a network address. Meaning, address must be in CIDR format with CIDR < 32.
            ipv_6_addresses (Union[Unset, list[str]]): IPv6 addresses of SVI. The service supports up to 1 IPv6 address, and
                address must be a network address. Meaning, address must be in CIDR format with CIDR < 128.
            node_id (Union[Unset, str]): The optional node identifier. Must be empty for static-anycast-gateway.
            vlan_id (Union[Unset, int]): The identifier of Vlan to which this SVI belongs to.
    """

    enabled: Union[Unset, bool] = UNSET
    ipv_4_addresses: Union[Unset, list[str]] = UNSET
    ipv_6_addresses: Union[Unset, list[str]] = UNSET
    node_id: Union[Unset, str] = UNSET
    vlan_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        ipv_4_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ipv_4_addresses, Unset):
            ipv_4_addresses = self.ipv_4_addresses

        ipv_6_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ipv_6_addresses, Unset):
            ipv_6_addresses = self.ipv_6_addresses

        node_id = self.node_id

        vlan_id = self.vlan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if ipv_4_addresses is not UNSET:
            field_dict["ipv4Addresses"] = ipv_4_addresses
        if ipv_6_addresses is not UNSET:
            field_dict["ipv6Addresses"] = ipv_6_addresses
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        ipv_4_addresses = cast(list[str], d.pop("ipv4Addresses", UNSET))

        ipv_6_addresses = cast(list[str], d.pop("ipv6Addresses", UNSET))

        node_id = d.pop("nodeId", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        models_svi = cls(
            enabled=enabled,
            ipv_4_addresses=ipv_4_addresses,
            ipv_6_addresses=ipv_6_addresses,
            node_id=node_id,
            vlan_id=vlan_id,
        )

        models_svi.additional_properties = d
        return models_svi

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
