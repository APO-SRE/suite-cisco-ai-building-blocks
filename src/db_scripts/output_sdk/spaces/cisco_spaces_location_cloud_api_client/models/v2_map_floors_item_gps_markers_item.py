from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V2MapFloorsItemGpsMarkersItem")


@_attrs_define
class V2MapFloorsItemGpsMarkersItem:
    """
    Attributes:
        latitude (Union[Unset, float]): Latitude coordinate value. Example: 37.40882873535156.
        x (Union[Unset, float]): x coordinate value. Example: 7.53.
        y (Union[Unset, float]): y coordinate value. Example: 174.83.
        z (Union[Unset, float]): z coordinate value. Example: 0.
        longitude (Union[Unset, float]): Longitude coordinate value. Example: -121.92741394042969.
    """

    latitude: Union[Unset, float] = UNSET
    x: Union[Unset, float] = UNSET
    y: Union[Unset, float] = UNSET
    z: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latitude = self.latitude

        x = self.x

        y = self.y

        z = self.z

        longitude = self.longitude

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if z is not UNSET:
            field_dict["z"] = z
        if longitude is not UNSET:
            field_dict["longitude"] = longitude

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latitude = d.pop("latitude", UNSET)

        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        z = d.pop("z", UNSET)

        longitude = d.pop("longitude", UNSET)

        v2_map_floors_item_gps_markers_item = cls(
            latitude=latitude,
            x=x,
            y=y,
            z=z,
            longitude=longitude,
        )

        v2_map_floors_item_gps_markers_item.additional_properties = d
        return v2_map_floors_item_gps_markers_item

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
