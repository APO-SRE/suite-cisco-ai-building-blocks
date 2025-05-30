from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessPointListItemMapCoordinates")


@_attrs_define
class AccessPointListItemMapCoordinates:
    """
    Attributes:
        x (Union[Unset, float]): X coordinate of the access point Example: 67.95191.
        y (Union[Unset, float]): Y coordinate of the access point Example: 148.05374.
        z (Union[Unset, float]): Z coordinate of the access point Example: 10.
        unit (Union[Unset, str]): unit of the coordinates Example: FEET.
    """

    x: Union[Unset, float] = UNSET
    y: Union[Unset, float] = UNSET
    z: Union[Unset, float] = UNSET
    unit: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        x = self.x

        y = self.y

        z = self.z

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if z is not UNSET:
            field_dict["z"] = z
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        z = d.pop("z", UNSET)

        unit = d.pop("unit", UNSET)

        access_point_list_item_map_coordinates = cls(
            x=x,
            y=y,
            z=z,
            unit=unit,
        )

        access_point_list_item_map_coordinates.additional_properties = d
        return access_point_list_item_map_coordinates

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
