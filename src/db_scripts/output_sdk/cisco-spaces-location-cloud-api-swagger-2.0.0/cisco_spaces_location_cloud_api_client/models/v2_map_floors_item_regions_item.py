from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v2_map_floors_item_regions_item_points import V2MapFloorsItemRegionsItemPoints


T = TypeVar("T", bound="V2MapFloorsItemRegionsItem")


@_attrs_define
class V2MapFloorsItemRegionsItem:
    """
    Attributes:
        type_ (Union[Unset, str]): Region type. Example: OUTSIDE.
        points (Union[Unset, V2MapFloorsItemRegionsItemPoints]):
    """

    type_: Union[Unset, str] = UNSET
    points: Union[Unset, "V2MapFloorsItemRegionsItemPoints"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        points: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.points, Unset):
            points = self.points.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if points is not UNSET:
            field_dict["points"] = points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v2_map_floors_item_regions_item_points import V2MapFloorsItemRegionsItemPoints

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _points = d.pop("points", UNSET)
        points: Union[Unset, V2MapFloorsItemRegionsItemPoints]
        if isinstance(_points, Unset):
            points = UNSET
        else:
            points = V2MapFloorsItemRegionsItemPoints.from_dict(_points)

        v2_map_floors_item_regions_item = cls(
            type_=type_,
            points=points,
        )

        v2_map_floors_item_regions_item.additional_properties = d
        return v2_map_floors_item_regions_item

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
