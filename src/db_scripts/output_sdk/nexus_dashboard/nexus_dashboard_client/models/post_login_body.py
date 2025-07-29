from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostLoginBody")


@_attrs_define
class PostLoginBody:
    """
    Attributes:
        domain (str):  Example: local.
        user_name (str): User ID as created by Nexus Dashboard admin or remote identity provider Example: admin.
        user_passwd (str):  Example: password.
    """

    domain: str
    user_name: str
    user_passwd: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        user_name = self.user_name

        user_passwd = self.user_passwd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
                "userName": user_name,
                "userPasswd": user_passwd,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain")

        user_name = d.pop("userName")

        user_passwd = d.pop("userPasswd")

        post_login_body = cls(
            domain=domain,
            user_name=user_name,
            user_passwd=user_passwd,
        )

        post_login_body.additional_properties = d
        return post_login_body

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
