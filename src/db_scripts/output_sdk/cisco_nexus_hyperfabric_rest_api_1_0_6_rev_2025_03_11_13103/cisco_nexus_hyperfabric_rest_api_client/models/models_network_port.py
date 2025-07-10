from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_port_role import ModelsPortRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_annotation import ModelsAnnotation
    from ..models.models_interface_stp import ModelsInterfaceStp
    from ..models.models_metadata import ModelsMetadata


T = TypeVar("T", bound="ModelsNetworkPort")


@_attrs_define
class ModelsNetworkPort:
    """A Port encapsulates the configuration and properties of a front panel network interface of a node used as fabric
    port to interconnect with other nodes, as routed port to peer at Layer 3 with external devices, as Link Aggregation
    Group member or as a host port to connect to other endpoints via Layer 2 (VLAN).

        Attributes:
            annotations (Union[Unset, list['ModelsAnnotation']]): A list of name-value annotations to store user-defined
                data including complex data such as JSON associated with the port.
            breakout (Union[Unset, bool]): This is a read-only field. The flag that indicates if the port is in breakout
                mode or not.
            breakout_index (Union[Unset, int]): This is a read-only field. The index number of the breakout in the parent
                port. The breakout index is not set when the port is not in breakout mode.
            description (Union[Unset, str]): The description is a user-defined field to store notes about the port.
            enabled (Union[Unset, bool]): The enabled state of the port which indicates if the port is enabled or disabled.
            fec (Union[Unset, str]): The Forward Error Correction (FEC) mode of the port. Supported modes are "rs" and
                "none". The FEC must be set to "none" for 100G DR/FR/LR pluggable optics.
            force_counter (Union[Unset, int]): The Force Counter can be incremented to force the port configuration to be
                forcefully reapplied when there are no other configuration changes such as to recover (un-shut) a port blocked
                by STP.
            id (Union[Unset, str]): This is a read-only field. The unique identifier of the port.
            index (Union[Unset, int]): This is a read-only field. The index number of the port on the linecard.
            ipv_4_addresses (Union[Unset, list[str]]): A list of up to two IPv4 host addresses with subnet mask to be
                configured on the port. Requires the `ROUTED_PORT` role to be configured in roles and the port to be associated
                with a VRF.
            ipv_6_addresses (Union[Unset, list[str]]): A list of up to two IPv6 host addresses with subnet mask to be
                configured on the port. Requires the `ROUTED_PORT` role to be configured in roles and the port to be associated
                with a VRF.
            labels (Union[Unset, list[str]]): A list of user-defined labels that can be used for grouping and filtering
                ports.
            linecard (Union[Unset, int]): This is a read-only field. The index number of the linecard to which this port
                belongs to.
            link_down (Union[Unset, bool]): Prevent traffic from being forwarded by the port. Requires `enabled` to be set
                to `true` (equivalent to `Admin State` set to `Up`) and role to be one of `UNUSED_PORT`, `ROUTED_PORT` or
                `HOST_PORT`.
            max_speed (Union[Unset, str]): This is a read-only field. The maximum speed of the port as reported by the
                system (E.g. 10G).
            metadata (Union[Unset, ModelsMetadata]): Metadata defines a map of attributes related to the lifecycle of the
                object.
            mtu (Union[Unset, int]): The Maximum Transmission Unit (MTU) of the port of the node. Default value is 9100. The
                MTU value must be between 1500 and 9100.
            name (Union[Unset, str]): The name of the port of the node. The name must have a prefix of Ethernet (E.g.
                Ethernet1_1) and cannot be modified.
            node_id (Union[Unset, str]): This is a read-only field. The unique identifier of the node to which this port
                belongs to.
            pluggable (Union[Unset, str]): The name of the model (PID) of the pluggable cable or optic expected to be used
                in the port.
            roles (Union[Unset, list[ModelsPortRole]]): A list of roles of the port. The port roles list is mandatory, and
                must contain exactly one role.
            speed (Union[Unset, str]): The configurable speed mode of the port (E.g. 10G). The port speed cannot be set for
                a port in breakout mode.
            stp (Union[Unset, ModelsInterfaceStp]): The Spanning Tree Protocol (STP) interface configuration for the port.
                The configuration is only used when a VLAN is deployed on the port.
            sub_inf_count (Union[Unset, int]): This is a read-only field. The number of sub-interfaces configured on the
                port.
            vlan_ids (Union[Unset, list[int]]): This is a read-only field. A list of VLAN IDs deployed on the port of the
                node.
            vnis (Union[Unset, list[int]]): This is a read-only field. A list of VNIs attached to the port of the node.
            vrf_id (Union[Unset, str]): The unique identifier of the VRF associated with the port. The VRF identifier is
                required for a port with the `ROUTED_PORT` role.
    """

    annotations: Union[Unset, list["ModelsAnnotation"]] = UNSET
    breakout: Union[Unset, bool] = UNSET
    breakout_index: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    fec: Union[Unset, str] = UNSET
    force_counter: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    index: Union[Unset, int] = UNSET
    ipv_4_addresses: Union[Unset, list[str]] = UNSET
    ipv_6_addresses: Union[Unset, list[str]] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    linecard: Union[Unset, int] = UNSET
    link_down: Union[Unset, bool] = UNSET
    max_speed: Union[Unset, str] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    mtu: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    pluggable: Union[Unset, str] = UNSET
    roles: Union[Unset, list[ModelsPortRole]] = UNSET
    speed: Union[Unset, str] = UNSET
    stp: Union[Unset, "ModelsInterfaceStp"] = UNSET
    sub_inf_count: Union[Unset, int] = UNSET
    vlan_ids: Union[Unset, list[int]] = UNSET
    vnis: Union[Unset, list[int]] = UNSET
    vrf_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = []
            for annotations_item_data in self.annotations:
                annotations_item = annotations_item_data.to_dict()
                annotations.append(annotations_item)

        breakout = self.breakout

        breakout_index = self.breakout_index

        description = self.description

        enabled = self.enabled

        fec = self.fec

        force_counter = self.force_counter

        id = self.id

        index = self.index

        ipv_4_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ipv_4_addresses, Unset):
            ipv_4_addresses = self.ipv_4_addresses

        ipv_6_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ipv_6_addresses, Unset):
            ipv_6_addresses = self.ipv_6_addresses

        labels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        linecard = self.linecard

        link_down = self.link_down

        max_speed = self.max_speed

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        mtu = self.mtu

        name = self.name

        node_id = self.node_id

        pluggable = self.pluggable

        roles: Union[Unset, list[str]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.value
                roles.append(roles_item)

        speed = self.speed

        stp: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stp, Unset):
            stp = self.stp.to_dict()

        sub_inf_count = self.sub_inf_count

        vlan_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.vlan_ids, Unset):
            vlan_ids = self.vlan_ids

        vnis: Union[Unset, list[int]] = UNSET
        if not isinstance(self.vnis, Unset):
            vnis = self.vnis

        vrf_id = self.vrf_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if breakout is not UNSET:
            field_dict["breakout"] = breakout
        if breakout_index is not UNSET:
            field_dict["breakoutIndex"] = breakout_index
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if fec is not UNSET:
            field_dict["fec"] = fec
        if force_counter is not UNSET:
            field_dict["forceCounter"] = force_counter
        if id is not UNSET:
            field_dict["id"] = id
        if index is not UNSET:
            field_dict["index"] = index
        if ipv_4_addresses is not UNSET:
            field_dict["ipv4Addresses"] = ipv_4_addresses
        if ipv_6_addresses is not UNSET:
            field_dict["ipv6Addresses"] = ipv_6_addresses
        if labels is not UNSET:
            field_dict["labels"] = labels
        if linecard is not UNSET:
            field_dict["linecard"] = linecard
        if link_down is not UNSET:
            field_dict["linkDown"] = link_down
        if max_speed is not UNSET:
            field_dict["maxSpeed"] = max_speed
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if name is not UNSET:
            field_dict["name"] = name
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if pluggable is not UNSET:
            field_dict["pluggable"] = pluggable
        if roles is not UNSET:
            field_dict["roles"] = roles
        if speed is not UNSET:
            field_dict["speed"] = speed
        if stp is not UNSET:
            field_dict["stp"] = stp
        if sub_inf_count is not UNSET:
            field_dict["subInfCount"] = sub_inf_count
        if vlan_ids is not UNSET:
            field_dict["vlanIds"] = vlan_ids
        if vnis is not UNSET:
            field_dict["vnis"] = vnis
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_annotation import ModelsAnnotation
        from ..models.models_interface_stp import ModelsInterfaceStp
        from ..models.models_metadata import ModelsMetadata

        d = dict(src_dict)
        annotations = []
        _annotations = d.pop("annotations", UNSET)
        for annotations_item_data in _annotations or []:
            annotations_item = ModelsAnnotation.from_dict(annotations_item_data)

            annotations.append(annotations_item)

        breakout = d.pop("breakout", UNSET)

        breakout_index = d.pop("breakoutIndex", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        fec = d.pop("fec", UNSET)

        force_counter = d.pop("forceCounter", UNSET)

        id = d.pop("id", UNSET)

        index = d.pop("index", UNSET)

        ipv_4_addresses = cast(list[str], d.pop("ipv4Addresses", UNSET))

        ipv_6_addresses = cast(list[str], d.pop("ipv6Addresses", UNSET))

        labels = cast(list[str], d.pop("labels", UNSET))

        linecard = d.pop("linecard", UNSET)

        link_down = d.pop("linkDown", UNSET)

        max_speed = d.pop("maxSpeed", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        mtu = d.pop("mtu", UNSET)

        name = d.pop("name", UNSET)

        node_id = d.pop("nodeId", UNSET)

        pluggable = d.pop("pluggable", UNSET)

        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = ModelsPortRole(roles_item_data)

            roles.append(roles_item)

        speed = d.pop("speed", UNSET)

        _stp = d.pop("stp", UNSET)
        stp: Union[Unset, ModelsInterfaceStp]
        if isinstance(_stp, Unset):
            stp = UNSET
        else:
            stp = ModelsInterfaceStp.from_dict(_stp)

        sub_inf_count = d.pop("subInfCount", UNSET)

        vlan_ids = cast(list[int], d.pop("vlanIds", UNSET))

        vnis = cast(list[int], d.pop("vnis", UNSET))

        vrf_id = d.pop("vrfId", UNSET)

        models_network_port = cls(
            annotations=annotations,
            breakout=breakout,
            breakout_index=breakout_index,
            description=description,
            enabled=enabled,
            fec=fec,
            force_counter=force_counter,
            id=id,
            index=index,
            ipv_4_addresses=ipv_4_addresses,
            ipv_6_addresses=ipv_6_addresses,
            labels=labels,
            linecard=linecard,
            link_down=link_down,
            max_speed=max_speed,
            metadata=metadata,
            mtu=mtu,
            name=name,
            node_id=node_id,
            pluggable=pluggable,
            roles=roles,
            speed=speed,
            stp=stp,
            sub_inf_count=sub_inf_count,
            vlan_ids=vlan_ids,
            vnis=vnis,
            vrf_id=vrf_id,
        )

        models_network_port.additional_properties = d
        return models_network_port

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
