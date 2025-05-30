from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaSonicConfig")


@_attrs_define
class SchemaSonicConfig:
    """Description not available

    Attributes:
        hostname (Union[Unset, str]): Description not available
        ipv_4_addr (Union[Unset, str]): Description not available
        ipv_4_gateway (Union[Unset, str]): Description not available
        ipv_6_addr (Union[Unset, str]): Description not available
        ipv_6_gateway (Union[Unset, str]): Description not available
    """

    hostname: Union[Unset, str] = UNSET
    ipv_4_addr: Union[Unset, str] = UNSET
    ipv_4_gateway: Union[Unset, str] = UNSET
    ipv_6_addr: Union[Unset, str] = UNSET
    ipv_6_gateway: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        ipv_4_addr = self.ipv_4_addr

        ipv_4_gateway = self.ipv_4_gateway

        ipv_6_addr = self.ipv_6_addr

        ipv_6_gateway = self.ipv_6_gateway

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if ipv_4_addr is not UNSET:
            field_dict["ipv4Addr"] = ipv_4_addr
        if ipv_4_gateway is not UNSET:
            field_dict["ipv4Gateway"] = ipv_4_gateway
        if ipv_6_addr is not UNSET:
            field_dict["ipv6Addr"] = ipv_6_addr
        if ipv_6_gateway is not UNSET:
            field_dict["ipv6Gateway"] = ipv_6_gateway

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hostname = d.pop("hostname", UNSET)

        ipv_4_addr = d.pop("ipv4Addr", UNSET)

        ipv_4_gateway = d.pop("ipv4Gateway", UNSET)

        ipv_6_addr = d.pop("ipv6Addr", UNSET)

        ipv_6_gateway = d.pop("ipv6Gateway", UNSET)

        schema_sonic_config = cls(
            hostname=hostname,
            ipv_4_addr=ipv_4_addr,
            ipv_4_gateway=ipv_4_gateway,
            ipv_6_addr=ipv_6_addr,
            ipv_6_gateway=ipv_6_gateway,
        )

        schema_sonic_config.additional_properties = d
        return schema_sonic_config

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
