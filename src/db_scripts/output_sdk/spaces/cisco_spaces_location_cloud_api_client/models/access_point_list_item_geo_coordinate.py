from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessPointListItemGeoCoordinate")


@_attrs_define
class AccessPointListItemGeoCoordinate:
    """only computed when there are valid GPS markers on the floor

    Attributes:
        latitude (Union[Unset, float]): latitude of the access point Example: 37.420169969548205.
        longitude (Union[Unset, float]): longitude of the access point Example: -121.91959646638128.
        unit (Union[Unset, str]): unit of the coordinates Example: DEGREES.
    """

    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    unit: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latitude = self.latitude

        longitude = self.longitude

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        unit = d.pop("unit", UNSET)

        access_point_list_item_geo_coordinate = cls(
            latitude=latitude,
            longitude=longitude,
            unit=unit,
        )

        access_point_list_item_geo_coordinate.additional_properties = d
        return access_point_list_item_geo_coordinate

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
