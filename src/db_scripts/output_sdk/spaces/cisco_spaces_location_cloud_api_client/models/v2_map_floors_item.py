from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v2_map_floors_item_access_points_item import V2MapFloorsItemAccessPointsItem
    from ..models.v2_map_floors_item_address import V2MapFloorsItemAddress
    from ..models.v2_map_floors_item_calib_models_item import V2MapFloorsItemCalibModelsItem
    from ..models.v2_map_floors_item_details import V2MapFloorsItemDetails
    from ..models.v2_map_floors_item_gps_markers_item import V2MapFloorsItemGpsMarkersItem
    from ..models.v2_map_floors_item_location_hierarchy_item import V2MapFloorsItemLocationHierarchyItem
    from ..models.v2_map_floors_item_maps_item import V2MapFloorsItemMapsItem
    from ..models.v2_map_floors_item_regions_item import V2MapFloorsItemRegionsItem
    from ..models.v2_map_floors_item_zones_item import V2MapFloorsItemZonesItem


T = TypeVar("T", bound="V2MapFloorsItem")


@_attrs_define
class V2MapFloorsItem:
    """
    Attributes:
        location_hierarchy (Union[Unset, list['V2MapFloorsItemLocationHierarchyItem']]): Location hierarchy for a given
            floor
        access_points (Union[Unset, list['V2MapFloorsItemAccessPointsItem']]):
        calib_models (Union[Unset, list['V2MapFloorsItemCalibModelsItem']]): Calibration models on given floor
        gps_markers (Union[Unset, list['V2MapFloorsItemGpsMarkersItem']]): GPS markers on given floor
        regions (Union[Unset, list['V2MapFloorsItemRegionsItem']]): Region details for given floor
        maps (Union[Unset, list['V2MapFloorsItemMapsItem']]): The map data for given floor
        details (Union[Unset, V2MapFloorsItemDetails]): details like importId, dimensions etc.
        address (Union[Unset, V2MapFloorsItemAddress]): Address of location
        loc_id (Union[Unset, str]): location id for given floor Example: 2a9a7134-47a7-4049-83e2-8d2f4d39bab4.
        zones (Union[Unset, list['V2MapFloorsItemZonesItem']]): zone details like location id and its hierarchy model
        hierarchy_map_sources (Union[Unset, list[Any]]): Array of hierarchy map sources Example: ["CMX","PRIME","DNAC"].
    """

    location_hierarchy: Union[Unset, list["V2MapFloorsItemLocationHierarchyItem"]] = UNSET
    access_points: Union[Unset, list["V2MapFloorsItemAccessPointsItem"]] = UNSET
    calib_models: Union[Unset, list["V2MapFloorsItemCalibModelsItem"]] = UNSET
    gps_markers: Union[Unset, list["V2MapFloorsItemGpsMarkersItem"]] = UNSET
    regions: Union[Unset, list["V2MapFloorsItemRegionsItem"]] = UNSET
    maps: Union[Unset, list["V2MapFloorsItemMapsItem"]] = UNSET
    details: Union[Unset, "V2MapFloorsItemDetails"] = UNSET
    address: Union[Unset, "V2MapFloorsItemAddress"] = UNSET
    loc_id: Union[Unset, str] = UNSET
    zones: Union[Unset, list["V2MapFloorsItemZonesItem"]] = UNSET
    hierarchy_map_sources: Union[Unset, list[Any]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location_hierarchy: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.location_hierarchy, Unset):
            location_hierarchy = []
            for location_hierarchy_item_data in self.location_hierarchy:
                location_hierarchy_item = location_hierarchy_item_data.to_dict()
                location_hierarchy.append(location_hierarchy_item)

        access_points: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.access_points, Unset):
            access_points = []
            for access_points_item_data in self.access_points:
                access_points_item = access_points_item_data.to_dict()
                access_points.append(access_points_item)

        calib_models: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.calib_models, Unset):
            calib_models = []
            for calib_models_item_data in self.calib_models:
                calib_models_item = calib_models_item_data.to_dict()
                calib_models.append(calib_models_item)

        gps_markers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.gps_markers, Unset):
            gps_markers = []
            for gps_markers_item_data in self.gps_markers:
                gps_markers_item = gps_markers_item_data.to_dict()
                gps_markers.append(gps_markers_item)

        regions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.regions, Unset):
            regions = []
            for regions_item_data in self.regions:
                regions_item = regions_item_data.to_dict()
                regions.append(regions_item)

        maps: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.maps, Unset):
            maps = []
            for maps_item_data in self.maps:
                maps_item = maps_item_data.to_dict()
                maps.append(maps_item)

        details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        loc_id = self.loc_id

        zones: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.zones, Unset):
            zones = []
            for zones_item_data in self.zones:
                zones_item = zones_item_data.to_dict()
                zones.append(zones_item)

        hierarchy_map_sources: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.hierarchy_map_sources, Unset):
            hierarchy_map_sources = self.hierarchy_map_sources

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location_hierarchy is not UNSET:
            field_dict["locationHierarchy"] = location_hierarchy
        if access_points is not UNSET:
            field_dict["accessPoints"] = access_points
        if calib_models is not UNSET:
            field_dict["calibModels"] = calib_models
        if gps_markers is not UNSET:
            field_dict["gpsMarkers"] = gps_markers
        if regions is not UNSET:
            field_dict["regions"] = regions
        if maps is not UNSET:
            field_dict["maps"] = maps
        if details is not UNSET:
            field_dict["details"] = details
        if address is not UNSET:
            field_dict["address"] = address
        if loc_id is not UNSET:
            field_dict["locId"] = loc_id
        if zones is not UNSET:
            field_dict["zones"] = zones
        if hierarchy_map_sources is not UNSET:
            field_dict["hierarchyMapSources"] = hierarchy_map_sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v2_map_floors_item_access_points_item import V2MapFloorsItemAccessPointsItem
        from ..models.v2_map_floors_item_address import V2MapFloorsItemAddress
        from ..models.v2_map_floors_item_calib_models_item import V2MapFloorsItemCalibModelsItem
        from ..models.v2_map_floors_item_details import V2MapFloorsItemDetails
        from ..models.v2_map_floors_item_gps_markers_item import V2MapFloorsItemGpsMarkersItem
        from ..models.v2_map_floors_item_location_hierarchy_item import V2MapFloorsItemLocationHierarchyItem
        from ..models.v2_map_floors_item_maps_item import V2MapFloorsItemMapsItem
        from ..models.v2_map_floors_item_regions_item import V2MapFloorsItemRegionsItem
        from ..models.v2_map_floors_item_zones_item import V2MapFloorsItemZonesItem

        d = dict(src_dict)
        location_hierarchy = []
        _location_hierarchy = d.pop("locationHierarchy", UNSET)
        for location_hierarchy_item_data in _location_hierarchy or []:
            location_hierarchy_item = V2MapFloorsItemLocationHierarchyItem.from_dict(location_hierarchy_item_data)

            location_hierarchy.append(location_hierarchy_item)

        access_points = []
        _access_points = d.pop("accessPoints", UNSET)
        for access_points_item_data in _access_points or []:
            access_points_item = V2MapFloorsItemAccessPointsItem.from_dict(access_points_item_data)

            access_points.append(access_points_item)

        calib_models = []
        _calib_models = d.pop("calibModels", UNSET)
        for calib_models_item_data in _calib_models or []:
            calib_models_item = V2MapFloorsItemCalibModelsItem.from_dict(calib_models_item_data)

            calib_models.append(calib_models_item)

        gps_markers = []
        _gps_markers = d.pop("gpsMarkers", UNSET)
        for gps_markers_item_data in _gps_markers or []:
            gps_markers_item = V2MapFloorsItemGpsMarkersItem.from_dict(gps_markers_item_data)

            gps_markers.append(gps_markers_item)

        regions = []
        _regions = d.pop("regions", UNSET)
        for regions_item_data in _regions or []:
            regions_item = V2MapFloorsItemRegionsItem.from_dict(regions_item_data)

            regions.append(regions_item)

        maps = []
        _maps = d.pop("maps", UNSET)
        for maps_item_data in _maps or []:
            maps_item = V2MapFloorsItemMapsItem.from_dict(maps_item_data)

            maps.append(maps_item)

        _details = d.pop("details", UNSET)
        details: Union[Unset, V2MapFloorsItemDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = V2MapFloorsItemDetails.from_dict(_details)

        _address = d.pop("address", UNSET)
        address: Union[Unset, V2MapFloorsItemAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = V2MapFloorsItemAddress.from_dict(_address)

        loc_id = d.pop("locId", UNSET)

        zones = []
        _zones = d.pop("zones", UNSET)
        for zones_item_data in _zones or []:
            zones_item = V2MapFloorsItemZonesItem.from_dict(zones_item_data)

            zones.append(zones_item)

        hierarchy_map_sources = cast(list[Any], d.pop("hierarchyMapSources", UNSET))

        v2_map_floors_item = cls(
            location_hierarchy=location_hierarchy,
            access_points=access_points,
            calib_models=calib_models,
            gps_markers=gps_markers,
            regions=regions,
            maps=maps,
            details=details,
            address=address,
            loc_id=loc_id,
            zones=zones,
            hierarchy_map_sources=hierarchy_map_sources,
        )

        v2_map_floors_item.additional_properties = d
        return v2_map_floors_item

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
