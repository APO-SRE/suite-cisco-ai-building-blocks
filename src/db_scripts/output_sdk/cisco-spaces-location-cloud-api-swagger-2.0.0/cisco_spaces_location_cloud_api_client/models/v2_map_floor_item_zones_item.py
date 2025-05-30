from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v2_map_floor_item_zones_item_details import V2MapFloorItemZonesItemDetails
    from ..models.v2_map_floor_item_zones_item_location_hierarchy_item import (
        V2MapFloorItemZonesItemLocationHierarchyItem,
    )


T = TypeVar("T", bound="V2MapFloorItemZonesItem")


@_attrs_define
class V2MapFloorItemZonesItem:
    """
    Attributes:
        loc_id (Union[Unset, str]): location id for given floor Example: 2a9a7134-47a7-4049-83e2-8d2f4d39bab4.
        location_hierarchy (Union[Unset, list['V2MapFloorItemZonesItemLocationHierarchyItem']]):
        details (Union[Unset, V2MapFloorItemZonesItemDetails]):
    """

    loc_id: Union[Unset, str] = UNSET
    location_hierarchy: Union[Unset, list["V2MapFloorItemZonesItemLocationHierarchyItem"]] = UNSET
    details: Union[Unset, "V2MapFloorItemZonesItemDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        loc_id = self.loc_id

        location_hierarchy: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.location_hierarchy, Unset):
            location_hierarchy = []
            for location_hierarchy_item_data in self.location_hierarchy:
                location_hierarchy_item = location_hierarchy_item_data.to_dict()
                location_hierarchy.append(location_hierarchy_item)

        details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if loc_id is not UNSET:
            field_dict["locId"] = loc_id
        if location_hierarchy is not UNSET:
            field_dict["locationHierarchy"] = location_hierarchy
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v2_map_floor_item_zones_item_details import V2MapFloorItemZonesItemDetails
        from ..models.v2_map_floor_item_zones_item_location_hierarchy_item import (
            V2MapFloorItemZonesItemLocationHierarchyItem,
        )

        d = dict(src_dict)
        loc_id = d.pop("locId", UNSET)

        location_hierarchy = []
        _location_hierarchy = d.pop("locationHierarchy", UNSET)
        for location_hierarchy_item_data in _location_hierarchy or []:
            location_hierarchy_item = V2MapFloorItemZonesItemLocationHierarchyItem.from_dict(
                location_hierarchy_item_data
            )

            location_hierarchy.append(location_hierarchy_item)

        _details = d.pop("details", UNSET)
        details: Union[Unset, V2MapFloorItemZonesItemDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = V2MapFloorItemZonesItemDetails.from_dict(_details)

        v2_map_floor_item_zones_item = cls(
            loc_id=loc_id,
            location_hierarchy=location_hierarchy,
            details=details,
        )

        v2_map_floor_item_zones_item.additional_properties = d
        return v2_map_floor_item_zones_item

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
