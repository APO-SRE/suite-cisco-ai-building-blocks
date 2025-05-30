from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocationDeviceDetails")


@_attrs_define
class LocationDeviceDetails:
    """
    Attributes:
        mac_address (Union[Unset, str]): Mac address Example: 8c:f5:a3:3c:07:d8.
        coordinates (Union[Unset, list[float]]): The coordinates represents cartesian location (x,y) of device which is
            always relative to a given floor Example: 55.36085, 67.7687.
        floor_id (Union[Unset, str]): The floor unique identifier Example: 3b3aad61352e4bc09cdea0119ee3d9f3.
    """

    mac_address: Union[Unset, str] = UNSET
    coordinates: Union[Unset, list[float]] = UNSET
    floor_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac_address = self.mac_address

        coordinates: Union[Unset, list[float]] = UNSET
        if not isinstance(self.coordinates, Unset):
            coordinates = self.coordinates

        floor_id = self.floor_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if floor_id is not UNSET:
            field_dict["floorId"] = floor_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mac_address = d.pop("macAddress", UNSET)

        coordinates = cast(list[float], d.pop("coordinates", UNSET))

        floor_id = d.pop("floorId", UNSET)

        location_device_details = cls(
            mac_address=mac_address,
            coordinates=coordinates,
            floor_id=floor_id,
        )

        location_device_details.additional_properties = d
        return location_device_details

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
