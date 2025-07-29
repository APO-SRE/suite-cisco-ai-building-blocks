from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_app_data_spec_v4_sitemanagement_get_site_annotation import (
        SiteAppDataSpecV4SitemanagementGETSiteAnnotation,
    )
    from ..models.site_app_data_spec_v4_sitemanagement_get_site_annotation_lock import (
        SiteAppDataSpecV4SitemanagementGETSiteAnnotationLock,
    )


T = TypeVar("T", bound="SiteAppDataSpecV4SitemanagementGET")


@_attrs_define
class SiteAppDataSpecV4SitemanagementGET:
    """
    Attributes:
        apps (Union[Unset, list[str]]):
        site_annotation (Union[Unset, SiteAppDataSpecV4SitemanagementGETSiteAnnotation]):
        site_annotation_lock (Union[Unset, SiteAppDataSpecV4SitemanagementGETSiteAnnotationLock]):
        site_uuid (Union[Unset, str]):
    """

    apps: Union[Unset, list[str]] = UNSET
    site_annotation: Union[Unset, "SiteAppDataSpecV4SitemanagementGETSiteAnnotation"] = UNSET
    site_annotation_lock: Union[Unset, "SiteAppDataSpecV4SitemanagementGETSiteAnnotationLock"] = UNSET
    site_uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apps: Union[Unset, list[str]] = UNSET
        if not isinstance(self.apps, Unset):
            apps = self.apps

        site_annotation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.site_annotation, Unset):
            site_annotation = self.site_annotation.to_dict()

        site_annotation_lock: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.site_annotation_lock, Unset):
            site_annotation_lock = self.site_annotation_lock.to_dict()

        site_uuid = self.site_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apps is not UNSET:
            field_dict["apps"] = apps
        if site_annotation is not UNSET:
            field_dict["siteAnnotation"] = site_annotation
        if site_annotation_lock is not UNSET:
            field_dict["siteAnnotationLock"] = site_annotation_lock
        if site_uuid is not UNSET:
            field_dict["siteUUID"] = site_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.site_app_data_spec_v4_sitemanagement_get_site_annotation import (
            SiteAppDataSpecV4SitemanagementGETSiteAnnotation,
        )
        from ..models.site_app_data_spec_v4_sitemanagement_get_site_annotation_lock import (
            SiteAppDataSpecV4SitemanagementGETSiteAnnotationLock,
        )

        d = dict(src_dict)
        apps = cast(list[str], d.pop("apps", UNSET))

        _site_annotation = d.pop("siteAnnotation", UNSET)
        site_annotation: Union[Unset, SiteAppDataSpecV4SitemanagementGETSiteAnnotation]
        if isinstance(_site_annotation, Unset):
            site_annotation = UNSET
        else:
            site_annotation = SiteAppDataSpecV4SitemanagementGETSiteAnnotation.from_dict(_site_annotation)

        _site_annotation_lock = d.pop("siteAnnotationLock", UNSET)
        site_annotation_lock: Union[Unset, SiteAppDataSpecV4SitemanagementGETSiteAnnotationLock]
        if isinstance(_site_annotation_lock, Unset):
            site_annotation_lock = UNSET
        else:
            site_annotation_lock = SiteAppDataSpecV4SitemanagementGETSiteAnnotationLock.from_dict(_site_annotation_lock)

        site_uuid = d.pop("siteUUID", UNSET)

        site_app_data_spec_v4_sitemanagement_get = cls(
            apps=apps,
            site_annotation=site_annotation,
            site_annotation_lock=site_annotation_lock,
            site_uuid=site_uuid,
        )

        site_app_data_spec_v4_sitemanagement_get.additional_properties = d
        return site_app_data_spec_v4_sitemanagement_get

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
