from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.syslog_sync_spec_v1_platform_get_forwarding_facility import SyslogSyncSpecV1PlatformGETForwardingFacility
from ..models.syslog_sync_spec_v1_platform_get_severity import SyslogSyncSpecV1PlatformGETSeverity
from ..models.syslog_sync_spec_v1_platform_get_transport import SyslogSyncSpecV1PlatformGETTransport
from ..types import UNSET, Unset

T = TypeVar("T", bound="SyslogSyncSpecV1PlatformGET")


@_attrs_define
class SyslogSyncSpecV1PlatformGET:
    """Syslog server configuration

    Attributes:
        address (Union[Unset, str]): Server hostname or ipaddress
        enabled (Union[Unset, bool]): Syslog server enabled flag
        forwarding_facility (Union[Unset, SyslogSyncSpecV1PlatformGETForwardingFacility]): Syslog server forwarding
            facility
        port (Union[Unset, int]): Syslog server port
        severity (Union[Unset, SyslogSyncSpecV1PlatformGETSeverity]): Syslog server severity level
        transport (Union[Unset, SyslogSyncSpecV1PlatformGETTransport]): Syslog server transport protocol
    """

    address: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    forwarding_facility: Union[Unset, SyslogSyncSpecV1PlatformGETForwardingFacility] = UNSET
    port: Union[Unset, int] = UNSET
    severity: Union[Unset, SyslogSyncSpecV1PlatformGETSeverity] = UNSET
    transport: Union[Unset, SyslogSyncSpecV1PlatformGETTransport] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        enabled = self.enabled

        forwarding_facility: Union[Unset, str] = UNSET
        if not isinstance(self.forwarding_facility, Unset):
            forwarding_facility = self.forwarding_facility.value

        port = self.port

        severity: Union[Unset, str] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        transport: Union[Unset, str] = UNSET
        if not isinstance(self.transport, Unset):
            transport = self.transport.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if forwarding_facility is not UNSET:
            field_dict["forwardingFacility"] = forwarding_facility
        if port is not UNSET:
            field_dict["port"] = port
        if severity is not UNSET:
            field_dict["severity"] = severity
        if transport is not UNSET:
            field_dict["transport"] = transport

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        enabled = d.pop("enabled", UNSET)

        _forwarding_facility = d.pop("forwardingFacility", UNSET)
        forwarding_facility: Union[Unset, SyslogSyncSpecV1PlatformGETForwardingFacility]
        if isinstance(_forwarding_facility, Unset):
            forwarding_facility = UNSET
        else:
            forwarding_facility = SyslogSyncSpecV1PlatformGETForwardingFacility(_forwarding_facility)

        port = d.pop("port", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, SyslogSyncSpecV1PlatformGETSeverity]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = SyslogSyncSpecV1PlatformGETSeverity(_severity)

        _transport = d.pop("transport", UNSET)
        transport: Union[Unset, SyslogSyncSpecV1PlatformGETTransport]
        if isinstance(_transport, Unset):
            transport = UNSET
        else:
            transport = SyslogSyncSpecV1PlatformGETTransport(_transport)

        syslog_sync_spec_v1_platform_get = cls(
            address=address,
            enabled=enabled,
            forwarding_facility=forwarding_facility,
            port=port,
            severity=severity,
            transport=transport,
        )

        syslog_sync_spec_v1_platform_get.additional_properties = d
        return syslog_sync_spec_v1_platform_get

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
