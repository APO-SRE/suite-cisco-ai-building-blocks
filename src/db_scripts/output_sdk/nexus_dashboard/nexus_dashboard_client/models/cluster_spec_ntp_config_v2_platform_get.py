from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cluster_spec_ntp_key_v2_platform_get import ClusterSpecNTPKeyV2PlatformGET
    from ..models.cluster_spec_ntp_server_v2_platform_get import ClusterSpecNTPServerV2PlatformGET


T = TypeVar("T", bound="ClusterSpecNTPConfigV2PlatformGET")


@_attrs_define
class ClusterSpecNTPConfigV2PlatformGET:
    """Cluster NTP config

    Attributes:
        keys (Union[Unset, list['ClusterSpecNTPKeyV2PlatformGET']]): Cluster NTP keys
        servers (Union[Unset, list['ClusterSpecNTPServerV2PlatformGET']]): Cluster NTP servers
    """

    keys: Union[Unset, list["ClusterSpecNTPKeyV2PlatformGET"]] = UNSET
    servers: Union[Unset, list["ClusterSpecNTPServerV2PlatformGET"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keys: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.keys, Unset):
            keys = []
            for keys_item_data in self.keys:
                keys_item = keys_item_data.to_dict()
                keys.append(keys_item)

        servers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for servers_item_data in self.servers:
                servers_item = servers_item_data.to_dict()
                servers.append(servers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keys is not UNSET:
            field_dict["keys"] = keys
        if servers is not UNSET:
            field_dict["servers"] = servers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cluster_spec_ntp_key_v2_platform_get import ClusterSpecNTPKeyV2PlatformGET
        from ..models.cluster_spec_ntp_server_v2_platform_get import ClusterSpecNTPServerV2PlatformGET

        d = dict(src_dict)
        keys = []
        _keys = d.pop("keys", UNSET)
        for keys_item_data in _keys or []:
            keys_item = ClusterSpecNTPKeyV2PlatformGET.from_dict(keys_item_data)

            keys.append(keys_item)

        servers = []
        _servers = d.pop("servers", UNSET)
        for servers_item_data in _servers or []:
            servers_item = ClusterSpecNTPServerV2PlatformGET.from_dict(servers_item_data)

            servers.append(servers_item)

        cluster_spec_ntp_config_v2_platform_get = cls(
            keys=keys,
            servers=servers,
        )

        cluster_spec_ntp_config_v2_platform_get.additional_properties = d
        return cluster_spec_ntp_config_v2_platform_get

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
