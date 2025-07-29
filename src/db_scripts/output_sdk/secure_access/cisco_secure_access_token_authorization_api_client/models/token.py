from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Token")


@_attrs_define
class Token:
    """
    Example:
        {'token_type': 'bearer', 'access_token': 'bearer access token', 'expires_in': 3600}

    Attributes:
        token_type (str): The type of token. Example: bearer.
        access_token (str): The access token. Example: xxxxxxx.
        expires_in (int): The number of seconds in which the token expires. Example: 3600.
    """

    token_type: str
    access_token: str
    expires_in: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token_type = self.token_type

        access_token = self.access_token

        expires_in = self.expires_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token_type": token_type,
                "access_token": access_token,
                "expires_in": expires_in,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token_type = d.pop("token_type")

        access_token = d.pop("access_token")

        expires_in = d.pop("expires_in")

        token = cls(
            token_type=token_type,
            access_token=access_token,
            expires_in=expires_in,
        )

        token.additional_properties = d
        return token

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
