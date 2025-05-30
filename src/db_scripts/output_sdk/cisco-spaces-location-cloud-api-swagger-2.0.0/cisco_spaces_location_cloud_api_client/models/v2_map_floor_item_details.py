from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V2MapFloorItemDetails")


@_attrs_define
class V2MapFloorItemDetails:
    """details like importId, dimensions etc.

    Attributes:
        imported_id (Union[Unset, str]): Imported ID for floor image Example: 7619989423031058460.
        length (Union[Unset, float]): the element length on map. Example: 72.
        width (Union[Unset, float]): the element width on map. Example: 65.37000274658203.
        height (Union[Unset, float]): the element height on map. Example: 10.
        calibration_model_id (Union[Unset, str]): Calibration Model ID. Example: -6550507210156277727.
        floor_number (Union[Unset, str]): Floor level Example: 1.
    """

    imported_id: Union[Unset, str] = UNSET
    length: Union[Unset, float] = UNSET
    width: Union[Unset, float] = UNSET
    height: Union[Unset, float] = UNSET
    calibration_model_id: Union[Unset, str] = UNSET
    floor_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        imported_id = self.imported_id

        length = self.length

        width = self.width

        height = self.height

        calibration_model_id = self.calibration_model_id

        floor_number = self.floor_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if imported_id is not UNSET:
            field_dict["importedId"] = imported_id
        if length is not UNSET:
            field_dict["length"] = length
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if calibration_model_id is not UNSET:
            field_dict["calibrationModelId"] = calibration_model_id
        if floor_number is not UNSET:
            field_dict["floorNumber"] = floor_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        imported_id = d.pop("importedId", UNSET)

        length = d.pop("length", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        calibration_model_id = d.pop("calibrationModelId", UNSET)

        floor_number = d.pop("floorNumber", UNSET)

        v2_map_floor_item_details = cls(
            imported_id=imported_id,
            length=length,
            width=width,
            height=height,
            calibration_model_id=calibration_model_id,
            floor_number=floor_number,
        )

        v2_map_floor_item_details.additional_properties = d
        return v2_map_floor_item_details

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
