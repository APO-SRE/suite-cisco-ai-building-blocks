from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventStoreV1EventmonitoringPUT")


@_attrs_define
class EventStoreV1EventmonitoringPUT:
    """Store of event records with currently active lifecycle

    Attributes:
        current_event_occurrences (Union[Unset, list[str]]): List of event records which signify the current alert state
            for the parent event configuration being monitored
        total_event_count (Union[Unset, int]): Number of event records captued during "Active" alert state
    """

    current_event_occurrences: Union[Unset, list[str]] = UNSET
    total_event_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_event_occurrences: Union[Unset, list[str]] = UNSET
        if not isinstance(self.current_event_occurrences, Unset):
            current_event_occurrences = self.current_event_occurrences

        total_event_count = self.total_event_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_event_occurrences is not UNSET:
            field_dict["currentEventOccurrences"] = current_event_occurrences
        if total_event_count is not UNSET:
            field_dict["totalEventCount"] = total_event_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_event_occurrences = cast(list[str], d.pop("currentEventOccurrences", UNSET))

        total_event_count = d.pop("totalEventCount", UNSET)

        event_store_v1_eventmonitoring_put = cls(
            current_event_occurrences=current_event_occurrences,
            total_event_count=total_event_count,
        )

        event_store_v1_eventmonitoring_put.additional_properties = d
        return event_store_v1_eventmonitoring_put

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
