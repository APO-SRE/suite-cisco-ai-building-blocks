import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="NotificationSeriesItem")


@_attrs_define
class NotificationSeriesItem:
    """
    Attributes:
        sent (int): The sent messages count Example: 200.
        ack (int): The acknowlege messages count Example: 200.
        time (datetime.datetime): The time Example: 2018-05-01T00:00:00.000Z.
    """

    sent: int
    ack: int
    time: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sent = self.sent

        ack = self.ack

        time = self.time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sent": sent,
                "ack": ack,
                "time": time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sent = d.pop("sent")

        ack = d.pop("ack")

        time = isoparse(d.pop("time"))

        notification_series_item = cls(
            sent=sent,
            ack=ack,
            time=time,
        )

        notification_series_item.additional_properties = d
        return notification_series_item

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
