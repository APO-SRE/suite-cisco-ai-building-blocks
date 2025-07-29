from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppInstancesV4AaaPOST")


@_attrs_define
class AppInstancesV4AaaPOST:
    """
    Attributes:
        app_id (Union[Unset, str]): Application ID
        last_updated (Union[Unset, str]): Application last updated timestamp
    """

    app_id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        last_updated = self.last_updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["appID"] = app_id
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_id = d.pop("appID", UNSET)

        last_updated = d.pop("lastUpdated", UNSET)

        app_instances_v4_aaa_post = cls(
            app_id=app_id,
            last_updated=last_updated,
        )

        app_instances_v4_aaa_post.additional_properties = d
        return app_instances_v4_aaa_post

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
