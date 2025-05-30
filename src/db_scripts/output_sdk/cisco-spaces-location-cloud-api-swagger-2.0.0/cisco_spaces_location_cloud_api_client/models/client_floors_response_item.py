from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientFloorsResponseItem")


@_attrs_define
class ClientFloorsResponseItem:
    """
    Attributes:
        floor_id (Union[Unset, str]): The floor unique identifier Example: 719d02e2b00e4535b6e095c0d757e44b.
        count (Union[Unset, int]): The total number of associated devices on this floor Example: 11000.
    """

    floor_id: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        floor_id = self.floor_id

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if floor_id is not UNSET:
            field_dict["floorId"] = floor_id
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        floor_id = d.pop("floorId", UNSET)

        count = d.pop("count", UNSET)

        client_floors_response_item = cls(
            floor_id=floor_id,
            count=count,
        )

        client_floors_response_item.additional_properties = d
        return client_floors_response_item

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
