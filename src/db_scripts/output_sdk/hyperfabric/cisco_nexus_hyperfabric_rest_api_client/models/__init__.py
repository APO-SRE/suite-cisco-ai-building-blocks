"""Contains all the data models used in inputs/outputs"""

from .assertions_assert_type import AssertionsAssertType
from .assertions_assertion import AssertionsAssertion
from .auth_bearer_token import AuthBearerToken
from .auth_bearer_tokens_response import AuthBearerTokensResponse
from .auth_create_bearer_tokens_request import AuthCreateBearerTokensRequest
from .auth_create_bearer_tokens_response import AuthCreateBearerTokensResponse
from .auth_new_bearer_token import AuthNewBearerToken
from .auth_set_users_request import AuthSetUsersRequest
from .auth_update_user import AuthUpdateUser
from .auth_users_response import AuthUsersResponse
from .common_err_code import CommonErrCode
from .common_pagination_response import CommonPaginationResponse
from .common_rest_error import CommonRestError
from .config_activity_event import ConfigActivityEvent
from .config_add_fabric_connections_request import ConfigAddFabricConnectionsRequest
from .config_add_fabric_nodes_request import ConfigAddFabricNodesRequest
from .config_add_fabric_nodes_response import ConfigAddFabricNodesResponse
from .config_add_fabric_static_routes_request import ConfigAddFabricStaticRoutesRequest
from .config_add_fabric_vnis_request import ConfigAddFabricVnisRequest
from .config_add_fabric_vrfs_request import ConfigAddFabricVrfsRequest
from .config_add_fabrics_request import ConfigAddFabricsRequest
from .config_add_fabrics_response import ConfigAddFabricsResponse
from .config_add_management_ports_request import ConfigAddManagementPortsRequest
from .config_assertion import ConfigAssertion
from .config_assertions_response import ConfigAssertionsResponse
from .config_bind_device_response import ConfigBindDeviceResponse
from .config_candidate_review import ConfigCandidateReview
from .config_commit_fabric_candidate_request import ConfigCommitFabricCandidateRequest
from .config_commit_fabric_candidate_response import ConfigCommitFabricCandidateResponse
from .config_device import ConfigDevice
from .config_fabric import ConfigFabric
from .config_fabric_candidate import ConfigFabricCandidate
from .config_fabric_config import ConfigFabricConfig
from .config_fabric_connections_response import ConfigFabricConnectionsResponse
from .config_fabric_static_routes_response import ConfigFabricStaticRoutesResponse
from .config_fabric_vni_members_response import ConfigFabricVniMembersResponse
from .config_fabric_vnis_response import ConfigFabricVnisResponse
from .config_fabric_vrfs_response import ConfigFabricVrfsResponse
from .config_get_all_fabrics_response import ConfigGetAllFabricsResponse
from .config_get_devices_response import ConfigGetDevicesResponse
from .config_get_fabric_candidates_response import ConfigGetFabricCandidatesResponse
from .config_get_fabric_config_response import ConfigGetFabricConfigResponse
from .config_get_fabric_nodes_response import ConfigGetFabricNodesResponse
from .config_latch_assertions_request import ConfigLatchAssertionsRequest
from .config_latch_state import ConfigLatchState
from .config_management_ports_response import ConfigManagementPortsResponse
from .config_node import ConfigNode
from .config_ports_response import ConfigPortsResponse
from .config_review_fabric_candidate_request import ConfigReviewFabricCandidateRequest
from .config_review_fabric_candidate_response import ConfigReviewFabricCandidateResponse
from .config_set_fabric_connections_request import ConfigSetFabricConnectionsRequest
from .config_set_ports_request import ConfigSetPortsRequest
from .config_tenant_objects import ConfigTenantObjects
from .models_admin_state import ModelsAdminState
from .models_annotation import ModelsAnnotation
from .models_assert_category_type import ModelsAssertCategoryType
from .models_assert_state_type import ModelsAssertStateType
from .models_bgp_match_group import ModelsBgpMatchGroup
from .models_bgp_peer import ModelsBgpPeer
from .models_bgp_policy import ModelsBgpPolicy
from .models_bgp_rule import ModelsBgpRule
from .models_bgp_set_group import ModelsBgpSetGroup
from .models_community import ModelsCommunity
from .models_config_origin import ModelsConfigOrigin
from .models_config_type import ModelsConfigType
from .models_connected_state import ModelsConnectedState
from .models_data_type import ModelsDataType
from .models_dhcp_relay import ModelsDhcpRelay
from .models_fabric import ModelsFabric
from .models_fabric_topology import ModelsFabricTopology
from .models_fabric_type import ModelsFabricType
from .models_interface_stp import ModelsInterfaceStp
from .models_interface_type import ModelsInterfaceType
from .models_ip_prefix import ModelsIpPrefix
from .models_lacp_mode import ModelsLacpMode
from .models_loopback import ModelsLoopback
from .models_management_port import ModelsManagementPort
from .models_match_type import ModelsMatchType
from .models_metadata import ModelsMetadata
from .models_network_interface import ModelsNetworkInterface
from .models_network_port import ModelsNetworkPort
from .models_node import ModelsNode
from .models_node_role import ModelsNodeRole
from .models_node_type import ModelsNodeType
from .models_object_type import ModelsObjectType
from .models_operation import ModelsOperation
from .models_os_type import ModelsOsType
from .models_per_vlan_stp import ModelsPerVlanStp
from .models_port_breakout import ModelsPortBreakout
from .models_port_channel import ModelsPortChannel
from .models_port_connection import ModelsPortConnection
from .models_port_endpoint import ModelsPortEndpoint
from .models_port_role import ModelsPortRole
from .models_route_info import ModelsRouteInfo
from .models_route_origin_type import ModelsRouteOriginType
from .models_static_routes import ModelsStaticRoutes
from .models_sub_interface import ModelsSubInterface
from .models_svi import ModelsSvi
from .models_token_scope import ModelsTokenScope
from .models_user import ModelsUser
from .models_user_role import ModelsUserRole
from .models_vlan import ModelsVlan
from .models_vlan_member import ModelsVlanMember
from .models_vni import ModelsVni
from .models_vni_dhcp import ModelsVniDhcp
from .models_vrf import ModelsVrf
from .reader_assert_bgp_peer_established import ReaderAssertBgpPeerEstablished
from .reader_assert_config_added_to_db import ReaderAssertConfigAddedToDb
from .reader_assert_counter_report import ReaderAssertCounterReport
from .reader_assert_counter_report_response import ReaderAssertCounterReportResponse
from .reader_assert_device_connected_to_cloud import ReaderAssertDeviceConnectedToCloud
from .reader_assert_device_connected_to_fabric import ReaderAssertDeviceConnectedToFabric
from .reader_assert_device_resource_usage_below_threshold import ReaderAssertDeviceResourceUsageBelowThreshold
from .reader_assert_history_api_record import ReaderAssertHistoryApiRecord
from .reader_assert_history_api_record_response import ReaderAssertHistoryApiRecordResponse
from .reader_assert_management_port_config_same import ReaderAssertManagementPortConfigSame
from .reader_assert_port_connection_speed_match import ReaderAssertPortConnectionSpeedMatch
from .reader_assert_port_expected_neighbor import ReaderAssertPortExpectedNeighbor
from .reader_assert_port_link_down import ReaderAssertPortLinkDown
from .reader_assert_port_link_up import ReaderAssertPortLinkUp
from .reader_assert_port_not_connected_to_fabric import ReaderAssertPortNotConnectedToFabric
from .reader_assert_port_speed_consistent import ReaderAssertPortSpeedConsistent
from .reader_assert_static_default_route_exists import ReaderAssertStaticDefaultRouteExists
from .reader_assert_vlan_has_traffic import ReaderAssertVlanHasTraffic
from .schema_assert_bgp_peer_established import SchemaAssertBgpPeerEstablished
from .schema_assert_config_bgp_peer_established_data import SchemaAssertConfigBgpPeerEstablishedData
from .schema_assert_config_connected_port_speeds_match_data import SchemaAssertConfigConnectedPortSpeedsMatchData
from .schema_assert_config_connected_to_cloud_data import SchemaAssertConfigConnectedToCloudData
from .schema_assert_config_connected_to_fabric_data import SchemaAssertConfigConnectedToFabricData
from .schema_assert_config_device_resource_usage_below_threshold_data import (
    SchemaAssertConfigDeviceResourceUsageBelowThresholdData,
)
from .schema_assert_config_expected_neighbor_data import SchemaAssertConfigExpectedNeighborData
from .schema_assert_config_link_down_data import SchemaAssertConfigLinkDownData
from .schema_assert_config_link_up_data import SchemaAssertConfigLinkUpData
from .schema_assert_config_management_port_config_data import SchemaAssertConfigManagementPortConfigData
from .schema_assert_config_not_connected_to_fabric_data import SchemaAssertConfigNotConnectedToFabricData
from .schema_assert_config_port_speed_consistent_data import SchemaAssertConfigPortSpeedConsistentData
from .schema_assert_config_static_default_route_exists_data import SchemaAssertConfigStaticDefaultRouteExistsData
from .schema_assert_config_vlan_has_traffic_data import SchemaAssertConfigVlanHasTrafficData
from .schema_assert_device_connected_to_cloud import SchemaAssertDeviceConnectedToCloud
from .schema_assert_device_connected_to_fabric import SchemaAssertDeviceConnectedToFabric
from .schema_assert_device_resource_usage_below_threshold import SchemaAssertDeviceResourceUsageBelowThreshold
from .schema_assert_management_port_config_same import SchemaAssertManagementPortConfigSame
from .schema_assert_port_connection_speed_match import SchemaAssertPortConnectionSpeedMatch
from .schema_assert_port_expected_neighbor import SchemaAssertPortExpectedNeighbor
from .schema_assert_port_link_down import SchemaAssertPortLinkDown
from .schema_assert_port_link_up import SchemaAssertPortLinkUp
from .schema_assert_port_not_connected_to_fabric import SchemaAssertPortNotConnectedToFabric
from .schema_assert_port_speed_consistent import SchemaAssertPortSpeedConsistent
from .schema_assert_static_default_route_exists import SchemaAssertStaticDefaultRouteExists
from .schema_assert_vlan_has_traffic import SchemaAssertVlanHasTraffic
from .schema_basic_counters import SchemaBasicCounters
from .schema_dac_counters import SchemaDacCounters
from .schema_dns_config import SchemaDnsConfig
from .schema_drake_config import SchemaDrakeConfig
from .schema_env_led_status import SchemaEnvLedStatus
from .schema_env_status import SchemaEnvStatus
from .schema_fan import SchemaFan
from .schema_fan_direction import SchemaFanDirection
from .schema_management_state import SchemaManagementState
from .schema_operation_status import SchemaOperationStatus
from .schema_path_path_id import SchemaPathPathId
from .schema_path_schema_type import SchemaPathSchemaType
from .schema_port_config_details import SchemaPortConfigDetails
from .schema_port_counters import SchemaPortCounters
from .schema_proxy_config import SchemaProxyConfig
from .schema_psu import SchemaPsu
from .schema_sonic_config import SchemaSonicConfig
from .schema_system_stats import SchemaSystemStats
from .schema_temp_sensor import SchemaTempSensor
from .schema_vlan_counters import SchemaVlanCounters
from .state_assertions_response import StateAssertionsResponse
from .state_counter import StateCounter
from .state_counters_response import StateCountersResponse
from .state_device_management_ports_response import StateDeviceManagementPortsResponse
from .state_sensor import StateSensor
from .state_sensors_response import StateSensorsResponse

