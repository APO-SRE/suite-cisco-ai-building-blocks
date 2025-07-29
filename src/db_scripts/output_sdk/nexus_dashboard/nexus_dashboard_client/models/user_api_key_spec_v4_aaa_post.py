from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAPIKeySpecV4AaaPOST")


@_attrs_define
class UserAPIKeySpecV4AaaPOST:
    """
    Attributes:
        api_key (Union[Unset, str]): User API Key for a local user to access ND Resources
        api_key_name (Union[Unset, str]): Name of the User API Key
        uuid (Union[Unset, str]): Unique identifier for an API Key made by MD5 hashing + formatting to appear as uuid
    """

    api_key: Union[Unset, str] = UNSET
    api_key_name: Union[Unset, str] = UNSET
    uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        api_key_name = self.api_key_name

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if api_key_name is not UNSET:
            field_dict["apiKeyName"] = api_key_name
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey", UNSET)

        api_key_name = d.pop("apiKeyName", UNSET)

        uuid = d.pop("uuid", UNSET)

        user_api_key_spec_v4_aaa_post = cls(
            api_key=api_key,
            api_key_name=api_key_name,
            uuid=uuid,
        )

        user_api_key_spec_v4_aaa_post.additional_properties = d
        return user_api_key_spec_v4_aaa_post

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
