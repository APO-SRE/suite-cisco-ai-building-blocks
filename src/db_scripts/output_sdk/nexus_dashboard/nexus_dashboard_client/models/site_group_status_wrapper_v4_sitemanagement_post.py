from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteGroupStatusWrapperV4SitemanagementPOST")


@_attrs_define
class SiteGroupStatusWrapperV4SitemanagementPOST:
    """
    Attributes:
        apps (Union[Unset, list[str]]):
        members (Union[Unset, list[str]]):
    """

    apps: Union[Unset, list[str]] = UNSET
    members: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apps: Union[Unset, list[str]] = UNSET
        if not isinstance(self.apps, Unset):
            apps = self.apps

        members: Union[Unset, list[str]] = UNSET
        if not isinstance(self.members, Unset):
            members = self.members

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apps is not UNSET:
            field_dict["apps"] = apps
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        apps = cast(list[str], d.pop("apps", UNSET))

        members = cast(list[str], d.pop("members", UNSET))

        site_group_status_wrapper_v4_sitemanagement_post = cls(
            apps=apps,
            members=members,
        )

        site_group_status_wrapper_v4_sitemanagement_post.additional_properties = d
        return site_group_status_wrapper_v4_sitemanagement_post

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
