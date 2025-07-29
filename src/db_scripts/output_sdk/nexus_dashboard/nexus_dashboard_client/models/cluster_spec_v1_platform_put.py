from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cluster_spec_v1_platform_put_network_mode import ClusterSpecV1PlatformPUTNetworkMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cluster_spec_network_v1_platform_put import ClusterSpecNetworkV1PlatformPUT
    from ..models.cluster_spec_proxy_config_v1_platform_put import ClusterSpecProxyConfigV1PlatformPUT


T = TypeVar("T", bound="ClusterSpecV1PlatformPUT")


@_attrs_define
class ClusterSpecV1PlatformPUT:
    """Cluster configuration

    Attributes:
        app_network (Union[Unset, ClusterSpecNetworkV1PlatformPUT]): Cluster network subnet configuration
        display_name (Union[Unset, str]): Cluster Display name
        dns_domain (Union[Unset, str]): DNS domain
        name (Union[Unset, str]): Cluster name
        name_servers (Union[Unset, list[str]]): DNS name servers
        network_mode (Union[Unset, ClusterSpecV1PlatformPUTNetworkMode]): Shows what IP protocols are configured on this
            cluster
        ntp_servers (Union[Unset, list[str]]): Cluster NTP servers
        proxy_config (Union[Unset, ClusterSpecProxyConfigV1PlatformPUT]): Cluster proxy server & ignorehosts config
        search_domains (Union[Unset, list[str]]): DNS search domains
        service_network (Union[Unset, ClusterSpecNetworkV1PlatformPUT]): Cluster network subnet configuration
    """

    app_network: Union[Unset, "ClusterSpecNetworkV1PlatformPUT"] = UNSET
    display_name: Union[Unset, str] = UNSET
    dns_domain: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    name_servers: Union[Unset, list[str]] = UNSET
    network_mode: Union[Unset, ClusterSpecV1PlatformPUTNetworkMode] = UNSET
    ntp_servers: Union[Unset, list[str]] = UNSET
    proxy_config: Union[Unset, "ClusterSpecProxyConfigV1PlatformPUT"] = UNSET
    search_domains: Union[Unset, list[str]] = UNSET
    service_network: Union[Unset, "ClusterSpecNetworkV1PlatformPUT"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_network: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app_network, Unset):
            app_network = self.app_network.to_dict()

        display_name = self.display_name

        dns_domain = self.dns_domain

        name = self.name

        name_servers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.name_servers, Unset):
            name_servers = self.name_servers

        network_mode: Union[Unset, str] = UNSET
        if not isinstance(self.network_mode, Unset):
            network_mode = self.network_mode.value

        ntp_servers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ntp_servers, Unset):
            ntp_servers = self.ntp_servers

        proxy_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.proxy_config, Unset):
            proxy_config = self.proxy_config.to_dict()

        search_domains: Union[Unset, list[str]] = UNSET
        if not isinstance(self.search_domains, Unset):
            search_domains = self.search_domains

        service_network: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.service_network, Unset):
            service_network = self.service_network.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_network is not UNSET:
            field_dict["appNetwork"] = app_network
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if dns_domain is not UNSET:
            field_dict["dnsDomain"] = dns_domain
        if name is not UNSET:
            field_dict["name"] = name
        if name_servers is not UNSET:
            field_dict["nameServers"] = name_servers
        if network_mode is not UNSET:
            field_dict["networkMode"] = network_mode
        if ntp_servers is not UNSET:
            field_dict["ntpServers"] = ntp_servers
        if proxy_config is not UNSET:
            field_dict["proxyConfig"] = proxy_config
        if search_domains is not UNSET:
            field_dict["searchDomains"] = search_domains
        if service_network is not UNSET:
            field_dict["serviceNetwork"] = service_network

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cluster_spec_network_v1_platform_put import ClusterSpecNetworkV1PlatformPUT
        from ..models.cluster_spec_proxy_config_v1_platform_put import ClusterSpecProxyConfigV1PlatformPUT

        d = dict(src_dict)
        _app_network = d.pop("appNetwork", UNSET)
        app_network: Union[Unset, ClusterSpecNetworkV1PlatformPUT]
        if isinstance(_app_network, Unset):
            app_network = UNSET
        else:
            app_network = ClusterSpecNetworkV1PlatformPUT.from_dict(_app_network)

        display_name = d.pop("displayName", UNSET)

        dns_domain = d.pop("dnsDomain", UNSET)

        name = d.pop("name", UNSET)

        name_servers = cast(list[str], d.pop("nameServers", UNSET))

        _network_mode = d.pop("networkMode", UNSET)
        network_mode: Union[Unset, ClusterSpecV1PlatformPUTNetworkMode]
        if isinstance(_network_mode, Unset):
            network_mode = UNSET
        else:
            network_mode = ClusterSpecV1PlatformPUTNetworkMode(_network_mode)

        ntp_servers = cast(list[str], d.pop("ntpServers", UNSET))

        _proxy_config = d.pop("proxyConfig", UNSET)
        proxy_config: Union[Unset, ClusterSpecProxyConfigV1PlatformPUT]
        if isinstance(_proxy_config, Unset):
            proxy_config = UNSET
        else:
            proxy_config = ClusterSpecProxyConfigV1PlatformPUT.from_dict(_proxy_config)

        search_domains = cast(list[str], d.pop("searchDomains", UNSET))

        _service_network = d.pop("serviceNetwork", UNSET)
        service_network: Union[Unset, ClusterSpecNetworkV1PlatformPUT]
        if isinstance(_service_network, Unset):
            service_network = UNSET
        else:
            service_network = ClusterSpecNetworkV1PlatformPUT.from_dict(_service_network)

        cluster_spec_v1_platform_put = cls(
            app_network=app_network,
            display_name=display_name,
            dns_domain=dns_domain,
            name=name,
            name_servers=name_servers,
            network_mode=network_mode,
            ntp_servers=ntp_servers,
            proxy_config=proxy_config,
            search_domains=search_domains,
            service_network=service_network,
        )

        cluster_spec_v1_platform_put.additional_properties = d
        return cluster_spec_v1_platform_put

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
