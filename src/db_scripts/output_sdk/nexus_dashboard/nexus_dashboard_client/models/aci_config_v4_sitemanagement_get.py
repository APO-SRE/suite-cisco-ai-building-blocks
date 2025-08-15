from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ACIConfigV4SitemanagementGET")


@_attrs_define
class ACIConfigV4SitemanagementGET:
    """
    Attributes:
        inband_epgdn (Union[Unset, str]): inband epg dn configured for site
    """

    inband_epgdn: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inband_epgdn = self.inband_epgdn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inband_epgdn is not UNSET:
            field_dict["InbandEPGDN"] = inband_epgdn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inband_epgdn = d.pop("InbandEPGDN", UNSET)

        aci_config_v4_sitemanagement_get = cls(
            inband_epgdn=inband_epgdn,
        )

        aci_config_v4_sitemanagement_get.additional_properties = d
        return aci_config_v4_sitemanagement_get

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
