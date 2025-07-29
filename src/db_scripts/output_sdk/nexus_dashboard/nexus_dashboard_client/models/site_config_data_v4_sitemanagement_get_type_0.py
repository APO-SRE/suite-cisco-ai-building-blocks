from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aci_config_v4_sitemanagement_get import ACIConfigV4SitemanagementGET


T = TypeVar("T", bound="SiteConfigDataV4SitemanagementGETType0")


@_attrs_define
class SiteConfigDataV4SitemanagementGETType0:
    """
    Attributes:
        aci (Union[Unset, ACIConfigV4SitemanagementGET]):
    """

    aci: Union[Unset, "ACIConfigV4SitemanagementGET"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aci: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.aci, Unset):
            aci = self.aci.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aci is not UNSET:
            field_dict["aci"] = aci

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aci_config_v4_sitemanagement_get import ACIConfigV4SitemanagementGET

        d = dict(src_dict)
        _aci = d.pop("aci", UNSET)
        aci: Union[Unset, ACIConfigV4SitemanagementGET]
        if isinstance(_aci, Unset):
            aci = UNSET
        else:
            aci = ACIConfigV4SitemanagementGET.from_dict(_aci)

        site_config_data_v4_sitemanagement_get_type_0 = cls(
            aci=aci,
        )

        site_config_data_v4_sitemanagement_get_type_0.additional_properties = d
        return site_config_data_v4_sitemanagement_get_type_0

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
