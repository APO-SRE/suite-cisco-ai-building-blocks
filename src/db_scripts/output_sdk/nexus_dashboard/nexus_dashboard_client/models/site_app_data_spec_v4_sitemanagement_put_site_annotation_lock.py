from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.annotation_lock_value_v4_sitemanagement_put import AnnotationLockValueV4SitemanagementPUT


T = TypeVar("T", bound="SiteAppDataSpecV4SitemanagementPUTSiteAnnotationLock")


@_attrs_define
class SiteAppDataSpecV4SitemanagementPUTSiteAnnotationLock:
    """ """

    additional_properties: dict[str, "AnnotationLockValueV4SitemanagementPUT"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.annotation_lock_value_v4_sitemanagement_put import AnnotationLockValueV4SitemanagementPUT

        d = dict(src_dict)
        site_app_data_spec_v4_sitemanagement_put_site_annotation_lock = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = AnnotationLockValueV4SitemanagementPUT.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        site_app_data_spec_v4_sitemanagement_put_site_annotation_lock.additional_properties = additional_properties
        return site_app_data_spec_v4_sitemanagement_put_site_annotation_lock

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "AnnotationLockValueV4SitemanagementPUT":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "AnnotationLockValueV4SitemanagementPUT") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
