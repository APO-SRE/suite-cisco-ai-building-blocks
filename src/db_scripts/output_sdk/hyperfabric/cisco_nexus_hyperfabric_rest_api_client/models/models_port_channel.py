from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_lacp_mode import ModelsLacpMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_annotation import ModelsAnnotation
    from ..models.models_interface_stp import ModelsInterfaceStp
    from ..models.models_metadata import ModelsMetadata
    from ..models.models_port_endpoint import ModelsPortEndpoint


T = TypeVar("T", bound="ModelsPortChannel")


@_attrs_define
class ModelsPortChannel:
    """PortChannel represents a set of physical ports in a PortChannel or LACP config. PortChannel name is unique within a
    fabric. The service automatically assigns a name if a name is not specified during PortChannel creation. NOTES: -
    PortChannel object must have HOST_PORT or ROUTED_PORT as role. - PortChannel members cannot be part of Vlans. -
    PortChannel member ports must have MLAG_PORT as port role.

        Attributes:
            annotations (Union[Unset, list['ModelsAnnotation']]): A set of annotations to store user-defined data.
            description (Union[Unset, str]): A user-defined description of PortChannel.
            enabled (Union[Unset, bool]): Indicates if PortChannel is enabled or disabled.
            fabric_id (Union[Unset, str]): The identifier of Fabric to which this PortChannel belongs to. FabricId is
                mandatory.
            id (Union[Unset, str]): The unique identifier of PortChannel. Identifier is required to update an existing
                PortChannel. If identifier is missing, then set operation defaults to CREATE mode.
            ipv_4_addresses (Union[Unset, list[str]]): IPv4 addresses of PortChannel. The service supports up to 2 IPv4
                addresses, and every address must be a network address. Meaning, address must be in CIDR format with CIDR < 32.
                IPv4 address is valid only for routed PortChannel.
            ipv_6_addresses (Union[Unset, list[str]]): IPv6 addresses of PortChannel. The service supports up to 2 IPv6
                addresses, and every address must be a network address. Meaning, address must be in CIDR format with CIDR < 128.
                IPv6 address is valid only for routed PortChannel.
            labels (Union[Unset, list[str]]): A set of user-defined labels for searching and locating objects.
            lacp_mode (Union[Unset, ModelsLacpMode]): LacpMode enumerates different LACP modes.
            max_speed (Union[Unset, str]): Maximum speed of the PortChannel (readonly) (E.g. 10G).
            members (Union[Unset, list['ModelsPortEndpoint']]): A set of member NetworkPort objects (E.g. Ethernet1_1,
                Ethernet1_4 etc.). There must be at least two members.
            metadata (Union[Unset, ModelsMetadata]): Metadata defines metadata of all objects in the service.
            min_links (Union[Unset, int]): Minimum number of active links needed for PortChannel to operate.
            mtu (Union[Unset, int]): MTU of the PortChannel. Value must be between 1500 and 9600.
            name (Union[Unset, str]): The name of PortChannel. Name must have a prefix of PortChannel (E.g. PortChannel1).
            roles (Union[Unset, list[int]]): A set of roles of the PortChannel. Roles must have exactly one entry, and it
                must be either HOST_PORT or ROUTED_PORT.
            stp (Union[Unset, ModelsInterfaceStp]): InterfaceStp encapsulates configurable STP parameters of a single
                interface. Interface/Port must be a member of a Vlan for the config to be applied.
            sys_mac (Union[Unset, str]): MAC address used for EVPN multi-homing.
            vlan_ids (Union[Unset, list[int]]): VlanIds defines the identifiers Vlan in which this PortChannel is a member
                of. VlanIds is readonly.
            vnis (Union[Unset, list[int]]): Vnis defines the identifiers Vni in which this PortChannel is a member of. Vnis
                is readonly.
            vrf_id (Union[Unset, str]): The identifier of VRF to which this PortChannel belongs to. VRF identifier is set
                only for routed PortChannel that are added to a VRF.
    """

    annotations: Union[Unset, list["ModelsAnnotation"]] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    ipv_4_addresses: Union[Unset, list[str]] = UNSET
    ipv_6_addresses: Union[Unset, list[str]] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    lacp_mode: Union[Unset, ModelsLacpMode] = UNSET
    max_speed: Union[Unset, str] = UNSET
    members: Union[Unset, list["ModelsPortEndpoint"]] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    min_links: Union[Unset, int] = UNSET
    mtu: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    roles: Union[Unset, list[int]] = UNSET
    stp: Union[Unset, "ModelsInterfaceStp"] = UNSET
    sys_mac: Union[Unset, str] = UNSET
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

        description = self.description

        enabled = self.enabled

        fabric_id = self.fabric_id

        id = self.id

        ipv_4_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ipv_4_addresses, Unset):
            ipv_4_addresses = self.ipv_4_addresses

        ipv_6_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ipv_6_addresses, Unset):
            ipv_6_addresses = self.ipv_6_addresses

        labels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        lacp_mode: Union[Unset, str] = UNSET
        if not isinstance(self.lacp_mode, Unset):
            lacp_mode = self.lacp_mode.value

        max_speed = self.max_speed

        members: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        min_links = self.min_links

        mtu = self.mtu

        name = self.name

        roles: Union[Unset, list[int]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        stp: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stp, Unset):
            stp = self.stp.to_dict()

        sys_mac = self.sys_mac

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
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if fabric_id is not UNSET:
            field_dict["fabricId"] = fabric_id
        if id is not UNSET:
            field_dict["id"] = id
        if ipv_4_addresses is not UNSET:
            field_dict["ipv4Addresses"] = ipv_4_addresses
        if ipv_6_addresses is not UNSET:
            field_dict["ipv6Addresses"] = ipv_6_addresses
        if labels is not UNSET:
            field_dict["labels"] = labels
        if lacp_mode is not UNSET:
            field_dict["lacpMode"] = lacp_mode
        if max_speed is not UNSET:
            field_dict["maxSpeed"] = max_speed
        if members is not UNSET:
            field_dict["members"] = members
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if min_links is not UNSET:
            field_dict["minLinks"] = min_links
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if name is not UNSET:
            field_dict["name"] = name
        if roles is not UNSET:
            field_dict["roles"] = roles
        if stp is not UNSET:
            field_dict["stp"] = stp
        if sys_mac is not UNSET:
            field_dict["sysMac"] = sys_mac
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
        from ..models.models_port_endpoint import ModelsPortEndpoint

        d = dict(src_dict)
        annotations = []
        _annotations = d.pop("annotations", UNSET)
        for annotations_item_data in _annotations or []:
            annotations_item = ModelsAnnotation.from_dict(annotations_item_data)

            annotations.append(annotations_item)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        fabric_id = d.pop("fabricId", UNSET)

        id = d.pop("id", UNSET)

        ipv_4_addresses = cast(list[str], d.pop("ipv4Addresses", UNSET))

        ipv_6_addresses = cast(list[str], d.pop("ipv6Addresses", UNSET))

        labels = cast(list[str], d.pop("labels", UNSET))

        _lacp_mode = d.pop("lacpMode", UNSET)
        lacp_mode: Union[Unset, ModelsLacpMode]
        if isinstance(_lacp_mode, Unset):
            lacp_mode = UNSET
        else:
            lacp_mode = ModelsLacpMode(_lacp_mode)

        max_speed = d.pop("maxSpeed", UNSET)

        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in _members or []:
            members_item = ModelsPortEndpoint.from_dict(members_item_data)

            members.append(members_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        min_links = d.pop("minLinks", UNSET)

        mtu = d.pop("mtu", UNSET)

        name = d.pop("name", UNSET)

        roles = cast(list[int], d.pop("roles", UNSET))

        _stp = d.pop("stp", UNSET)
        stp: Union[Unset, ModelsInterfaceStp]
        if isinstance(_stp, Unset):
            stp = UNSET
        else:
            stp = ModelsInterfaceStp.from_dict(_stp)

        sys_mac = d.pop("sysMac", UNSET)

        vlan_ids = cast(list[int], d.pop("vlanIds", UNSET))

        vnis = cast(list[int], d.pop("vnis", UNSET))

        vrf_id = d.pop("vrfId", UNSET)

        models_port_channel = cls(
            annotations=annotations,
            description=description,
            enabled=enabled,
            fabric_id=fabric_id,
            id=id,
            ipv_4_addresses=ipv_4_addresses,
            ipv_6_addresses=ipv_6_addresses,
            labels=labels,
            lacp_mode=lacp_mode,
            max_speed=max_speed,
            members=members,
            metadata=metadata,
            min_links=min_links,
            mtu=mtu,
            name=name,
            roles=roles,
            stp=stp,
            sys_mac=sys_mac,
            vlan_ids=vlan_ids,
            vnis=vnis,
            vrf_id=vrf_id,
        )

        models_port_channel.additional_properties = d
        return models_port_channel

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
