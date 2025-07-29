from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalIpSpecWrapperV1PlatformPOST")


@_attrs_define
class ExternalIpSpecWrapperV1PlatformPOST:
    """
    Attributes:
        name (str): External service name
        ip (Union[Unset, list[str]]): External IP list
        target_network (Union[Unset, str]): External IP target network
    """

    name: str
    ip: Union[Unset, list[str]] = UNSET
    target_network: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        ip: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ip, Unset):
            ip = self.ip

        target_network = self.target_network

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if ip is not UNSET:
            field_dict["ip"] = ip
        if target_network is not UNSET:
            field_dict["targetNetwork"] = target_network

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        ip = cast(list[str], d.pop("ip", UNSET))

        target_network = d.pop("targetNetwork", UNSET)

        external_ip_spec_wrapper_v1_platform_post = cls(
            name=name,
            ip=ip,
            target_network=target_network,
        )

        external_ip_spec_wrapper_v1_platform_post.additional_properties = d
        return external_ip_spec_wrapper_v1_platform_post

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
