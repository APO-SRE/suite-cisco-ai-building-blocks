import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.br_type import BrType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BrScheduleRequest")


@_attrs_define
class BrScheduleRequest:
    """
    Attributes:
        name (str): Backup schedule name
        type_ (BrType): Operation type
        start_time (datetime.datetime): Time of first scheduled backup
        frequency (int): Frequency in days
        destination (str): Remote location where the backup is stored
        encryption_key (Union[Unset, str]): Backup file encryption key
    """

    name: str
    type_: BrType
    start_time: datetime.datetime
    frequency: int
    destination: str
    encryption_key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        start_time = self.start_time.isoformat()

        frequency = self.frequency

        destination = self.destination

        encryption_key = self.encryption_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "startTime": start_time,
                "frequency": frequency,
                "destination": destination,
            }
        )
        if encryption_key is not UNSET:
            field_dict["encryptionKey"] = encryption_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = BrType(d.pop("type"))

        start_time = isoparse(d.pop("startTime"))

        frequency = d.pop("frequency")

        destination = d.pop("destination")

        encryption_key = d.pop("encryptionKey", UNSET)

        br_schedule_request = cls(
            name=name,
            type_=type_,
            start_time=start_time,
            frequency=frequency,
            destination=destination,
            encryption_key=encryption_key,
        )

        br_schedule_request.additional_properties = d
        return br_schedule_request

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
