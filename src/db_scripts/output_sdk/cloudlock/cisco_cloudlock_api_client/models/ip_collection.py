from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPCollection")


@_attrs_define
class IPCollection:
    """
    Attributes:
        name (Union[Unset, str]): The library item name. Example: Safe IP.
        description (Union[Unset, str]): The library item description. Example: trusted.
        ip_address (Union[Unset, str]): The IP address in the library. Example: 172.255.255.0.
        location (Union[Unset, str]): The location of the item. Example: Regional Office.
        type_ (Union[Unset, str]): The item type. Example: trusted.
        categories (Union[Unset, str]): The item categories. Example: offices, locations.
        updated_on (Union[Unset, str]): The last update date specified as a timestamp in UTC. Example:
            2016-06-20T13:05:23.034264+00:00.
        created_on (Union[Unset, str]): The creation date specified as a timestamp in UTC. Example:
            2016-06-20T13:05:23.034264+00:00.
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    categories: Union[Unset, str] = UNSET
    updated_on: Union[Unset, str] = UNSET
    created_on: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        ip_address = self.ip_address

        location = self.location

        type_ = self.type_

        categories = self.categories

        updated_on = self.updated_on

        created_on = self.created_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address
        if location is not UNSET:
            field_dict["location"] = location
        if type_ is not UNSET:
            field_dict["type"] = type_
        if categories is not UNSET:
            field_dict["categories"] = categories
        if updated_on is not UNSET:
            field_dict["updated_on"] = updated_on
        if created_on is not UNSET:
            field_dict["created_on"] = created_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        ip_address = d.pop("ip_address", UNSET)

        location = d.pop("location", UNSET)

        type_ = d.pop("type", UNSET)

        categories = d.pop("categories", UNSET)

        updated_on = d.pop("updated_on", UNSET)

        created_on = d.pop("created_on", UNSET)

        ip_collection = cls(
            name=name,
            description=description,
            ip_address=ip_address,
            location=location,
            type_=type_,
            categories=categories,
            updated_on=updated_on,
            created_on=created_on,
        )

        ip_collection.additional_properties = d
        return ip_collection

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
