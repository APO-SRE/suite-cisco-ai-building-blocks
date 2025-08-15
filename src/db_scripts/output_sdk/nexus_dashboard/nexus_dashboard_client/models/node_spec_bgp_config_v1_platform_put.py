from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_bgp_peer_v1_platform_put import NodeBGPPeerV1PlatformPUT


T = TypeVar("T", bound="NodeSpecBgpConfigV1PlatformPUT")


@_attrs_define
class NodeSpecBgpConfigV1PlatformPUT:
    """Node BGP config

    Attributes:
        as_ (Union[Unset, int]): Node autonomous system (AS) number
        peers (Union[Unset, list['NodeBGPPeerV1PlatformPUT']]): BGP peer list
        router_id (Union[Unset, str]): Unique Router ID
    """

    as_: Union[Unset, int] = UNSET
    peers: Union[Unset, list["NodeBGPPeerV1PlatformPUT"]] = UNSET
    router_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_ = self.as_

        peers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.peers, Unset):
            peers = []
            for peers_item_data in self.peers:
                peers_item = peers_item_data.to_dict()
                peers.append(peers_item)

        router_id = self.router_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if as_ is not UNSET:
            field_dict["as"] = as_
        if peers is not UNSET:
            field_dict["peers"] = peers
        if router_id is not UNSET:
            field_dict["routerID"] = router_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node_bgp_peer_v1_platform_put import NodeBGPPeerV1PlatformPUT

        d = dict(src_dict)
        as_ = d.pop("as", UNSET)

        peers = []
        _peers = d.pop("peers", UNSET)
        for peers_item_data in _peers or []:
            peers_item = NodeBGPPeerV1PlatformPUT.from_dict(peers_item_data)

            peers.append(peers_item)

        router_id = d.pop("routerID", UNSET)

        node_spec_bgp_config_v1_platform_put = cls(
            as_=as_,
            peers=peers,
            router_id=router_id,
        )

        node_spec_bgp_config_v1_platform_put.additional_properties = d
        return node_spec_bgp_config_v1_platform_put

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
