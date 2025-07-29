from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_restrictions_v4_sitemanagement_put import GroupRestrictionsV4SitemanagementPUT
    from ..models.site_group_selector_sites_v4_sitemanagement_put import SiteGroupSelectorSitesV4SitemanagementPUT


T = TypeVar("T", bound="SiteGroupSpecV4SitemanagementPUT")


@_attrs_define
class SiteGroupSpecV4SitemanagementPUT:
    """
    Attributes:
        default_group (Union[Unset, bool]):
        description (Union[Unset, str]):
        name (Union[Unset, str]):
        restrictions (Union[Unset, GroupRestrictionsV4SitemanagementPUT]):
        selector_sites (Union[Unset, SiteGroupSelectorSitesV4SitemanagementPUT]):
    """

    default_group: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    restrictions: Union[Unset, "GroupRestrictionsV4SitemanagementPUT"] = UNSET
    selector_sites: Union[Unset, "SiteGroupSelectorSitesV4SitemanagementPUT"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_group = self.default_group

        description = self.description

        name = self.name

        restrictions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.restrictions, Unset):
            restrictions = self.restrictions.to_dict()

        selector_sites: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.selector_sites, Unset):
            selector_sites = self.selector_sites.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_group is not UNSET:
            field_dict["defaultGroup"] = default_group
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions
        if selector_sites is not UNSET:
            field_dict["selector-sites"] = selector_sites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_restrictions_v4_sitemanagement_put import GroupRestrictionsV4SitemanagementPUT
        from ..models.site_group_selector_sites_v4_sitemanagement_put import SiteGroupSelectorSitesV4SitemanagementPUT

        d = dict(src_dict)
        default_group = d.pop("defaultGroup", UNSET)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        _restrictions = d.pop("restrictions", UNSET)
        restrictions: Union[Unset, GroupRestrictionsV4SitemanagementPUT]
        if isinstance(_restrictions, Unset):
            restrictions = UNSET
        else:
            restrictions = GroupRestrictionsV4SitemanagementPUT.from_dict(_restrictions)

        _selector_sites = d.pop("selector-sites", UNSET)
        selector_sites: Union[Unset, SiteGroupSelectorSitesV4SitemanagementPUT]
        if isinstance(_selector_sites, Unset):
            selector_sites = UNSET
        else:
            selector_sites = SiteGroupSelectorSitesV4SitemanagementPUT.from_dict(_selector_sites)

        site_group_spec_v4_sitemanagement_put = cls(
            default_group=default_group,
            description=description,
            name=name,
            restrictions=restrictions,
            selector_sites=selector_sites,
        )

        site_group_spec_v4_sitemanagement_put.additional_properties = d
        return site_group_spec_v4_sitemanagement_put

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
