from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dcnm_status_v4_sitemanagement_put import DCNMStatusV4SitemanagementPUT


T = TypeVar("T", bound="SiteStatusDataV4SitemanagementPUTType2")


@_attrs_define
class SiteStatusDataV4SitemanagementPUTType2:
    """
    Attributes:
        dcnm (Union[Unset, DCNMStatusV4SitemanagementPUT]):
    """

    dcnm: Union[Unset, "DCNMStatusV4SitemanagementPUT"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dcnm: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dcnm, Unset):
            dcnm = self.dcnm.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dcnm is not UNSET:
            field_dict["dcnm"] = dcnm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dcnm_status_v4_sitemanagement_put import DCNMStatusV4SitemanagementPUT

        d = dict(src_dict)
        _dcnm = d.pop("dcnm", UNSET)
        dcnm: Union[Unset, DCNMStatusV4SitemanagementPUT]
        if isinstance(_dcnm, Unset):
            dcnm = UNSET
        else:
            dcnm = DCNMStatusV4SitemanagementPUT.from_dict(_dcnm)

        site_status_data_v4_sitemanagement_put_type_2 = cls(
            dcnm=dcnm,
        )

        site_status_data_v4_sitemanagement_put_type_2.additional_properties = d
        return site_status_data_v4_sitemanagement_put_type_2

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
