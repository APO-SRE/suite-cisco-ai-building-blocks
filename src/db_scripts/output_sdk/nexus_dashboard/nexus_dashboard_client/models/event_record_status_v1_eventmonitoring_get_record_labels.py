from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EventRecordStatusV1EventmonitoringGETRecordLabels")


@_attrs_define
class EventRecordStatusV1EventmonitoringGETRecordLabels:
    """Query result labels that differentiate between multiple entities being tracked under the same parent event
    configuration

    """

    additional_properties: dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_record_status_v1_eventmonitoring_get_record_labels = cls()

        event_record_status_v1_eventmonitoring_get_record_labels.additional_properties = d
        return event_record_status_v1_eventmonitoring_get_record_labels

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
