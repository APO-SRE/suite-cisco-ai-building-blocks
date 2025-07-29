from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_occurrence_v1_eventmonitoring_post_severity import EventOccurrenceV1EventmonitoringPOSTSeverity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_stream_v1_eventmonitoring_post import RecordStreamV1EventmonitoringPOST


T = TypeVar("T", bound="EventOccurrenceV1EventmonitoringPOST")


@_attrs_define
class EventOccurrenceV1EventmonitoringPOST:
    """Current status of the event record being monitored

    Attributes:
        alert_description (Union[Unset, str]): Description of the alert being raised
        cleared_time (Union[Unset, str]): Timestamp when the alert is cleared
        correlated_faults (Union[Unset, list[str]]): List of event records which are correlated to the current record
        encrypted (Union[Unset, bool]): Whether event record information is encrypted
        event_count (Union[Unset, int]): Number of events captured during "Active" alert state
        id (Union[Unset, str]):
        is_root_cause (Union[Unset, bool]): Whether the event record is marked as the root cause of the alerts raised by
            other correlated event records
        result_value (Union[Unset, str]): Current result value of the resource being monitored as part of event
            configuration
        severity (Union[Unset, EventOccurrenceV1EventmonitoringPOSTSeverity]): Severity of the event configuration being
            monitored with respect to the threshold
        stream_history (Union[Unset, list['RecordStreamV1EventmonitoringPOST']]): List of streams where event record
            alert information is broadcasted and the status of the stream operation
    """

    alert_description: Union[Unset, str] = UNSET
    cleared_time: Union[Unset, str] = UNSET
    correlated_faults: Union[Unset, list[str]] = UNSET
    encrypted: Union[Unset, bool] = UNSET
    event_count: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    is_root_cause: Union[Unset, bool] = UNSET
    result_value: Union[Unset, str] = UNSET
    severity: Union[Unset, EventOccurrenceV1EventmonitoringPOSTSeverity] = UNSET
    stream_history: Union[Unset, list["RecordStreamV1EventmonitoringPOST"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_description = self.alert_description

        cleared_time = self.cleared_time

        correlated_faults: Union[Unset, list[str]] = UNSET
        if not isinstance(self.correlated_faults, Unset):
            correlated_faults = self.correlated_faults

        encrypted = self.encrypted

        event_count = self.event_count

        id = self.id

        is_root_cause = self.is_root_cause

        result_value = self.result_value

        severity: Union[Unset, str] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        stream_history: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.stream_history, Unset):
            stream_history = []
            for stream_history_item_data in self.stream_history:
                stream_history_item = stream_history_item_data.to_dict()
                stream_history.append(stream_history_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_description is not UNSET:
            field_dict["alertDescription"] = alert_description
        if cleared_time is not UNSET:
            field_dict["clearedTime"] = cleared_time
        if correlated_faults is not UNSET:
            field_dict["correlatedFaults"] = correlated_faults
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if event_count is not UNSET:
            field_dict["eventCount"] = event_count
        if id is not UNSET:
            field_dict["id"] = id
        if is_root_cause is not UNSET:
            field_dict["isRootCause"] = is_root_cause
        if result_value is not UNSET:
            field_dict["resultValue"] = result_value
        if severity is not UNSET:
            field_dict["severity"] = severity
        if stream_history is not UNSET:
            field_dict["streamHistory"] = stream_history

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_stream_v1_eventmonitoring_post import RecordStreamV1EventmonitoringPOST

        d = dict(src_dict)
        alert_description = d.pop("alertDescription", UNSET)

        cleared_time = d.pop("clearedTime", UNSET)

        correlated_faults = cast(list[str], d.pop("correlatedFaults", UNSET))

        encrypted = d.pop("encrypted", UNSET)

        event_count = d.pop("eventCount", UNSET)

        id = d.pop("id", UNSET)

        is_root_cause = d.pop("isRootCause", UNSET)

        result_value = d.pop("resultValue", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, EventOccurrenceV1EventmonitoringPOSTSeverity]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = EventOccurrenceV1EventmonitoringPOSTSeverity(_severity)

        stream_history = []
        _stream_history = d.pop("streamHistory", UNSET)
        for stream_history_item_data in _stream_history or []:
            stream_history_item = RecordStreamV1EventmonitoringPOST.from_dict(stream_history_item_data)

            stream_history.append(stream_history_item)

        event_occurrence_v1_eventmonitoring_post = cls(
            alert_description=alert_description,
            cleared_time=cleared_time,
            correlated_faults=correlated_faults,
            encrypted=encrypted,
            event_count=event_count,
            id=id,
            is_root_cause=is_root_cause,
            result_value=result_value,
            severity=severity,
            stream_history=stream_history,
        )

        event_occurrence_v1_eventmonitoring_post.additional_properties = d
        return event_occurrence_v1_eventmonitoring_post

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
