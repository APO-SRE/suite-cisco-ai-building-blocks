from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V2MapFloorsItemMapsItem")


@_attrs_define
class V2MapFloorsItemMapsItem:
    """
    Attributes:
        name (Union[Unset, str]): Map name Example: 70db1dd1d1c38e144b293e6ff348159f.
        source (Union[Unset, str]): Map source Example: PRIME.
        zoom_level (Union[Unset, float]): Map's zoom level Example: 3.
        max_dimensions (Union[Unset, float]): Map's maximum dimensions. Example: 782.
        max_resolution (Union[Unset, float]): Map's maximum resolution. Example: 4.
        image_path (Union[Unset, str]): Image path Example: mapservices/floor/ccdc36267d0d3f468dea2afe36ef1dd252baaa14a6
            2ddfdd3d714a9793644484/70db1dd1d1c38e144b293e6ff348159f.
        mime_type (Union[Unset, str]): Image type Example: image/png.
        mongo_id (Union[Unset, str]): Mongo location ID Example: DNASpacesLAB_DNASpacesLab_SJC-19_DNA Spaces Lab.
        image_width (Union[Unset, float]): Image width Example: 712.
        image_height (Union[Unset, float]): Image height Example: 782.
        length (Union[Unset, float]): the element length on map. Example: 72.
        width (Union[Unset, float]): the element width on map. Example: 65.37000274658203.
        height (Union[Unset, float]): the element height on map. Example: 10.
        offset_x (Union[Unset, float]):
        offset_y (Union[Unset, float]):
        unit (Union[Unset, str]): Unit used for measurements. Example: FEET.
        map_coordinates (Union[Unset, list[Any]]): Map's coordinates. Example: ["7.53,174.83,0.0", "7.53,92.77,0.0",
            "8.23,10.9,0.0"].
        gps_markers (Union[Unset, list[Any]]): GPS Markers Example: ["37.40882873535156,-121.92741394042969",
            "37.40882873535156,-121.92713165283203", "37.408599853515625,-121.92691040039062"].
    """

    name: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    zoom_level: Union[Unset, float] = UNSET
    max_dimensions: Union[Unset, float] = UNSET
    max_resolution: Union[Unset, float] = UNSET
    image_path: Union[Unset, str] = UNSET
    mime_type: Union[Unset, str] = UNSET
    mongo_id: Union[Unset, str] = UNSET
    image_width: Union[Unset, float] = UNSET
    image_height: Union[Unset, float] = UNSET
    length: Union[Unset, float] = UNSET
    width: Union[Unset, float] = UNSET
    height: Union[Unset, float] = UNSET
    offset_x: Union[Unset, float] = UNSET
    offset_y: Union[Unset, float] = UNSET
    unit: Union[Unset, str] = UNSET
    map_coordinates: Union[Unset, list[Any]] = UNSET
    gps_markers: Union[Unset, list[Any]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        source = self.source

        zoom_level = self.zoom_level

        max_dimensions = self.max_dimensions

        max_resolution = self.max_resolution

        image_path = self.image_path

        mime_type = self.mime_type

        mongo_id = self.mongo_id

        image_width = self.image_width

        image_height = self.image_height

        length = self.length

        width = self.width

        height = self.height

        offset_x = self.offset_x

        offset_y = self.offset_y

        unit = self.unit

        map_coordinates: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.map_coordinates, Unset):
            map_coordinates = self.map_coordinates

        gps_markers: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.gps_markers, Unset):
            gps_markers = self.gps_markers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if source is not UNSET:
            field_dict["source"] = source
        if zoom_level is not UNSET:
            field_dict["zoomLevel"] = zoom_level
        if max_dimensions is not UNSET:
            field_dict["maxDimensions"] = max_dimensions
        if max_resolution is not UNSET:
            field_dict["maxResolution"] = max_resolution
        if image_path is not UNSET:
            field_dict["imagePath"] = image_path
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if mongo_id is not UNSET:
            field_dict["mongoId"] = mongo_id
        if image_width is not UNSET:
            field_dict["imageWidth"] = image_width
        if image_height is not UNSET:
            field_dict["imageHeight"] = image_height
        if length is not UNSET:
            field_dict["length"] = length
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if offset_x is not UNSET:
            field_dict["offsetX"] = offset_x
        if offset_y is not UNSET:
            field_dict["offsetY"] = offset_y
        if unit is not UNSET:
            field_dict["unit"] = unit
        if map_coordinates is not UNSET:
            field_dict["mapCoordinates"] = map_coordinates
        if gps_markers is not UNSET:
            field_dict["gpsMarkers"] = gps_markers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        source = d.pop("source", UNSET)

        zoom_level = d.pop("zoomLevel", UNSET)

        max_dimensions = d.pop("maxDimensions", UNSET)

        max_resolution = d.pop("maxResolution", UNSET)

        image_path = d.pop("imagePath", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        mongo_id = d.pop("mongoId", UNSET)

        image_width = d.pop("imageWidth", UNSET)

        image_height = d.pop("imageHeight", UNSET)

        length = d.pop("length", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        offset_x = d.pop("offsetX", UNSET)

        offset_y = d.pop("offsetY", UNSET)

        unit = d.pop("unit", UNSET)

        map_coordinates = cast(list[Any], d.pop("mapCoordinates", UNSET))

        gps_markers = cast(list[Any], d.pop("gpsMarkers", UNSET))

        v2_map_floors_item_maps_item = cls(
            name=name,
            source=source,
            zoom_level=zoom_level,
            max_dimensions=max_dimensions,
            max_resolution=max_resolution,
            image_path=image_path,
            mime_type=mime_type,
            mongo_id=mongo_id,
            image_width=image_width,
            image_height=image_height,
            length=length,
            width=width,
            height=height,
            offset_x=offset_x,
            offset_y=offset_y,
            unit=unit,
            map_coordinates=map_coordinates,
            gps_markers=gps_markers,
        )

        v2_map_floors_item_maps_item.additional_properties = d
        return v2_map_floors_item_maps_item

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
