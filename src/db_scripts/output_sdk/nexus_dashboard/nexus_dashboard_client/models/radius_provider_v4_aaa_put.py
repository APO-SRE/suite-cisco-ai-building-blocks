from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.radius_provider_v4_aaa_put_auth_protocol import RADIUSProviderV4AaaPUTAuthProtocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="RADIUSProviderV4AaaPUT")


@_attrs_define
class RADIUSProviderV4AaaPUT:
    """
    Attributes:
        auth_protocol (Union[Unset, RADIUSProviderV4AaaPUTAuthProtocol]): RADIUS provider server authentication
            mechanism
        description (Union[Unset, str]): Description about the RADIUS provider server
        key (Union[Unset, str]): Base64 encoded RADIUS provider server secret
        monitor (Union[Unset, bool]): Flag to determine whether to monitor this LDAP provider
        monitor_password (Union[Unset, str]): Monitoring user password
        monitor_username (Union[Unset, str]): User name used for monitoring
        port (Union[Unset, int]): RADIUS provider server connection port
        priority (Union[Unset, int]): RADIUS provider server priority based on which authentication will be attempted
        retries (Union[Unset, int]): RADIUS provider server connection retries parameter
        state_code (Union[Unset, str]): RADIUS state code
        timeout (Union[Unset, int]): RADIUS provider server connection timeout parameter
    """

    auth_protocol: Union[Unset, RADIUSProviderV4AaaPUTAuthProtocol] = UNSET
    description: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    monitor: Union[Unset, bool] = UNSET
    monitor_password: Union[Unset, str] = UNSET
    monitor_username: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    priority: Union[Unset, int] = UNSET
    retries: Union[Unset, int] = UNSET
    state_code: Union[Unset, str] = UNSET
    timeout: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_protocol: Union[Unset, str] = UNSET
        if not isinstance(self.auth_protocol, Unset):
            auth_protocol = self.auth_protocol.value

        description = self.description

        key = self.key

        monitor = self.monitor

        monitor_password = self.monitor_password

        monitor_username = self.monitor_username

        port = self.port

        priority = self.priority

        retries = self.retries

        state_code = self.state_code

        timeout = self.timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_protocol is not UNSET:
            field_dict["authProtocol"] = auth_protocol
        if description is not UNSET:
            field_dict["description"] = description
        if key is not UNSET:
            field_dict["key"] = key
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if monitor_password is not UNSET:
            field_dict["monitorPassword"] = monitor_password
        if monitor_username is not UNSET:
            field_dict["monitorUsername"] = monitor_username
        if port is not UNSET:
            field_dict["port"] = port
        if priority is not UNSET:
            field_dict["priority"] = priority
        if retries is not UNSET:
            field_dict["retries"] = retries
        if state_code is not UNSET:
            field_dict["stateCode"] = state_code
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _auth_protocol = d.pop("authProtocol", UNSET)
        auth_protocol: Union[Unset, RADIUSProviderV4AaaPUTAuthProtocol]
        if isinstance(_auth_protocol, Unset):
            auth_protocol = UNSET
        else:
            auth_protocol = RADIUSProviderV4AaaPUTAuthProtocol(_auth_protocol)

        description = d.pop("description", UNSET)

        key = d.pop("key", UNSET)

        monitor = d.pop("monitor", UNSET)

        monitor_password = d.pop("monitorPassword", UNSET)

        monitor_username = d.pop("monitorUsername", UNSET)

        port = d.pop("port", UNSET)

        priority = d.pop("priority", UNSET)

        retries = d.pop("retries", UNSET)

        state_code = d.pop("stateCode", UNSET)

        timeout = d.pop("timeout", UNSET)

        radius_provider_v4_aaa_put = cls(
            auth_protocol=auth_protocol,
            description=description,
            key=key,
            monitor=monitor,
            monitor_password=monitor_password,
            monitor_username=monitor_username,
            port=port,
            priority=priority,
            retries=retries,
            state_code=state_code,
            timeout=timeout,
        )

        radius_provider_v4_aaa_put.additional_properties = d
        return radius_provider_v4_aaa_put

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
