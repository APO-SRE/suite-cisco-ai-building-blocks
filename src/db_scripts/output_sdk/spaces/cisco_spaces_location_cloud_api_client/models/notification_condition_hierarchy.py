from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationConditionHierarchy")


@_attrs_define
class NotificationConditionHierarchy:
    """
    Attributes:
        name (Union[Unset, str]): location hierachy name Example: System Campus -&gt; Building 24 -&gt; 3rd Floor.
        id (Union[Unset, str]): hierachy id Example: 789.
        floor (Union[Unset, list[str]]):
        level (Union[Unset, str]): the floor id Example: FLOOR.
        campus (Union[Unset, str]): campus id Example: 123.
        building (Union[Unset, str]): building id Example: 456.
    """

    name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    floor: Union[Unset, list[str]] = UNSET
    level: Union[Unset, str] = UNSET
    campus: Union[Unset, str] = UNSET
    building: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        floor: Union[Unset, list[str]] = UNSET
        if not isinstance(self.floor, Unset):
            floor = self.floor

        level = self.level

        campus = self.campus

        building = self.building

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if floor is not UNSET:
            field_dict["floor"] = floor
        if level is not UNSET:
            field_dict["level"] = level
        if campus is not UNSET:
            field_dict["campus"] = campus
        if building is not UNSET:
            field_dict["building"] = building

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        floor = cast(list[str], d.pop("floor", UNSET))

        level = d.pop("level", UNSET)

        campus = d.pop("campus", UNSET)

        building = d.pop("building", UNSET)

        notification_condition_hierarchy = cls(
            name=name,
            id=id,
            floor=floor,
            level=level,
            campus=campus,
            building=building,
        )

        notification_condition_hierarchy.additional_properties = d
        return notification_condition_hierarchy

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
