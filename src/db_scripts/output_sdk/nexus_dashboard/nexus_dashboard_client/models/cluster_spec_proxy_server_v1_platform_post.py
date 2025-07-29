from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cluster_spec_proxy_server_v1_platform_post_type import ClusterSpecProxyServerV1PlatformPOSTType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterSpecProxyServerV1PlatformPOST")


@_attrs_define
class ClusterSpecProxyServerV1PlatformPOST:
    """Cluster proxy server config

    Attributes:
        password (Union[Unset, str]): Proxy password
        type_ (Union[Unset, ClusterSpecProxyServerV1PlatformPOSTType]): Proxy type
        url (Union[Unset, str]): Proxy url
        username (Union[Unset, str]): Proxy username
    """

    password: Union[Unset, str] = UNSET
    type_: Union[Unset, ClusterSpecProxyServerV1PlatformPOSTType] = UNSET
    url: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        password = self.password

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        url = self.url

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if password is not UNSET:
            field_dict["password"] = password
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        password = d.pop("password", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ClusterSpecProxyServerV1PlatformPOSTType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ClusterSpecProxyServerV1PlatformPOSTType(_type_)

        url = d.pop("url", UNSET)

        username = d.pop("username", UNSET)

        cluster_spec_proxy_server_v1_platform_post = cls(
            password=password,
            type_=type_,
            url=url,
            username=username,
        )

        cluster_spec_proxy_server_v1_platform_post.additional_properties = d
        return cluster_spec_proxy_server_v1_platform_post

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
