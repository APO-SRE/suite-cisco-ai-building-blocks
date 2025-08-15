from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_restrictions_v4_sitemanagement_post import GroupRestrictionsV4SitemanagementPOST
    from ..models.site_group_selector_sites_v4_sitemanagement_post import SiteGroupSelectorSitesV4SitemanagementPOST


T = TypeVar("T", bound="SiteGroupSpecWrapperV4SitemanagementPOST")


@_attrs_define
class SiteGroupSpecWrapperV4SitemanagementPOST:
    """
    Attributes:
        name (str):
        default_group (Union[Unset, bool]):
        description (Union[Unset, str]):
        restrictions (Union[Unset, GroupRestrictionsV4SitemanagementPOST]):
        selector_sites (Union[Unset, SiteGroupSelectorSitesV4SitemanagementPOST]):
    """

    name: str
    default_group: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    restrictions: Union[Unset, "GroupRestrictionsV4SitemanagementPOST"] = UNSET
    selector_sites: Union[Unset, "SiteGroupSelectorSitesV4SitemanagementPOST"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        default_group = self.default_group

        description = self.description

        restrictions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.restrictions, Unset):
            restrictions = self.restrictions.to_dict()

        selector_sites: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.selector_sites, Unset):
            selector_sites = self.selector_sites.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if default_group is not UNSET:
            field_dict["defaultGroup"] = default_group
        if description is not UNSET:
            field_dict["description"] = description
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions
        if selector_sites is not UNSET:
            field_dict["selector-sites"] = selector_sites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_restrictions_v4_sitemanagement_post import GroupRestrictionsV4SitemanagementPOST
        from ..models.site_group_selector_sites_v4_sitemanagement_post import SiteGroupSelectorSitesV4SitemanagementPOST

        d = dict(src_dict)
        name = d.pop("name")

        default_group = d.pop("defaultGroup", UNSET)

        description = d.pop("description", UNSET)

        _restrictions = d.pop("restrictions", UNSET)
        restrictions: Union[Unset, GroupRestrictionsV4SitemanagementPOST]
        if isinstance(_restrictions, Unset):
            restrictions = UNSET
        else:
            restrictions = GroupRestrictionsV4SitemanagementPOST.from_dict(_restrictions)

        _selector_sites = d.pop("selector-sites", UNSET)
        selector_sites: Union[Unset, SiteGroupSelectorSitesV4SitemanagementPOST]
        if isinstance(_selector_sites, Unset):
            selector_sites = UNSET
        else:
            selector_sites = SiteGroupSelectorSitesV4SitemanagementPOST.from_dict(_selector_sites)

        site_group_spec_wrapper_v4_sitemanagement_post = cls(
            name=name,
            default_group=default_group,
            description=description,
            restrictions=restrictions,
            selector_sites=selector_sites,
        )

        site_group_spec_wrapper_v4_sitemanagement_post.additional_properties = d
        return site_group_spec_wrapper_v4_sitemanagement_post

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
