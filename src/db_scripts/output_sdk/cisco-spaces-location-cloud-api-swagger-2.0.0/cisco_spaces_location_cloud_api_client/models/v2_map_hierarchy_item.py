from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v2_map_hierarchy_item_children_item import V2MapHierarchyItemChildrenItem


T = TypeVar("T", bound="V2MapHierarchyItem")


@_attrs_define
class V2MapHierarchyItem:
    """
    Attributes:
        id (Union[Unset, str]): Location hierarchy id for the map element. Map element can be root, organization, group,
            cmx, meraki, campus, building, network, floor. Example: 236b74fe-83c2-403b-acee-9cfa5345f960.
        parent_id (Union[Unset, str]): Parent Id of parent location of current location type. Defaulted to -1 for root
            level as root is on top of hierarchy. Example: -1.
        inferred_time_zone_id (Union[Unset, str]): Time zone id Example: PST8PDT.
        name (Union[Unset, str]): Name for given location level. Example: DNASpacesLAB.
        mongo_location_id (Union[Unset, int]): Mongo location id Example: 167783.
        inferred_location_types (Union[Unset, list[Any]]): Location type in the hierarchy. This can be root,
            organization, group, cmx, meraki, campus, building, network, floor. Example: ["ROOT"].
        total_area (Union[Unset, int]): Total area for location type Example: 0.
        total_area_unit (Union[Unset, str]): Total area unit for location type
        total_capacity (Union[Unset, int]): Total capacity for location type Example: 0.
        geo_location (Union[Unset, str]): Location coordinates of latitude and longitude. Example: 0.0.0.0.
        location_path (Union[Unset, list[Any]]): Location IDs of child location entities Example:
            ["236b74fe-83c2-403b-acee-9cfa5345f960"].
        child_count (Union[Unset, int]): Number of child location entities under current location. Example: 1.
        hierarchy_map_sources (Union[Unset, list[Any]]): Array of hierarchy map sources. Possible values are CMX, PRIME,
            DNAC. Example: ["PRIME"].
        children (Union[Unset, list['V2MapHierarchyItemChildrenItem']]): children location to given parent hierarchy
        last_update_timestamp (Union[Unset, float]): Timestamp of last update made on location hierarchy Example:
            1667424446448.
    """

    id: Union[Unset, str] = UNSET
    parent_id: Union[Unset, str] = UNSET
    inferred_time_zone_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    mongo_location_id: Union[Unset, int] = UNSET
    inferred_location_types: Union[Unset, list[Any]] = UNSET
    total_area: Union[Unset, int] = UNSET
    total_area_unit: Union[Unset, str] = UNSET
    total_capacity: Union[Unset, int] = UNSET
    geo_location: Union[Unset, str] = UNSET
    location_path: Union[Unset, list[Any]] = UNSET
    child_count: Union[Unset, int] = UNSET
    hierarchy_map_sources: Union[Unset, list[Any]] = UNSET
    children: Union[Unset, list["V2MapHierarchyItemChildrenItem"]] = UNSET
    last_update_timestamp: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        parent_id = self.parent_id

        inferred_time_zone_id = self.inferred_time_zone_id

        name = self.name

        mongo_location_id = self.mongo_location_id

        inferred_location_types: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.inferred_location_types, Unset):
            inferred_location_types = self.inferred_location_types

        total_area = self.total_area

        total_area_unit = self.total_area_unit

        total_capacity = self.total_capacity

        geo_location = self.geo_location

        location_path: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.location_path, Unset):
            location_path = self.location_path

        child_count = self.child_count

        hierarchy_map_sources: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.hierarchy_map_sources, Unset):
            hierarchy_map_sources = self.hierarchy_map_sources

        children: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        last_update_timestamp = self.last_update_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if inferred_time_zone_id is not UNSET:
            field_dict["inferredTimeZoneId"] = inferred_time_zone_id
        if name is not UNSET:
            field_dict["name"] = name
        if mongo_location_id is not UNSET:
            field_dict["mongoLocationId"] = mongo_location_id
        if inferred_location_types is not UNSET:
            field_dict["inferredLocationTypes"] = inferred_location_types
        if total_area is not UNSET:
            field_dict["totalArea"] = total_area
        if total_area_unit is not UNSET:
            field_dict["totalAreaUnit"] = total_area_unit
        if total_capacity is not UNSET:
            field_dict["totalCapacity"] = total_capacity
        if geo_location is not UNSET:
            field_dict["geoLocation"] = geo_location
        if location_path is not UNSET:
            field_dict["locationPath"] = location_path
        if child_count is not UNSET:
            field_dict["childCount"] = child_count
        if hierarchy_map_sources is not UNSET:
            field_dict["hierarchyMapSources"] = hierarchy_map_sources
        if children is not UNSET:
            field_dict["children"] = children
        if last_update_timestamp is not UNSET:
            field_dict["lastUpdateTimestamp"] = last_update_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v2_map_hierarchy_item_children_item import V2MapHierarchyItemChildrenItem

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        parent_id = d.pop("parentId", UNSET)

        inferred_time_zone_id = d.pop("inferredTimeZoneId", UNSET)

        name = d.pop("name", UNSET)

        mongo_location_id = d.pop("mongoLocationId", UNSET)

        inferred_location_types = cast(list[Any], d.pop("inferredLocationTypes", UNSET))

        total_area = d.pop("totalArea", UNSET)

        total_area_unit = d.pop("totalAreaUnit", UNSET)

        total_capacity = d.pop("totalCapacity", UNSET)

        geo_location = d.pop("geoLocation", UNSET)

        location_path = cast(list[Any], d.pop("locationPath", UNSET))

        child_count = d.pop("childCount", UNSET)

        hierarchy_map_sources = cast(list[Any], d.pop("hierarchyMapSources", UNSET))

        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in _children or []:
            children_item = V2MapHierarchyItemChildrenItem.from_dict(children_item_data)

            children.append(children_item)

        last_update_timestamp = d.pop("lastUpdateTimestamp", UNSET)

        v2_map_hierarchy_item = cls(
            id=id,
            parent_id=parent_id,
            inferred_time_zone_id=inferred_time_zone_id,
            name=name,
            mongo_location_id=mongo_location_id,
            inferred_location_types=inferred_location_types,
            total_area=total_area,
            total_area_unit=total_area_unit,
            total_capacity=total_capacity,
            geo_location=geo_location,
            location_path=location_path,
            child_count=child_count,
            hierarchy_map_sources=hierarchy_map_sources,
            children=children,
            last_update_timestamp=last_update_timestamp,
        )

        v2_map_hierarchy_item.additional_properties = d
        return v2_map_hierarchy_item

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
