from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reader_assert_bgp_peer_established import ReaderAssertBgpPeerEstablished
    from ..models.reader_assert_config_added_to_db import ReaderAssertConfigAddedToDb
    from ..models.reader_assert_device_connected_to_cloud import ReaderAssertDeviceConnectedToCloud
    from ..models.reader_assert_device_connected_to_fabric import ReaderAssertDeviceConnectedToFabric
    from ..models.reader_assert_device_resource_usage_below_threshold import (
        ReaderAssertDeviceResourceUsageBelowThreshold,
    )
    from ..models.reader_assert_management_port_config_same import ReaderAssertManagementPortConfigSame
    from ..models.reader_assert_port_connection_speed_match import ReaderAssertPortConnectionSpeedMatch
    from ..models.reader_assert_port_expected_neighbor import ReaderAssertPortExpectedNeighbor
    from ..models.reader_assert_port_link_down import ReaderAssertPortLinkDown
    from ..models.reader_assert_port_link_up import ReaderAssertPortLinkUp
    from ..models.reader_assert_port_not_connected_to_fabric import ReaderAssertPortNotConnectedToFabric
    from ..models.reader_assert_port_speed_consistent import ReaderAssertPortSpeedConsistent
    from ..models.reader_assert_static_default_route_exists import ReaderAssertStaticDefaultRouteExists
    from ..models.reader_assert_vlan_has_traffic import ReaderAssertVlanHasTraffic


T = TypeVar("T", bound="ReaderAssertHistoryApiRecord")


