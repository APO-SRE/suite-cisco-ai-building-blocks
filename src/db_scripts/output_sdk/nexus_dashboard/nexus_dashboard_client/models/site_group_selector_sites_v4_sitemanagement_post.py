from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.site_group_selector_sites_v4_sitemanagement_post_selector_site_type import (
    SiteGroupSelectorSitesV4SitemanagementPOSTSelectorSiteType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_group_selector_sites_v4_sitemanagement_post_selector import (
        SiteGroupSelectorSitesV4SitemanagementPOSTSelector,
    )


T = TypeVar("T", bound="SiteGroupSelectorSitesV4SitemanagementPOST")


@_attrs_define
class SiteGroupSelectorSitesV4SitemanagementPOST:
    """
    Attributes:
        selector (Union[Unset, SiteGroupSelectorSitesV4SitemanagementPOSTSelector]):
        selector_site_type (Union[Unset, SiteGroupSelectorSitesV4SitemanagementPOSTSelectorSiteType]):
    """

    selector: Union[Unset, "SiteGroupSelectorSitesV4SitemanagementPOSTSelector"] = UNSET
    selector_site_type: Union[Unset, SiteGroupSelectorSitesV4SitemanagementPOSTSelectorSiteType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        selector: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.selector, Unset):
            selector = self.selector.to_dict()

        selector_site_type: Union[Unset, str] = UNSET
        if not isinstance(self.selector_site_type, Unset):
            selector_site_type = self.selector_site_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if selector is not UNSET:
            field_dict["selector"] = selector
        if selector_site_type is not UNSET:
            field_dict["selector-site-type"] = selector_site_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.site_group_selector_sites_v4_sitemanagement_post_selector import (
            SiteGroupSelectorSitesV4SitemanagementPOSTSelector,
        )

        d = dict(src_dict)
        _selector = d.pop("selector", UNSET)
        selector: Union[Unset, SiteGroupSelectorSitesV4SitemanagementPOSTSelector]
        if isinstance(_selector, Unset):
            selector = UNSET
        else:
            selector = SiteGroupSelectorSitesV4SitemanagementPOSTSelector.from_dict(_selector)

        _selector_site_type = d.pop("selector-site-type", UNSET)
        selector_site_type: Union[Unset, SiteGroupSelectorSitesV4SitemanagementPOSTSelectorSiteType]
        if isinstance(_selector_site_type, Unset):
            selector_site_type = UNSET
        else:
            selector_site_type = SiteGroupSelectorSitesV4SitemanagementPOSTSelectorSiteType(_selector_site_type)

        site_group_selector_sites_v4_sitemanagement_post = cls(
            selector=selector,
            selector_site_type=selector_site_type,
        )

        site_group_selector_sites_v4_sitemanagement_post.additional_properties = d
        return site_group_selector_sites_v4_sitemanagement_post

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
