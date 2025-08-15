from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterSpecNetworkV2PlatformPOST")


@_attrs_define
class ClusterSpecNetworkV2PlatformPOST:
    """Cluster network subnet configuration

    Attributes:
        subnet (Union[Unset, str]): IPv4 network address and mask
        subnetv6 (Union[Unset, str]): IPv6 network address and mask
    """

    subnet: Union[Unset, str] = UNSET
    subnetv6: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subnet = self.subnet

        subnetv6 = self.subnetv6

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subnet is not UNSET:
            field_dict["subnet"] = subnet
        if subnetv6 is not UNSET:
            field_dict["subnetv6"] = subnetv6

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subnet = d.pop("subnet", UNSET)

        subnetv6 = d.pop("subnetv6", UNSET)

        cluster_spec_network_v2_platform_post = cls(
            subnet=subnet,
            subnetv6=subnetv6,
        )

        cluster_spec_network_v2_platform_post.additional_properties = d
        return cluster_spec_network_v2_platform_post

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
