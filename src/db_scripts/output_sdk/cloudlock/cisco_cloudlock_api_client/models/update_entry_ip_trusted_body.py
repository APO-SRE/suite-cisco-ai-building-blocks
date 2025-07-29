from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateEntryIpTrustedBody")


@_attrs_define
class UpdateEntryIpTrustedBody:
    """
    Attributes:
        categories (Union[Unset, str]): Change categories.
        description (Union[Unset, str]): Internal short description.
        ip_address (Union[Unset, str]): Change IP address.
        name (Union[Unset, str]): Name of entry.
    """

    categories: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categories = self.categories

        description = self.description

        ip_address = self.ip_address

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories
        if description is not UNSET:
            field_dict["description"] = description
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        categories = d.pop("categories", UNSET)

        description = d.pop("description", UNSET)

        ip_address = d.pop("ip_address", UNSET)

        name = d.pop("name", UNSET)

        update_entry_ip_trusted_body = cls(
            categories=categories,
            description=description,
            ip_address=ip_address,
            name=name,
        )

        update_entry_ip_trusted_body.additional_properties = d
        return update_entry_ip_trusted_body

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
