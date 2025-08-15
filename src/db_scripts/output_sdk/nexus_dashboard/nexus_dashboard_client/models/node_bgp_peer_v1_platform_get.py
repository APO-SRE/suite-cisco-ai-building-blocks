from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeBGPPeerV1PlatformGET")


@_attrs_define
class NodeBGPPeerV1PlatformGET:
    """Node bgp peer

    Attributes:
        as_ (Union[Unset, int]): Peer autonomous system (AS) number
        ip (Union[Unset, str]): IPv4 peer address
        ipv6 (Union[Unset, str]): IPv6 peer address
    """

    as_: Union[Unset, int] = UNSET
    ip: Union[Unset, str] = UNSET
    ipv6: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_ = self.as_

        ip = self.ip

        ipv6 = self.ipv6

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if as_ is not UNSET:
            field_dict["as"] = as_
        if ip is not UNSET:
            field_dict["ip"] = ip
        if ipv6 is not UNSET:
            field_dict["ipv6"] = ipv6

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        as_ = d.pop("as", UNSET)

        ip = d.pop("ip", UNSET)

        ipv6 = d.pop("ipv6", UNSET)

        node_bgp_peer_v1_platform_get = cls(
            as_=as_,
            ip=ip,
            ipv6=ipv6,
        )

        node_bgp_peer_v1_platform_get.additional_properties = d
        return node_bgp_peer_v1_platform_get

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
