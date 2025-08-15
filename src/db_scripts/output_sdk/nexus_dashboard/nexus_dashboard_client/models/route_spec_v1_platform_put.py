from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.route_spec_v1_platform_put_target_network import RouteSpecV1PlatformPUTTargetNetwork
from ..types import UNSET, Unset

T = TypeVar("T", bound="RouteSpecV1PlatformPUT")


@_attrs_define
class RouteSpecV1PlatformPUT:
    """Route configuration

    Attributes:
        destination (Union[Unset, str]): Route Destination address/mask
        target_network (Union[Unset, RouteSpecV1PlatformPUTTargetNetwork]): Route Target Network
    """

    destination: Union[Unset, str] = UNSET
    target_network: Union[Unset, RouteSpecV1PlatformPUTTargetNetwork] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination = self.destination

        target_network: Union[Unset, str] = UNSET
        if not isinstance(self.target_network, Unset):
            target_network = self.target_network.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination is not UNSET:
            field_dict["destination"] = destination
        if target_network is not UNSET:
            field_dict["targetNetwork"] = target_network

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        destination = d.pop("destination", UNSET)

        _target_network = d.pop("targetNetwork", UNSET)
        target_network: Union[Unset, RouteSpecV1PlatformPUTTargetNetwork]
        if isinstance(_target_network, Unset):
            target_network = UNSET
        else:
            target_network = RouteSpecV1PlatformPUTTargetNetwork(_target_network)

        route_spec_v1_platform_put = cls(
            destination=destination,
            target_network=target_network,
        )

        route_spec_v1_platform_put.additional_properties = d
        return route_spec_v1_platform_put

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
