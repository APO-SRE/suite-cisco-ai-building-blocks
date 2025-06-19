from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_interface_type import ModelsInterfaceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsNetworkInterface")


@_attrs_define
class ModelsNetworkInterface:
    """NetworkInterface encapsulates properties of a network interface attached to a VRF. A NetworkInterface maybe a
    network port, VLAN interface (SVI), loopback, port channel or a sub-interface.

        Attributes:
            ipv_4_addresses (Union[Unset, list[str]]): IPv4 addresses of network interface. IPv4 addresses are readonly, and
                are set by some APIs (E.g. GetVrfs API when NeedIps is set to true).
            ipv_6_addresses (Union[Unset, list[str]]): IPv6 addresses of network interface. IPv6 addresses are readonly, and
                are set by some APIs (E.g. GetVrfs API when NeedIps is set to true).
            name (Union[Unset, str]): The name of the network interface.
            node_id (Union[Unset, str]): The node identifier where the interface is located. API users may specify either
                node name or node identifier.
            type_ (Union[Unset, ModelsInterfaceType]): InterfaceType defines an enumeration of network interface types.
            vlan_id (Union[Unset, int]): VLAN identifier - required only for VLAN interface. Name field is ignored when
                VlanId is specified.
            vni (Union[Unset, int]): The parent VNI of the VLAN. Valid only for VLAN interfaces.
    """

    ipv_4_addresses: Union[Unset, list[str]] = UNSET
    ipv_6_addresses: Union[Unset, list[str]] = UNSET
    name: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    type_: Union[Unset, ModelsInterfaceType] = UNSET
    vlan_id: Union[Unset, int] = UNSET
    vni: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipv_4_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ipv_4_addresses, Unset):
            ipv_4_addresses = self.ipv_4_addresses

        ipv_6_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ipv_6_addresses, Unset):
            ipv_6_addresses = self.ipv_6_addresses

        name = self.name

        node_id = self.node_id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        vlan_id = self.vlan_id

        vni = self.vni

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ipv_4_addresses is not UNSET:
            field_dict["ipv4Addresses"] = ipv_4_addresses
        if ipv_6_addresses is not UNSET:
            field_dict["ipv6Addresses"] = ipv_6_addresses
        if name is not UNSET:
            field_dict["name"] = name
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id
        if vni is not UNSET:
            field_dict["vni"] = vni

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ipv_4_addresses = cast(list[str], d.pop("ipv4Addresses", UNSET))

        ipv_6_addresses = cast(list[str], d.pop("ipv6Addresses", UNSET))

        name = d.pop("name", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ModelsInterfaceType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ModelsInterfaceType(_type_)

        vlan_id = d.pop("vlanId", UNSET)

        vni = d.pop("vni", UNSET)

        models_network_interface = cls(
            ipv_4_addresses=ipv_4_addresses,
            ipv_6_addresses=ipv_6_addresses,
            name=name,
            node_id=node_id,
            type_=type_,
            vlan_id=vlan_id,
            vni=vni,
        )

        models_network_interface.additional_properties = d
        return models_network_interface

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
