from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v2_map_hierarchy_item_children_item_children_children_children import (
        V2MapHierarchyItemChildrenItemChildrenChildrenChildren,
    )
    from ..models.v2_map_hierarchy_item_children_item_children_children_maps_item import (
        V2MapHierarchyItemChildrenItemChildrenChildrenMapsItem,
    )


T = TypeVar("T", bound="V2MapHierarchyItemChildrenItemChildrenChildren")


@_attrs_define
class V2MapHierarchyItemChildrenItemChildrenChildren:
    """children location to given parent hierarchy

    Attributes:
        id (Union[Unset, str]): Location hierarchy id for the map element. Map element can be root, organization, group,
            cmx, meraki, campus, building, network, floor. Example: 351dd14a-8c75-4ffe-98d8-8279b4db575e.
        parent_id (Union[Unset, str]): Parent Id of parent location of current location type. Defaulted to -1 for root
            level as root is on top of hierarchy. Example: 8d2424bf-6877-405c-aa51-16b4ab280d40.
        inferred_time_zone_id (Union[Unset, str]): Time zone id Example: America/Los_Angeles.
        name (Union[Unset, str]): Name for given location level. Example: Spaces Lab.
        mongo_location_id (Union[Unset, int]): Mongo location id Example: 1220636.
        inferred_location_types (Union[Unset, list[Any]]): Location type in the hierarchy. This can be root,
            organization, group, cmx, meraki, campus, building, network, floor. Example: ["FLOOR"].
        network_id (Union[Unset, str]): Legacy network ID for location. Example: 284914a4-f3a9-4fca-92a3-0c9b9b24739a.
        city (Union[Unset, str]): Location entity's city in address Example: San Jose.
        state (Union[Unset, str]): Location entity's state in address Example: California.
        country (Union[Unset, str]): Location entity's country in address Example: USA.
        address (Union[Unset, str]): Address of given location. Example: 3600 Cisco Way.
        zipcode (Union[Unset, str]): Location entity's zipcode in address Example: 95134.
        total_area (Union[Unset, int]): Total area for location type Example: 24000.
        total_area_unit (Union[Unset, str]): Total area unit for location type Example: SQUARE_FEET.
        total_capacity (Union[Unset, int]): Total capacity for location type Example: 100.
        brand_name (Union[Unset, str]): Brand name of location entity. Example: Cisco Spaces.
        geo_location (Union[Unset, str]): Location coordinates of latitude and longitude Example: 37.406097,-121.92466.
        maps (Union[Unset, list['V2MapHierarchyItemChildrenItemChildrenChildrenMapsItem']]): Map details for given
            location entity
        ap_count (Union[Unset, float]): Number of AccessPoints Example: 8.
        location_path (Union[Unset, list[Any]]): Location IDs of child location entities Example:
            ["236b74fe-83c2-403b-acee-9cfa5345f960", "8ebbcf5e-bad2-46c4-abbe-159dd0607b9d",
            "8d2424bf-6877-405c-aa51-16b4ab280d40","351dd14a-8c75-4ffe-98d8-8279b4db575e"].
        child_count (Union[Unset, int]): Number of child location entities under current location. Example: 1.
        hierarchy_map_sources (Union[Unset, list[Any]]): Array of hierarchy map sources. Possible values are CMX, PRIME,
            DNAC. Example: ["PRIME"].
        children (Union[Unset, V2MapHierarchyItemChildrenItemChildrenChildrenChildren]): children location to given
            parent hierarchy
    """

    id: Union[Unset, str] = UNSET
    parent_id: Union[Unset, str] = UNSET
    inferred_time_zone_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    mongo_location_id: Union[Unset, int] = UNSET
    inferred_location_types: Union[Unset, list[Any]] = UNSET
    network_id: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    zipcode: Union[Unset, str] = UNSET
    total_area: Union[Unset, int] = UNSET
    total_area_unit: Union[Unset, str] = UNSET
    total_capacity: Union[Unset, int] = UNSET
    brand_name: Union[Unset, str] = UNSET
    geo_location: Union[Unset, str] = UNSET
    maps: Union[Unset, list["V2MapHierarchyItemChildrenItemChildrenChildrenMapsItem"]] = UNSET
    ap_count: Union[Unset, float] = UNSET
    location_path: Union[Unset, list[Any]] = UNSET
    child_count: Union[Unset, int] = UNSET
    hierarchy_map_sources: Union[Unset, list[Any]] = UNSET
    children: Union[Unset, "V2MapHierarchyItemChildrenItemChildrenChildrenChildren"] = UNSET
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

        network_id = self.network_id

        city = self.city

        state = self.state

        country = self.country

        address = self.address

        zipcode = self.zipcode

        total_area = self.total_area

        total_area_unit = self.total_area_unit

        total_capacity = self.total_capacity

        brand_name = self.brand_name

        geo_location = self.geo_location

        maps: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.maps, Unset):
            maps = []
            for maps_item_data in self.maps:
                maps_item = maps_item_data.to_dict()
                maps.append(maps_item)

        ap_count = self.ap_count

        location_path: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.location_path, Unset):
            location_path = self.location_path

        child_count = self.child_count

        hierarchy_map_sources: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.hierarchy_map_sources, Unset):
            hierarchy_map_sources = self.hierarchy_map_sources

        children: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.children, Unset):
            children = self.children.to_dict()

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
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if country is not UNSET:
            field_dict["country"] = country
        if address is not UNSET:
            field_dict["address"] = address
        if zipcode is not UNSET:
            field_dict["zipcode"] = zipcode
        if total_area is not UNSET:
            field_dict["totalArea"] = total_area
        if total_area_unit is not UNSET:
            field_dict["totalAreaUnit"] = total_area_unit
        if total_capacity is not UNSET:
            field_dict["totalCapacity"] = total_capacity
        if brand_name is not UNSET:
            field_dict["brandName"] = brand_name
        if geo_location is not UNSET:
            field_dict["geoLocation"] = geo_location
        if maps is not UNSET:
            field_dict["maps"] = maps
        if ap_count is not UNSET:
            field_dict["apCount"] = ap_count
        if location_path is not UNSET:
            field_dict["locationPath"] = location_path
        if child_count is not UNSET:
            field_dict["childCount"] = child_count
        if hierarchy_map_sources is not UNSET:
            field_dict["hierarchyMapSources"] = hierarchy_map_sources
        if children is not UNSET:
            field_dict["children"] = children

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v2_map_hierarchy_item_children_item_children_children_children import (
            V2MapHierarchyItemChildrenItemChildrenChildrenChildren,
        )
        from ..models.v2_map_hierarchy_item_children_item_children_children_maps_item import (
            V2MapHierarchyItemChildrenItemChildrenChildrenMapsItem,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        parent_id = d.pop("parentId", UNSET)

        inferred_time_zone_id = d.pop("inferredTimeZoneId", UNSET)

        name = d.pop("name", UNSET)

        mongo_location_id = d.pop("mongoLocationId", UNSET)

        inferred_location_types = cast(list[Any], d.pop("inferredLocationTypes", UNSET))

        network_id = d.pop("networkId", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        country = d.pop("country", UNSET)

        address = d.pop("address", UNSET)

        zipcode = d.pop("zipcode", UNSET)

        total_area = d.pop("totalArea", UNSET)

        total_area_unit = d.pop("totalAreaUnit", UNSET)

        total_capacity = d.pop("totalCapacity", UNSET)

        brand_name = d.pop("brandName", UNSET)

        geo_location = d.pop("geoLocation", UNSET)

        maps = []
        _maps = d.pop("maps", UNSET)
        for maps_item_data in _maps or []:
            maps_item = V2MapHierarchyItemChildrenItemChildrenChildrenMapsItem.from_dict(maps_item_data)

            maps.append(maps_item)

        ap_count = d.pop("apCount", UNSET)

        location_path = cast(list[Any], d.pop("locationPath", UNSET))

        child_count = d.pop("childCount", UNSET)

        hierarchy_map_sources = cast(list[Any], d.pop("hierarchyMapSources", UNSET))

        _children = d.pop("children", UNSET)
        children: Union[Unset, V2MapHierarchyItemChildrenItemChildrenChildrenChildren]
        if isinstance(_children, Unset):
            children = UNSET
        else:
            children = V2MapHierarchyItemChildrenItemChildrenChildrenChildren.from_dict(_children)

        v2_map_hierarchy_item_children_item_children_children = cls(
            id=id,
            parent_id=parent_id,
            inferred_time_zone_id=inferred_time_zone_id,
            name=name,
            mongo_location_id=mongo_location_id,
            inferred_location_types=inferred_location_types,
            network_id=network_id,
            city=city,
            state=state,
            country=country,
            address=address,
            zipcode=zipcode,
            total_area=total_area,
            total_area_unit=total_area_unit,
            total_capacity=total_capacity,
            brand_name=brand_name,
            geo_location=geo_location,
            maps=maps,
            ap_count=ap_count,
            location_path=location_path,
            child_count=child_count,
            hierarchy_map_sources=hierarchy_map_sources,
            children=children,
        )

        v2_map_hierarchy_item_children_item_children_children.additional_properties = d
        return v2_map_hierarchy_item_children_item_children_children

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
