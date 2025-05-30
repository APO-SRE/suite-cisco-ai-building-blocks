from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaDnsConfig")


@_attrs_define
class SchemaDnsConfig:
    """Description not available

    Attributes:
        dns_servers (Union[Unset, list[str]]): Description not available
    """

    dns_servers: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dns_servers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.dns_servers, Unset):
            dns_servers = self.dns_servers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dns_servers is not UNSET:
            field_dict["dnsServers"] = dns_servers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dns_servers = cast(list[str], d.pop("dnsServers", UNSET))

        schema_dns_config = cls(
            dns_servers=dns_servers,
        )

        schema_dns_config.additional_properties = d
        return schema_dns_config

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
