from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteControllerV4SitemanagementGET")


@_attrs_define
class SiteControllerV4SitemanagementGET:
    """
    Attributes:
        data_ip (Union[Unset, str]): ACI/cloudACI/DCNM/NDFC controller node Data IP
        data_url (Union[Unset, str]): ACI/cloudACI/DCNM/NDFC controller node Data URL
        fabric_domain (Union[Unset, str]): ACI/cloudACI/DCNM/NDFC fabric domain
        management_ip (Union[Unset, str]): ACI/cloudACI/DCNM/NDFC controller node Management IP
        management_url (Union[Unset, str]): ACI/cloudACI/DCNM/NDFC controller node management URL
        sn (Union[Unset, str]): ACI/cloudACI/DCNM/NDFC controller node Serial number
        version (Union[Unset, str]): ACI/cloudACI/DCNM/NDFC controller node version
    """

    data_ip: Union[Unset, str] = UNSET
    data_url: Union[Unset, str] = UNSET
    fabric_domain: Union[Unset, str] = UNSET
    management_ip: Union[Unset, str] = UNSET
    management_url: Union[Unset, str] = UNSET
    sn: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_ip = self.data_ip

        data_url = self.data_url

        fabric_domain = self.fabric_domain

        management_ip = self.management_ip

        management_url = self.management_url

        sn = self.sn

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_ip is not UNSET:
            field_dict["dataIP"] = data_ip
        if data_url is not UNSET:
            field_dict["dataURL"] = data_url
        if fabric_domain is not UNSET:
            field_dict["fabricDomain"] = fabric_domain
        if management_ip is not UNSET:
            field_dict["managementIP"] = management_ip
        if management_url is not UNSET:
            field_dict["managementURL"] = management_url
        if sn is not UNSET:
            field_dict["sn"] = sn
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_ip = d.pop("dataIP", UNSET)

        data_url = d.pop("dataURL", UNSET)

        fabric_domain = d.pop("fabricDomain", UNSET)

        management_ip = d.pop("managementIP", UNSET)

        management_url = d.pop("managementURL", UNSET)

        sn = d.pop("sn", UNSET)

        version = d.pop("version", UNSET)

        site_controller_v4_sitemanagement_get = cls(
            data_ip=data_ip,
            data_url=data_url,
            fabric_domain=fabric_domain,
            management_ip=management_ip,
            management_url=management_url,
            sn=sn,
            version=version,
        )

        site_controller_v4_sitemanagement_get.additional_properties = d
        return site_controller_v4_sitemanagement_get

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
