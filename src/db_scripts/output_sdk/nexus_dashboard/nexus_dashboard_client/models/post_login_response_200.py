from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostLoginResponse200")


@_attrs_define
class PostLoginResponse200:
    """
    Attributes:
        jwttoken (Union[Unset, str]):
        rbac (Union[Unset, str]):
        status_code (Union[Unset, int]):
        token (Union[Unset, str]):
        username (Union[Unset, str]):
        usertype (Union[Unset, str]):
    """

    jwttoken: Union[Unset, str] = UNSET
    rbac: Union[Unset, str] = UNSET
    status_code: Union[Unset, int] = UNSET
    token: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    usertype: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jwttoken = self.jwttoken

        rbac = self.rbac

        status_code = self.status_code

        token = self.token

        username = self.username

        usertype = self.usertype

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if jwttoken is not UNSET:
            field_dict["jwttoken"] = jwttoken
        if rbac is not UNSET:
            field_dict["rbac"] = rbac
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if token is not UNSET:
            field_dict["token"] = token
        if username is not UNSET:
            field_dict["username"] = username
        if usertype is not UNSET:
            field_dict["usertype"] = usertype

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        jwttoken = d.pop("jwttoken", UNSET)

        rbac = d.pop("rbac", UNSET)

        status_code = d.pop("statusCode", UNSET)

        token = d.pop("token", UNSET)

        username = d.pop("username", UNSET)

        usertype = d.pop("usertype", UNSET)

        post_login_response_200 = cls(
            jwttoken=jwttoken,
            rbac=rbac,
            status_code=status_code,
            token=token,
            username=username,
            usertype=usertype,
        )

        post_login_response_200.additional_properties = d
        return post_login_response_200

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
