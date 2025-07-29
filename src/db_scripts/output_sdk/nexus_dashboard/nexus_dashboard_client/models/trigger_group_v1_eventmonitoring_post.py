from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TriggerGroupV1EventmonitoringPOST")


@_attrs_define
class TriggerGroupV1EventmonitoringPOST:
    """List of triggers that govern the stream types where the alert can be broadcasted

    Attributes:
        considered_duration (Union[Unset, str]): Duration for which the alert remains Active
        considered_severities (Union[Unset, list[str]]): Types of severities that are eligible for the trigger
        streams (Union[Unset, list[str]]): Types of streams to broadcast the alert
        threshold_occurrence (Union[Unset, int]): Number of events occurred to initiate the trigger
        trigger (Union[Unset, str]): Type of trigger
    """

    considered_duration: Union[Unset, str] = UNSET
    considered_severities: Union[Unset, list[str]] = UNSET
    streams: Union[Unset, list[str]] = UNSET
    threshold_occurrence: Union[Unset, int] = UNSET
    trigger: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        considered_duration = self.considered_duration

        considered_severities: Union[Unset, list[str]] = UNSET
        if not isinstance(self.considered_severities, Unset):
            considered_severities = self.considered_severities

        streams: Union[Unset, list[str]] = UNSET
        if not isinstance(self.streams, Unset):
            streams = self.streams

        threshold_occurrence = self.threshold_occurrence

        trigger = self.trigger

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if considered_duration is not UNSET:
            field_dict["consideredDuration"] = considered_duration
        if considered_severities is not UNSET:
            field_dict["consideredSeverities"] = considered_severities
        if streams is not UNSET:
            field_dict["streams"] = streams
        if threshold_occurrence is not UNSET:
            field_dict["thresholdOccurrence"] = threshold_occurrence
        if trigger is not UNSET:
            field_dict["trigger"] = trigger

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        considered_duration = d.pop("consideredDuration", UNSET)

        considered_severities = cast(list[str], d.pop("consideredSeverities", UNSET))

        streams = cast(list[str], d.pop("streams", UNSET))

        threshold_occurrence = d.pop("thresholdOccurrence", UNSET)

        trigger = d.pop("trigger", UNSET)

        trigger_group_v1_eventmonitoring_post = cls(
            considered_duration=considered_duration,
            considered_severities=considered_severities,
            streams=streams,
            threshold_occurrence=threshold_occurrence,
            trigger=trigger,
        )

        trigger_group_v1_eventmonitoring_post.additional_properties = d
        return trigger_group_v1_eventmonitoring_post

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
