from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schema_path_schema_type import SchemaPathSchemaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaPathPathId")


@_attrs_define
class SchemaPathPathId:
    """PathId identifies the specific "schema coordinates" identifier of an object in the schema tree.

    Attributes:
        aggregated_device_claim (Union[Unset, str]): Description not available
        api_key (Union[Unset, str]): Description not available
        api_path (Union[Unset, str]): Description not available
        api_path_method (Union[Unset, str]): Description not available
        api_service_mapping (Union[Unset, int]): Description not available
        application (Union[Unset, int]): Description not available
        assert_bgp_peer_established (Union[Unset, int]): Description not available
        assert_config_bgp_peer_established (Union[Unset, int]): Description not available
        assert_config_device_connected_to_cloud (Union[Unset, int]): Description not available
        assert_config_device_connected_to_fabric (Union[Unset, int]): Description not available
        assert_config_device_env_fan_usage_below_threshold (Union[Unset, int]): Description not available
        assert_config_device_env_psu_usage_below_threshold (Union[Unset, int]): Description not available
        assert_config_device_env_temp_sensor_usage_below_threshold (Union[Unset, int]): Description not available
        assert_config_device_resource_usage_below_threshold (Union[Unset, int]): Description not available
        assert_config_expected_port_breakout_exists (Union[Unset, int]): Description not available
        assert_config_ipm_latency_below_threshold (Union[Unset, int]): Description not available
        assert_config_ipm_loss_below_threshold (Union[Unset, int]): Description not available
        assert_config_management_port_config_same (Union[Unset, int]): Description not available
        assert_config_port_channel_member_up (Union[Unset, int]): Description not available
        assert_config_port_connection_speed_match (Union[Unset, int]): Description not available
        assert_config_port_expected_neighbor (Union[Unset, int]): Description not available
        assert_config_port_link_down (Union[Unset, int]): Description not available
        assert_config_port_link_up (Union[Unset, int]): Description not available
        assert_config_port_not_connected_to_fabric (Union[Unset, int]): Description not available
        assert_config_port_speed_consistent (Union[Unset, int]): Description not available
        assert_config_port_vlan_stp_state_consistent (Union[Unset, int]): Description not available
        assert_config_static_default_route_exists (Union[Unset, int]): Description not available
        assert_config_sub_interface_down (Union[Unset, int]): Description not available
        assert_config_sub_interface_up (Union[Unset, int]): Description not available
        assert_config_vlan_has_traffic (Union[Unset, int]): Description not available
        assert_device_connected_to_cloud (Union[Unset, int]): Description not available
        assert_device_connected_to_fabric (Union[Unset, int]): Description not available
        assert_device_env_fan_usage_below_threshold (Union[Unset, int]): Description not available
        assert_device_env_psu_usage_below_threshold (Union[Unset, int]): Description not available
        assert_device_env_temp_sensor_usage_below_threshold (Union[Unset, int]): Description not available
        assert_device_resource_usage_below_threshold (Union[Unset, int]): Description not available
        assert_expected_port_breakout_exists (Union[Unset, int]): Description not available
        assert_ipm_latency_below_threshold (Union[Unset, int]): Description not available
        assert_ipm_loss_below_threshold (Union[Unset, int]): Description not available
        assert_management_port_config_same (Union[Unset, int]): Description not available
        assert_port_channel_member_up (Union[Unset, int]): Description not available
        assert_port_connection_speed_match (Union[Unset, int]): Description not available
        assert_port_expected_neighbor (Union[Unset, int]): Description not available
        assert_port_link_down (Union[Unset, int]): Description not available
        assert_port_link_up (Union[Unset, int]): Description not available
        assert_port_not_connected_to_fabric (Union[Unset, int]): Description not available
        assert_port_speed_consistent (Union[Unset, int]): Description not available
        assert_port_vlan_stp_state_consistent (Union[Unset, int]): Description not available
        assert_static_default_route_exists (Union[Unset, int]): Description not available
        assert_sub_interface_down (Union[Unset, int]): Description not available
        assert_sub_interface_up (Union[Unset, int]): Description not available
        assert_vlan_has_traffic (Union[Unset, int]): Description not available
        bearer_token (Union[Unset, str]): Description not available
        bgp_neighbor_family (Union[Unset, int]): Description not available
        bgp_neighbor_summary (Union[Unset, str]): Description not available
        bmc (Union[Unset, int]): Description not available
        bmc_config (Union[Unset, int]): Description not available
        breakout (Union[Unset, int]): Description not available
        claim_and_bind_task (Union[Unset, int]): Description not available
        dac_qsfp (Union[Unset, int]): Description not available
        deleted (Union[Unset, bool]): Indicates that this object was deleted.
        device (Union[Unset, str]): Description not available
        device_claim (Union[Unset, int]): Description not available
        device_connection (Union[Unset, int]): Description not available
        esi_info (Union[Unset, str]): Description not available
        esi_vtep_info (Union[Unset, str]): Description not available
        fabric (Union[Unset, str]): Description not available
        fabric_assignment_status (Union[Unset, str]): Description not available
        fabric_config (Union[Unset, str]): Description not available
        fabric_config_event (Union[Unset, int]): Description not available
        fabric_config_notification (Union[Unset, int]): Description not available
        fabric_connection_task (Union[Unset, int]): Description not available
        fabric_device (Union[Unset, str]): Description not available
        fabric_memory_usage (Union[Unset, str]): Description not available
        fabric_transaction (Union[Unset, str]): Description not available
        fabric_uuid (Union[Unset, str]): Description not available
        fan (Union[Unset, int]): Description not available
        fiber_qsfp (Union[Unset, int]): Description not available
        ip_next_hop (Union[Unset, int]): Description not available
        ip_prefix (Union[Unset, str]): Description not available
        ip_route_table (Union[Unset, str]): Description not available
        ipm_liveness_counters (Union[Unset, int]): Description not available
        ipm_proc_latency_counters (Union[Unset, int]): Description not available
        ipm_proc_loss_counters (Union[Unset, int]): Description not available
        ipm_raw_latency_counters (Union[Unset, int]): Description not available
        ipm_session_id (Union[Unset, str]): Description not available
        kubernetes_service_instance (Union[Unset, str]): Description not available
        l_2_fdb (Union[Unset, int]): Description not available
        l_2_mac (Union[Unset, str]): Description not available
        l_3_table (Union[Unset, str]): Description not available
        line_card (Union[Unset, int]): Description not available
        mac (Union[Unset, int]): Description not available
        management_config (Union[Unset, int]): Description not available
        management_state (Union[Unset, str]): Description not available
        manifest_partition_file_cache_status (Union[Unset, str]): Description not available
        manifest_running_image_status (Union[Unset, int]): Description not available
        negative_connection_task (Union[Unset, int]): Description not available
        node (Union[Unset, str]): Description not available
        node_breakout (Union[Unset, int]): Description not available
        node_config (Union[Unset, int]): Description not available
        node_line_card (Union[Unset, int]): Description not available
        node_port (Union[Unset, int]): Description not available
        org_service_proto (Union[Unset, str]): Description not available
        org_service_route (Union[Unset, int]): Description not available
        org_service_svc (Union[Unset, str]): Description not available
        org_to_cell_pair_mapping (Union[Unset, int]): Description not available
        org_uuid (Union[Unset, str]): Description not available
        path_string (Union[Unset, str]): Optional string representation of the schema path. Only populated on request.
        planned_config (Union[Unset, int]): Description not available
        port (Union[Unset, int]): Description not available
        port_channel_member_state (Union[Unset, str]): Description not available
        port_channel_state (Union[Unset, str]): Description not available
        port_config (Union[Unset, int]): Description not available
        port_counters (Union[Unset, int]): Description not available
        port_neighbor (Union[Unset, str]): Description not available
        port_setup_task (Union[Unset, int]): Description not available
        port_vlan (Union[Unset, str]): Description not available
        proc_table (Union[Unset, int]): Description not available
        proxy_connection_state (Union[Unset, str]): Description not available
        proxy_connection_stats (Union[Unset, int]): Description not available
        proxy_stats (Union[Unset, int]): Description not available
        psu (Union[Unset, int]): Description not available
        qsfp_dom_sensor (Union[Unset, int]): Description not available
        qsfp_dom_threshold (Union[Unset, int]): Description not available
        qsfp_info (Union[Unset, int]): Description not available
        rack_and_power_on_task (Union[Unset, int]): Description not available
        remedy_action (Union[Unset, str]): Description not available
        remote_vtep (Union[Unset, int]): Description not available
        resource_assignment (Union[Unset, str]): Description not available
        routed_interface_counters (Union[Unset, int]): Description not available
        server_temperature_sensor (Union[Unset, int]): Description not available
        server_voltage_sensor (Union[Unset, int]): Description not available
        service_instance_health (Union[Unset, str]): Description not available
        sextant_fabric_assignment (Union[Unset, str]): Description not available
        smart_nic_dpu (Union[Unset, int]): Description not available
        spyglass_broker_entry (Union[Unset, str]): Description not available
        spyglass_device (Union[Unset, str]): Description not available
        spyglass_ginger_entry (Union[Unset, int]): Description not available
        spyglass_ssh_session_entry (Union[Unset, int]): Description not available
        spyglass_tcp_listener (Union[Unset, int]): Description not available
        spyglass_tcp_session (Union[Unset, int]): Description not available
        stp_port_state (Union[Unset, str]): Description not available
        stp_vlan_port_state (Union[Unset, str]): Description not available
        stp_vlan_state (Union[Unset, int]): Description not available
        sub_interface (Union[Unset, int]): Description not available
        system_stats (Union[Unset, int]): Description not available
        temp_sensor (Union[Unset, int]): Description not available
        tenant_metadata (Union[Unset, int]): Description not available
        tenant_uuid (Union[Unset, str]): Description not available
        test_ip_address (Union[Unset, str]): Description not available
        test_ip_prefix (Union[Unset, str]): Description not available
        test_leaf_one (Union[Unset, str]): Description not available
        test_mac_address (Union[Unset, str]): Description not available
        test_mid_one (Union[Unset, int]): Description not available
        test_place_holder_1_secret (Union[Unset, int]): Description not available
        test_root_one (Union[Unset, str]): Description not available
        test_root_two (Union[Unset, str]): Description not available
        type_ (Union[Unset, SchemaPathSchemaType]): Description not available
        type_memory_usage (Union[Unset, int]): Description not available
        underlay_info (Union[Unset, int]): Description not available
        unknown_vlan (Union[Unset, int]): Description not available
        unknown_vlan_port (Union[Unset, str]): Description not available
        unpack_and_assemble_task (Union[Unset, int]): Description not available
        user_email (Union[Unset, str]): Description not available
        vlan_counters (Union[Unset, int]): Description not available
        vlan_state (Union[Unset, int]): Description not available
        vlan_vni_map (Union[Unset, int]): Description not available
        vni_port (Union[Unset, int]): Description not available
        vrf (Union[Unset, str]): Description not available
        vtep (Union[Unset, int]): Description not available
    """

    aggregated_device_claim: Union[Unset, str] = UNSET
    api_key: Union[Unset, str] = UNSET
    api_path: Union[Unset, str] = UNSET
    api_path_method: Union[Unset, str] = UNSET
    api_service_mapping: Union[Unset, int] = UNSET
    application: Union[Unset, int] = UNSET
    assert_bgp_peer_established: Union[Unset, int] = UNSET
    assert_config_bgp_peer_established: Union[Unset, int] = UNSET
    assert_config_device_connected_to_cloud: Union[Unset, int] = UNSET
    assert_config_device_connected_to_fabric: Union[Unset, int] = UNSET
    assert_config_device_env_fan_usage_below_threshold: Union[Unset, int] = UNSET
    assert_config_device_env_psu_usage_below_threshold: Union[Unset, int] = UNSET
    assert_config_device_env_temp_sensor_usage_below_threshold: Union[Unset, int] = UNSET
    assert_config_device_resource_usage_below_threshold: Union[Unset, int] = UNSET
    assert_config_expected_port_breakout_exists: Union[Unset, int] = UNSET
    assert_config_ipm_latency_below_threshold: Union[Unset, int] = UNSET
    assert_config_ipm_loss_below_threshold: Union[Unset, int] = UNSET
    assert_config_management_port_config_same: Union[Unset, int] = UNSET
    assert_config_port_channel_member_up: Union[Unset, int] = UNSET
    assert_config_port_connection_speed_match: Union[Unset, int] = UNSET
    assert_config_port_expected_neighbor: Union[Unset, int] = UNSET
    assert_config_port_link_down: Union[Unset, int] = UNSET
    assert_config_port_link_up: Union[Unset, int] = UNSET
    assert_config_port_not_connected_to_fabric: Union[Unset, int] = UNSET
    assert_config_port_speed_consistent: Union[Unset, int] = UNSET
    assert_config_port_vlan_stp_state_consistent: Union[Unset, int] = UNSET
    assert_config_static_default_route_exists: Union[Unset, int] = UNSET
    assert_config_sub_interface_down: Union[Unset, int] = UNSET
    assert_config_sub_interface_up: Union[Unset, int] = UNSET
    assert_config_vlan_has_traffic: Union[Unset, int] = UNSET
    assert_device_connected_to_cloud: Union[Unset, int] = UNSET
    assert_device_connected_to_fabric: Union[Unset, int] = UNSET
    assert_device_env_fan_usage_below_threshold: Union[Unset, int] = UNSET
    assert_device_env_psu_usage_below_threshold: Union[Unset, int] = UNSET
    assert_device_env_temp_sensor_usage_below_threshold: Union[Unset, int] = UNSET
    assert_device_resource_usage_below_threshold: Union[Unset, int] = UNSET
    assert_expected_port_breakout_exists: Union[Unset, int] = UNSET
    assert_ipm_latency_below_threshold: Union[Unset, int] = UNSET
    assert_ipm_loss_below_threshold: Union[Unset, int] = UNSET
    assert_management_port_config_same: Union[Unset, int] = UNSET
    assert_port_channel_member_up: Union[Unset, int] = UNSET
    assert_port_connection_speed_match: Union[Unset, int] = UNSET
    assert_port_expected_neighbor: Union[Unset, int] = UNSET
    assert_port_link_down: Union[Unset, int] = UNSET
    assert_port_link_up: Union[Unset, int] = UNSET
    assert_port_not_connected_to_fabric: Union[Unset, int] = UNSET
    assert_port_speed_consistent: Union[Unset, int] = UNSET
    assert_port_vlan_stp_state_consistent: Union[Unset, int] = UNSET
    assert_static_default_route_exists: Union[Unset, int] = UNSET
    assert_sub_interface_down: Union[Unset, int] = UNSET
    assert_sub_interface_up: Union[Unset, int] = UNSET
    assert_vlan_has_traffic: Union[Unset, int] = UNSET
    bearer_token: Union[Unset, str] = UNSET
    bgp_neighbor_family: Union[Unset, int] = UNSET
    bgp_neighbor_summary: Union[Unset, str] = UNSET
    bmc: Union[Unset, int] = UNSET
    bmc_config: Union[Unset, int] = UNSET
    breakout: Union[Unset, int] = UNSET
    claim_and_bind_task: Union[Unset, int] = UNSET
    dac_qsfp: Union[Unset, int] = UNSET
    deleted: Union[Unset, bool] = UNSET
    device: Union[Unset, str] = UNSET
    device_claim: Union[Unset, int] = UNSET
    device_connection: Union[Unset, int] = UNSET
    esi_info: Union[Unset, str] = UNSET
    esi_vtep_info: Union[Unset, str] = UNSET
    fabric: Union[Unset, str] = UNSET
    fabric_assignment_status: Union[Unset, str] = UNSET
    fabric_config: Union[Unset, str] = UNSET
    fabric_config_event: Union[Unset, int] = UNSET
    fabric_config_notification: Union[Unset, int] = UNSET
    fabric_connection_task: Union[Unset, int] = UNSET
    fabric_device: Union[Unset, str] = UNSET
    fabric_memory_usage: Union[Unset, str] = UNSET
    fabric_transaction: Union[Unset, str] = UNSET
    fabric_uuid: Union[Unset, str] = UNSET
    fan: Union[Unset, int] = UNSET
    fiber_qsfp: Union[Unset, int] = UNSET
    ip_next_hop: Union[Unset, int] = UNSET
    ip_prefix: Union[Unset, str] = UNSET
    ip_route_table: Union[Unset, str] = UNSET
    ipm_liveness_counters: Union[Unset, int] = UNSET
    ipm_proc_latency_counters: Union[Unset, int] = UNSET
    ipm_proc_loss_counters: Union[Unset, int] = UNSET
    ipm_raw_latency_counters: Union[Unset, int] = UNSET
    ipm_session_id: Union[Unset, str] = UNSET
    kubernetes_service_instance: Union[Unset, str] = UNSET
    l_2_fdb: Union[Unset, int] = UNSET
    l_2_mac: Union[Unset, str] = UNSET
    l_3_table: Union[Unset, str] = UNSET
    line_card: Union[Unset, int] = UNSET
    mac: Union[Unset, int] = UNSET
    management_config: Union[Unset, int] = UNSET
    management_state: Union[Unset, str] = UNSET
    manifest_partition_file_cache_status: Union[Unset, str] = UNSET
    manifest_running_image_status: Union[Unset, int] = UNSET
    negative_connection_task: Union[Unset, int] = UNSET
    node: Union[Unset, str] = UNSET
    node_breakout: Union[Unset, int] = UNSET
    node_config: Union[Unset, int] = UNSET
    node_line_card: Union[Unset, int] = UNSET
    node_port: Union[Unset, int] = UNSET
    org_service_proto: Union[Unset, str] = UNSET
    org_service_route: Union[Unset, int] = UNSET
    org_service_svc: Union[Unset, str] = UNSET
    org_to_cell_pair_mapping: Union[Unset, int] = UNSET
    org_uuid: Union[Unset, str] = UNSET
    path_string: Union[Unset, str] = UNSET
    planned_config: Union[Unset, int] = UNSET
    port: Union[Unset, int] = UNSET
    port_channel_member_state: Union[Unset, str] = UNSET
    port_channel_state: Union[Unset, str] = UNSET
    port_config: Union[Unset, int] = UNSET
    port_counters: Union[Unset, int] = UNSET
    port_neighbor: Union[Unset, str] = UNSET
    port_setup_task: Union[Unset, int] = UNSET
    port_vlan: Union[Unset, str] = UNSET
    proc_table: Union[Unset, int] = UNSET
    proxy_connection_state: Union[Unset, str] = UNSET
    proxy_connection_stats: Union[Unset, int] = UNSET
    proxy_stats: Union[Unset, int] = UNSET
    psu: Union[Unset, int] = UNSET
    qsfp_dom_sensor: Union[Unset, int] = UNSET
    qsfp_dom_threshold: Union[Unset, int] = UNSET
    qsfp_info: Union[Unset, int] = UNSET
    rack_and_power_on_task: Union[Unset, int] = UNSET
    remedy_action: Union[Unset, str] = UNSET
    remote_vtep: Union[Unset, int] = UNSET
    resource_assignment: Union[Unset, str] = UNSET
    routed_interface_counters: Union[Unset, int] = UNSET
    server_temperature_sensor: Union[Unset, int] = UNSET
    server_voltage_sensor: Union[Unset, int] = UNSET
    service_instance_health: Union[Unset, str] = UNSET
    sextant_fabric_assignment: Union[Unset, str] = UNSET
    smart_nic_dpu: Union[Unset, int] = UNSET
    spyglass_broker_entry: Union[Unset, str] = UNSET
    spyglass_device: Union[Unset, str] = UNSET
    spyglass_ginger_entry: Union[Unset, int] = UNSET
    spyglass_ssh_session_entry: Union[Unset, int] = UNSET
    spyglass_tcp_listener: Union[Unset, int] = UNSET
    spyglass_tcp_session: Union[Unset, int] = UNSET
    stp_port_state: Union[Unset, str] = UNSET
    stp_vlan_port_state: Union[Unset, str] = UNSET
    stp_vlan_state: Union[Unset, int] = UNSET
    sub_interface: Union[Unset, int] = UNSET
    system_stats: Union[Unset, int] = UNSET
    temp_sensor: Union[Unset, int] = UNSET
    tenant_metadata: Union[Unset, int] = UNSET
    tenant_uuid: Union[Unset, str] = UNSET
    test_ip_address: Union[Unset, str] = UNSET
    test_ip_prefix: Union[Unset, str] = UNSET
    test_leaf_one: Union[Unset, str] = UNSET
    test_mac_address: Union[Unset, str] = UNSET
    test_mid_one: Union[Unset, int] = UNSET
    test_place_holder_1_secret: Union[Unset, int] = UNSET
    test_root_one: Union[Unset, str] = UNSET
    test_root_two: Union[Unset, str] = UNSET
    type_: Union[Unset, SchemaPathSchemaType] = UNSET
    type_memory_usage: Union[Unset, int] = UNSET
    underlay_info: Union[Unset, int] = UNSET
    unknown_vlan: Union[Unset, int] = UNSET
    unknown_vlan_port: Union[Unset, str] = UNSET
    unpack_and_assemble_task: Union[Unset, int] = UNSET
    user_email: Union[Unset, str] = UNSET
    vlan_counters: Union[Unset, int] = UNSET
    vlan_state: Union[Unset, int] = UNSET
    vlan_vni_map: Union[Unset, int] = UNSET
    vni_port: Union[Unset, int] = UNSET
    vrf: Union[Unset, str] = UNSET
    vtep: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregated_device_claim = self.aggregated_device_claim

        api_key = self.api_key

        api_path = self.api_path

        api_path_method = self.api_path_method

        api_service_mapping = self.api_service_mapping

        application = self.application

        assert_bgp_peer_established = self.assert_bgp_peer_established

        assert_config_bgp_peer_established = self.assert_config_bgp_peer_established

        assert_config_device_connected_to_cloud = self.assert_config_device_connected_to_cloud

        assert_config_device_connected_to_fabric = self.assert_config_device_connected_to_fabric

        assert_config_device_env_fan_usage_below_threshold = self.assert_config_device_env_fan_usage_below_threshold

        assert_config_device_env_psu_usage_below_threshold = self.assert_config_device_env_psu_usage_below_threshold

        assert_config_device_env_temp_sensor_usage_below_threshold = (
            self.assert_config_device_env_temp_sensor_usage_below_threshold
        )

        assert_config_device_resource_usage_below_threshold = self.assert_config_device_resource_usage_below_threshold

        assert_config_expected_port_breakout_exists = self.assert_config_expected_port_breakout_exists

        assert_config_ipm_latency_below_threshold = self.assert_config_ipm_latency_below_threshold

        assert_config_ipm_loss_below_threshold = self.assert_config_ipm_loss_below_threshold

        assert_config_management_port_config_same = self.assert_config_management_port_config_same

        assert_config_port_channel_member_up = self.assert_config_port_channel_member_up

        assert_config_port_connection_speed_match = self.assert_config_port_connection_speed_match

        assert_config_port_expected_neighbor = self.assert_config_port_expected_neighbor

        assert_config_port_link_down = self.assert_config_port_link_down

        assert_config_port_link_up = self.assert_config_port_link_up

        assert_config_port_not_connected_to_fabric = self.assert_config_port_not_connected_to_fabric

        assert_config_port_speed_consistent = self.assert_config_port_speed_consistent

        assert_config_port_vlan_stp_state_consistent = self.assert_config_port_vlan_stp_state_consistent

        assert_config_static_default_route_exists = self.assert_config_static_default_route_exists

        assert_config_sub_interface_down = self.assert_config_sub_interface_down

        assert_config_sub_interface_up = self.assert_config_sub_interface_up

        assert_config_vlan_has_traffic = self.assert_config_vlan_has_traffic

        assert_device_connected_to_cloud = self.assert_device_connected_to_cloud

        assert_device_connected_to_fabric = self.assert_device_connected_to_fabric

        assert_device_env_fan_usage_below_threshold = self.assert_device_env_fan_usage_below_threshold

        assert_device_env_psu_usage_below_threshold = self.assert_device_env_psu_usage_below_threshold

        assert_device_env_temp_sensor_usage_below_threshold = self.assert_device_env_temp_sensor_usage_below_threshold

        assert_device_resource_usage_below_threshold = self.assert_device_resource_usage_below_threshold

        assert_expected_port_breakout_exists = self.assert_expected_port_breakout_exists

        assert_ipm_latency_below_threshold = self.assert_ipm_latency_below_threshold

        assert_ipm_loss_below_threshold = self.assert_ipm_loss_below_threshold

        assert_management_port_config_same = self.assert_management_port_config_same

        assert_port_channel_member_up = self.assert_port_channel_member_up

        assert_port_connection_speed_match = self.assert_port_connection_speed_match

        assert_port_expected_neighbor = self.assert_port_expected_neighbor

        assert_port_link_down = self.assert_port_link_down

        assert_port_link_up = self.assert_port_link_up

        assert_port_not_connected_to_fabric = self.assert_port_not_connected_to_fabric

        assert_port_speed_consistent = self.assert_port_speed_consistent

        assert_port_vlan_stp_state_consistent = self.assert_port_vlan_stp_state_consistent

        assert_static_default_route_exists = self.assert_static_default_route_exists

        assert_sub_interface_down = self.assert_sub_interface_down

        assert_sub_interface_up = self.assert_sub_interface_up

        assert_vlan_has_traffic = self.assert_vlan_has_traffic

        bearer_token = self.bearer_token

        bgp_neighbor_family = self.bgp_neighbor_family

        bgp_neighbor_summary = self.bgp_neighbor_summary

        bmc = self.bmc

        bmc_config = self.bmc_config

        breakout = self.breakout

        claim_and_bind_task = self.claim_and_bind_task

        dac_qsfp = self.dac_qsfp

        deleted = self.deleted

        device = self.device

        device_claim = self.device_claim

        device_connection = self.device_connection

        esi_info = self.esi_info

        esi_vtep_info = self.esi_vtep_info

        fabric = self.fabric

        fabric_assignment_status = self.fabric_assignment_status

        fabric_config = self.fabric_config

        fabric_config_event = self.fabric_config_event

        fabric_config_notification = self.fabric_config_notification

        fabric_connection_task = self.fabric_connection_task

        fabric_device = self.fabric_device

        fabric_memory_usage = self.fabric_memory_usage

        fabric_transaction = self.fabric_transaction

        fabric_uuid = self.fabric_uuid

        fan = self.fan

        fiber_qsfp = self.fiber_qsfp

        ip_next_hop = self.ip_next_hop

        ip_prefix = self.ip_prefix

        ip_route_table = self.ip_route_table

        ipm_liveness_counters = self.ipm_liveness_counters

        ipm_proc_latency_counters = self.ipm_proc_latency_counters

        ipm_proc_loss_counters = self.ipm_proc_loss_counters

        ipm_raw_latency_counters = self.ipm_raw_latency_counters

        ipm_session_id = self.ipm_session_id

        kubernetes_service_instance = self.kubernetes_service_instance

        l_2_fdb = self.l_2_fdb

        l_2_mac = self.l_2_mac

        l_3_table = self.l_3_table

        line_card = self.line_card

        mac = self.mac

        management_config = self.management_config

        management_state = self.management_state

        manifest_partition_file_cache_status = self.manifest_partition_file_cache_status

        manifest_running_image_status = self.manifest_running_image_status

        negative_connection_task = self.negative_connection_task

        node = self.node

        node_breakout = self.node_breakout

        node_config = self.node_config

        node_line_card = self.node_line_card

        node_port = self.node_port

        org_service_proto = self.org_service_proto

        org_service_route = self.org_service_route

        org_service_svc = self.org_service_svc

        org_to_cell_pair_mapping = self.org_to_cell_pair_mapping

        org_uuid = self.org_uuid

        path_string = self.path_string

        planned_config = self.planned_config

        port = self.port

        port_channel_member_state = self.port_channel_member_state

        port_channel_state = self.port_channel_state

        port_config = self.port_config

        port_counters = self.port_counters

        port_neighbor = self.port_neighbor

        port_setup_task = self.port_setup_task

        port_vlan = self.port_vlan

        proc_table = self.proc_table

        proxy_connection_state = self.proxy_connection_state

        proxy_connection_stats = self.proxy_connection_stats

        proxy_stats = self.proxy_stats

        psu = self.psu

        qsfp_dom_sensor = self.qsfp_dom_sensor

        qsfp_dom_threshold = self.qsfp_dom_threshold

        qsfp_info = self.qsfp_info

        rack_and_power_on_task = self.rack_and_power_on_task

        remedy_action = self.remedy_action

        remote_vtep = self.remote_vtep

        resource_assignment = self.resource_assignment

        routed_interface_counters = self.routed_interface_counters

        server_temperature_sensor = self.server_temperature_sensor

        server_voltage_sensor = self.server_voltage_sensor

        service_instance_health = self.service_instance_health

        sextant_fabric_assignment = self.sextant_fabric_assignment

        smart_nic_dpu = self.smart_nic_dpu

        spyglass_broker_entry = self.spyglass_broker_entry

        spyglass_device = self.spyglass_device

        spyglass_ginger_entry = self.spyglass_ginger_entry

        spyglass_ssh_session_entry = self.spyglass_ssh_session_entry

        spyglass_tcp_listener = self.spyglass_tcp_listener

        spyglass_tcp_session = self.spyglass_tcp_session

        stp_port_state = self.stp_port_state

        stp_vlan_port_state = self.stp_vlan_port_state

        stp_vlan_state = self.stp_vlan_state

        sub_interface = self.sub_interface

        system_stats = self.system_stats

        temp_sensor = self.temp_sensor

        tenant_metadata = self.tenant_metadata

        tenant_uuid = self.tenant_uuid

        test_ip_address = self.test_ip_address

        test_ip_prefix = self.test_ip_prefix

        test_leaf_one = self.test_leaf_one

        test_mac_address = self.test_mac_address

        test_mid_one = self.test_mid_one

        test_place_holder_1_secret = self.test_place_holder_1_secret

        test_root_one = self.test_root_one

        test_root_two = self.test_root_two

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        type_memory_usage = self.type_memory_usage

        underlay_info = self.underlay_info

        unknown_vlan = self.unknown_vlan

        unknown_vlan_port = self.unknown_vlan_port

        unpack_and_assemble_task = self.unpack_and_assemble_task

        user_email = self.user_email

        vlan_counters = self.vlan_counters

        vlan_state = self.vlan_state

        vlan_vni_map = self.vlan_vni_map

        vni_port = self.vni_port

        vrf = self.vrf

        vtep = self.vtep

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aggregated_device_claim is not UNSET:
            field_dict["aggregatedDeviceClaim"] = aggregated_device_claim
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if api_path is not UNSET:
            field_dict["apiPath"] = api_path
        if api_path_method is not UNSET:
            field_dict["apiPathMethod"] = api_path_method
        if api_service_mapping is not UNSET:
            field_dict["apiServiceMapping"] = api_service_mapping
        if application is not UNSET:
            field_dict["application"] = application
        if assert_bgp_peer_established is not UNSET:
            field_dict["assertBgpPeerEstablished"] = assert_bgp_peer_established
        if assert_config_bgp_peer_established is not UNSET:
            field_dict["assertConfigBgpPeerEstablished"] = assert_config_bgp_peer_established
        if assert_config_device_connected_to_cloud is not UNSET:
            field_dict["assertConfigDeviceConnectedToCloud"] = assert_config_device_connected_to_cloud
        if assert_config_device_connected_to_fabric is not UNSET:
            field_dict["assertConfigDeviceConnectedToFabric"] = assert_config_device_connected_to_fabric
        if assert_config_device_env_fan_usage_below_threshold is not UNSET:
            field_dict["assertConfigDeviceEnvFanUsageBelowThreshold"] = (
                assert_config_device_env_fan_usage_below_threshold
            )
        if assert_config_device_env_psu_usage_below_threshold is not UNSET:
            field_dict["assertConfigDeviceEnvPsuUsageBelowThreshold"] = (
                assert_config_device_env_psu_usage_below_threshold
            )
        if assert_config_device_env_temp_sensor_usage_below_threshold is not UNSET:
            field_dict["assertConfigDeviceEnvTempSensorUsageBelowThreshold"] = (
                assert_config_device_env_temp_sensor_usage_below_threshold
            )
        if assert_config_device_resource_usage_below_threshold is not UNSET:
            field_dict["assertConfigDeviceResourceUsageBelowThreshold"] = (
                assert_config_device_resource_usage_below_threshold
            )
        if assert_config_expected_port_breakout_exists is not UNSET:
            field_dict["assertConfigExpectedPortBreakoutExists"] = assert_config_expected_port_breakout_exists
        if assert_config_ipm_latency_below_threshold is not UNSET:
            field_dict["assertConfigIpmLatencyBelowThreshold"] = assert_config_ipm_latency_below_threshold
        if assert_config_ipm_loss_below_threshold is not UNSET:
            field_dict["assertConfigIpmLossBelowThreshold"] = assert_config_ipm_loss_below_threshold
        if assert_config_management_port_config_same is not UNSET:
            field_dict["assertConfigManagementPortConfigSame"] = assert_config_management_port_config_same
        if assert_config_port_channel_member_up is not UNSET:
            field_dict["assertConfigPortChannelMemberUp"] = assert_config_port_channel_member_up
        if assert_config_port_connection_speed_match is not UNSET:
            field_dict["assertConfigPortConnectionSpeedMatch"] = assert_config_port_connection_speed_match
        if assert_config_port_expected_neighbor is not UNSET:
            field_dict["assertConfigPortExpectedNeighbor"] = assert_config_port_expected_neighbor
        if assert_config_port_link_down is not UNSET:
            field_dict["assertConfigPortLinkDown"] = assert_config_port_link_down
        if assert_config_port_link_up is not UNSET:
            field_dict["assertConfigPortLinkUp"] = assert_config_port_link_up
        if assert_config_port_not_connected_to_fabric is not UNSET:
            field_dict["assertConfigPortNotConnectedToFabric"] = assert_config_port_not_connected_to_fabric
        if assert_config_port_speed_consistent is not UNSET:
            field_dict["assertConfigPortSpeedConsistent"] = assert_config_port_speed_consistent
        if assert_config_port_vlan_stp_state_consistent is not UNSET:
            field_dict["assertConfigPortVlanStpStateConsistent"] = assert_config_port_vlan_stp_state_consistent
        if assert_config_static_default_route_exists is not UNSET:
            field_dict["assertConfigStaticDefaultRouteExists"] = assert_config_static_default_route_exists
        if assert_config_sub_interface_down is not UNSET:
            field_dict["assertConfigSubInterfaceDown"] = assert_config_sub_interface_down
        if assert_config_sub_interface_up is not UNSET:
            field_dict["assertConfigSubInterfaceUp"] = assert_config_sub_interface_up
        if assert_config_vlan_has_traffic is not UNSET:
            field_dict["assertConfigVlanHasTraffic"] = assert_config_vlan_has_traffic
        if assert_device_connected_to_cloud is not UNSET:
            field_dict["assertDeviceConnectedToCloud"] = assert_device_connected_to_cloud
        if assert_device_connected_to_fabric is not UNSET:
            field_dict["assertDeviceConnectedToFabric"] = assert_device_connected_to_fabric
        if assert_device_env_fan_usage_below_threshold is not UNSET:
            field_dict["assertDeviceEnvFanUsageBelowThreshold"] = assert_device_env_fan_usage_below_threshold
        if assert_device_env_psu_usage_below_threshold is not UNSET:
            field_dict["assertDeviceEnvPsuUsageBelowThreshold"] = assert_device_env_psu_usage_below_threshold
        if assert_device_env_temp_sensor_usage_below_threshold is not UNSET:
            field_dict["assertDeviceEnvTempSensorUsageBelowThreshold"] = (
                assert_device_env_temp_sensor_usage_below_threshold
            )
        if assert_device_resource_usage_below_threshold is not UNSET:
            field_dict["assertDeviceResourceUsageBelowThreshold"] = assert_device_resource_usage_below_threshold
        if assert_expected_port_breakout_exists is not UNSET:
            field_dict["assertExpectedPortBreakoutExists"] = assert_expected_port_breakout_exists
        if assert_ipm_latency_below_threshold is not UNSET:
            field_dict["assertIpmLatencyBelowThreshold"] = assert_ipm_latency_below_threshold
        if assert_ipm_loss_below_threshold is not UNSET:
            field_dict["assertIpmLossBelowThreshold"] = assert_ipm_loss_below_threshold
        if assert_management_port_config_same is not UNSET:
            field_dict["assertManagementPortConfigSame"] = assert_management_port_config_same
        if assert_port_channel_member_up is not UNSET:
            field_dict["assertPortChannelMemberUp"] = assert_port_channel_member_up
        if assert_port_connection_speed_match is not UNSET:
            field_dict["assertPortConnectionSpeedMatch"] = assert_port_connection_speed_match
        if assert_port_expected_neighbor is not UNSET:
            field_dict["assertPortExpectedNeighbor"] = assert_port_expected_neighbor
        if assert_port_link_down is not UNSET:
            field_dict["assertPortLinkDown"] = assert_port_link_down
        if assert_port_link_up is not UNSET:
            field_dict["assertPortLinkUp"] = assert_port_link_up
        if assert_port_not_connected_to_fabric is not UNSET:
            field_dict["assertPortNotConnectedToFabric"] = assert_port_not_connected_to_fabric
        if assert_port_speed_consistent is not UNSET:
            field_dict["assertPortSpeedConsistent"] = assert_port_speed_consistent
        if assert_port_vlan_stp_state_consistent is not UNSET:
            field_dict["assertPortVlanStpStateConsistent"] = assert_port_vlan_stp_state_consistent
        if assert_static_default_route_exists is not UNSET:
            field_dict["assertStaticDefaultRouteExists"] = assert_static_default_route_exists
        if assert_sub_interface_down is not UNSET:
            field_dict["assertSubInterfaceDown"] = assert_sub_interface_down
        if assert_sub_interface_up is not UNSET:
            field_dict["assertSubInterfaceUp"] = assert_sub_interface_up
        if assert_vlan_has_traffic is not UNSET:
            field_dict["assertVlanHasTraffic"] = assert_vlan_has_traffic
        if bearer_token is not UNSET:
            field_dict["bearerToken"] = bearer_token
        if bgp_neighbor_family is not UNSET:
            field_dict["bgpNeighborFamily"] = bgp_neighbor_family
        if bgp_neighbor_summary is not UNSET:
            field_dict["bgpNeighborSummary"] = bgp_neighbor_summary
        if bmc is not UNSET:
            field_dict["bmc"] = bmc
        if bmc_config is not UNSET:
            field_dict["bmcConfig"] = bmc_config
        if breakout is not UNSET:
            field_dict["breakout"] = breakout
        if claim_and_bind_task is not UNSET:
            field_dict["claimAndBindTask"] = claim_and_bind_task
        if dac_qsfp is not UNSET:
            field_dict["dacQsfp"] = dac_qsfp
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if device is not UNSET:
            field_dict["device"] = device
        if device_claim is not UNSET:
            field_dict["deviceClaim"] = device_claim
        if device_connection is not UNSET:
            field_dict["deviceConnection"] = device_connection
        if esi_info is not UNSET:
            field_dict["esiInfo"] = esi_info
        if esi_vtep_info is not UNSET:
            field_dict["esiVtepInfo"] = esi_vtep_info
        if fabric is not UNSET:
            field_dict["fabric"] = fabric
        if fabric_assignment_status is not UNSET:
            field_dict["fabricAssignmentStatus"] = fabric_assignment_status
        if fabric_config is not UNSET:
            field_dict["fabricConfig"] = fabric_config
        if fabric_config_event is not UNSET:
            field_dict["fabricConfigEvent"] = fabric_config_event
        if fabric_config_notification is not UNSET:
            field_dict["fabricConfigNotification"] = fabric_config_notification
        if fabric_connection_task is not UNSET:
            field_dict["fabricConnectionTask"] = fabric_connection_task
        if fabric_device is not UNSET:
            field_dict["fabricDevice"] = fabric_device
        if fabric_memory_usage is not UNSET:
            field_dict["fabricMemoryUsage"] = fabric_memory_usage
        if fabric_transaction is not UNSET:
            field_dict["fabricTransaction"] = fabric_transaction
        if fabric_uuid is not UNSET:
            field_dict["fabricUuid"] = fabric_uuid
        if fan is not UNSET:
            field_dict["fan"] = fan
        if fiber_qsfp is not UNSET:
            field_dict["fiberQsfp"] = fiber_qsfp
        if ip_next_hop is not UNSET:
            field_dict["ipNextHop"] = ip_next_hop
        if ip_prefix is not UNSET:
            field_dict["ipPrefix"] = ip_prefix
        if ip_route_table is not UNSET:
            field_dict["ipRouteTable"] = ip_route_table
        if ipm_liveness_counters is not UNSET:
            field_dict["ipmLivenessCounters"] = ipm_liveness_counters
        if ipm_proc_latency_counters is not UNSET:
            field_dict["ipmProcLatencyCounters"] = ipm_proc_latency_counters
        if ipm_proc_loss_counters is not UNSET:
            field_dict["ipmProcLossCounters"] = ipm_proc_loss_counters
        if ipm_raw_latency_counters is not UNSET:
            field_dict["ipmRawLatencyCounters"] = ipm_raw_latency_counters
        if ipm_session_id is not UNSET:
            field_dict["ipmSessionId"] = ipm_session_id
        if kubernetes_service_instance is not UNSET:
            field_dict["kubernetesServiceInstance"] = kubernetes_service_instance
        if l_2_fdb is not UNSET:
            field_dict["l2Fdb"] = l_2_fdb
        if l_2_mac is not UNSET:
            field_dict["l2Mac"] = l_2_mac
        if l_3_table is not UNSET:
            field_dict["l3Table"] = l_3_table
        if line_card is not UNSET:
            field_dict["lineCard"] = line_card
        if mac is not UNSET:
            field_dict["mac"] = mac
        if management_config is not UNSET:
            field_dict["managementConfig"] = management_config
        if management_state is not UNSET:
            field_dict["managementState"] = management_state
        if manifest_partition_file_cache_status is not UNSET:
            field_dict["manifestPartitionFileCacheStatus"] = manifest_partition_file_cache_status
        if manifest_running_image_status is not UNSET:
            field_dict["manifestRunningImageStatus"] = manifest_running_image_status
        if negative_connection_task is not UNSET:
            field_dict["negativeConnectionTask"] = negative_connection_task
        if node is not UNSET:
            field_dict["node"] = node
        if node_breakout is not UNSET:
            field_dict["nodeBreakout"] = node_breakout
        if node_config is not UNSET:
            field_dict["nodeConfig"] = node_config
        if node_line_card is not UNSET:
            field_dict["nodeLineCard"] = node_line_card
        if node_port is not UNSET:
            field_dict["nodePort"] = node_port
        if org_service_proto is not UNSET:
            field_dict["orgServiceProto"] = org_service_proto
        if org_service_route is not UNSET:
            field_dict["orgServiceRoute"] = org_service_route
        if org_service_svc is not UNSET:
            field_dict["orgServiceSvc"] = org_service_svc
        if org_to_cell_pair_mapping is not UNSET:
            field_dict["orgToCellPairMapping"] = org_to_cell_pair_mapping
        if org_uuid is not UNSET:
            field_dict["orgUuid"] = org_uuid
        if path_string is not UNSET:
            field_dict["pathString"] = path_string
        if planned_config is not UNSET:
            field_dict["plannedConfig"] = planned_config
        if port is not UNSET:
            field_dict["port"] = port
        if port_channel_member_state is not UNSET:
            field_dict["portChannelMemberState"] = port_channel_member_state
        if port_channel_state is not UNSET:
            field_dict["portChannelState"] = port_channel_state
        if port_config is not UNSET:
            field_dict["portConfig"] = port_config
        if port_counters is not UNSET:
            field_dict["portCounters"] = port_counters
        if port_neighbor is not UNSET:
            field_dict["portNeighbor"] = port_neighbor
        if port_setup_task is not UNSET:
            field_dict["portSetupTask"] = port_setup_task
        if port_vlan is not UNSET:
            field_dict["portVlan"] = port_vlan
        if proc_table is not UNSET:
            field_dict["procTable"] = proc_table
        if proxy_connection_state is not UNSET:
            field_dict["proxyConnectionState"] = proxy_connection_state
        if proxy_connection_stats is not UNSET:
            field_dict["proxyConnectionStats"] = proxy_connection_stats
        if proxy_stats is not UNSET:
            field_dict["proxyStats"] = proxy_stats
        if psu is not UNSET:
            field_dict["psu"] = psu
        if qsfp_dom_sensor is not UNSET:
            field_dict["qsfpDomSensor"] = qsfp_dom_sensor
        if qsfp_dom_threshold is not UNSET:
            field_dict["qsfpDomThreshold"] = qsfp_dom_threshold
        if qsfp_info is not UNSET:
            field_dict["qsfpInfo"] = qsfp_info
        if rack_and_power_on_task is not UNSET:
            field_dict["rackAndPowerOnTask"] = rack_and_power_on_task
        if remedy_action is not UNSET:
            field_dict["remedyAction"] = remedy_action
        if remote_vtep is not UNSET:
            field_dict["remoteVtep"] = remote_vtep
        if resource_assignment is not UNSET:
            field_dict["resourceAssignment"] = resource_assignment
        if routed_interface_counters is not UNSET:
            field_dict["routedInterfaceCounters"] = routed_interface_counters
        if server_temperature_sensor is not UNSET:
            field_dict["serverTemperatureSensor"] = server_temperature_sensor
        if server_voltage_sensor is not UNSET:
            field_dict["serverVoltageSensor"] = server_voltage_sensor
        if service_instance_health is not UNSET:
            field_dict["serviceInstanceHealth"] = service_instance_health
        if sextant_fabric_assignment is not UNSET:
            field_dict["sextantFabricAssignment"] = sextant_fabric_assignment
        if smart_nic_dpu is not UNSET:
            field_dict["smartNicDpu"] = smart_nic_dpu
        if spyglass_broker_entry is not UNSET:
            field_dict["spyglassBrokerEntry"] = spyglass_broker_entry
        if spyglass_device is not UNSET:
            field_dict["spyglassDevice"] = spyglass_device
        if spyglass_ginger_entry is not UNSET:
            field_dict["spyglassGingerEntry"] = spyglass_ginger_entry
        if spyglass_ssh_session_entry is not UNSET:
            field_dict["spyglassSshSessionEntry"] = spyglass_ssh_session_entry
        if spyglass_tcp_listener is not UNSET:
            field_dict["spyglassTcpListener"] = spyglass_tcp_listener
        if spyglass_tcp_session is not UNSET:
            field_dict["spyglassTcpSession"] = spyglass_tcp_session
        if stp_port_state is not UNSET:
            field_dict["stpPortState"] = stp_port_state
        if stp_vlan_port_state is not UNSET:
            field_dict["stpVlanPortState"] = stp_vlan_port_state
        if stp_vlan_state is not UNSET:
            field_dict["stpVlanState"] = stp_vlan_state
        if sub_interface is not UNSET:
            field_dict["subInterface"] = sub_interface
        if system_stats is not UNSET:
            field_dict["systemStats"] = system_stats
        if temp_sensor is not UNSET:
            field_dict["tempSensor"] = temp_sensor
        if tenant_metadata is not UNSET:
            field_dict["tenantMetadata"] = tenant_metadata
        if tenant_uuid is not UNSET:
            field_dict["tenantUuid"] = tenant_uuid
        if test_ip_address is not UNSET:
            field_dict["testIpAddress"] = test_ip_address
        if test_ip_prefix is not UNSET:
            field_dict["testIpPrefix"] = test_ip_prefix
        if test_leaf_one is not UNSET:
            field_dict["testLeafOne"] = test_leaf_one
        if test_mac_address is not UNSET:
            field_dict["testMacAddress"] = test_mac_address
        if test_mid_one is not UNSET:
            field_dict["testMidOne"] = test_mid_one
        if test_place_holder_1_secret is not UNSET:
            field_dict["testPlaceHolder1Secret"] = test_place_holder_1_secret
        if test_root_one is not UNSET:
            field_dict["testRootOne"] = test_root_one
        if test_root_two is not UNSET:
            field_dict["testRootTwo"] = test_root_two
        if type_ is not UNSET:
            field_dict["type"] = type_
        if type_memory_usage is not UNSET:
            field_dict["typeMemoryUsage"] = type_memory_usage
        if underlay_info is not UNSET:
            field_dict["underlayInfo"] = underlay_info
        if unknown_vlan is not UNSET:
            field_dict["unknownVlan"] = unknown_vlan
        if unknown_vlan_port is not UNSET:
            field_dict["unknownVlanPort"] = unknown_vlan_port
        if unpack_and_assemble_task is not UNSET:
            field_dict["unpackAndAssembleTask"] = unpack_and_assemble_task
        if user_email is not UNSET:
            field_dict["userEmail"] = user_email
        if vlan_counters is not UNSET:
            field_dict["vlanCounters"] = vlan_counters
        if vlan_state is not UNSET:
            field_dict["vlanState"] = vlan_state
        if vlan_vni_map is not UNSET:
            field_dict["vlanVniMap"] = vlan_vni_map
        if vni_port is not UNSET:
            field_dict["vniPort"] = vni_port
        if vrf is not UNSET:
            field_dict["vrf"] = vrf
        if vtep is not UNSET:
            field_dict["vtep"] = vtep

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aggregated_device_claim = d.pop("aggregatedDeviceClaim", UNSET)

        api_key = d.pop("apiKey", UNSET)

        api_path = d.pop("apiPath", UNSET)

        api_path_method = d.pop("apiPathMethod", UNSET)

        api_service_mapping = d.pop("apiServiceMapping", UNSET)

        application = d.pop("application", UNSET)

        assert_bgp_peer_established = d.pop("assertBgpPeerEstablished", UNSET)

        assert_config_bgp_peer_established = d.pop("assertConfigBgpPeerEstablished", UNSET)

        assert_config_device_connected_to_cloud = d.pop("assertConfigDeviceConnectedToCloud", UNSET)

        assert_config_device_connected_to_fabric = d.pop("assertConfigDeviceConnectedToFabric", UNSET)

        assert_config_device_env_fan_usage_below_threshold = d.pop("assertConfigDeviceEnvFanUsageBelowThreshold", UNSET)

        assert_config_device_env_psu_usage_below_threshold = d.pop("assertConfigDeviceEnvPsuUsageBelowThreshold", UNSET)

        assert_config_device_env_temp_sensor_usage_below_threshold = d.pop(
            "assertConfigDeviceEnvTempSensorUsageBelowThreshold", UNSET
        )

        assert_config_device_resource_usage_below_threshold = d.pop(
            "assertConfigDeviceResourceUsageBelowThreshold", UNSET
        )

        assert_config_expected_port_breakout_exists = d.pop("assertConfigExpectedPortBreakoutExists", UNSET)

        assert_config_ipm_latency_below_threshold = d.pop("assertConfigIpmLatencyBelowThreshold", UNSET)

        assert_config_ipm_loss_below_threshold = d.pop("assertConfigIpmLossBelowThreshold", UNSET)

        assert_config_management_port_config_same = d.pop("assertConfigManagementPortConfigSame", UNSET)

        assert_config_port_channel_member_up = d.pop("assertConfigPortChannelMemberUp", UNSET)

        assert_config_port_connection_speed_match = d.pop("assertConfigPortConnectionSpeedMatch", UNSET)

        assert_config_port_expected_neighbor = d.pop("assertConfigPortExpectedNeighbor", UNSET)

        assert_config_port_link_down = d.pop("assertConfigPortLinkDown", UNSET)

        assert_config_port_link_up = d.pop("assertConfigPortLinkUp", UNSET)

        assert_config_port_not_connected_to_fabric = d.pop("assertConfigPortNotConnectedToFabric", UNSET)

        assert_config_port_speed_consistent = d.pop("assertConfigPortSpeedConsistent", UNSET)

        assert_config_port_vlan_stp_state_consistent = d.pop("assertConfigPortVlanStpStateConsistent", UNSET)

        assert_config_static_default_route_exists = d.pop("assertConfigStaticDefaultRouteExists", UNSET)

        assert_config_sub_interface_down = d.pop("assertConfigSubInterfaceDown", UNSET)

        assert_config_sub_interface_up = d.pop("assertConfigSubInterfaceUp", UNSET)

        assert_config_vlan_has_traffic = d.pop("assertConfigVlanHasTraffic", UNSET)

        assert_device_connected_to_cloud = d.pop("assertDeviceConnectedToCloud", UNSET)

        assert_device_connected_to_fabric = d.pop("assertDeviceConnectedToFabric", UNSET)

        assert_device_env_fan_usage_below_threshold = d.pop("assertDeviceEnvFanUsageBelowThreshold", UNSET)

        assert_device_env_psu_usage_below_threshold = d.pop("assertDeviceEnvPsuUsageBelowThreshold", UNSET)

        assert_device_env_temp_sensor_usage_below_threshold = d.pop(
            "assertDeviceEnvTempSensorUsageBelowThreshold", UNSET
        )

        assert_device_resource_usage_below_threshold = d.pop("assertDeviceResourceUsageBelowThreshold", UNSET)

        assert_expected_port_breakout_exists = d.pop("assertExpectedPortBreakoutExists", UNSET)

        assert_ipm_latency_below_threshold = d.pop("assertIpmLatencyBelowThreshold", UNSET)

        assert_ipm_loss_below_threshold = d.pop("assertIpmLossBelowThreshold", UNSET)

        assert_management_port_config_same = d.pop("assertManagementPortConfigSame", UNSET)

        assert_port_channel_member_up = d.pop("assertPortChannelMemberUp", UNSET)

        assert_port_connection_speed_match = d.pop("assertPortConnectionSpeedMatch", UNSET)

        assert_port_expected_neighbor = d.pop("assertPortExpectedNeighbor", UNSET)

        assert_port_link_down = d.pop("assertPortLinkDown", UNSET)

        assert_port_link_up = d.pop("assertPortLinkUp", UNSET)

        assert_port_not_connected_to_fabric = d.pop("assertPortNotConnectedToFabric", UNSET)

        assert_port_speed_consistent = d.pop("assertPortSpeedConsistent", UNSET)

        assert_port_vlan_stp_state_consistent = d.pop("assertPortVlanStpStateConsistent", UNSET)

        assert_static_default_route_exists = d.pop("assertStaticDefaultRouteExists", UNSET)

        assert_sub_interface_down = d.pop("assertSubInterfaceDown", UNSET)

        assert_sub_interface_up = d.pop("assertSubInterfaceUp", UNSET)

        assert_vlan_has_traffic = d.pop("assertVlanHasTraffic", UNSET)

        bearer_token = d.pop("bearerToken", UNSET)

        bgp_neighbor_family = d.pop("bgpNeighborFamily", UNSET)

        bgp_neighbor_summary = d.pop("bgpNeighborSummary", UNSET)

        bmc = d.pop("bmc", UNSET)

        bmc_config = d.pop("bmcConfig", UNSET)

        breakout = d.pop("breakout", UNSET)

        claim_and_bind_task = d.pop("claimAndBindTask", UNSET)

        dac_qsfp = d.pop("dacQsfp", UNSET)

        deleted = d.pop("deleted", UNSET)

        device = d.pop("device", UNSET)

        device_claim = d.pop("deviceClaim", UNSET)

        device_connection = d.pop("deviceConnection", UNSET)

        esi_info = d.pop("esiInfo", UNSET)

        esi_vtep_info = d.pop("esiVtepInfo", UNSET)

        fabric = d.pop("fabric", UNSET)

        fabric_assignment_status = d.pop("fabricAssignmentStatus", UNSET)

        fabric_config = d.pop("fabricConfig", UNSET)

        fabric_config_event = d.pop("fabricConfigEvent", UNSET)

        fabric_config_notification = d.pop("fabricConfigNotification", UNSET)

        fabric_connection_task = d.pop("fabricConnectionTask", UNSET)

        fabric_device = d.pop("fabricDevice", UNSET)

        fabric_memory_usage = d.pop("fabricMemoryUsage", UNSET)

        fabric_transaction = d.pop("fabricTransaction", UNSET)

        fabric_uuid = d.pop("fabricUuid", UNSET)

        fan = d.pop("fan", UNSET)

        fiber_qsfp = d.pop("fiberQsfp", UNSET)

        ip_next_hop = d.pop("ipNextHop", UNSET)

        ip_prefix = d.pop("ipPrefix", UNSET)

        ip_route_table = d.pop("ipRouteTable", UNSET)

        ipm_liveness_counters = d.pop("ipmLivenessCounters", UNSET)

        ipm_proc_latency_counters = d.pop("ipmProcLatencyCounters", UNSET)

        ipm_proc_loss_counters = d.pop("ipmProcLossCounters", UNSET)

        ipm_raw_latency_counters = d.pop("ipmRawLatencyCounters", UNSET)

        ipm_session_id = d.pop("ipmSessionId", UNSET)

        kubernetes_service_instance = d.pop("kubernetesServiceInstance", UNSET)

        l_2_fdb = d.pop("l2Fdb", UNSET)

        l_2_mac = d.pop("l2Mac", UNSET)

        l_3_table = d.pop("l3Table", UNSET)

        line_card = d.pop("lineCard", UNSET)

        mac = d.pop("mac", UNSET)

        management_config = d.pop("managementConfig", UNSET)

        management_state = d.pop("managementState", UNSET)

        manifest_partition_file_cache_status = d.pop("manifestPartitionFileCacheStatus", UNSET)

        manifest_running_image_status = d.pop("manifestRunningImageStatus", UNSET)

        negative_connection_task = d.pop("negativeConnectionTask", UNSET)

        node = d.pop("node", UNSET)

        node_breakout = d.pop("nodeBreakout", UNSET)

        node_config = d.pop("nodeConfig", UNSET)

        node_line_card = d.pop("nodeLineCard", UNSET)

        node_port = d.pop("nodePort", UNSET)

        org_service_proto = d.pop("orgServiceProto", UNSET)

        org_service_route = d.pop("orgServiceRoute", UNSET)

        org_service_svc = d.pop("orgServiceSvc", UNSET)

        org_to_cell_pair_mapping = d.pop("orgToCellPairMapping", UNSET)

        org_uuid = d.pop("orgUuid", UNSET)

        path_string = d.pop("pathString", UNSET)

        planned_config = d.pop("plannedConfig", UNSET)

        port = d.pop("port", UNSET)

        port_channel_member_state = d.pop("portChannelMemberState", UNSET)

        port_channel_state = d.pop("portChannelState", UNSET)

        port_config = d.pop("portConfig", UNSET)

        port_counters = d.pop("portCounters", UNSET)

        port_neighbor = d.pop("portNeighbor", UNSET)

        port_setup_task = d.pop("portSetupTask", UNSET)

        port_vlan = d.pop("portVlan", UNSET)

        proc_table = d.pop("procTable", UNSET)

        proxy_connection_state = d.pop("proxyConnectionState", UNSET)

        proxy_connection_stats = d.pop("proxyConnectionStats", UNSET)

        proxy_stats = d.pop("proxyStats", UNSET)

        psu = d.pop("psu", UNSET)

        qsfp_dom_sensor = d.pop("qsfpDomSensor", UNSET)

        qsfp_dom_threshold = d.pop("qsfpDomThreshold", UNSET)

        qsfp_info = d.pop("qsfpInfo", UNSET)

        rack_and_power_on_task = d.pop("rackAndPowerOnTask", UNSET)

        remedy_action = d.pop("remedyAction", UNSET)

        remote_vtep = d.pop("remoteVtep", UNSET)

        resource_assignment = d.pop("resourceAssignment", UNSET)

        routed_interface_counters = d.pop("routedInterfaceCounters", UNSET)

        server_temperature_sensor = d.pop("serverTemperatureSensor", UNSET)

        server_voltage_sensor = d.pop("serverVoltageSensor", UNSET)

        service_instance_health = d.pop("serviceInstanceHealth", UNSET)

        sextant_fabric_assignment = d.pop("sextantFabricAssignment", UNSET)

        smart_nic_dpu = d.pop("smartNicDpu", UNSET)

        spyglass_broker_entry = d.pop("spyglassBrokerEntry", UNSET)

        spyglass_device = d.pop("spyglassDevice", UNSET)

        spyglass_ginger_entry = d.pop("spyglassGingerEntry", UNSET)

        spyglass_ssh_session_entry = d.pop("spyglassSshSessionEntry", UNSET)

        spyglass_tcp_listener = d.pop("spyglassTcpListener", UNSET)

        spyglass_tcp_session = d.pop("spyglassTcpSession", UNSET)

        stp_port_state = d.pop("stpPortState", UNSET)

        stp_vlan_port_state = d.pop("stpVlanPortState", UNSET)

        stp_vlan_state = d.pop("stpVlanState", UNSET)

        sub_interface = d.pop("subInterface", UNSET)

        system_stats = d.pop("systemStats", UNSET)

        temp_sensor = d.pop("tempSensor", UNSET)

        tenant_metadata = d.pop("tenantMetadata", UNSET)

        tenant_uuid = d.pop("tenantUuid", UNSET)

        test_ip_address = d.pop("testIpAddress", UNSET)

        test_ip_prefix = d.pop("testIpPrefix", UNSET)

        test_leaf_one = d.pop("testLeafOne", UNSET)

        test_mac_address = d.pop("testMacAddress", UNSET)

        test_mid_one = d.pop("testMidOne", UNSET)

        test_place_holder_1_secret = d.pop("testPlaceHolder1Secret", UNSET)

        test_root_one = d.pop("testRootOne", UNSET)

        test_root_two = d.pop("testRootTwo", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, SchemaPathSchemaType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SchemaPathSchemaType(_type_)

        type_memory_usage = d.pop("typeMemoryUsage", UNSET)

        underlay_info = d.pop("underlayInfo", UNSET)

        unknown_vlan = d.pop("unknownVlan", UNSET)

        unknown_vlan_port = d.pop("unknownVlanPort", UNSET)

        unpack_and_assemble_task = d.pop("unpackAndAssembleTask", UNSET)

        user_email = d.pop("userEmail", UNSET)

        vlan_counters = d.pop("vlanCounters", UNSET)

        vlan_state = d.pop("vlanState", UNSET)

        vlan_vni_map = d.pop("vlanVniMap", UNSET)

        vni_port = d.pop("vniPort", UNSET)

        vrf = d.pop("vrf", UNSET)

        vtep = d.pop("vtep", UNSET)

        schema_path_path_id = cls(
            aggregated_device_claim=aggregated_device_claim,
            api_key=api_key,
            api_path=api_path,
            api_path_method=api_path_method,
            api_service_mapping=api_service_mapping,
            application=application,
            assert_bgp_peer_established=assert_bgp_peer_established,
            assert_config_bgp_peer_established=assert_config_bgp_peer_established,
            assert_config_device_connected_to_cloud=assert_config_device_connected_to_cloud,
            assert_config_device_connected_to_fabric=assert_config_device_connected_to_fabric,
            assert_config_device_env_fan_usage_below_threshold=assert_config_device_env_fan_usage_below_threshold,
            assert_config_device_env_psu_usage_below_threshold=assert_config_device_env_psu_usage_below_threshold,
            assert_config_device_env_temp_sensor_usage_below_threshold=assert_config_device_env_temp_sensor_usage_below_threshold,
            assert_config_device_resource_usage_below_threshold=assert_config_device_resource_usage_below_threshold,
            assert_config_expected_port_breakout_exists=assert_config_expected_port_breakout_exists,
            assert_config_ipm_latency_below_threshold=assert_config_ipm_latency_below_threshold,
            assert_config_ipm_loss_below_threshold=assert_config_ipm_loss_below_threshold,
            assert_config_management_port_config_same=assert_config_management_port_config_same,
            assert_config_port_channel_member_up=assert_config_port_channel_member_up,
            assert_config_port_connection_speed_match=assert_config_port_connection_speed_match,
            assert_config_port_expected_neighbor=assert_config_port_expected_neighbor,
            assert_config_port_link_down=assert_config_port_link_down,
            assert_config_port_link_up=assert_config_port_link_up,
            assert_config_port_not_connected_to_fabric=assert_config_port_not_connected_to_fabric,
            assert_config_port_speed_consistent=assert_config_port_speed_consistent,
            assert_config_port_vlan_stp_state_consistent=assert_config_port_vlan_stp_state_consistent,
            assert_config_static_default_route_exists=assert_config_static_default_route_exists,
            assert_config_sub_interface_down=assert_config_sub_interface_down,
            assert_config_sub_interface_up=assert_config_sub_interface_up,
            assert_config_vlan_has_traffic=assert_config_vlan_has_traffic,
            assert_device_connected_to_cloud=assert_device_connected_to_cloud,
            assert_device_connected_to_fabric=assert_device_connected_to_fabric,
            assert_device_env_fan_usage_below_threshold=assert_device_env_fan_usage_below_threshold,
            assert_device_env_psu_usage_below_threshold=assert_device_env_psu_usage_below_threshold,
            assert_device_env_temp_sensor_usage_below_threshold=assert_device_env_temp_sensor_usage_below_threshold,
            assert_device_resource_usage_below_threshold=assert_device_resource_usage_below_threshold,
            assert_expected_port_breakout_exists=assert_expected_port_breakout_exists,
            assert_ipm_latency_below_threshold=assert_ipm_latency_below_threshold,
            assert_ipm_loss_below_threshold=assert_ipm_loss_below_threshold,
            assert_management_port_config_same=assert_management_port_config_same,
            assert_port_channel_member_up=assert_port_channel_member_up,
            assert_port_connection_speed_match=assert_port_connection_speed_match,
            assert_port_expected_neighbor=assert_port_expected_neighbor,
            assert_port_link_down=assert_port_link_down,
            assert_port_link_up=assert_port_link_up,
            assert_port_not_connected_to_fabric=assert_port_not_connected_to_fabric,
            assert_port_speed_consistent=assert_port_speed_consistent,
            assert_port_vlan_stp_state_consistent=assert_port_vlan_stp_state_consistent,
            assert_static_default_route_exists=assert_static_default_route_exists,
            assert_sub_interface_down=assert_sub_interface_down,
            assert_sub_interface_up=assert_sub_interface_up,
            assert_vlan_has_traffic=assert_vlan_has_traffic,
            bearer_token=bearer_token,
            bgp_neighbor_family=bgp_neighbor_family,
            bgp_neighbor_summary=bgp_neighbor_summary,
            bmc=bmc,
            bmc_config=bmc_config,
            breakout=breakout,
            claim_and_bind_task=claim_and_bind_task,
            dac_qsfp=dac_qsfp,
            deleted=deleted,
            device=device,
            device_claim=device_claim,
            device_connection=device_connection,
            esi_info=esi_info,
            esi_vtep_info=esi_vtep_info,
            fabric=fabric,
            fabric_assignment_status=fabric_assignment_status,
            fabric_config=fabric_config,
            fabric_config_event=fabric_config_event,
            fabric_config_notification=fabric_config_notification,
            fabric_connection_task=fabric_connection_task,
            fabric_device=fabric_device,
            fabric_memory_usage=fabric_memory_usage,
            fabric_transaction=fabric_transaction,
            fabric_uuid=fabric_uuid,
            fan=fan,
            fiber_qsfp=fiber_qsfp,
            ip_next_hop=ip_next_hop,
            ip_prefix=ip_prefix,
            ip_route_table=ip_route_table,
            ipm_liveness_counters=ipm_liveness_counters,
            ipm_proc_latency_counters=ipm_proc_latency_counters,
            ipm_proc_loss_counters=ipm_proc_loss_counters,
            ipm_raw_latency_counters=ipm_raw_latency_counters,
            ipm_session_id=ipm_session_id,
            kubernetes_service_instance=kubernetes_service_instance,
            l_2_fdb=l_2_fdb,
            l_2_mac=l_2_mac,
            l_3_table=l_3_table,
            line_card=line_card,
            mac=mac,
            management_config=management_config,
            management_state=management_state,
            manifest_partition_file_cache_status=manifest_partition_file_cache_status,
            manifest_running_image_status=manifest_running_image_status,
            negative_connection_task=negative_connection_task,
            node=node,
            node_breakout=node_breakout,
            node_config=node_config,
            node_line_card=node_line_card,
            node_port=node_port,
            org_service_proto=org_service_proto,
            org_service_route=org_service_route,
            org_service_svc=org_service_svc,
            org_to_cell_pair_mapping=org_to_cell_pair_mapping,
            org_uuid=org_uuid,
            path_string=path_string,
            planned_config=planned_config,
            port=port,
            port_channel_member_state=port_channel_member_state,
            port_channel_state=port_channel_state,
            port_config=port_config,
            port_counters=port_counters,
            port_neighbor=port_neighbor,
            port_setup_task=port_setup_task,
            port_vlan=port_vlan,
            proc_table=proc_table,
            proxy_connection_state=proxy_connection_state,
            proxy_connection_stats=proxy_connection_stats,
            proxy_stats=proxy_stats,
            psu=psu,
            qsfp_dom_sensor=qsfp_dom_sensor,
            qsfp_dom_threshold=qsfp_dom_threshold,
            qsfp_info=qsfp_info,
            rack_and_power_on_task=rack_and_power_on_task,
            remedy_action=remedy_action,
            remote_vtep=remote_vtep,
            resource_assignment=resource_assignment,
            routed_interface_counters=routed_interface_counters,
            server_temperature_sensor=server_temperature_sensor,
            server_voltage_sensor=server_voltage_sensor,
            service_instance_health=service_instance_health,
            sextant_fabric_assignment=sextant_fabric_assignment,
            smart_nic_dpu=smart_nic_dpu,
            spyglass_broker_entry=spyglass_broker_entry,
            spyglass_device=spyglass_device,
            spyglass_ginger_entry=spyglass_ginger_entry,
            spyglass_ssh_session_entry=spyglass_ssh_session_entry,
            spyglass_tcp_listener=spyglass_tcp_listener,
            spyglass_tcp_session=spyglass_tcp_session,
            stp_port_state=stp_port_state,
            stp_vlan_port_state=stp_vlan_port_state,
            stp_vlan_state=stp_vlan_state,
            sub_interface=sub_interface,
            system_stats=system_stats,
            temp_sensor=temp_sensor,
            tenant_metadata=tenant_metadata,
            tenant_uuid=tenant_uuid,
            test_ip_address=test_ip_address,
            test_ip_prefix=test_ip_prefix,
            test_leaf_one=test_leaf_one,
            test_mac_address=test_mac_address,
            test_mid_one=test_mid_one,
            test_place_holder_1_secret=test_place_holder_1_secret,
            test_root_one=test_root_one,
            test_root_two=test_root_two,
            type_=type_,
            type_memory_usage=type_memory_usage,
            underlay_info=underlay_info,
            unknown_vlan=unknown_vlan,
            unknown_vlan_port=unknown_vlan_port,
            unpack_and_assemble_task=unpack_and_assemble_task,
            user_email=user_email,
            vlan_counters=vlan_counters,
            vlan_state=vlan_state,
            vlan_vni_map=vlan_vni_map,
            vni_port=vni_port,
            vrf=vrf,
            vtep=vtep,
        )

        schema_path_path_id.additional_properties = d
        return schema_path_path_id

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
