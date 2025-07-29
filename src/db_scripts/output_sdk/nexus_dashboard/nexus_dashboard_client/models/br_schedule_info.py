import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.br_type import BrType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BrScheduleInfo")


@_attrs_define
class BrScheduleInfo:
    """
    Attributes:
        name (Union[Unset, str]): Backup schedule name
        type_ (Union[Unset, BrType]): Operation type
        start_time (Union[Unset, datetime.datetime]): Time of first scheduled backup
        frequency (Union[Unset, int]): Frequency in days
        user (Union[Unset, str]): ID of the user creating the schedule
        destination (Union[Unset, str]): Remote location where the backup is stored
        path (Union[Unset, str]): Path to the backup file on the remote location
    """

    name: Union[Unset, str] = UNSET
    type_: Union[Unset, BrType] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    frequency: Union[Unset, int] = UNSET
    user: Union[Unset, str] = UNSET
    destination: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        frequency = self.frequency

        user = self.user

        destination = self.destination

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if user is not UNSET:
            field_dict["user"] = user
        if destination is not UNSET:
            field_dict["destination"] = destination
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BrType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BrType(_type_)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        frequency = d.pop("frequency", UNSET)

        user = d.pop("user", UNSET)

        destination = d.pop("destination", UNSET)

        path = d.pop("path", UNSET)

        br_schedule_info = cls(
            name=name,
            type_=type_,
            start_time=start_time,
            frequency=frequency,
            user=user,
            destination=destination,
            path=path,
        )

        br_schedule_info.additional_properties = d
        return br_schedule_info

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
