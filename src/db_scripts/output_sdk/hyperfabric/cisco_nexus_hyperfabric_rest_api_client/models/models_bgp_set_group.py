from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_route_origin_type import ModelsRouteOriginType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsBgpSetGroup")


@_attrs_define
class ModelsBgpSetGroup:
    """BgpSetGroup encapsulates "SET" part of a BgpRule. E.g. set tag 5000

    Attributes:
        as_path (Union[Unset, list[int]]): Set as-path for for outbound routes (export).
        community (Union[Unset, str]): Set community tag for import or export. For export, BGP stamps outbound routes
            with this community tag. For route import, BGP sets this tag within the fabric.
        ipv_4_next_hop (Union[Unset, str]): Set next-hop IPv4 address for outbound routes (export).
        ipv_6_next_hop (Union[Unset, str]): Set next-hop IPv6 address for outbound routes (export).
        origin (Union[Unset, ModelsRouteOriginType]): RouteOriginType enumerates different BGP route origins.
        tag (Union[Unset, int]): Set tag of routes for outbound routes (export).
    """

    as_path: Union[Unset, list[int]] = UNSET
    community: Union[Unset, str] = UNSET
    ipv_4_next_hop: Union[Unset, str] = UNSET
    ipv_6_next_hop: Union[Unset, str] = UNSET
    origin: Union[Unset, ModelsRouteOriginType] = UNSET
    tag: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_path: Union[Unset, list[int]] = UNSET
        if not isinstance(self.as_path, Unset):
            as_path = self.as_path

        community = self.community

        ipv_4_next_hop = self.ipv_4_next_hop

        ipv_6_next_hop = self.ipv_6_next_hop

        origin: Union[Unset, str] = UNSET
        if not isinstance(self.origin, Unset):
            origin = self.origin.value

        tag = self.tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if as_path is not UNSET:
            field_dict["asPath"] = as_path
        if community is not UNSET:
            field_dict["community"] = community
        if ipv_4_next_hop is not UNSET:
            field_dict["ipv4NextHop"] = ipv_4_next_hop
        if ipv_6_next_hop is not UNSET:
            field_dict["ipv6NextHop"] = ipv_6_next_hop
        if origin is not UNSET:
            field_dict["origin"] = origin
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        as_path = cast(list[int], d.pop("asPath", UNSET))

        community = d.pop("community", UNSET)

        ipv_4_next_hop = d.pop("ipv4NextHop", UNSET)

        ipv_6_next_hop = d.pop("ipv6NextHop", UNSET)

        _origin = d.pop("origin", UNSET)
        origin: Union[Unset, ModelsRouteOriginType]
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = ModelsRouteOriginType(_origin)

        tag = d.pop("tag", UNSET)

        models_bgp_set_group = cls(
            as_path=as_path,
            community=community,
            ipv_4_next_hop=ipv_4_next_hop,
            ipv_6_next_hop=ipv_6_next_hop,
            origin=origin,
            tag=tag,
        )

        models_bgp_set_group.additional_properties = d
        return models_bgp_set_group

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
