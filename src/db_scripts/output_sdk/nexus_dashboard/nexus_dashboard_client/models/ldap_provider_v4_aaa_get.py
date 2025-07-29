from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_provider_v4_aaa_get_ssl_strictness_level import LDAPProviderV4AaaGETSslStrictnessLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPProviderV4AaaGET")


@_attrs_define
class LDAPProviderV4AaaGET:
    """
    Attributes:
        attribute (Union[Unset, str]): LDAP provider server authentication mechanism
        base_dn (Union[Unset, str]): Starting point when searching for users authentication within LDAP directory
        bind_dn (Union[Unset, str]): Specifies the login DN to access the LDAP provider server
        description (Union[Unset, str]): Description about the LDAP provider server
        filter_dn (Union[Unset, str]): Field based on which to filter DN
        key (Union[Unset, str]): Base64 encoded LDAP provider server secret
        monitor (Union[Unset, bool]): Flag to determine whether to monitor this LDAP provider
        monitor_password (Union[Unset, str]): Monitoring user password
        monitor_username (Union[Unset, str]): User name used for monitoring
        port (Union[Unset, int]): LDAP provider server connection port
        priority (Union[Unset, int]): LDAP provider server priority based on which authentication will be attempted
        retries (Union[Unset, int]): LDAP provider server connection retries parameter
        ssl_cert (Union[Unset, str]): SSL Certificate
        ssl_enabled (Union[Unset, bool]): Flag to determine whether to enable SSL
        ssl_strictness_level (Union[Unset, LDAPProviderV4AaaGETSslStrictnessLevel]): SSL Strictness Level
        timeout (Union[Unset, int]): LDAP provider server connection timeout parameter
    """

    attribute: Union[Unset, str] = UNSET
    base_dn: Union[Unset, str] = UNSET
    bind_dn: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    filter_dn: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    monitor: Union[Unset, bool] = UNSET
    monitor_password: Union[Unset, str] = UNSET
    monitor_username: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    priority: Union[Unset, int] = UNSET
    retries: Union[Unset, int] = UNSET
    ssl_cert: Union[Unset, str] = UNSET
    ssl_enabled: Union[Unset, bool] = UNSET
    ssl_strictness_level: Union[Unset, LDAPProviderV4AaaGETSslStrictnessLevel] = UNSET
    timeout: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute = self.attribute

        base_dn = self.base_dn

        bind_dn = self.bind_dn

        description = self.description

        filter_dn = self.filter_dn

        key = self.key

        monitor = self.monitor

        monitor_password = self.monitor_password

        monitor_username = self.monitor_username

        port = self.port

        priority = self.priority

        retries = self.retries

        ssl_cert = self.ssl_cert

        ssl_enabled = self.ssl_enabled

        ssl_strictness_level: Union[Unset, str] = UNSET
        if not isinstance(self.ssl_strictness_level, Unset):
            ssl_strictness_level = self.ssl_strictness_level.value

        timeout = self.timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute is not UNSET:
            field_dict["attribute"] = attribute
        if base_dn is not UNSET:
            field_dict["baseDN"] = base_dn
        if bind_dn is not UNSET:
            field_dict["bindDN"] = bind_dn
        if description is not UNSET:
            field_dict["description"] = description
        if filter_dn is not UNSET:
            field_dict["filterDN"] = filter_dn
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
        if ssl_cert is not UNSET:
            field_dict["sslCert"] = ssl_cert
        if ssl_enabled is not UNSET:
            field_dict["sslEnabled"] = ssl_enabled
        if ssl_strictness_level is not UNSET:
            field_dict["sslStrictnessLevel"] = ssl_strictness_level
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attribute = d.pop("attribute", UNSET)

        base_dn = d.pop("baseDN", UNSET)

        bind_dn = d.pop("bindDN", UNSET)

        description = d.pop("description", UNSET)

        filter_dn = d.pop("filterDN", UNSET)

        key = d.pop("key", UNSET)

        monitor = d.pop("monitor", UNSET)

        monitor_password = d.pop("monitorPassword", UNSET)

        monitor_username = d.pop("monitorUsername", UNSET)

        port = d.pop("port", UNSET)

        priority = d.pop("priority", UNSET)

        retries = d.pop("retries", UNSET)

        ssl_cert = d.pop("sslCert", UNSET)

        ssl_enabled = d.pop("sslEnabled", UNSET)

        _ssl_strictness_level = d.pop("sslStrictnessLevel", UNSET)
        ssl_strictness_level: Union[Unset, LDAPProviderV4AaaGETSslStrictnessLevel]
        if isinstance(_ssl_strictness_level, Unset):
            ssl_strictness_level = UNSET
        else:
            ssl_strictness_level = LDAPProviderV4AaaGETSslStrictnessLevel(_ssl_strictness_level)

        timeout = d.pop("timeout", UNSET)

        ldap_provider_v4_aaa_get = cls(
            attribute=attribute,
            base_dn=base_dn,
            bind_dn=bind_dn,
            description=description,
            filter_dn=filter_dn,
            key=key,
            monitor=monitor,
            monitor_password=monitor_password,
            monitor_username=monitor_username,
            port=port,
            priority=priority,
            retries=retries,
            ssl_cert=ssl_cert,
            ssl_enabled=ssl_enabled,
            ssl_strictness_level=ssl_strictness_level,
            timeout=timeout,
        )

        ldap_provider_v4_aaa_get.additional_properties = d
        return ldap_provider_v4_aaa_get

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
