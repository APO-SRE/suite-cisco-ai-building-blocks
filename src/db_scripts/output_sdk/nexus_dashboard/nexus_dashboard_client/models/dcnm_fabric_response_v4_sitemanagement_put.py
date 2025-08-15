from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DCNMFabricResponseV4SitemanagementPUT")


@_attrs_define
class DCNMFabricResponseV4SitemanagementPUT:
    """
    Attributes:
        in_use (Union[Unset, bool]): DCNM Site already on-boarded
        name (Union[Unset, str]): DCNM fabric name
        parent_name (Union[Unset, str]): DCNM parent fabric name
        technology (Union[Unset, str]): DCNM/NDFC fabric technology - VxlanFabric, External, EBGPVxlanFabric,
            EBGPRoutedFabric, LanClassic,  Meta, IosXEVxlanFabric, Srv6Fabric, LanMonitor, SwitchGroup, MsoSiteGroup,
            SanFabric,  IpfmFabric, IpfmClassic, VlanFabric
        type_ (Union[Unset, str]): DCNM Site fabric type
    """

    in_use: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    parent_name: Union[Unset, str] = UNSET
    technology: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        in_use = self.in_use

        name = self.name

        parent_name = self.parent_name

        technology = self.technology

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if in_use is not UNSET:
            field_dict["inUse"] = in_use
        if name is not UNSET:
            field_dict["name"] = name
        if parent_name is not UNSET:
            field_dict["parentName"] = parent_name
        if technology is not UNSET:
            field_dict["technology"] = technology
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        in_use = d.pop("inUse", UNSET)

        name = d.pop("name", UNSET)

        parent_name = d.pop("parentName", UNSET)

        technology = d.pop("technology", UNSET)

        type_ = d.pop("type", UNSET)

        dcnm_fabric_response_v4_sitemanagement_put = cls(
            in_use=in_use,
            name=name,
            parent_name=parent_name,
            technology=technology,
            type_=type_,
        )

        dcnm_fabric_response_v4_sitemanagement_put.additional_properties = d
        return dcnm_fabric_response_v4_sitemanagement_put

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
