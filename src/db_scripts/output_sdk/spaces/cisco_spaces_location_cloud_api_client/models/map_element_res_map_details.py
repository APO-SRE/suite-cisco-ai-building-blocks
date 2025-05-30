from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MapElementResMapDetails")


@_attrs_define
class MapElementResMapDetails:
    """
    Attributes:
        width (Union[Unset, float]): the element width on map. Example: 91.8.
        height (Union[Unset, float]): the element height on map. Example: 10.
        length (Union[Unset, float]): the element length on map. Example: 91.8.
        offset_x (Union[Unset, float]):
        offset_y (Union[Unset, float]):
    """

    width: Union[Unset, float] = UNSET
    height: Union[Unset, float] = UNSET
    length: Union[Unset, float] = UNSET
    offset_x: Union[Unset, float] = UNSET
    offset_y: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        width = self.width

        height = self.height

        length = self.length

        offset_x = self.offset_x

        offset_y = self.offset_y

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if length is not UNSET:
            field_dict["length"] = length
        if offset_x is not UNSET:
            field_dict["offsetX"] = offset_x
        if offset_y is not UNSET:
            field_dict["offsetY"] = offset_y

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        length = d.pop("length", UNSET)

        offset_x = d.pop("offsetX", UNSET)

        offset_y = d.pop("offsetY", UNSET)

        map_element_res_map_details = cls(
            width=width,
            height=height,
            length=length,
            offset_x=offset_x,
            offset_y=offset_y,
        )

        map_element_res_map_details.additional_properties = d
        return map_element_res_map_details

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
