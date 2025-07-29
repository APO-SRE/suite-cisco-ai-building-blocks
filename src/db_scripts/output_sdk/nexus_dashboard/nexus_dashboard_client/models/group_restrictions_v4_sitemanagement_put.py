from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupRestrictionsV4SitemanagementPUT")


@_attrs_define
class GroupRestrictionsV4SitemanagementPUT:
    """
    Attributes:
        allow_non_empty_delete (Union[Unset, bool]):
        allow_remote_members (Union[Unset, bool]):
    """

    allow_non_empty_delete: Union[Unset, bool] = UNSET
    allow_remote_members: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_non_empty_delete = self.allow_non_empty_delete

        allow_remote_members = self.allow_remote_members

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_non_empty_delete is not UNSET:
            field_dict["allow-non-empty-delete"] = allow_non_empty_delete
        if allow_remote_members is not UNSET:
            field_dict["allow-remote-members"] = allow_remote_members

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_non_empty_delete = d.pop("allow-non-empty-delete", UNSET)

        allow_remote_members = d.pop("allow-remote-members", UNSET)

        group_restrictions_v4_sitemanagement_put = cls(
            allow_non_empty_delete=allow_non_empty_delete,
            allow_remote_members=allow_remote_members,
        )

        group_restrictions_v4_sitemanagement_put.additional_properties = d
        return group_restrictions_v4_sitemanagement_put

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
