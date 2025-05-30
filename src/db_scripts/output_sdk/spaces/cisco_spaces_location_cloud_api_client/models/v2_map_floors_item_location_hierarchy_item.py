from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V2MapFloorsItemLocationHierarchyItem")


@_attrs_define
class V2MapFloorsItemLocationHierarchyItem:
    """
    Attributes:
        id (Union[Unset, str]): Unique location ID for a Map element. Example: 0c872fbb-0545-45fd-b7e2-6ce6ff6f08af.
        name (Union[Unset, str]): Name of Map element. Example: Campus-Name.
        type_ (Union[Unset, str]): Type of location element. Example: CAMPUS.
        mongo_location_id (Union[Unset, float]): Mongo location ID Example: 622031.
        network_id (Union[Unset, str]): Legacy network ID Example: 4a23245d-0053-42c7-b0d3-940d92eca16d.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    mongo_location_id: Union[Unset, float] = UNSET
    network_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_

        mongo_location_id = self.mongo_location_id

        network_id = self.network_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if mongo_location_id is not UNSET:
            field_dict["mongoLocationId"] = mongo_location_id
        if network_id is not UNSET:
            field_dict["networkId"] = network_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        mongo_location_id = d.pop("mongoLocationId", UNSET)

        network_id = d.pop("networkId", UNSET)

        v2_map_floors_item_location_hierarchy_item = cls(
            id=id,
            name=name,
            type_=type_,
            mongo_location_id=mongo_location_id,
            network_id=network_id,
        )

        v2_map_floors_item_location_hierarchy_item.additional_properties = d
        return v2_map_floors_item_location_hierarchy_item

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
