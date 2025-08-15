from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RouteStatusErrorV1PlatformPUT")


@_attrs_define
class RouteStatusErrorV1PlatformPUT:
    """error is the last observed error, if any.

    Attributes:
        message (Union[Unset, str]): message is a string detailing the encountered error
        time (Union[Unset, str]): time is the timestamp when the error was encountered.
    """

    message: Union[Unset, str] = UNSET
    time: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        time = d.pop("time", UNSET)

        route_status_error_v1_platform_put = cls(
            message=message,
            time=time,
        )

        route_status_error_v1_platform_put.additional_properties = d
        return route_status_error_v1_platform_put

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
