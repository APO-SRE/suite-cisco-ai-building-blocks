from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V2MapFloorItemRegionsItemPoints")


@_attrs_define
class V2MapFloorItemRegionsItemPoints:
    """
    Attributes:
        x (Union[Unset, float]): x coordinate value for region. Example: 316.96.
        y (Union[Unset, float]): y coordinate value for region. Example: 204.03.
        z (Union[Unset, float]): z coordinate value for region.
        order (Union[Unset, float]): order value for region. Example: 3.
    """

    x: Union[Unset, float] = UNSET
    y: Union[Unset, float] = UNSET
    z: Union[Unset, float] = UNSET
    order: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        x = self.x

        y = self.y

        z = self.z

        order = self.order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if z is not UNSET:
            field_dict["z"] = z
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        z = d.pop("z", UNSET)

        order = d.pop("order", UNSET)

        v2_map_floor_item_regions_item_points = cls(
            x=x,
            y=y,
            z=z,
            order=order,
        )

        v2_map_floor_item_regions_item_points.additional_properties = d
        return v2_map_floor_item_regions_item_points

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
