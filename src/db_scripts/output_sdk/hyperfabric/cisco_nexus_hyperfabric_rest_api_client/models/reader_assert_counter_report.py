import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReaderAssertCounterReport")


@_attrs_define
class ReaderAssertCounterReport:
    """AssertCounterReport holds an assertion counter record at particular time instance

    Attributes:
        cleared_false_asserts (Union[Unset, int]): The number of cleared false asserts per time granularity
        config_activities (Union[Unset, int]): The number of config activities during the time granularity
        device (Union[Unset, str]): the device name or UUID
        new_false_asserts (Union[Unset, int]): The number of new false asserts per time granularity
        port_name (Union[Unset, str]): The port index.
        timestamp (Union[Unset, datetime.datetime]): The timestamp associated this report
        type_ (Union[Unset, str]): The assert type
    """

    cleared_false_asserts: Union[Unset, int] = UNSET
    config_activities: Union[Unset, int] = UNSET
    device: Union[Unset, str] = UNSET
    new_false_asserts: Union[Unset, int] = UNSET
    port_name: Union[Unset, str] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cleared_false_asserts = self.cleared_false_asserts

        config_activities = self.config_activities

        device = self.device

        new_false_asserts = self.new_false_asserts

        port_name = self.port_name

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cleared_false_asserts is not UNSET:
            field_dict["clearedFalseAsserts"] = cleared_false_asserts
        if config_activities is not UNSET:
            field_dict["configActivities"] = config_activities
        if device is not UNSET:
            field_dict["device"] = device
        if new_false_asserts is not UNSET:
            field_dict["newFalseAsserts"] = new_false_asserts
        if port_name is not UNSET:
            field_dict["portName"] = port_name
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cleared_false_asserts = d.pop("clearedFalseAsserts", UNSET)

        config_activities = d.pop("configActivities", UNSET)

        device = d.pop("device", UNSET)

        new_false_asserts = d.pop("newFalseAsserts", UNSET)

        port_name = d.pop("portName", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        type_ = d.pop("type", UNSET)

        reader_assert_counter_report = cls(
            cleared_false_asserts=cleared_false_asserts,
            config_activities=config_activities,
            device=device,
            new_false_asserts=new_false_asserts,
            port_name=port_name,
            timestamp=timestamp,
            type_=type_,
        )

        reader_assert_counter_report.additional_properties = d
        return reader_assert_counter_report

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
