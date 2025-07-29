from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.record_stream_v1_eventmonitoring_put_status import RecordStreamV1EventmonitoringPUTStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordStreamV1EventmonitoringPUT")


@_attrs_define
class RecordStreamV1EventmonitoringPUT:
    """List of streams where event record alert information is broadcasted and the status of the stream operation

    Attributes:
        name (Union[Unset, str]): Type of stream
        status (Union[Unset, RecordStreamV1EventmonitoringPUTStatus]): Whether the stream broadcast was "Completed" or
            "Failed"
        timestamp (Union[Unset, str]): Timestamp when the stream operation was attempted
    """

    name: Union[Unset, str] = UNSET
    status: Union[Unset, RecordStreamV1EventmonitoringPUTStatus] = UNSET
    timestamp: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, RecordStreamV1EventmonitoringPUTStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RecordStreamV1EventmonitoringPUTStatus(_status)

        timestamp = d.pop("timestamp", UNSET)

        record_stream_v1_eventmonitoring_put = cls(
            name=name,
            status=status,
            timestamp=timestamp,
        )

        record_stream_v1_eventmonitoring_put.additional_properties = d
        return record_stream_v1_eventmonitoring_put

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
