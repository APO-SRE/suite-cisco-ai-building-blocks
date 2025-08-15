from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.group_selector_v4_sitemanagement_post import GroupSelectorV4SitemanagementPOST


T = TypeVar("T", bound="SiteGroupSelectorSitesV4SitemanagementPOSTSelector")


@_attrs_define
class SiteGroupSelectorSitesV4SitemanagementPOSTSelector:
    """ """

    additional_properties: dict[str, "GroupSelectorV4SitemanagementPOST"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_selector_v4_sitemanagement_post import GroupSelectorV4SitemanagementPOST

        d = dict(src_dict)
        site_group_selector_sites_v4_sitemanagement_post_selector = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = GroupSelectorV4SitemanagementPOST.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        site_group_selector_sites_v4_sitemanagement_post_selector.additional_properties = additional_properties
        return site_group_selector_sites_v4_sitemanagement_post_selector

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "GroupSelectorV4SitemanagementPOST":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "GroupSelectorV4SitemanagementPOST") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
