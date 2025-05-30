from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsVniDhcp")


@_attrs_define
class ModelsVniDhcp:
    """VniDhcp encapsulates properties of a VNI DHCP relay. VniDhcp is used for setting up inter-VNI DHCP relay.

    Attributes:
        ipv_4_enabled (Union[Unset, bool]): Indicates that IPv4 DHCP relay is enabled for VNI.
        ipv_6_enabled (Union[Unset, bool]): Indicates that IPv6 DHCP relay is enabled for VNI.
        vni (Union[Unset, int]): The identifier of VNI that needs DHCP relay.
    """

    ipv_4_enabled: Union[Unset, bool] = UNSET
    ipv_6_enabled: Union[Unset, bool] = UNSET
    vni: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipv_4_enabled = self.ipv_4_enabled

        ipv_6_enabled = self.ipv_6_enabled

        vni = self.vni

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ipv_4_enabled is not UNSET:
            field_dict["ipv4Enabled"] = ipv_4_enabled
        if ipv_6_enabled is not UNSET:
            field_dict["ipv6Enabled"] = ipv_6_enabled
        if vni is not UNSET:
            field_dict["vni"] = vni

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ipv_4_enabled = d.pop("ipv4Enabled", UNSET)

        ipv_6_enabled = d.pop("ipv6Enabled", UNSET)

        vni = d.pop("vni", UNSET)

        models_vni_dhcp = cls(
            ipv_4_enabled=ipv_4_enabled,
            ipv_6_enabled=ipv_6_enabled,
            vni=vni,
        )

        models_vni_dhcp.additional_properties = d
        return models_vni_dhcp

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
