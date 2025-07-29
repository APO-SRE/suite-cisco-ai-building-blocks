from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.syslog_sync_status_error_v1_platform_put import SyslogSyncStatusErrorV1PlatformPUT


T = TypeVar("T", bound="SyslogSyncStatusWrapperV1PlatformPUT")


@_attrs_define
class SyslogSyncStatusWrapperV1PlatformPUT:
    """
    Attributes:
        error (Union[Unset, SyslogSyncStatusErrorV1PlatformPUT]): error is the last observed error, if any.
    """

    error: Union[Unset, "SyslogSyncStatusErrorV1PlatformPUT"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.syslog_sync_status_error_v1_platform_put import SyslogSyncStatusErrorV1PlatformPUT

        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: Union[Unset, SyslogSyncStatusErrorV1PlatformPUT]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = SyslogSyncStatusErrorV1PlatformPUT.from_dict(_error)

        syslog_sync_status_wrapper_v1_platform_put = cls(
            error=error,
        )

        syslog_sync_status_wrapper_v1_platform_put.additional_properties = d
        return syslog_sync_status_wrapper_v1_platform_put

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
