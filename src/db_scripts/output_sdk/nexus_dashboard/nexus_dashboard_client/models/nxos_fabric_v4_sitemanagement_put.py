from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NXOSFabricV4SitemanagementPUT")


@_attrs_define
class NXOSFabricV4SitemanagementPUT:
    """
    Attributes:
        name (Union[Unset, str]): DCNM/NDFC fabric name
        read_only (Union[Unset, bool]): DCNM/NDFC fabric readonly mode
        site_id (Union[Unset, str]): DCNM/NDFC fabric siteID
        technology (Union[Unset, str]): DCNM/NDFC fabric technology - VxlanFabric, External, EBGPVxlanFabric,
            EBGPRoutedFabric,  LanClassic, Meta, IosXEVxlanFabric, Srv6Fabric, LanMonitor, SwitchGroup, MsoSiteGroup,
            SanFabric,  IpfmFabric, IpfmClassic, VlanFabric
        type_ (Union[Unset, str]): DCNM/NDFC fabric types - SwitchFabric, External,LanMonitor, Mfd,
            MsoSiteGroup,SanFabric
    """

    name: Union[Unset, str] = UNSET
    read_only: Union[Unset, bool] = UNSET
    site_id: Union[Unset, str] = UNSET
    technology: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        read_only = self.read_only

        site_id = self.site_id

        technology = self.technology

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only
        if site_id is not UNSET:
            field_dict["siteID"] = site_id
        if technology is not UNSET:
            field_dict["technology"] = technology
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        read_only = d.pop("readOnly", UNSET)

        site_id = d.pop("siteID", UNSET)

        technology = d.pop("technology", UNSET)

        type_ = d.pop("type", UNSET)

        nxos_fabric_v4_sitemanagement_put = cls(
            name=name,
            read_only=read_only,
            site_id=site_id,
            technology=technology,
            type_=type_,
        )

        nxos_fabric_v4_sitemanagement_put.additional_properties = d
        return nxos_fabric_v4_sitemanagement_put

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
