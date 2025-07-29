from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemberSpecV4FederationGET")


@_attrs_define
class MemberSpecV4FederationGET:
    """
    Attributes:
        host (Union[Unset, str]): hostname/IP address used to on-board the member to the Nexus Dashboard federation
        login_domain (Union[Unset, str]): logindomain used to on-board member to the federation
        password (Union[Unset, str]): password used to on-board member to the federation, base64 encoded
        user_name (Union[Unset, str]): user name used to on-board member to the federation
    """

    host: Union[Unset, str] = UNSET
    login_domain: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        login_domain = self.login_domain

        password = self.password

        user_name = self.user_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if login_domain is not UNSET:
            field_dict["loginDomain"] = login_domain
        if password is not UNSET:
            field_dict["password"] = password
        if user_name is not UNSET:
            field_dict["userName"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host = d.pop("host", UNSET)

        login_domain = d.pop("loginDomain", UNSET)

        password = d.pop("password", UNSET)

        user_name = d.pop("userName", UNSET)

        member_spec_v4_federation_get = cls(
            host=host,
            login_domain=login_domain,
            password=password,
            user_name=user_name,
        )

        member_spec_v4_federation_get.additional_properties = d
        return member_spec_v4_federation_get

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
