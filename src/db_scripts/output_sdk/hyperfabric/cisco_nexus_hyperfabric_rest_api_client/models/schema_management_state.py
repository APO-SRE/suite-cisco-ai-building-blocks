import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.schema_operation_status import SchemaOperationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_dns_config import SchemaDnsConfig
    from ..models.schema_drake_config import SchemaDrakeConfig
    from ..models.schema_path_path_id import SchemaPathPathId
    from ..models.schema_proxy_config import SchemaProxyConfig
    from ..models.schema_sonic_config import SchemaSonicConfig


T = TypeVar("T", bound="SchemaManagementState")


@_attrs_define
class SchemaManagementState:
    """Description not available

    Attributes:
        collected_at (Union[Unset, datetime.datetime]): Description not available
        config_source (Union[Unset, str]): Description not available
        dns (Union[Unset, SchemaDnsConfig]): Description not available
        drake (Union[Unset, SchemaDrakeConfig]): Description not available
        id (Union[Unset, SchemaPathPathId]): PathId identifies the specific "schema coordinates" identifier of an object
            in the schema tree.
        ipv_4_method (Union[Unset, str]): Description not available
        ipv_6_method (Union[Unset, str]): Description not available
        ntp_servers (Union[Unset, list[str]]): Description not available
        operation_status (Union[Unset, SchemaOperationStatus]): Description not available
        proxy (Union[Unset, SchemaProxyConfig]): Description not available
        sonic (Union[Unset, SchemaSonicConfig]): Description not available
    """

    collected_at: Union[Unset, datetime.datetime] = UNSET
    config_source: Union[Unset, str] = UNSET
    dns: Union[Unset, "SchemaDnsConfig"] = UNSET
    drake: Union[Unset, "SchemaDrakeConfig"] = UNSET
    id: Union[Unset, "SchemaPathPathId"] = UNSET
    ipv_4_method: Union[Unset, str] = UNSET
    ipv_6_method: Union[Unset, str] = UNSET
    ntp_servers: Union[Unset, list[str]] = UNSET
    operation_status: Union[Unset, SchemaOperationStatus] = UNSET
    proxy: Union[Unset, "SchemaProxyConfig"] = UNSET
    sonic: Union[Unset, "SchemaSonicConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collected_at: Union[Unset, str] = UNSET
        if not isinstance(self.collected_at, Unset):
            collected_at = self.collected_at.isoformat()

        config_source = self.config_source

        dns: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dns, Unset):
            dns = self.dns.to_dict()

        drake: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.drake, Unset):
            drake = self.drake.to_dict()

        id: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        ipv_4_method = self.ipv_4_method

        ipv_6_method = self.ipv_6_method

        ntp_servers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ntp_servers, Unset):
            ntp_servers = self.ntp_servers

        operation_status: Union[Unset, str] = UNSET
        if not isinstance(self.operation_status, Unset):
            operation_status = self.operation_status.value

        proxy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.proxy, Unset):
            proxy = self.proxy.to_dict()

        sonic: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sonic, Unset):
            sonic = self.sonic.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collected_at is not UNSET:
            field_dict["collectedAt"] = collected_at
        if config_source is not UNSET:
            field_dict["configSource"] = config_source
        if dns is not UNSET:
            field_dict["dns"] = dns
        if drake is not UNSET:
            field_dict["drake"] = drake
        if id is not UNSET:
            field_dict["id"] = id
        if ipv_4_method is not UNSET:
            field_dict["ipv4Method"] = ipv_4_method
        if ipv_6_method is not UNSET:
            field_dict["ipv6Method"] = ipv_6_method
        if ntp_servers is not UNSET:
            field_dict["ntpServers"] = ntp_servers
        if operation_status is not UNSET:
            field_dict["operationStatus"] = operation_status
        if proxy is not UNSET:
            field_dict["proxy"] = proxy
        if sonic is not UNSET:
            field_dict["sonic"] = sonic

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_dns_config import SchemaDnsConfig
        from ..models.schema_drake_config import SchemaDrakeConfig
        from ..models.schema_path_path_id import SchemaPathPathId
        from ..models.schema_proxy_config import SchemaProxyConfig
        from ..models.schema_sonic_config import SchemaSonicConfig

        d = dict(src_dict)
        _collected_at = d.pop("collectedAt", UNSET)
        collected_at: Union[Unset, datetime.datetime]
        if isinstance(_collected_at, Unset):
            collected_at = UNSET
        else:
            collected_at = isoparse(_collected_at)

        config_source = d.pop("configSource", UNSET)

        _dns = d.pop("dns", UNSET)
        dns: Union[Unset, SchemaDnsConfig]
        if isinstance(_dns, Unset):
            dns = UNSET
        else:
            dns = SchemaDnsConfig.from_dict(_dns)

        _drake = d.pop("drake", UNSET)
        drake: Union[Unset, SchemaDrakeConfig]
        if isinstance(_drake, Unset):
            drake = UNSET
        else:
            drake = SchemaDrakeConfig.from_dict(_drake)

        _id = d.pop("id", UNSET)
        id: Union[Unset, SchemaPathPathId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = SchemaPathPathId.from_dict(_id)

        ipv_4_method = d.pop("ipv4Method", UNSET)

        ipv_6_method = d.pop("ipv6Method", UNSET)

        ntp_servers = cast(list[str], d.pop("ntpServers", UNSET))

        _operation_status = d.pop("operationStatus", UNSET)
        operation_status: Union[Unset, SchemaOperationStatus]
        if isinstance(_operation_status, Unset):
            operation_status = UNSET
        else:
            operation_status = SchemaOperationStatus(_operation_status)

        _proxy = d.pop("proxy", UNSET)
        proxy: Union[Unset, SchemaProxyConfig]
        if isinstance(_proxy, Unset):
            proxy = UNSET
        else:
            proxy = SchemaProxyConfig.from_dict(_proxy)

        _sonic = d.pop("sonic", UNSET)
        sonic: Union[Unset, SchemaSonicConfig]
        if isinstance(_sonic, Unset):
            sonic = UNSET
        else:
            sonic = SchemaSonicConfig.from_dict(_sonic)

        schema_management_state = cls(
            collected_at=collected_at,
            config_source=config_source,
            dns=dns,
            drake=drake,
            id=id,
            ipv_4_method=ipv_4_method,
            ipv_6_method=ipv_6_method,
            ntp_servers=ntp_servers,
            operation_status=operation_status,
            proxy=proxy,
            sonic=sonic,
        )

        schema_management_state.additional_properties = d
        return schema_management_state

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
