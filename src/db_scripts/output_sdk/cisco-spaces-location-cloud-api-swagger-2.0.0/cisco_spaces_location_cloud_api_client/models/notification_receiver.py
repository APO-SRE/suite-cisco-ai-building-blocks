from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_receiver_header import NotificationReceiverHeader


T = TypeVar("T", bound="NotificationReceiver")


@_attrs_define
class NotificationReceiver:
    """
    Attributes:
        url (str): receiver URL Example: https://test.customer.com:443.
        headers (Union[Unset, NotificationReceiverHeader]):
    """

    url: str
    headers: Union[Unset, "NotificationReceiverHeader"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_receiver_header import NotificationReceiverHeader

        d = dict(src_dict)
        url = d.pop("url")

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, NotificationReceiverHeader]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = NotificationReceiverHeader.from_dict(_headers)

        notification_receiver = cls(
            url=url,
            headers=headers,
        )

        notification_receiver.additional_properties = d
        return notification_receiver

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
