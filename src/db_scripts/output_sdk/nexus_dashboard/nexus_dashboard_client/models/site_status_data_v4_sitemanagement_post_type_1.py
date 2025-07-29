from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ndfc_status_v4_sitemanagement_post import NDFCStatusV4SitemanagementPOST


T = TypeVar("T", bound="SiteStatusDataV4SitemanagementPOSTType1")


@_attrs_define
class SiteStatusDataV4SitemanagementPOSTType1:
    """
    Attributes:
        ndfc (Union[Unset, NDFCStatusV4SitemanagementPOST]):
    """

    ndfc: Union[Unset, "NDFCStatusV4SitemanagementPOST"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ndfc: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ndfc, Unset):
            ndfc = self.ndfc.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ndfc is not UNSET:
            field_dict["ndfc"] = ndfc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ndfc_status_v4_sitemanagement_post import NDFCStatusV4SitemanagementPOST

        d = dict(src_dict)
        _ndfc = d.pop("ndfc", UNSET)
        ndfc: Union[Unset, NDFCStatusV4SitemanagementPOST]
        if isinstance(_ndfc, Unset):
            ndfc = UNSET
        else:
            ndfc = NDFCStatusV4SitemanagementPOST.from_dict(_ndfc)

        site_status_data_v4_sitemanagement_post_type_1 = cls(
            ndfc=ndfc,
        )

        site_status_data_v4_sitemanagement_post_type_1.additional_properties = d
        return site_status_data_v4_sitemanagement_post_type_1

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
