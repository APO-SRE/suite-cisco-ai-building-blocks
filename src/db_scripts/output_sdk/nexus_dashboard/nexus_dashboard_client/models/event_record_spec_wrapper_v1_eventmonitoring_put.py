from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_record_spec_wrapper_v1_eventmonitoring_put_alert_state import (
    EventRecordSpecWrapperV1EventmonitoringPUTAlertState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventRecordSpecWrapperV1EventmonitoringPUT")


@_attrs_define
class EventRecordSpecWrapperV1EventmonitoringPUT:
    """
    Attributes:
        acked (Union[Unset, bool]): Tracks customer acknowledgment of the raised alert
        alert_state (Union[Unset, EventRecordSpecWrapperV1EventmonitoringPUTAlertState]): Tracks the last observed state
            of the alert (Active / Cleared) for the parent event configuration being monitored
        meta_name (Union[Unset, str]): Unique name for event record
        record_id (Union[Unset, str]): Encrypted record id for the resource being monitored
    """

    acked: Union[Unset, bool] = UNSET
    alert_state: Union[Unset, EventRecordSpecWrapperV1EventmonitoringPUTAlertState] = UNSET
    meta_name: Union[Unset, str] = UNSET
    record_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acked = self.acked

        alert_state: Union[Unset, str] = UNSET
        if not isinstance(self.alert_state, Unset):
            alert_state = self.alert_state.value

        meta_name = self.meta_name

        record_id = self.record_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acked is not UNSET:
            field_dict["acked"] = acked
        if alert_state is not UNSET:
            field_dict["alertState"] = alert_state
        if meta_name is not UNSET:
            field_dict["metaName"] = meta_name
        if record_id is not UNSET:
            field_dict["recordId"] = record_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        acked = d.pop("acked", UNSET)

        _alert_state = d.pop("alertState", UNSET)
        alert_state: Union[Unset, EventRecordSpecWrapperV1EventmonitoringPUTAlertState]
        if isinstance(_alert_state, Unset):
            alert_state = UNSET
        else:
            alert_state = EventRecordSpecWrapperV1EventmonitoringPUTAlertState(_alert_state)

        meta_name = d.pop("metaName", UNSET)

        record_id = d.pop("recordId", UNSET)

        event_record_spec_wrapper_v1_eventmonitoring_put = cls(
            acked=acked,
            alert_state=alert_state,
            meta_name=meta_name,
            record_id=record_id,
        )

        event_record_spec_wrapper_v1_eventmonitoring_put.additional_properties = d
        return event_record_spec_wrapper_v1_eventmonitoring_put

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