__all__ = (
    "AssertionsAssertion",
    "AssertionsAssertType",
    "AuthBearerToken",
    "AuthBearerTokensResponse",
    "AuthCreateBearerTokensRequest",
    "AuthCreateBearerTokensResponse",
    "AuthNewBearerToken",
    "AuthSetUsersRequest",
    "AuthUpdateUser",
    "AuthUsersResponse",
    "CommonErrCode",
    "CommonPaginationResponse",
    "CommonRestError",
    "ConfigActivityEvent",
    "ConfigAddFabricConnectionsRequest",
    "ConfigAddFabricNodesRequest",
    "ConfigAddFabricNodesResponse",
    "ConfigAddFabricsRequest",
    "ConfigAddFabricsResponse",
    "ConfigAddFabricStaticRoutesRequest",
    "ConfigAddFabricVnisRequest",
    "ConfigAddFabricVrfsRequest",
    "ConfigAddManagementPortsRequest",
    "ConfigAssertion",
    "ConfigAssertionsResponse",
    "ConfigBindDeviceResponse",
    "ConfigCandidateReview",
    "ConfigCommitFabricCandidateRequest",
    "ConfigCommitFabricCandidateResponse",
    "ConfigDevice",
    "ConfigFabric",
    "ConfigFabricCandidate",
    "ConfigFabricConfig",
    "ConfigFabricConnectionsResponse",
    "ConfigFabricStaticRoutesResponse",
    "ConfigFabricVniMembersResponse",
    "ConfigFabricVnisResponse",
    "ConfigFabricVrfsResponse",
    "ConfigGetAllFabricsResponse",
    "ConfigGetDevicesResponse",
    "ConfigGetFabricCandidatesResponse",
    "ConfigGetFabricConfigResponse",
    "ConfigGetFabricNodesResponse",
    "ConfigLatchAssertionsRequest",
    "ConfigLatchState",
    "ConfigManagementPortsResponse",
    "ConfigNode",
    "ConfigPortsResponse",
    "ConfigReviewFabricCandidateRequest",
    "ConfigReviewFabricCandidateResponse",
    "ConfigSetFabricConnectionsRequest",
    "ConfigSetPortsRequest",
    "ConfigTenantObjects",
    "ModelsAdminState",
    "ModelsAnnotation",
    "ModelsAssertCategoryType",
    "ModelsAssertStateType",
    "ModelsBgpMatchGroup",
    "ModelsBgpPeer",
    "ModelsBgpPolicy",
    "ModelsBgpRule",
    "ModelsBgpSetGroup",
    "ModelsCommunity",
    "ModelsConfigOrigin",
    "ModelsConfigType",
    "ModelsConnectedState",
    "ModelsDataType",
    "ModelsDhcpRelay",
    "ModelsFabric",
    "ModelsFabricTopology",
    "ModelsFabricType",
    "ModelsInterfaceStp",
    "ModelsInterfaceType",
    "ModelsIpPrefix",
    "ModelsLacpMode",
    "ModelsLoopback",
    "ModelsManagementPort",
    "ModelsMatchType",
    "ModelsMetadata",
    "ModelsNetworkInterface",
    "ModelsNetworkPort",
    "ModelsNode",
    "ModelsNodeRole",
    "ModelsNodeType",
    "ModelsObjectType",
    "ModelsOperation",
    "ModelsOsType",
    "ModelsPerVlanStp",
    "ModelsPortBreakout",
    "ModelsPortChannel",
    "ModelsPortConnection",
    "ModelsPortEndpoint",
    "ModelsPortRole",
    "ModelsRouteInfo",
    "ModelsRouteOriginType",
    "ModelsStaticRoutes",
    "ModelsSubInterface",
    "ModelsSvi",
    "ModelsTokenScope",
    "ModelsUser",
    "ModelsUserRole",
    "ModelsVlan",
    "ModelsVlanMember",
    "ModelsVni",
    "ModelsVniDhcp",
    "ModelsVrf",
    "ReaderAssertBgpPeerEstablished",
    "ReaderAssertConfigAddedToDb",
    "ReaderAssertCounterReport",
    "ReaderAssertCounterReportResponse",
    "ReaderAssertDeviceConnectedToCloud",
    "ReaderAssertDeviceConnectedToFabric",
    "ReaderAssertDeviceResourceUsageBelowThreshold",
    "ReaderAssertHistoryApiRecord",
    "ReaderAssertHistoryApiRecordResponse",
    "ReaderAssertManagementPortConfigSame",
    "ReaderAssertPortConnectionSpeedMatch",
    "ReaderAssertPortExpectedNeighbor",
    "ReaderAssertPortLinkDown",
    "ReaderAssertPortLinkUp",
    "ReaderAssertPortNotConnectedToFabric",
    "ReaderAssertPortSpeedConsistent",
    "ReaderAssertStaticDefaultRouteExists",
    "ReaderAssertVlanHasTraffic",
    "SchemaAssertBgpPeerEstablished",
    "SchemaAssertConfigBgpPeerEstablishedData",
    "SchemaAssertConfigConnectedPortSpeedsMatchData",
    "SchemaAssertConfigConnectedToCloudData",
    "SchemaAssertConfigConnectedToFabricData",
    "SchemaAssertConfigDeviceResourceUsageBelowThresholdData",
    "SchemaAssertConfigExpectedNeighborData",
    "SchemaAssertConfigLinkDownData",
    "SchemaAssertConfigLinkUpData",
    "SchemaAssertConfigManagementPortConfigData",
    "SchemaAssertConfigNotConnectedToFabricData",
    "SchemaAssertConfigPortSpeedConsistentData",
    "SchemaAssertConfigStaticDefaultRouteExistsData",
    "SchemaAssertConfigVlanHasTrafficData",
    "SchemaAssertDeviceConnectedToCloud",
    "SchemaAssertDeviceConnectedToFabric",
    "SchemaAssertDeviceResourceUsageBelowThreshold",
    "SchemaAssertManagementPortConfigSame",
    "SchemaAssertPortConnectionSpeedMatch",
    "SchemaAssertPortExpectedNeighbor",
    "SchemaAssertPortLinkDown",
    "SchemaAssertPortLinkUp",
    "SchemaAssertPortNotConnectedToFabric",
    "SchemaAssertPortSpeedConsistent",
    "SchemaAssertStaticDefaultRouteExists",
    "SchemaAssertVlanHasTraffic",
    "SchemaBasicCounters",
    "SchemaDacCounters",
    "SchemaDnsConfig",
    "SchemaDrakeConfig",
    "SchemaEnvLedStatus",
    "SchemaEnvStatus",
    "SchemaFan",
    "SchemaFanDirection",
    "SchemaManagementState",
    "SchemaOperationStatus",
    "SchemaPathPathId",
    "SchemaPathSchemaType",
    "SchemaPortConfigDetails",
    "SchemaPortCounters",
    "SchemaProxyConfig",
    "SchemaPsu",
    "SchemaSonicConfig",
    "SchemaSystemStats",
    "SchemaTempSensor",
    "SchemaVlanCounters",
    "StateAssertionsResponse",
    "StateCounter",
    "StateCountersResponse",
    "StateDeviceManagementPortsResponse",
    "StateSensor",
    "StateSensorsResponse",
)
