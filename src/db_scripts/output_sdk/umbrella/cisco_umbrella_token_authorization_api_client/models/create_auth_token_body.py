from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_auth_token_body_grant_type import CreateAuthTokenBodyGrantType

T = TypeVar("T", bound="CreateAuthTokenBody")


@_attrs_define
class CreateAuthTokenBody:
    """The authentication information that is required to create an access token.

    Attributes:
        grant_type (CreateAuthTokenBodyGrantType): The type of client grant type. Example: client_credentials.
    """

    grant_type: CreateAuthTokenBodyGrantType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grant_type = self.grant_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grant_type": grant_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grant_type = CreateAuthTokenBodyGrantType(d.pop("grant_type"))

        create_auth_token_body = cls(
            grant_type=grant_type,
        )

        create_auth_token_body.additional_properties = d
        return create_auth_token_body

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
