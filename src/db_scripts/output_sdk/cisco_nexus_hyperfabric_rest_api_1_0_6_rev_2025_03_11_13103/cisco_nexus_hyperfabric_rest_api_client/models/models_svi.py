from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSvi")


@_attrs_define
class ModelsSvi:
    """A Switch Virtual Interface (SVI) or VLAN interface is a logical Layer 3 interface that connects a VLAN to a Layer 3
    virtual routing and forwarding (VRF) instance and acts as a gateway for the hosts connected to the VLAN. A Static
    Anycast Gateway SVI is an SVI deployed on multiple devices enabling the use of the same gateway IP addresses across
    all the nodes that are part of a VNI.

        Attributes:
            enabled (Union[Unset, bool]): The enabled state of the SVI which indicates if the SVI is enabled or disabled.
            ipv_4_addresses (Union[Unset, list[str]]): A list of up to two IPv4 host addresses with subnet mask to be
                configured on the SVI. If there are two IP addresses on the SVI, then there are two possibilities. 	a) If IPS
                are in two different networks, then SVI gets two networks. 	b) If IPS are in the same network, then the first IP
                address is the primary gateway 	  and second IP address is the secondary gateway.
            ipv_6_addresses (Union[Unset, list[str]]): A list of up to one IPv6 host address with subnet mask to be
                configured on the SVI.
    """

    enabled: Union[Unset, bool] = UNSET
    ipv_4_addresses: Union[Unset, list[str]] = UNSET
    ipv_6_addresses: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        ipv_4_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ipv_4_addresses, Unset):
            ipv_4_addresses = self.ipv_4_addresses

        ipv_6_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ipv_6_addresses, Unset):
            ipv_6_addresses = self.ipv_6_addresses

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if ipv_4_addresses is not UNSET:
            field_dict["ipv4Addresses"] = ipv_4_addresses
        if ipv_6_addresses is not UNSET:
            field_dict["ipv6Addresses"] = ipv_6_addresses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        ipv_4_addresses = cast(list[str], d.pop("ipv4Addresses", UNSET))

        ipv_6_addresses = cast(list[str], d.pop("ipv6Addresses", UNSET))

        models_svi = cls(
            enabled=enabled,
            ipv_4_addresses=ipv_4_addresses,
            ipv_6_addresses=ipv_6_addresses,
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
