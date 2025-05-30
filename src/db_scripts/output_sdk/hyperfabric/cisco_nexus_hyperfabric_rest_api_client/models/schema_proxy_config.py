from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaProxyConfig")


@_attrs_define
class SchemaProxyConfig:
    """Description not available

    Attributes:
        http_proxy (Union[Unset, str]): Description not available
        https_proxy (Union[Unset, str]): Description not available
        no_proxy (Union[Unset, str]): Description not available
        pass_ (Union[Unset, str]): Description not available
        user (Union[Unset, str]): Description not available
    """

    http_proxy: Union[Unset, str] = UNSET
    https_proxy: Union[Unset, str] = UNSET
    no_proxy: Union[Unset, str] = UNSET
    pass_: Union[Unset, str] = UNSET
    user: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        http_proxy = self.http_proxy

        https_proxy = self.https_proxy

        no_proxy = self.no_proxy

        pass_ = self.pass_

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if http_proxy is not UNSET:
            field_dict["httpProxy"] = http_proxy
        if https_proxy is not UNSET:
            field_dict["httpsProxy"] = https_proxy
        if no_proxy is not UNSET:
            field_dict["noProxy"] = no_proxy
        if pass_ is not UNSET:
            field_dict["pass"] = pass_
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        http_proxy = d.pop("httpProxy", UNSET)

        https_proxy = d.pop("httpsProxy", UNSET)

        no_proxy = d.pop("noProxy", UNSET)

        pass_ = d.pop("pass", UNSET)

        user = d.pop("user", UNSET)

        schema_proxy_config = cls(
            http_proxy=http_proxy,
            https_proxy=https_proxy,
            no_proxy=no_proxy,
            pass_=pass_,
            user=user,
        )

        schema_proxy_config.additional_properties = d
        return schema_proxy_config

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
