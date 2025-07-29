from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.site_group_selector_sites_v4_sitemanagement_get_selector_site_type import (
    SiteGroupSelectorSitesV4SitemanagementGETSelectorSiteType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_group_selector_sites_v4_sitemanagement_get_selector import (
        SiteGroupSelectorSitesV4SitemanagementGETSelector,
    )


T = TypeVar("T", bound="SiteGroupSelectorSitesV4SitemanagementGET")


@_attrs_define
class SiteGroupSelectorSitesV4SitemanagementGET:
    """
    Attributes:
        selector (Union[Unset, SiteGroupSelectorSitesV4SitemanagementGETSelector]):
        selector_site_type (Union[Unset, SiteGroupSelectorSitesV4SitemanagementGETSelectorSiteType]):
    """

    selector: Union[Unset, "SiteGroupSelectorSitesV4SitemanagementGETSelector"] = UNSET
    selector_site_type: Union[Unset, SiteGroupSelectorSitesV4SitemanagementGETSelectorSiteType] = UNSET
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
        from ..models.site_group_selector_sites_v4_sitemanagement_get_selector import (
            SiteGroupSelectorSitesV4SitemanagementGETSelector,
        )

        d = dict(src_dict)
        _selector = d.pop("selector", UNSET)
        selector: Union[Unset, SiteGroupSelectorSitesV4SitemanagementGETSelector]
        if isinstance(_selector, Unset):
            selector = UNSET
        else:
            selector = SiteGroupSelectorSitesV4SitemanagementGETSelector.from_dict(_selector)

        _selector_site_type = d.pop("selector-site-type", UNSET)
        selector_site_type: Union[Unset, SiteGroupSelectorSitesV4SitemanagementGETSelectorSiteType]
        if isinstance(_selector_site_type, Unset):
            selector_site_type = UNSET
        else:
            selector_site_type = SiteGroupSelectorSitesV4SitemanagementGETSelectorSiteType(_selector_site_type)

        site_group_selector_sites_v4_sitemanagement_get = cls(
            selector=selector,
            selector_site_type=selector_site_type,
        )

        site_group_selector_sites_v4_sitemanagement_get.additional_properties = d
        return site_group_selector_sites_v4_sitemanagement_get

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
