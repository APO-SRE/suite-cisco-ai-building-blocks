from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MacAndDetails")


@_attrs_define
class MacAndDetails:
    """
    Attributes:
        floor_id (Union[Unset, str]): The floor unique id Example: 0561791ba1804dd9af957e4291d5a204.
        source_timestamp (Union[Unset, str]): The UTC timestamp of the client source. Example: 1526667280060.
        coordinates (Union[Unset, list[float]]):
        associated (Union[Unset, bool]): The client is associated to AP or not. True means yes, false otherwise.
            Example: True.
    """

    floor_id: Union[Unset, str] = UNSET
    source_timestamp: Union[Unset, str] = UNSET
    coordinates: Union[Unset, list[float]] = UNSET
    associated: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        floor_id = self.floor_id

        source_timestamp = self.source_timestamp

        coordinates: Union[Unset, list[float]] = UNSET
        if not isinstance(self.coordinates, Unset):
            coordinates = self.coordinates

        associated = self.associated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if floor_id is not UNSET:
            field_dict["floorId"] = floor_id
        if source_timestamp is not UNSET:
            field_dict["sourceTimestamp"] = source_timestamp
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if associated is not UNSET:
            field_dict["associated"] = associated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        floor_id = d.pop("floorId", UNSET)

        source_timestamp = d.pop("sourceTimestamp", UNSET)

        coordinates = cast(list[float], d.pop("coordinates", UNSET))

        associated = d.pop("associated", UNSET)

        mac_and_details = cls(
            floor_id=floor_id,
            source_timestamp=source_timestamp,
            coordinates=coordinates,
            associated=associated,
        )

        mac_and_details.additional_properties = d
        return mac_and_details

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
