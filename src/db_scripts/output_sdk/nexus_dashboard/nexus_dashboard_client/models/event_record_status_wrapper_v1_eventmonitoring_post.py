from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_occurrence_v1_eventmonitoring_post import EventOccurrenceV1EventmonitoringPOST
    from ..models.event_record_status_wrapper_v1_eventmonitoring_post_labels import (
        EventRecordStatusWrapperV1EventmonitoringPOSTLabels,
    )
    from ..models.event_record_status_wrapper_v1_eventmonitoring_post_record_labels import (
        EventRecordStatusWrapperV1EventmonitoringPOSTRecordLabels,
    )


T = TypeVar("T", bound="EventRecordStatusWrapperV1EventmonitoringPOST")


@_attrs_define
class EventRecordStatusWrapperV1EventmonitoringPOST:
    """
    Attributes:
        event_occurrence (Union[Unset, EventOccurrenceV1EventmonitoringPOST]): Current status of the event record being
            monitored
        labels (Union[Unset, EventRecordStatusWrapperV1EventmonitoringPOSTLabels]): Set of (key,values) uniquely
            identifying a resource being monitored as part of event configuration
        record_labels (Union[Unset, EventRecordStatusWrapperV1EventmonitoringPOSTRecordLabels]): Query result labels
            that differentiate between multiple entities being tracked under the same parent event configuration
    """

    event_occurrence: Union[Unset, "EventOccurrenceV1EventmonitoringPOST"] = UNSET
    labels: Union[Unset, "EventRecordStatusWrapperV1EventmonitoringPOSTLabels"] = UNSET
    record_labels: Union[Unset, "EventRecordStatusWrapperV1EventmonitoringPOSTRecordLabels"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_occurrence: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_occurrence, Unset):
            event_occurrence = self.event_occurrence.to_dict()

        labels: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        record_labels: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.record_labels, Unset):
            record_labels = self.record_labels.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_occurrence is not UNSET:
            field_dict["eventOccurrence"] = event_occurrence
        if labels is not UNSET:
            field_dict["labels"] = labels
        if record_labels is not UNSET:
            field_dict["recordLabels"] = record_labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_occurrence_v1_eventmonitoring_post import EventOccurrenceV1EventmonitoringPOST
        from ..models.event_record_status_wrapper_v1_eventmonitoring_post_labels import (
            EventRecordStatusWrapperV1EventmonitoringPOSTLabels,
        )
        from ..models.event_record_status_wrapper_v1_eventmonitoring_post_record_labels import (
            EventRecordStatusWrapperV1EventmonitoringPOSTRecordLabels,
        )

        d = dict(src_dict)
        _event_occurrence = d.pop("eventOccurrence", UNSET)
        event_occurrence: Union[Unset, EventOccurrenceV1EventmonitoringPOST]
        if isinstance(_event_occurrence, Unset):
            event_occurrence = UNSET
        else:
            event_occurrence = EventOccurrenceV1EventmonitoringPOST.from_dict(_event_occurrence)

        _labels = d.pop("labels", UNSET)
        labels: Union[Unset, EventRecordStatusWrapperV1EventmonitoringPOSTLabels]
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = EventRecordStatusWrapperV1EventmonitoringPOSTLabels.from_dict(_labels)

        _record_labels = d.pop("recordLabels", UNSET)
        record_labels: Union[Unset, EventRecordStatusWrapperV1EventmonitoringPOSTRecordLabels]
        if isinstance(_record_labels, Unset):
            record_labels = UNSET
        else:
            record_labels = EventRecordStatusWrapperV1EventmonitoringPOSTRecordLabels.from_dict(_record_labels)

        event_record_status_wrapper_v1_eventmonitoring_post = cls(
            event_occurrence=event_occurrence,
            labels=labels,
            record_labels=record_labels,
        )

        event_record_status_wrapper_v1_eventmonitoring_post.additional_properties = d
        return event_record_status_wrapper_v1_eventmonitoring_post

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
