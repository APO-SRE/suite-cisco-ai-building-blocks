from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assertions_assert_type import AssertionsAssertType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_assert_bgp_peer_established import SchemaAssertBgpPeerEstablished
    from ..models.schema_assert_device_connected_to_cloud import SchemaAssertDeviceConnectedToCloud
    from ..models.schema_assert_device_connected_to_fabric import SchemaAssertDeviceConnectedToFabric
    from ..models.schema_assert_device_resource_usage_below_threshold import (
        SchemaAssertDeviceResourceUsageBelowThreshold,
    )
    from ..models.schema_assert_management_port_config_same import SchemaAssertManagementPortConfigSame
    from ..models.schema_assert_port_connection_speed_match import SchemaAssertPortConnectionSpeedMatch
    from ..models.schema_assert_port_expected_neighbor import SchemaAssertPortExpectedNeighbor
    from ..models.schema_assert_port_link_down import SchemaAssertPortLinkDown
    from ..models.schema_assert_port_link_up import SchemaAssertPortLinkUp
    from ..models.schema_assert_port_not_connected_to_fabric import SchemaAssertPortNotConnectedToFabric
    from ..models.schema_assert_port_speed_consistent import SchemaAssertPortSpeedConsistent
    from ..models.schema_assert_static_default_route_exists import SchemaAssertStaticDefaultRouteExists
    from ..models.schema_assert_vlan_has_traffic import SchemaAssertVlanHasTraffic


T = TypeVar("T", bound="AssertionsAssertion")


