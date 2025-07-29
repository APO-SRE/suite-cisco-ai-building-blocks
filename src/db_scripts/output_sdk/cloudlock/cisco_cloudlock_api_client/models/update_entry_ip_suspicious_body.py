from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateEntryIpSuspiciousBody")


@_attrs_define
class UpdateEntryIpSuspiciousBody:
    """
    Attributes:
        categories (Union[Unset, str]): Change categories.
        description (Union[Unset, str]): Internal short description.
        expires_on (Union[Unset, str]): Datetime to expire the ip address.
        ip_address (Union[Unset, str]): Change IP address.
    """

    categories: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    expires_on: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categories = self.categories

        description = self.description

        expires_on = self.expires_on

        ip_address = self.ip_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories
        if description is not UNSET:
            field_dict["description"] = description
        if expires_on is not UNSET:
            field_dict["expires_on"] = expires_on
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        categories = d.pop("categories", UNSET)

        description = d.pop("description", UNSET)

        expires_on = d.pop("expires_on", UNSET)

        ip_address = d.pop("ip_address", UNSET)

        update_entry_ip_suspicious_body = cls(
            categories=categories,
            description=description,
            expires_on=expires_on,
            ip_address=ip_address,
        )

        update_entry_ip_suspicious_body.additional_properties = d
        return update_entry_ip_suspicious_body

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
