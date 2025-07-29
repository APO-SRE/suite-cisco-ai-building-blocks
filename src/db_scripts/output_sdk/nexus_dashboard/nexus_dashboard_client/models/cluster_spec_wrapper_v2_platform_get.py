from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cluster_spec_wrapper_v2_platform_get_network_mode import ClusterSpecWrapperV2PlatformGETNetworkMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cluster_spec_network_v1_platform_get import ClusterSpecNetworkV1PlatformGET
    from ..models.cluster_spec_ntp_config_v2_platform_get import ClusterSpecNTPConfigV2PlatformGET
    from ..models.cluster_spec_proxy_config_v1_platform_get import ClusterSpecProxyConfigV1PlatformGET


T = TypeVar("T", bound="ClusterSpecWrapperV2PlatformGET")


@_attrs_define
class ClusterSpecWrapperV2PlatformGET:
    """
    Attributes:
        app_network (Union[Unset, ClusterSpecNetworkV1PlatformGET]): Cluster network subnet configuration
        display_name (Union[Unset, str]): Cluster Display name
        dns_domain (Union[Unset, str]): DNS domain
        name (Union[Unset, str]): Cluster name
        name_servers (Union[Unset, list[str]]): DNS name servers
        network_mode (Union[Unset, ClusterSpecWrapperV2PlatformGETNetworkMode]): Shows what IP protocols are configured
            on this cluster
        ntp_config (Union[Unset, ClusterSpecNTPConfigV2PlatformGET]): Cluster NTP config
        proxy_config (Union[Unset, ClusterSpecProxyConfigV1PlatformGET]): Cluster proxy server & ignorehosts config
        search_domains (Union[Unset, list[str]]): DNS search domains
        service_network (Union[Unset, ClusterSpecNetworkV1PlatformGET]): Cluster network subnet configuration
    """

    app_network: Union[Unset, "ClusterSpecNetworkV1PlatformGET"] = UNSET
    display_name: Union[Unset, str] = UNSET
    dns_domain: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    name_servers: Union[Unset, list[str]] = UNSET
    network_mode: Union[Unset, ClusterSpecWrapperV2PlatformGETNetworkMode] = UNSET
    ntp_config: Union[Unset, "ClusterSpecNTPConfigV2PlatformGET"] = UNSET
    proxy_config: Union[Unset, "ClusterSpecProxyConfigV1PlatformGET"] = UNSET
    search_domains: Union[Unset, list[str]] = UNSET
    service_network: Union[Unset, "ClusterSpecNetworkV1PlatformGET"] = UNSET
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

        ntp_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ntp_config, Unset):
            ntp_config = self.ntp_config.to_dict()

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
        if ntp_config is not UNSET:
            field_dict["ntpConfig"] = ntp_config
        if proxy_config is not UNSET:
            field_dict["proxyConfig"] = proxy_config
        if search_domains is not UNSET:
            field_dict["searchDomains"] = search_domains
        if service_network is not UNSET:
            field_dict["serviceNetwork"] = service_network

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cluster_spec_network_v1_platform_get import ClusterSpecNetworkV1PlatformGET
        from ..models.cluster_spec_ntp_config_v2_platform_get import ClusterSpecNTPConfigV2PlatformGET
        from ..models.cluster_spec_proxy_config_v1_platform_get import ClusterSpecProxyConfigV1PlatformGET

        d = dict(src_dict)
        _app_network = d.pop("appNetwork", UNSET)
        app_network: Union[Unset, ClusterSpecNetworkV1PlatformGET]
        if isinstance(_app_network, Unset):
            app_network = UNSET
        else:
            app_network = ClusterSpecNetworkV1PlatformGET.from_dict(_app_network)

        display_name = d.pop("displayName", UNSET)

        dns_domain = d.pop("dnsDomain", UNSET)

        name = d.pop("name", UNSET)

        name_servers = cast(list[str], d.pop("nameServers", UNSET))

        _network_mode = d.pop("networkMode", UNSET)
        network_mode: Union[Unset, ClusterSpecWrapperV2PlatformGETNetworkMode]
        if isinstance(_network_mode, Unset):
            network_mode = UNSET
        else:
            network_mode = ClusterSpecWrapperV2PlatformGETNetworkMode(_network_mode)

        _ntp_config = d.pop("ntpConfig", UNSET)
        ntp_config: Union[Unset, ClusterSpecNTPConfigV2PlatformGET]
        if isinstance(_ntp_config, Unset):
            ntp_config = UNSET
        else:
            ntp_config = ClusterSpecNTPConfigV2PlatformGET.from_dict(_ntp_config)

        _proxy_config = d.pop("proxyConfig", UNSET)
        proxy_config: Union[Unset, ClusterSpecProxyConfigV1PlatformGET]
        if isinstance(_proxy_config, Unset):
            proxy_config = UNSET
        else:
            proxy_config = ClusterSpecProxyConfigV1PlatformGET.from_dict(_proxy_config)

        search_domains = cast(list[str], d.pop("searchDomains", UNSET))

        _service_network = d.pop("serviceNetwork", UNSET)
        service_network: Union[Unset, ClusterSpecNetworkV1PlatformGET]
        if isinstance(_service_network, Unset):
            service_network = UNSET
        else:
            service_network = ClusterSpecNetworkV1PlatformGET.from_dict(_service_network)

        cluster_spec_wrapper_v2_platform_get = cls(
            app_network=app_network,
            display_name=display_name,
            dns_domain=dns_domain,
            name=name,
            name_servers=name_servers,
            network_mode=network_mode,
            ntp_config=ntp_config,
            proxy_config=proxy_config,
            search_domains=search_domains,
            service_network=service_network,
        )

        cluster_spec_wrapper_v2_platform_get.additional_properties = d
        return cluster_spec_wrapper_v2_platform_get

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
