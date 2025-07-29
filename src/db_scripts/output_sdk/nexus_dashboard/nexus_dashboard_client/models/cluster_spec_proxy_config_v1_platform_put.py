from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cluster_spec_proxy_server_v1_platform_put import ClusterSpecProxyServerV1PlatformPUT


T = TypeVar("T", bound="ClusterSpecProxyConfigV1PlatformPUT")


@_attrs_define
class ClusterSpecProxyConfigV1PlatformPUT:
    """Cluster proxy server & ignorehosts config

    Attributes:
        ignore_hosts (Union[Unset, list[str]]): Proxy ignore host list
        password (Union[Unset, str]): Cluster proxy password
        servers (Union[Unset, list['ClusterSpecProxyServerV1PlatformPUT']]): Proxy server list
        username (Union[Unset, str]): Cluster proxy username
    """

    ignore_hosts: Union[Unset, list[str]] = UNSET
    password: Union[Unset, str] = UNSET
    servers: Union[Unset, list["ClusterSpecProxyServerV1PlatformPUT"]] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ignore_hosts: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ignore_hosts, Unset):
            ignore_hosts = self.ignore_hosts

        password = self.password

        servers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for servers_item_data in self.servers:
                servers_item = servers_item_data.to_dict()
                servers.append(servers_item)

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ignore_hosts is not UNSET:
            field_dict["ignoreHosts"] = ignore_hosts
        if password is not UNSET:
            field_dict["password"] = password
        if servers is not UNSET:
            field_dict["servers"] = servers
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cluster_spec_proxy_server_v1_platform_put import ClusterSpecProxyServerV1PlatformPUT

        d = dict(src_dict)
        ignore_hosts = cast(list[str], d.pop("ignoreHosts", UNSET))

        password = d.pop("password", UNSET)

        servers = []
        _servers = d.pop("servers", UNSET)
        for servers_item_data in _servers or []:
            servers_item = ClusterSpecProxyServerV1PlatformPUT.from_dict(servers_item_data)

            servers.append(servers_item)

        username = d.pop("username", UNSET)

        cluster_spec_proxy_config_v1_platform_put = cls(
            ignore_hosts=ignore_hosts,
            password=password,
            servers=servers,
            username=username,
        )

        cluster_spec_proxy_config_v1_platform_put.additional_properties = d
        return cluster_spec_proxy_config_v1_platform_put

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
