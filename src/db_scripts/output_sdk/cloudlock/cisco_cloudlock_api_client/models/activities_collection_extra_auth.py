from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivitiesCollectionExtraAuth")


@_attrs_define
class ActivitiesCollectionExtraAuth:
    """
    Attributes:
        auth_type (Union[Unset, str]): The type of authentication.
        is_suspicious (Union[Unset, bool]): Indicates whether the activity is flagged as being suspicious.
    """

    auth_type: Union[Unset, str] = UNSET
    is_suspicious: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_type = self.auth_type

        is_suspicious = self.is_suspicious

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_type is not UNSET:
            field_dict["auth_type"] = auth_type
        if is_suspicious is not UNSET:
            field_dict["is_suspicious"] = is_suspicious

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth_type = d.pop("auth_type", UNSET)

        is_suspicious = d.pop("is_suspicious", UNSET)

        activities_collection_extra_auth = cls(
            auth_type=auth_type,
            is_suspicious=is_suspicious,
        )

        activities_collection_extra_auth.additional_properties = d
        return activities_collection_extra_auth

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
