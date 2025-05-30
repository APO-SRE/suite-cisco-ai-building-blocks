from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_bgp_peer import ModelsBgpPeer
    from ..models.models_bgp_policy import ModelsBgpPolicy
    from ..models.models_dhcp_relay import ModelsDhcpRelay
    from ..models.models_loopback import ModelsLoopback
    from ..models.models_port_channel import ModelsPortChannel
    from ..models.models_static_routes import ModelsStaticRoutes
    from ..models.models_sub_interface import ModelsSubInterface
    from ..models.models_vlan import ModelsVlan
    from ..models.models_vni import ModelsVni
    from ..models.models_vrf import ModelsVrf


T = TypeVar("T", bound="ConfigTenantObjects")


@_attrs_define
class ConfigTenantObjects:
    """TenantObjects defines an envelope to hold tenant objects.

    Attributes:
        bgp_peers (Union[Unset, list['ModelsBgpPeer']]): Description not available
        bgp_policies (Union[Unset, list['ModelsBgpPolicy']]): Description not available
        candidate (Union[Unset, str]): The transaction name.
        dhcp_relays (Union[Unset, list['ModelsDhcpRelay']]): Description not available
        enabled (Union[Unset, bool]): Description not available
        id (Union[Unset, str]): Description not available
        loopbacks (Union[Unset, list['ModelsLoopback']]): Description not available
        name (Union[Unset, str]): Description not available
        port_channels (Union[Unset, list['ModelsPortChannel']]): Description not available
        static_routes (Union[Unset, list['ModelsStaticRoutes']]): Description not available
        sub_interfaces (Union[Unset, list['ModelsSubInterface']]): Description not available
        vlans (Union[Unset, list['ModelsVlan']]): Description not available
        vnis (Union[Unset, list['ModelsVni']]): Description not available
        vrfs (Union[Unset, list['ModelsVrf']]): Description not available
    """

    bgp_peers: Union[Unset, list["ModelsBgpPeer"]] = UNSET
    bgp_policies: Union[Unset, list["ModelsBgpPolicy"]] = UNSET
    candidate: Union[Unset, str] = UNSET
    dhcp_relays: Union[Unset, list["ModelsDhcpRelay"]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    loopbacks: Union[Unset, list["ModelsLoopback"]] = UNSET
    name: Union[Unset, str] = UNSET
    port_channels: Union[Unset, list["ModelsPortChannel"]] = UNSET
    static_routes: Union[Unset, list["ModelsStaticRoutes"]] = UNSET
    sub_interfaces: Union[Unset, list["ModelsSubInterface"]] = UNSET
    vlans: Union[Unset, list["ModelsVlan"]] = UNSET
    vnis: Union[Unset, list["ModelsVni"]] = UNSET
    vrfs: Union[Unset, list["ModelsVrf"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bgp_peers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bgp_peers, Unset):
            bgp_peers = []
            for bgp_peers_item_data in self.bgp_peers:
                bgp_peers_item = bgp_peers_item_data.to_dict()
                bgp_peers.append(bgp_peers_item)

        bgp_policies: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bgp_policies, Unset):
            bgp_policies = []
            for bgp_policies_item_data in self.bgp_policies:
                bgp_policies_item = bgp_policies_item_data.to_dict()
                bgp_policies.append(bgp_policies_item)

        candidate = self.candidate

        dhcp_relays: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dhcp_relays, Unset):
            dhcp_relays = []
            for dhcp_relays_item_data in self.dhcp_relays:
                dhcp_relays_item = dhcp_relays_item_data.to_dict()
                dhcp_relays.append(dhcp_relays_item)

        enabled = self.enabled

        id = self.id

        loopbacks: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.loopbacks, Unset):
            loopbacks = []
            for loopbacks_item_data in self.loopbacks:
                loopbacks_item = loopbacks_item_data.to_dict()
                loopbacks.append(loopbacks_item)

        name = self.name

        port_channels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.port_channels, Unset):
            port_channels = []
            for port_channels_item_data in self.port_channels:
                port_channels_item = port_channels_item_data.to_dict()
                port_channels.append(port_channels_item)

        static_routes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.static_routes, Unset):
            static_routes = []
            for static_routes_item_data in self.static_routes:
                static_routes_item = static_routes_item_data.to_dict()
                static_routes.append(static_routes_item)

        sub_interfaces: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sub_interfaces, Unset):
            sub_interfaces = []
            for sub_interfaces_item_data in self.sub_interfaces:
                sub_interfaces_item = sub_interfaces_item_data.to_dict()
                sub_interfaces.append(sub_interfaces_item)

        vlans: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vlans, Unset):
            vlans = []
            for vlans_item_data in self.vlans:
                vlans_item = vlans_item_data.to_dict()
                vlans.append(vlans_item)

        vnis: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vnis, Unset):
            vnis = []
            for vnis_item_data in self.vnis:
                vnis_item = vnis_item_data.to_dict()
                vnis.append(vnis_item)

        vrfs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vrfs, Unset):
            vrfs = []
            for vrfs_item_data in self.vrfs:
                vrfs_item = vrfs_item_data.to_dict()
                vrfs.append(vrfs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bgp_peers is not UNSET:
            field_dict["bgpPeers"] = bgp_peers
        if bgp_policies is not UNSET:
            field_dict["bgpPolicies"] = bgp_policies
        if candidate is not UNSET:
            field_dict["candidate"] = candidate
        if dhcp_relays is not UNSET:
            field_dict["dhcpRelays"] = dhcp_relays
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if loopbacks is not UNSET:
            field_dict["loopbacks"] = loopbacks
        if name is not UNSET:
            field_dict["name"] = name
        if port_channels is not UNSET:
            field_dict["portChannels"] = port_channels
        if static_routes is not UNSET:
            field_dict["staticRoutes"] = static_routes
        if sub_interfaces is not UNSET:
            field_dict["subInterfaces"] = sub_interfaces
        if vlans is not UNSET:
            field_dict["vlans"] = vlans
        if vnis is not UNSET:
            field_dict["vnis"] = vnis
        if vrfs is not UNSET:
            field_dict["vrfs"] = vrfs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_bgp_peer import ModelsBgpPeer
        from ..models.models_bgp_policy import ModelsBgpPolicy
        from ..models.models_dhcp_relay import ModelsDhcpRelay
        from ..models.models_loopback import ModelsLoopback
        from ..models.models_port_channel import ModelsPortChannel
        from ..models.models_static_routes import ModelsStaticRoutes
        from ..models.models_sub_interface import ModelsSubInterface
        from ..models.models_vlan import ModelsVlan
        from ..models.models_vni import ModelsVni
        from ..models.models_vrf import ModelsVrf

        d = dict(src_dict)
        bgp_peers = []
        _bgp_peers = d.pop("bgpPeers", UNSET)
        for bgp_peers_item_data in _bgp_peers or []:
            bgp_peers_item = ModelsBgpPeer.from_dict(bgp_peers_item_data)

            bgp_peers.append(bgp_peers_item)

        bgp_policies = []
        _bgp_policies = d.pop("bgpPolicies", UNSET)
        for bgp_policies_item_data in _bgp_policies or []:
            bgp_policies_item = ModelsBgpPolicy.from_dict(bgp_policies_item_data)

            bgp_policies.append(bgp_policies_item)

        candidate = d.pop("candidate", UNSET)

        dhcp_relays = []
        _dhcp_relays = d.pop("dhcpRelays", UNSET)
        for dhcp_relays_item_data in _dhcp_relays or []:
            dhcp_relays_item = ModelsDhcpRelay.from_dict(dhcp_relays_item_data)

            dhcp_relays.append(dhcp_relays_item)

        enabled = d.pop("enabled", UNSET)

        id = d.pop("id", UNSET)

        loopbacks = []
        _loopbacks = d.pop("loopbacks", UNSET)
        for loopbacks_item_data in _loopbacks or []:
            loopbacks_item = ModelsLoopback.from_dict(loopbacks_item_data)

            loopbacks.append(loopbacks_item)

        name = d.pop("name", UNSET)

        port_channels = []
        _port_channels = d.pop("portChannels", UNSET)
        for port_channels_item_data in _port_channels or []:
            port_channels_item = ModelsPortChannel.from_dict(port_channels_item_data)

            port_channels.append(port_channels_item)

        static_routes = []
        _static_routes = d.pop("staticRoutes", UNSET)
        for static_routes_item_data in _static_routes or []:
            static_routes_item = ModelsStaticRoutes.from_dict(static_routes_item_data)

            static_routes.append(static_routes_item)

        sub_interfaces = []
        _sub_interfaces = d.pop("subInterfaces", UNSET)
        for sub_interfaces_item_data in _sub_interfaces or []:
            sub_interfaces_item = ModelsSubInterface.from_dict(sub_interfaces_item_data)

            sub_interfaces.append(sub_interfaces_item)

        vlans = []
        _vlans = d.pop("vlans", UNSET)
        for vlans_item_data in _vlans or []:
            vlans_item = ModelsVlan.from_dict(vlans_item_data)

            vlans.append(vlans_item)

        vnis = []
        _vnis = d.pop("vnis", UNSET)
        for vnis_item_data in _vnis or []:
            vnis_item = ModelsVni.from_dict(vnis_item_data)

            vnis.append(vnis_item)

        vrfs = []
        _vrfs = d.pop("vrfs", UNSET)
        for vrfs_item_data in _vrfs or []:
            vrfs_item = ModelsVrf.from_dict(vrfs_item_data)

            vrfs.append(vrfs_item)

        config_tenant_objects = cls(
            bgp_peers=bgp_peers,
            bgp_policies=bgp_policies,
            candidate=candidate,
            dhcp_relays=dhcp_relays,
            enabled=enabled,
            id=id,
            loopbacks=loopbacks,
            name=name,
            port_channels=port_channels,
            static_routes=static_routes,
            sub_interfaces=sub_interfaces,
            vlans=vlans,
            vnis=vnis,
            vrfs=vrfs,
        )

        config_tenant_objects.additional_properties = d
        return config_tenant_objects

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
