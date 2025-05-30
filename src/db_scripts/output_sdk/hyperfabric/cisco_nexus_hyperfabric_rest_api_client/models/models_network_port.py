from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_annotation import ModelsAnnotation
    from ..models.models_interface_stp import ModelsInterfaceStp
    from ..models.models_metadata import ModelsMetadata


T = TypeVar("T", bound="ModelsNetworkPort")


@_attrs_define
class ModelsNetworkPort:
    """NetworkPort encapsulates properties of a physical network port.

    Attributes:
        annotations (Union[Unset, list['ModelsAnnotation']]): A set of annotations to store user-defined data.
        breakout (Union[Unset, bool]): Indicates that port is in a break-out mode. Breakout flag is readonly.
        breakout_index (Union[Unset, int]): Breakout index of the port. Breakout index is not set when port is not in
            breakout mode. Breakout index is readonly.
        description (Union[Unset, str]): A user-defined description of NetworkPort.
        enabled (Union[Unset, bool]): Indicates if NetworkPort is enabled or disabled.
        fec (Union[Unset, str]): FEC for the network port. Supported modes are "rs" and "none". FEC must be "none" for
            100G DR/FR/LR cables.
        force_counter (Union[Unset, int]): User may increment ForceCounter attribute to force a config update when there
            are no real changes. This maybe needed to startup (un-shut) a port when STP triggers port shutdown.
        id (Union[Unset, str]): The unique identifier of NetworkPort. Identifier is required to update an existing
            NetworkPort. If identifier is missing, then set operation defaults to CREATE mode.
        index (Union[Unset, int]): Index of the NetworkPort on the linecard. Port index is one based. Index remains same
            for all NetworkPort objects in break-out mode. Index is readonly.
        ipv_4_addresses (Union[Unset, list[str]]): Port's IPv4 addresses. The service supports up to 2 IPv4 addresses,
            and every address must be a network address. Meaning, address must be in CIDR format with CIDR < 32. IPv4
            address is valid only for routed ports.
        ipv_6_addresses (Union[Unset, list[str]]): Port's IPv6 addresses. The service supports up to 2 IPv6 addresses,
            and every address must be a network address. Meaning, address must be in CIDR format with CIDR < 128. IPv6
            address is valid only for routed ports.
        labels (Union[Unset, list[str]]): A set of user-defined labels for searching and locating objects.
        linecard (Union[Unset, int]): Linecard index of the port. Linecard is readonly.
        link_down (Union[Unset, bool]): Indicates that port is in link-down state. In this mode, AdminState is UP,
            however, port may not forward any traffic to external hosts. LinkDown state is not supported for Fabric ports.
        max_speed (Union[Unset, str]): Maximum speed of the NetworkPort as reported by system (readonly) (E.g. 10G).
        metadata (Union[Unset, ModelsMetadata]): Metadata defines metadata of all objects in the service.
        mtu (Union[Unset, int]): MTU of the NetworkPort. Default value is 9100. MTU value must be between 1500 and 9100.
        name (Union[Unset, str]): The canonical name of NetworkPort. Name must have a prefix of Ethernet (E.g.
            Ethernet1_1). NetworkPort name cannot be modified.
        node_id (Union[Unset, str]): The identifier of th Node that owns the NetworkPort. NodeId is readonly, and cannot
            be modified.
        pluggable (Union[Unset, str]): User provided cable model name (PID).
        roles (Union[Unset, list[int]]): A set of roles of the NetworkPort. Port roles are mandatory, and must have
            exactly one role in it.
        speed (Union[Unset, str]): Configurable speed mode of the port, E.g. 1x10G(1). Note that port speed cannot be
            set for breakout ports.
        stp (Union[Unset, ModelsInterfaceStp]): InterfaceStp encapsulates configurable STP parameters of a single
            interface. Interface/Port must be a member of a Vlan for the config to be applied.
        sub_inf_count (Union[Unset, int]): Number of SubInterface objects attached to the NetworkPort object. This
            property is readonly.
        vlan_ids (Union[Unset, list[int]]): VlanIds defines the identifiers Vlan in which this port is a member of.
            VlanIds is readonly. VlanIds is set by GetNodesPorts API.
        vnis (Union[Unset, list[int]]): Vnis defines the identifiers Vni to which this port is attached to. Vnis is
            readonly. Vnis is set by GetNodesPorts API.
        vrf_id (Union[Unset, str]): The identifier of VRF to which this port belongs to. VRF identifier is set only for
            routed ports that are added to a VRF.
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
    roles: Union[Unset, list[int]] = UNSET
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

        roles: Union[Unset, list[int]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

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

        roles = cast(list[int], d.pop("roles", UNSET))

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