@_attrs_define
class AssertionsAssertion:
    """Description not available

    Attributes:
        assert_type (Union[Unset, AssertionsAssertType]): Description not available
        bgp_peer_established_data (Union[Unset, SchemaAssertBgpPeerEstablished]): Description not available
        device_connected_to_cloud (Union[Unset, SchemaAssertDeviceConnectedToCloud]): Description not available
        device_connected_to_fabric (Union[Unset, SchemaAssertDeviceConnectedToFabric]): Description not available
        device_resource_usage_below_threshold (Union[Unset, SchemaAssertDeviceResourceUsageBelowThreshold]): Description
            not available
        management_port_config_same (Union[Unset, SchemaAssertManagementPortConfigSame]): Description not available
        port_connection_speed_match (Union[Unset, SchemaAssertPortConnectionSpeedMatch]): Description not available
        port_expected_neighbor (Union[Unset, SchemaAssertPortExpectedNeighbor]): Description not available
        port_link_down (Union[Unset, SchemaAssertPortLinkDown]): Description not available
        port_link_up (Union[Unset, SchemaAssertPortLinkUp]): Description not available
        port_not_connected_to_fabric (Union[Unset, SchemaAssertPortNotConnectedToFabric]): Description not available
        port_speed_consistent (Union[Unset, SchemaAssertPortSpeedConsistent]): Description not available
        static_default_route_exists (Union[Unset, SchemaAssertStaticDefaultRouteExists]): Description not available
        vlan_has_traffic (Union[Unset, SchemaAssertVlanHasTraffic]): Description not available
    """

    assert_type: Union[Unset, AssertionsAssertType] = UNSET
    bgp_peer_established_data: Union[Unset, "SchemaAssertBgpPeerEstablished"] = UNSET
    device_connected_to_cloud: Union[Unset, "SchemaAssertDeviceConnectedToCloud"] = UNSET
    device_connected_to_fabric: Union[Unset, "SchemaAssertDeviceConnectedToFabric"] = UNSET
    device_resource_usage_below_threshold: Union[Unset, "SchemaAssertDeviceResourceUsageBelowThreshold"] = UNSET
    management_port_config_same: Union[Unset, "SchemaAssertManagementPortConfigSame"] = UNSET
    port_connection_speed_match: Union[Unset, "SchemaAssertPortConnectionSpeedMatch"] = UNSET
    port_expected_neighbor: Union[Unset, "SchemaAssertPortExpectedNeighbor"] = UNSET
    port_link_down: Union[Unset, "SchemaAssertPortLinkDown"] = UNSET
    port_link_up: Union[Unset, "SchemaAssertPortLinkUp"] = UNSET
    port_not_connected_to_fabric: Union[Unset, "SchemaAssertPortNotConnectedToFabric"] = UNSET
    port_speed_consistent: Union[Unset, "SchemaAssertPortSpeedConsistent"] = UNSET
    static_default_route_exists: Union[Unset, "SchemaAssertStaticDefaultRouteExists"] = UNSET
    vlan_has_traffic: Union[Unset, "SchemaAssertVlanHasTraffic"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assert_type: Union[Unset, str] = UNSET
        if not isinstance(self.assert_type, Unset):
            assert_type = self.assert_type.value

        bgp_peer_established_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bgp_peer_established_data, Unset):
            bgp_peer_established_data = self.bgp_peer_established_data.to_dict()

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
        if bgp_peer_established_data is not UNSET:
            field_dict["bgpPeerEstablishedData"] = bgp_peer_established_data
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
        from ..models.schema_assert_bgp_peer_established import SchemaAssertBgpPeerEstablished
        from ..models.schema_assert_device_connected_to_cloud import SchemaAssertDeviceConnectedToCloud
        from ..models.schema_assert_device_connected_to_fabric import SchemaAssertDeviceConnectedToFabric
        from ..models.schema_assert_device_resource_usage_below_threshold import (
            SchemaAssertDeviceResourceUsageBelowThreshold,
        )
        from ..models.schema_assert_management_port_config_same import SchemaAssertManagementPortConfigSame
        from ..models.schema_assert_port_connection_speed_match import SchemaAssertPortConnectionSpeedMatch
        from ..models.schema_assert_port_expected_neighbor import SchemaAssertPortExpectedNeighbor
        from ..models.schema_assert_port_link_down import SchemaAssertPortLinkDown
        from ..models.schema_assert_port_link_up import SchemaAssertPortLinkUp
        from ..models.schema_assert_port_not_connected_to_fabric import SchemaAssertPortNotConnectedToFabric
        from ..models.schema_assert_port_speed_consistent import SchemaAssertPortSpeedConsistent
        from ..models.schema_assert_static_default_route_exists import SchemaAssertStaticDefaultRouteExists
        from ..models.schema_assert_vlan_has_traffic import SchemaAssertVlanHasTraffic

        d = dict(src_dict)
        _assert_type = d.pop("assertType", UNSET)
        assert_type: Union[Unset, AssertionsAssertType]
        if isinstance(_assert_type, Unset):
            assert_type = UNSET
        else:
            assert_type = AssertionsAssertType(_assert_type)

        _bgp_peer_established_data = d.pop("bgpPeerEstablishedData", UNSET)
        bgp_peer_established_data: Union[Unset, SchemaAssertBgpPeerEstablished]
        if isinstance(_bgp_peer_established_data, Unset):
            bgp_peer_established_data = UNSET
        else:
            bgp_peer_established_data = SchemaAssertBgpPeerEstablished.from_dict(_bgp_peer_established_data)

        _device_connected_to_cloud = d.pop("deviceConnectedToCloud", UNSET)
        device_connected_to_cloud: Union[Unset, SchemaAssertDeviceConnectedToCloud]
        if isinstance(_device_connected_to_cloud, Unset):
            device_connected_to_cloud = UNSET
        else:
            device_connected_to_cloud = SchemaAssertDeviceConnectedToCloud.from_dict(_device_connected_to_cloud)

        _device_connected_to_fabric = d.pop("deviceConnectedToFabric", UNSET)
        device_connected_to_fabric: Union[Unset, SchemaAssertDeviceConnectedToFabric]
        if isinstance(_device_connected_to_fabric, Unset):
            device_connected_to_fabric = UNSET
        else:
            device_connected_to_fabric = SchemaAssertDeviceConnectedToFabric.from_dict(_device_connected_to_fabric)

        _device_resource_usage_below_threshold = d.pop("deviceResourceUsageBelowThreshold", UNSET)
        device_resource_usage_below_threshold: Union[Unset, SchemaAssertDeviceResourceUsageBelowThreshold]
        if isinstance(_device_resource_usage_below_threshold, Unset):
            device_resource_usage_below_threshold = UNSET
        else:
            device_resource_usage_below_threshold = SchemaAssertDeviceResourceUsageBelowThreshold.from_dict(
                _device_resource_usage_below_threshold
            )

        _management_port_config_same = d.pop("managementPortConfigSame", UNSET)
        management_port_config_same: Union[Unset, SchemaAssertManagementPortConfigSame]
        if isinstance(_management_port_config_same, Unset):
            management_port_config_same = UNSET
        else:
            management_port_config_same = SchemaAssertManagementPortConfigSame.from_dict(_management_port_config_same)

        _port_connection_speed_match = d.pop("portConnectionSpeedMatch", UNSET)
        port_connection_speed_match: Union[Unset, SchemaAssertPortConnectionSpeedMatch]
        if isinstance(_port_connection_speed_match, Unset):
            port_connection_speed_match = UNSET
        else:
            port_connection_speed_match = SchemaAssertPortConnectionSpeedMatch.from_dict(_port_connection_speed_match)

        _port_expected_neighbor = d.pop("portExpectedNeighbor", UNSET)
        port_expected_neighbor: Union[Unset, SchemaAssertPortExpectedNeighbor]
        if isinstance(_port_expected_neighbor, Unset):
            port_expected_neighbor = UNSET
        else:
            port_expected_neighbor = SchemaAssertPortExpectedNeighbor.from_dict(_port_expected_neighbor)

        _port_link_down = d.pop("portLinkDown", UNSET)
        port_link_down: Union[Unset, SchemaAssertPortLinkDown]
        if isinstance(_port_link_down, Unset):
            port_link_down = UNSET
        else:
            port_link_down = SchemaAssertPortLinkDown.from_dict(_port_link_down)

        _port_link_up = d.pop("portLinkUp", UNSET)
        port_link_up: Union[Unset, SchemaAssertPortLinkUp]
        if isinstance(_port_link_up, Unset):
            port_link_up = UNSET
        else:
            port_link_up = SchemaAssertPortLinkUp.from_dict(_port_link_up)

        _port_not_connected_to_fabric = d.pop("portNotConnectedToFabric", UNSET)
        port_not_connected_to_fabric: Union[Unset, SchemaAssertPortNotConnectedToFabric]
        if isinstance(_port_not_connected_to_fabric, Unset):
            port_not_connected_to_fabric = UNSET
        else:
            port_not_connected_to_fabric = SchemaAssertPortNotConnectedToFabric.from_dict(_port_not_connected_to_fabric)

        _port_speed_consistent = d.pop("portSpeedConsistent", UNSET)
        port_speed_consistent: Union[Unset, SchemaAssertPortSpeedConsistent]
        if isinstance(_port_speed_consistent, Unset):
            port_speed_consistent = UNSET
        else:
            port_speed_consistent = SchemaAssertPortSpeedConsistent.from_dict(_port_speed_consistent)

        _static_default_route_exists = d.pop("staticDefaultRouteExists", UNSET)
        static_default_route_exists: Union[Unset, SchemaAssertStaticDefaultRouteExists]
        if isinstance(_static_default_route_exists, Unset):
            static_default_route_exists = UNSET
        else:
            static_default_route_exists = SchemaAssertStaticDefaultRouteExists.from_dict(_static_default_route_exists)

        _vlan_has_traffic = d.pop("vlanHasTraffic", UNSET)
        vlan_has_traffic: Union[Unset, SchemaAssertVlanHasTraffic]
        if isinstance(_vlan_has_traffic, Unset):
            vlan_has_traffic = UNSET
        else:
            vlan_has_traffic = SchemaAssertVlanHasTraffic.from_dict(_vlan_has_traffic)

        assertions_assertion = cls(
            assert_type=assert_type,
            bgp_peer_established_data=bgp_peer_established_data,
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

        assertions_assertion.additional_properties = d
        return assertions_assertion

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
