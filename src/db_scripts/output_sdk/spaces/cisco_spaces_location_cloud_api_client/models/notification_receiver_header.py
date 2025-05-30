from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationReceiverHeader")


@_attrs_define
class NotificationReceiverHeader:
    """
    Attributes:
        accept (Union[Unset, str]): Accepted MIME type. Example: application/json.
        content_type (Union[Unset, str]): Content type Example: application/json.
    """

    accept: Union[Unset, str] = UNSET
    content_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accept = self.accept

        content_type = self.content_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accept is not UNSET:
            field_dict["Accept"] = accept
        if content_type is not UNSET:
            field_dict["Content-Type"] = content_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accept = d.pop("Accept", UNSET)

        content_type = d.pop("Content-Type", UNSET)

        notification_receiver_header = cls(
            accept=accept,
            content_type=content_type,
        )

        notification_receiver_header.additional_properties = d
        return notification_receiver_header

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