@_attrs_define
class ReaderAssertHistoryApiRecord:
    """Description not available

    Attributes:
        assert_type (Union[Unset, str]): Description not available
        bgp_peer_established (Union[Unset, ReaderAssertBgpPeerEstablished]): Description not available
        config_added_to_db (Union[Unset, ReaderAssertConfigAddedToDb]): Description not available
        device_connected_to_cloud (Union[Unset, ReaderAssertDeviceConnectedToCloud]): Description not available
        device_connected_to_fabric (Union[Unset, ReaderAssertDeviceConnectedToFabric]): Description not available
        device_resource_usage_below_threshold (Union[Unset, ReaderAssertDeviceResourceUsageBelowThreshold]): Description
            not available
        management_port_config_same (Union[Unset, ReaderAssertManagementPortConfigSame]): Description not available
        port_connection_speed_match (Union[Unset, ReaderAssertPortConnectionSpeedMatch]): Description not available
        port_expected_neighbor (Union[Unset, ReaderAssertPortExpectedNeighbor]): Description not available
        port_link_down (Union[Unset, ReaderAssertPortLinkDown]): Description not available
        port_link_up (Union[Unset, ReaderAssertPortLinkUp]): Description not available
        port_not_connected_to_fabric (Union[Unset, ReaderAssertPortNotConnectedToFabric]): Description not available
        port_speed_consistent (Union[Unset, ReaderAssertPortSpeedConsistent]): Description not available
        static_default_route_exists (Union[Unset, ReaderAssertStaticDefaultRouteExists]): Description not available
        vlan_has_traffic (Union[Unset, ReaderAssertVlanHasTraffic]): Description not available
    """

    assert_type: Union[Unset, str] = UNSET
    bgp_peer_established: Union[Unset, "ReaderAssertBgpPeerEstablished"] = UNSET
    config_added_to_db: Union[Unset, "ReaderAssertConfigAddedToDb"] = UNSET
    device_connected_to_cloud: Union[Unset, "ReaderAssertDeviceConnectedToCloud"] = UNSET
    device_connected_to_fabric: Union[Unset, "ReaderAssertDeviceConnectedToFabric"] = UNSET
    device_resource_usage_below_threshold: Union[Unset, "ReaderAssertDeviceResourceUsageBelowThreshold"] = UNSET
    management_port_config_same: Union[Unset, "ReaderAssertManagementPortConfigSame"] = UNSET
    port_connection_speed_match: Union[Unset, "ReaderAssertPortConnectionSpeedMatch"] = UNSET
    port_expected_neighbor: Union[Unset, "ReaderAssertPortExpectedNeighbor"] = UNSET
    port_link_down: Union[Unset, "ReaderAssertPortLinkDown"] = UNSET
    port_link_up: Union[Unset, "ReaderAssertPortLinkUp"] = UNSET
    port_not_connected_to_fabric: Union[Unset, "ReaderAssertPortNotConnectedToFabric"] = UNSET
    port_speed_consistent: Union[Unset, "ReaderAssertPortSpeedConsistent"] = UNSET
    static_default_route_exists: Union[Unset, "ReaderAssertStaticDefaultRouteExists"] = UNSET
    vlan_has_traffic: Union[Unset, "ReaderAssertVlanHasTraffic"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assert_type = self.assert_type

        bgp_peer_established: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bgp_peer_established, Unset):
            bgp_peer_established = self.bgp_peer_established.to_dict()

        config_added_to_db: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.config_added_to_db, Unset):
            config_added_to_db = self.config_added_to_db.to_dict()

        device_connected_to_cloud: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.device_connected_to_cloud, Unset):
            device_connected_to_cloud = self.device_connected_to_cloud.to_dict()

        device_connected_to_fabric: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.device_connected_to_fabric, Unset):
            device_connected_to_fabric = self.device_connected_to_fabric.to_dict()

        device_resource_usage_below_threshold: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.device_resource_usage_below_threshold, Unset):
            device_resource_usage_below_threshold = self.device_resource_usage_below_threshold.to_dict()

        management_port_config_same: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.management_port_config_same, Unset):
            management_port_config_same = self.management_port_config_same.to_dict()

        port_connection_speed_match: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.port_connection_speed_match, Unset):
            port_connection_speed_match = self.port_connection_speed_match.to_dict()

        port_expected_neighbor: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.port_expected_neighbor, Unset):
            port_expected_neighbor = self.port_expected_neighbor.to_dict()

        port_link_down: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.port_link_down, Unset):
            port_link_down = self.port_link_down.to_dict()

        port_link_up: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.port_link_up, Unset):
            port_link_up = self.port_link_up.to_dict()

        port_not_connected_to_fabric: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.port_not_connected_to_fabric, Unset):
            port_not_connected_to_fabric = self.port_not_connected_to_fabric.to_dict()

        port_speed_consistent: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.port_speed_consistent, Unset):
            port_speed_consistent = self.port_speed_consistent.to_dict()

        static_default_route_exists: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.static_default_route_exists, Unset):
            static_default_route_exists = self.static_default_route_exists.to_dict()

        vlan_has_traffic: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vlan_has_traffic, Unset):
            vlan_has_traffic = self.vlan_has_traffic.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assert_type is not UNSET:
            field_dict["assertType"] = assert_type
        if bgp_peer_established is not UNSET:
            field_dict["bgpPeerEstablished"] = bgp_peer_established
        if config_added_to_db is not UNSET:
            field_dict["configAddedToDb"] = config_added_to_db
        if device_connected_to_cloud is not UNSET:
            field_dict["deviceConnectedToCloud"] = device_connected_to_cloud
        if device_connected_to_fabric is not UNSET:
            field_dict["deviceConnectedToFabric"] = device_connected_to_fabric
        if device_resource_usage_below_threshold is not UNSET:
            field_dict["deviceResourceUsageBelowThreshold"] = device_resource_usage_below_threshold
        if management_port_config_same is not UNSET:
            field_dict["managementPortConfigSame"] = management_port_config_same
        if port_connection_speed_match is not UNSET:
            field_dict["portConnectionSpeedMatch"] = port_connection_speed_match
        if port_expected_neighbor is not UNSET:
            field_dict["portExpectedNeighbor"] = port_expected_neighbor
        if port_link_down is not UNSET:
            field_dict["portLinkDown"] = port_link_down
        if port_link_up is not UNSET:
            field_dict["portLinkUp"] = port_link_up
        if port_not_connected_to_fabric is not UNSET:
            field_dict["portNotConnectedToFabric"] = port_not_connected_to_fabric
        if port_speed_consistent is not UNSET:
            field_dict["portSpeedConsistent"] = port_speed_consistent
        if static_default_route_exists is not UNSET:
            field_dict["staticDefaultRouteExists"] = static_default_route_exists
        if vlan_has_traffic is not UNSET:
            field_dict["vlanHasTraffic"] = vlan_has_traffic

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reader_assert_bgp_peer_established import ReaderAssertBgpPeerEstablished
        from ..models.reader_assert_config_added_to_db import ReaderAssertConfigAddedToDb
        from ..models.reader_assert_device_connected_to_cloud import ReaderAssertDeviceConnectedToCloud
        from ..models.reader_assert_device_connected_to_fabric import ReaderAssertDeviceConnectedToFabric
        from ..models.reader_assert_device_resource_usage_below_threshold import (
            ReaderAssertDeviceResourceUsageBelowThreshold,
        )
        from ..models.reader_assert_management_port_config_same import ReaderAssertManagementPortConfigSame
        from ..models.reader_assert_port_connection_speed_match import ReaderAssertPortConnectionSpeedMatch
        from ..models.reader_assert_port_expected_neighbor import ReaderAssertPortExpectedNeighbor
        from ..models.reader_assert_port_link_down import ReaderAssertPortLinkDown
        from ..models.reader_assert_port_link_up import ReaderAssertPortLinkUp
        from ..models.reader_assert_port_not_connected_to_fabric import ReaderAssertPortNotConnectedToFabric
        from ..models.reader_assert_port_speed_consistent import ReaderAssertPortSpeedConsistent
        from ..models.reader_assert_static_default_route_exists import ReaderAssertStaticDefaultRouteExists
        from ..models.reader_assert_vlan_has_traffic import ReaderAssertVlanHasTraffic

        d = dict(src_dict)
        assert_type = d.pop("assertType", UNSET)

        _bgp_peer_established = d.pop("bgpPeerEstablished", UNSET)
        bgp_peer_established: Union[Unset, ReaderAssertBgpPeerEstablished]
        if isinstance(_bgp_peer_established, Unset):
            bgp_peer_established = UNSET
        else:
            bgp_peer_established = ReaderAssertBgpPeerEstablished.from_dict(_bgp_peer_established)

        _config_added_to_db = d.pop("configAddedToDb", UNSET)
        config_added_to_db: Union[Unset, ReaderAssertConfigAddedToDb]
        if isinstance(_config_added_to_db, Unset):
            config_added_to_db = UNSET
        else:
            config_added_to_db = ReaderAssertConfigAddedToDb.from_dict(_config_added_to_db)

        _device_connected_to_cloud = d.pop("deviceConnectedToCloud", UNSET)
        device_connected_to_cloud: Union[Unset, ReaderAssertDeviceConnectedToCloud]
        if isinstance(_device_connected_to_cloud, Unset):
            device_connected_to_cloud = UNSET
        else:
            device_connected_to_cloud = ReaderAssertDeviceConnectedToCloud.from_dict(_device_connected_to_cloud)

        _device_connected_to_fabric = d.pop("deviceConnectedToFabric", UNSET)
        device_connected_to_fabric: Union[Unset, ReaderAssertDeviceConnectedToFabric]
        if isinstance(_device_connected_to_fabric, Unset):
            device_connected_to_fabric = UNSET
        else:
            device_connected_to_fabric = ReaderAssertDeviceConnectedToFabric.from_dict(_device_connected_to_fabric)

        _device_resource_usage_below_threshold = d.pop("deviceResourceUsageBelowThreshold", UNSET)
        device_resource_usage_below_threshold: Union[Unset, ReaderAssertDeviceResourceUsageBelowThreshold]
        if isinstance(_device_resource_usage_below_threshold, Unset):
            device_resource_usage_below_threshold = UNSET
        else:
            device_resource_usage_below_threshold = ReaderAssertDeviceResourceUsageBelowThreshold.from_dict(
                _device_resource_usage_below_threshold
            )

        _management_port_config_same = d.pop("managementPortConfigSame", UNSET)
        management_port_config_same: Union[Unset, ReaderAssertManagementPortConfigSame]
        if isinstance(_management_port_config_same, Unset):
            management_port_config_same = UNSET
        else:
            management_port_config_same = ReaderAssertManagementPortConfigSame.from_dict(_management_port_config_same)

        _port_connection_speed_match = d.pop("portConnectionSpeedMatch", UNSET)
        port_connection_speed_match: Union[Unset, ReaderAssertPortConnectionSpeedMatch]
        if isinstance(_port_connection_speed_match, Unset):
            port_connection_speed_match = UNSET
        else:
            port_connection_speed_match = ReaderAssertPortConnectionSpeedMatch.from_dict(_port_connection_speed_match)

        _port_expected_neighbor = d.pop("portExpectedNeighbor", UNSET)
        port_expected_neighbor: Union[Unset, ReaderAssertPortExpectedNeighbor]
        if isinstance(_port_expected_neighbor, Unset):
            port_expected_neighbor = UNSET
        else:
            port_expected_neighbor = ReaderAssertPortExpectedNeighbor.from_dict(_port_expected_neighbor)

        _port_link_down = d.pop("portLinkDown", UNSET)
        port_link_down: Union[Unset, ReaderAssertPortLinkDown]
        if isinstance(_port_link_down, Unset):
            port_link_down = UNSET
        else:
            port_link_down = ReaderAssertPortLinkDown.from_dict(_port_link_down)

        _port_link_up = d.pop("portLinkUp", UNSET)
        port_link_up: Union[Unset, ReaderAssertPortLinkUp]
        if isinstance(_port_link_up, Unset):
            port_link_up = UNSET
        else:
            port_link_up = ReaderAssertPortLinkUp.from_dict(_port_link_up)

        _port_not_connected_to_fabric = d.pop("portNotConnectedToFabric", UNSET)
        port_not_connected_to_fabric: Union[Unset, ReaderAssertPortNotConnectedToFabric]
        if isinstance(_port_not_connected_to_fabric, Unset):
            port_not_connected_to_fabric = UNSET
        else:
            port_not_connected_to_fabric = ReaderAssertPortNotConnectedToFabric.from_dict(_port_not_connected_to_fabric)

        _port_speed_consistent = d.pop("portSpeedConsistent", UNSET)
        port_speed_consistent: Union[Unset, ReaderAssertPortSpeedConsistent]
        if isinstance(_port_speed_consistent, Unset):
            port_speed_consistent = UNSET
        else:
            port_speed_consistent = ReaderAssertPortSpeedConsistent.from_dict(_port_speed_consistent)

        _static_default_route_exists = d.pop("staticDefaultRouteExists", UNSET)
        static_default_route_exists: Union[Unset, ReaderAssertStaticDefaultRouteExists]
        if isinstance(_static_default_route_exists, Unset):
            static_default_route_exists = UNSET
        else:
            static_default_route_exists = ReaderAssertStaticDefaultRouteExists.from_dict(_static_default_route_exists)

        _vlan_has_traffic = d.pop("vlanHasTraffic", UNSET)
        vlan_has_traffic: Union[Unset, ReaderAssertVlanHasTraffic]
        if isinstance(_vlan_has_traffic, Unset):
            vlan_has_traffic = UNSET
        else:
            vlan_has_traffic = ReaderAssertVlanHasTraffic.from_dict(_vlan_has_traffic)

        reader_assert_history_api_record = cls(
            assert_type=assert_type,
            bgp_peer_established=bgp_peer_established,
            config_added_to_db=config_added_to_db,
            device_connected_to_cloud=device_connected_to_cloud,
            device_connected_to_fabric=device_connected_to_fabric,
            device_resource_usage_below_threshold=device_resource_usage_below_threshold,
            management_port_config_same=management_port_config_same,
            port_connection_speed_match=port_connection_speed_match,
            port_expected_neighbor=port_expected_neighbor,
            port_link_down=port_link_down,
            port_link_up=port_link_up,
            port_not_connected_to_fabric=port_not_connected_to_fabric,
            port_speed_consistent=port_speed_consistent,
            static_default_route_exists=static_default_route_exists,
            vlan_has_traffic=vlan_has_traffic,
        )

        reader_assert_history_api_record.additional_properties = d
        return reader_assert_history_api_record

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
