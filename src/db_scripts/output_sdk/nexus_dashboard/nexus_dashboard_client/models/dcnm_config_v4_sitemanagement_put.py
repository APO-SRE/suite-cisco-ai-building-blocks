from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DCNMConfigV4SitemanagementPUT")


@_attrs_define
class DCNMConfigV4SitemanagementPUT:
    """
    Attributes:
        fabric_name (Union[Unset, str]): DCNM fabric name
        fabric_technology (Union[Unset, str]): DCNM/NDFC fabric technology - VxlanFabric, External, EBGPVxlanFabric,
            EBGPRoutedFabric,  LanClassic, Meta, IosXEVxlanFabric, Srv6Fabric, LanMonitor, SwitchGroup, MsoSiteGroup,
            SanFabric,  IpfmFabric, IpfmClassic, VlanFabric
        fabric_type (Union[Unset, str]): DCNM fabric type
    """

    fabric_name: Union[Unset, str] = UNSET
    fabric_technology: Union[Unset, str] = UNSET
    fabric_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fabric_name = self.fabric_name

        fabric_technology = self.fabric_technology

        fabric_type = self.fabric_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fabric_name is not UNSET:
            field_dict["fabricName"] = fabric_name
        if fabric_technology is not UNSET:
            field_dict["fabricTechnology"] = fabric_technology
        if fabric_type is not UNSET:
            field_dict["fabricType"] = fabric_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fabric_name = d.pop("fabricName", UNSET)

        fabric_technology = d.pop("fabricTechnology", UNSET)

        fabric_type = d.pop("fabricType", UNSET)

        dcnm_config_v4_sitemanagement_put = cls(
            fabric_name=fabric_name,
            fabric_technology=fabric_technology,
            fabric_type=fabric_type,
        )

        dcnm_config_v4_sitemanagement_put.additional_properties = d
        return dcnm_config_v4_sitemanagement_put

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
