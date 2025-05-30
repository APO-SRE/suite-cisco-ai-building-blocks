from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.notification_series_item import NotificationSeriesItem


T = TypeVar("T", bound="NotificationsStatisticsResponse")


@_attrs_define
class NotificationsStatisticsResponse:
    """
    Attributes:
        id (str): subscription id Example: c877e1cc-569c-44b0-af8b-1405141968ae.
        sent (int): The total sent messages in last 24 hours Example: 8000.
        acknowledge (int): The total acknowledged messages in last 24 hours Example: 7000.
        rate (float): The message sent rate Example: 333.33.
        success_percent (float): The successful rate Example: 87.5.
        series (list['NotificationSeriesItem']):
    """

    id: str
    sent: int
    acknowledge: int
    rate: float
    success_percent: float
    series: list["NotificationSeriesItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sent = self.sent

        acknowledge = self.acknowledge

        rate = self.rate

        success_percent = self.success_percent

        series = []
        for series_item_data in self.series:
            series_item = series_item_data.to_dict()
            series.append(series_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "sent": sent,
                "acknowledge": acknowledge,
                "rate": rate,
                "successPercent": success_percent,
                "series": series,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_series_item import NotificationSeriesItem

        d = dict(src_dict)
        id = d.pop("id")

        sent = d.pop("sent")

        acknowledge = d.pop("acknowledge")

        rate = d.pop("rate")

        success_percent = d.pop("successPercent")

        series = []
        _series = d.pop("series")
        for series_item_data in _series:
            series_item = NotificationSeriesItem.from_dict(series_item_data)

            series.append(series_item)

        notifications_statistics_response = cls(
            id=id,
            sent=sent,
            acknowledge=acknowledge,
            rate=rate,
            success_percent=success_percent,
            series=series,
        )

        notifications_statistics_response.additional_properties = d
        return notifications_statistics_response

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
