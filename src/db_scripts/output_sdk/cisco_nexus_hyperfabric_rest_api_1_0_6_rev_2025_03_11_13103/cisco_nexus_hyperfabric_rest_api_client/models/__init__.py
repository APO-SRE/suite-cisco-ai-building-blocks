"""Contains all the data models used in inputs/outputs"""

from .auth_bearer_token import AuthBearerToken
from .auth_bearer_tokens_response import AuthBearerTokensResponse
from .auth_create_bearer_tokens_request import AuthCreateBearerTokensRequest
from .auth_create_bearer_tokens_response import AuthCreateBearerTokensResponse
from .auth_get_users_roles import AuthGetUsersRoles
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
from .config_bind_device_response import ConfigBindDeviceResponse
from .config_candidate_review import ConfigCandidateReview
from .config_commit_fabric_candidate_request import ConfigCommitFabricCandidateRequest
from .config_commit_fabric_candidate_response import ConfigCommitFabricCandidateResponse
from .config_device import ConfigDevice
from .config_fabric import ConfigFabric
from .config_fabric_candidate import ConfigFabricCandidate
from .config_fabric_connections_response import ConfigFabricConnectionsResponse
from .config_fabric_static_routes_response import ConfigFabricStaticRoutesResponse
from .config_fabric_vni_members_response import ConfigFabricVniMembersResponse
from .config_fabric_vnis_response import ConfigFabricVnisResponse
from .config_fabric_vrfs_response import ConfigFabricVrfsResponse
from .config_get_all_fabrics_response import ConfigGetAllFabricsResponse
from .config_get_devices_response import ConfigGetDevicesResponse
from .config_get_fabric_candidates_response import ConfigGetFabricCandidatesResponse
from .config_get_fabric_nodes_response import ConfigGetFabricNodesResponse
from .config_management_ports_response import ConfigManagementPortsResponse
from .config_node import ConfigNode
from .config_ports_response import ConfigPortsResponse
from .config_review_fabric_candidate_request import ConfigReviewFabricCandidateRequest
from .config_review_fabric_candidate_response import ConfigReviewFabricCandidateResponse
from .config_set_fabric_connections_request import ConfigSetFabricConnectionsRequest
from .config_set_ports_request import ConfigSetPortsRequest
from .models_airflow_type import ModelsAirflowType
from .models_annotation import ModelsAnnotation
from .models_candidate_type import ModelsCandidateType
from .models_config_origin import ModelsConfigOrigin
from .models_config_type import ModelsConfigType
from .models_connected_state import ModelsConnectedState
from .models_data_type import ModelsDataType
from .models_fabric_topology import ModelsFabricTopology
from .models_interface_stp import ModelsInterfaceStp
from .models_interface_type import ModelsInterfaceType
from .models_management_port import ModelsManagementPort
from .models_metadata import ModelsMetadata
from .models_network_interface import ModelsNetworkInterface
from .models_network_port import ModelsNetworkPort
from .models_node_role import ModelsNodeRole
from .models_node_type import ModelsNodeType
from .models_object_type import ModelsObjectType
from .models_operation import ModelsOperation
from .models_os_type import ModelsOsType
from .models_port_connection import ModelsPortConnection
from .models_port_endpoint import ModelsPortEndpoint
from .models_port_role import ModelsPortRole
from .models_psu_airflow import ModelsPsuAirflow
from .models_route_info import ModelsRouteInfo
from .models_route_tag import ModelsRouteTag
from .models_static_routes import ModelsStaticRoutes
from .models_svi import ModelsSvi
from .models_token_scope import ModelsTokenScope
from .models_user import ModelsUser
from .models_user_role import ModelsUserRole
from .models_vlan_member import ModelsVlanMember
from .models_vni import ModelsVni
from .models_vrf import ModelsVrf

__all__ = (
    "AuthBearerToken",
    "AuthBearerTokensResponse",
    "AuthCreateBearerTokensRequest",
    "AuthCreateBearerTokensResponse",
    "AuthGetUsersRoles",
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
    "ConfigBindDeviceResponse",
    "ConfigCandidateReview",
    "ConfigCommitFabricCandidateRequest",
    "ConfigCommitFabricCandidateResponse",
    "ConfigDevice",
    "ConfigFabric",
    "ConfigFabricCandidate",
    "ConfigFabricConnectionsResponse",
    "ConfigFabricStaticRoutesResponse",
    "ConfigFabricVniMembersResponse",
    "ConfigFabricVnisResponse",
    "ConfigFabricVrfsResponse",
    "ConfigGetAllFabricsResponse",
    "ConfigGetDevicesResponse",
    "ConfigGetFabricCandidatesResponse",
    "ConfigGetFabricNodesResponse",
    "ConfigManagementPortsResponse",
    "ConfigNode",
    "ConfigPortsResponse",
    "ConfigReviewFabricCandidateRequest",
    "ConfigReviewFabricCandidateResponse",
    "ConfigSetFabricConnectionsRequest",
    "ConfigSetPortsRequest",
    "ModelsAirflowType",
    "ModelsAnnotation",
    "ModelsCandidateType",
    "ModelsConfigOrigin",
    "ModelsConfigType",
    "ModelsConnectedState",
    "ModelsDataType",
    "ModelsFabricTopology",
    "ModelsInterfaceStp",
    "ModelsInterfaceType",
    "ModelsManagementPort",
    "ModelsMetadata",
    "ModelsNetworkInterface",
    "ModelsNetworkPort",
    "ModelsNodeRole",
    "ModelsNodeType",
    "ModelsObjectType",
    "ModelsOperation",
    "ModelsOsType",
    "ModelsPortConnection",
    "ModelsPortEndpoint",
    "ModelsPortRole",
    "ModelsPsuAirflow",
    "ModelsRouteInfo",
    "ModelsRouteTag",
    "ModelsStaticRoutes",
    "ModelsSvi",
    "ModelsTokenScope",
    "ModelsUser",
    "ModelsUserRole",
    "ModelsVlanMember",
    "ModelsVni",
    "ModelsVrf",
)
