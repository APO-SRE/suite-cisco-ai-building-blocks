from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_route_tag import ModelsRouteTag
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsRouteInfo")


@_attrs_define
class ModelsRouteInfo:
    """RouteInfo defines a specific single IPv4 or IPv6 static route which inludes an IPv4 or IPv6 prefix in CIDR notation
    and a next-hop address of the same IP version.

        Attributes:
            discard (Union[Unset, bool]): The flag that defines if the traffic matching the static route is silently
                discarded or not. This is also referred to as a null route or a black hole route.
            interface (Union[Unset, str]): The next-hop interface or network port name.
            next_hop (Union[Unset, str]): The next-hop IP address. Must be a host IP address.
            next_vrf (Union[Unset, str]): The name of the VRF where the next-hop is present.
            node_id (Union[Unset, str]): The unique identifier of the node where the route is deployed.
            preference (Union[Unset, int]): The route preference value (ascending) which sets the administrative distance.
                The range is from 1 to 255.
            prefix (Union[Unset, str]): The IPv4 or IPv6 prefix in CIDR notation.
            tag (Union[Unset, ModelsRouteTag]): RouteTag defines an enumeration of custom route tags.
    """

    discard: Union[Unset, bool] = UNSET
    interface: Union[Unset, str] = UNSET
    next_hop: Union[Unset, str] = UNSET
    next_vrf: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    preference: Union[Unset, int] = UNSET
    prefix: Union[Unset, str] = UNSET
    tag: Union[Unset, ModelsRouteTag] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discard = self.discard

        interface = self.interface

        next_hop = self.next_hop

        next_vrf = self.next_vrf

        node_id = self.node_id

        preference = self.preference

        prefix = self.prefix

        tag: Union[Unset, str] = UNSET
        if not isinstance(self.tag, Unset):
            tag = self.tag.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if discard is not UNSET:
            field_dict["discard"] = discard
        if interface is not UNSET:
            field_dict["interface"] = interface
        if next_hop is not UNSET:
            field_dict["nextHop"] = next_hop
        if next_vrf is not UNSET:
            field_dict["nextVrf"] = next_vrf
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if preference is not UNSET:
            field_dict["preference"] = preference
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        discard = d.pop("discard", UNSET)

        interface = d.pop("interface", UNSET)

        next_hop = d.pop("nextHop", UNSET)

        next_vrf = d.pop("nextVrf", UNSET)

        node_id = d.pop("nodeId", UNSET)

        preference = d.pop("preference", UNSET)

        prefix = d.pop("prefix", UNSET)

        _tag = d.pop("tag", UNSET)
        tag: Union[Unset, ModelsRouteTag]
        if isinstance(_tag, Unset):
            tag = UNSET
        else:
            tag = ModelsRouteTag(_tag)

        models_route_info = cls(
            discard=discard,
            interface=interface,
            next_hop=next_hop,
            next_vrf=next_vrf,
            node_id=node_id,
            preference=preference,
            prefix=prefix,
            tag=tag,
        )

        models_route_info.additional_properties = d
        return models_route_info

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
