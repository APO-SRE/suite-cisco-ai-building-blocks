from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_aggregates_agg import IncidentAggregatesAgg


T = TypeVar("T", bound="IncidentAggregates")


@_attrs_define
class IncidentAggregates:
    """
    Attributes:
        agg (Union[Unset, IncidentAggregatesAgg]): The aggregates object.
        id (Union[Unset, str]): The ID of the policy/status/user.
        name (Union[Unset, str]): The name of the policy/status/user.
    """

    agg: Union[Unset, "IncidentAggregatesAgg"] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agg: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.agg, Unset):
            agg = self.agg.to_dict()

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agg is not UNSET:
            field_dict["agg"] = agg
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.incident_aggregates_agg import IncidentAggregatesAgg

        d = dict(src_dict)
        _agg = d.pop("agg", UNSET)
        agg: Union[Unset, IncidentAggregatesAgg]
        if isinstance(_agg, Unset):
            agg = UNSET
        else:
            agg = IncidentAggregatesAgg.from_dict(_agg)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        incident_aggregates = cls(
            agg=agg,
            id=id,
            name=name,
        )

        incident_aggregates.additional_properties = d
        return incident_aggregates

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
