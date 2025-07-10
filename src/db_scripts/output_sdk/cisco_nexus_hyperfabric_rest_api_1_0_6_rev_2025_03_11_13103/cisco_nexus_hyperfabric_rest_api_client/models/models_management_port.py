from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_config_origin import ModelsConfigOrigin
from ..models.models_config_type import ModelsConfigType
from ..models.models_connected_state import ModelsConnectedState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_metadata import ModelsMetadata


T = TypeVar("T", bound="ModelsManagementPort")


@_attrs_define
class ModelsManagementPort:
    """A management port encapsulates the configuration and properties of an Out of Band network interface of a node used
    to communicate with the Cisco Nexus Hyperfabric service.

        Attributes:
            cloud_urls (Union[Unset, list[str]]): A list of one or more Cloud URLs used by a node.
            config_origin (Union[Unset, ModelsConfigOrigin]): ConfigOrigin is used by a management port to indicate if the
                configuration was provided by the cloud or the device.
            connected_state (Union[Unset, ModelsConnectedState]): ConnectedState is used by a management port to indicate if
                the port is successfully connected to the Hyperfabric service. It is distinct from the AdminState.
            description (Union[Unset, str]): The description is a user-defined field to store notes about the management
                port.
            dns_addresses (Union[Unset, list[str]]): A list of one or more DNS IP addresses used by the node.
            enabled (Union[Unset, bool]): The administrative state of the management port which indicates if the management
                port is enabled or disabled.
            id (Union[Unset, str]): This is a read-only field. The unique identifier of the management port.
            ipv_4_address (Union[Unset, str]): The IPv4 host address for the management port of the node.
            ipv_4_config_type (Union[Unset, ModelsConfigType]): ConfigType is used by a management port to indicate if the
                IP configuration is static or DHCP.
            ipv_4_gateway (Union[Unset, str]): The IPv4 gateway address for the management port of the node.
            ipv_6_address (Union[Unset, str]): The IPv6 host address for the management port of the node.
            ipv_6_config_type (Union[Unset, ModelsConfigType]): ConfigType is used by a management port to indicate if the
                IP configuration is static or DHCP.
            ipv_6_gateway (Union[Unset, str]): The IPv6 gateway address for the management port of the node.
            metadata (Union[Unset, ModelsMetadata]): Metadata defines a map of attributes related to the lifecycle of the
                object.
            name (Union[Unset, str]): The name of the management port of the node (E.g. eth0)
            no_proxy (Union[Unset, list[str]]): A list of IP addresses or domain names that should not be proxied.
            node_id (Union[Unset, str]): This is a read-only field. The unique identifier of the node to which this
                management port belongs to.
            proxy_address (Union[Unset, str]): The URL for a configured HTTPs proxy for the node.
            proxy_credentials_id (Union[Unset, str]): A unique identifier of a set of credentials for the proxy.
            proxy_password (Union[Unset, str]): A password to be used to authenticate to the proxy. Once set, this attribute
                is not returned.
            proxy_username (Union[Unset, str]): A username to be used to authenticate to the proxy.
            set_proxy_password (Union[Unset, bool]): The flag to indicate that the proxy password should be cleared.
    """

    cloud_urls: Union[Unset, list[str]] = UNSET
    config_origin: Union[Unset, ModelsConfigOrigin] = UNSET
    connected_state: Union[Unset, ModelsConnectedState] = UNSET
    description: Union[Unset, str] = UNSET
    dns_addresses: Union[Unset, list[str]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    ipv_4_address: Union[Unset, str] = UNSET
    ipv_4_config_type: Union[Unset, ModelsConfigType] = UNSET
    ipv_4_gateway: Union[Unset, str] = UNSET
    ipv_6_address: Union[Unset, str] = UNSET
    ipv_6_config_type: Union[Unset, ModelsConfigType] = UNSET
    ipv_6_gateway: Union[Unset, str] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    name: Union[Unset, str] = UNSET
    no_proxy: Union[Unset, list[str]] = UNSET
    node_id: Union[Unset, str] = UNSET
    proxy_address: Union[Unset, str] = UNSET
    proxy_credentials_id: Union[Unset, str] = UNSET
    proxy_password: Union[Unset, str] = UNSET
    proxy_username: Union[Unset, str] = UNSET
    set_proxy_password: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_urls: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cloud_urls, Unset):
            cloud_urls = self.cloud_urls

        config_origin: Union[Unset, str] = UNSET
        if not isinstance(self.config_origin, Unset):
            config_origin = self.config_origin.value

        connected_state: Union[Unset, str] = UNSET
        if not isinstance(self.connected_state, Unset):
            connected_state = self.connected_state.value

        description = self.description

        dns_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.dns_addresses, Unset):
            dns_addresses = self.dns_addresses

        enabled = self.enabled

        id = self.id

        ipv_4_address = self.ipv_4_address

        ipv_4_config_type: Union[Unset, str] = UNSET
        if not isinstance(self.ipv_4_config_type, Unset):
            ipv_4_config_type = self.ipv_4_config_type.value

        ipv_4_gateway = self.ipv_4_gateway

        ipv_6_address = self.ipv_6_address

        ipv_6_config_type: Union[Unset, str] = UNSET
        if not isinstance(self.ipv_6_config_type, Unset):
            ipv_6_config_type = self.ipv_6_config_type.value

        ipv_6_gateway = self.ipv_6_gateway

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        no_proxy: Union[Unset, list[str]] = UNSET
        if not isinstance(self.no_proxy, Unset):
            no_proxy = self.no_proxy

        node_id = self.node_id

        proxy_address = self.proxy_address

        proxy_credentials_id = self.proxy_credentials_id

        proxy_password = self.proxy_password

        proxy_username = self.proxy_username

        set_proxy_password = self.set_proxy_password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloud_urls is not UNSET:
            field_dict["cloudUrls"] = cloud_urls
        if config_origin is not UNSET:
            field_dict["configOrigin"] = config_origin
        if connected_state is not UNSET:
            field_dict["connectedState"] = connected_state
        if description is not UNSET:
            field_dict["description"] = description
        if dns_addresses is not UNSET:
            field_dict["dnsAddresses"] = dns_addresses
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if ipv_4_address is not UNSET:
            field_dict["ipv4Address"] = ipv_4_address
        if ipv_4_config_type is not UNSET:
            field_dict["ipv4ConfigType"] = ipv_4_config_type
        if ipv_4_gateway is not UNSET:
            field_dict["ipv4Gateway"] = ipv_4_gateway
        if ipv_6_address is not UNSET:
            field_dict["ipv6Address"] = ipv_6_address
        if ipv_6_config_type is not UNSET:
            field_dict["ipv6ConfigType"] = ipv_6_config_type
        if ipv_6_gateway is not UNSET:
            field_dict["ipv6Gateway"] = ipv_6_gateway
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if no_proxy is not UNSET:
            field_dict["noProxy"] = no_proxy
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if proxy_address is not UNSET:
            field_dict["proxyAddress"] = proxy_address
        if proxy_credentials_id is not UNSET:
            field_dict["proxyCredentialsId"] = proxy_credentials_id
        if proxy_password is not UNSET:
            field_dict["proxyPassword"] = proxy_password
        if proxy_username is not UNSET:
            field_dict["proxyUsername"] = proxy_username
        if set_proxy_password is not UNSET:
            field_dict["setProxyPassword"] = set_proxy_password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_metadata import ModelsMetadata

        d = dict(src_dict)
        cloud_urls = cast(list[str], d.pop("cloudUrls", UNSET))

        _config_origin = d.pop("configOrigin", UNSET)
        config_origin: Union[Unset, ModelsConfigOrigin]
        if isinstance(_config_origin, Unset):
            config_origin = UNSET
        else:
            config_origin = ModelsConfigOrigin(_config_origin)

        _connected_state = d.pop("connectedState", UNSET)
        connected_state: Union[Unset, ModelsConnectedState]
        if isinstance(_connected_state, Unset):
            connected_state = UNSET
        else:
            connected_state = ModelsConnectedState(_connected_state)

        description = d.pop("description", UNSET)

        dns_addresses = cast(list[str], d.pop("dnsAddresses", UNSET))

        enabled = d.pop("enabled", UNSET)

        id = d.pop("id", UNSET)

        ipv_4_address = d.pop("ipv4Address", UNSET)

        _ipv_4_config_type = d.pop("ipv4ConfigType", UNSET)
        ipv_4_config_type: Union[Unset, ModelsConfigType]
        if isinstance(_ipv_4_config_type, Unset):
            ipv_4_config_type = UNSET
        else:
            ipv_4_config_type = ModelsConfigType(_ipv_4_config_type)

        ipv_4_gateway = d.pop("ipv4Gateway", UNSET)

        ipv_6_address = d.pop("ipv6Address", UNSET)

        _ipv_6_config_type = d.pop("ipv6ConfigType", UNSET)
        ipv_6_config_type: Union[Unset, ModelsConfigType]
        if isinstance(_ipv_6_config_type, Unset):
            ipv_6_config_type = UNSET
        else:
            ipv_6_config_type = ModelsConfigType(_ipv_6_config_type)

        ipv_6_gateway = d.pop("ipv6Gateway", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        no_proxy = cast(list[str], d.pop("noProxy", UNSET))

        node_id = d.pop("nodeId", UNSET)

        proxy_address = d.pop("proxyAddress", UNSET)

        proxy_credentials_id = d.pop("proxyCredentialsId", UNSET)

        proxy_password = d.pop("proxyPassword", UNSET)

        proxy_username = d.pop("proxyUsername", UNSET)

        set_proxy_password = d.pop("setProxyPassword", UNSET)

        models_management_port = cls(
            cloud_urls=cloud_urls,
            config_origin=config_origin,
            connected_state=connected_state,
            description=description,
            dns_addresses=dns_addresses,
            enabled=enabled,
            id=id,
            ipv_4_address=ipv_4_address,
            ipv_4_config_type=ipv_4_config_type,
            ipv_4_gateway=ipv_4_gateway,
            ipv_6_address=ipv_6_address,
            ipv_6_config_type=ipv_6_config_type,
            ipv_6_gateway=ipv_6_gateway,
            metadata=metadata,
            name=name,
            no_proxy=no_proxy,
            node_id=node_id,
            proxy_address=proxy_address,
            proxy_credentials_id=proxy_credentials_id,
            proxy_password=proxy_password,
            proxy_username=proxy_username,
            set_proxy_password=set_proxy_password,
        )

        models_management_port.additional_properties = d
        return models_management_port

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
