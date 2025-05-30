from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V2MapFloorItemZonesItemLocationHierarchyItem")


@_attrs_define
class V2MapFloorItemZonesItemLocationHierarchyItem:
    """
    Attributes:
        id (Union[Unset, str]): Unique Location ID. Example: 0c872fbb-0545-45fd-b7e2-6ce6ff6f08af.
        name (Union[Unset, str]): Name for location. Example: Some-campus-name.
        type_ (Union[Unset, str]): Location Type Example: campus.
        mongo_location_id (Union[Unset, float]): Mongo location ID. Example: 6589.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    mongo_location_id: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_

        mongo_location_id = self.mongo_location_id

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        mongo_location_id = d.pop("mongoLocationId", UNSET)

        v2_map_floor_item_zones_item_location_hierarchy_item = cls(
            id=id,
            name=name,
            type_=type_,
            mongo_location_id=mongo_location_id,
        )

        v2_map_floor_item_zones_item_location_hierarchy_item.additional_properties = d
        return v2_map_floor_item_zones_item_location_hierarchy_item

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
