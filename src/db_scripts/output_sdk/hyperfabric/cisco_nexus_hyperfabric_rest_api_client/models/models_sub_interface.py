from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_annotation import ModelsAnnotation
    from ..models.models_metadata import ModelsMetadata


T = TypeVar("T", bound="ModelsSubInterface")


@_attrs_define
class ModelsSubInterface:
    """SubInterface encapsulates properties of a sub-port or sub-interface. SubInterface provides logical division of a
    physical interface. SubInterface cannot be added to a NetworkPort or a PortChannel attached to Vlans. SubInterface
    maybe added a routed port or routed PortChannel.

        Attributes:
            annotations (Union[Unset, list['ModelsAnnotation']]): A set of annotations to store user-defined data.
            description (Union[Unset, str]): A user-defined description of SubInterface.
            enabled (Union[Unset, bool]): Indicates if SubInterface is enabled or disabled.
            fabric_id (Union[Unset, str]): The identifier of Fabric to which this SubInterface belongs to. FabricId is
                mandatory.
            id (Union[Unset, str]): The unique identifier of SubInterface. Identifier is required to update an existing
                SubInterface. If identifier is missing, then set operation defaults to CREATE mode.
            ipv_4_addresses (Union[Unset, list[str]]): SubInterface's IPv4 addresses. The service supports up to 2 IPv4
                addresses, and every address must be a network address. Meaning, address must be in CIDR format with CIDR < 32.
            ipv_6_addresses (Union[Unset, list[str]]): SubInterface's IPv6 addresses. The service supports up to 2 IPv6
                addresses, and every address must be a network address. Meaning, address must be in CIDR format with CIDR < 128.
            labels (Union[Unset, list[str]]): A set of user-defined labels for searching and locating objects.
            metadata (Union[Unset, ModelsMetadata]): Metadata defines metadata of all objects in the service.
            name (Union[Unset, str]): The user-defined name of the SubInterface. SubInterface name is unique, and must be in
                the format (<Ethernet1_4_1|<PortChannel0>)[.]<ID>
            node_id (Union[Unset, str]): The identifier of the Node where SubInterface is located. NodeId is mandatory.
            parent (Union[Unset, str]): The name of parent interface. This property is readonly.
            vlan_id (Union[Unset, int]): Vlan identifier of SubInterface.
            vrf_id (Union[Unset, str]): The identifier of VRF to which this SubInterface belongs to.
    """

    annotations: Union[Unset, list["ModelsAnnotation"]] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    ipv_4_addresses: Union[Unset, list[str]] = UNSET
    ipv_6_addresses: Union[Unset, list[str]] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    name: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    parent: Union[Unset, str] = UNSET
    vlan_id: Union[Unset, int] = UNSET
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

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        node_id = self.node_id

        parent = self.parent

        vlan_id = self.vlan_id

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
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if parent is not UNSET:
            field_dict["parent"] = parent
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_annotation import ModelsAnnotation
        from ..models.models_metadata import ModelsMetadata

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

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        node_id = d.pop("nodeId", UNSET)

        parent = d.pop("parent", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        models_sub_interface = cls(
            annotations=annotations,
            description=description,
            enabled=enabled,
            fabric_id=fabric_id,
            id=id,
            ipv_4_addresses=ipv_4_addresses,
            ipv_6_addresses=ipv_6_addresses,
            labels=labels,
            metadata=metadata,
            name=name,
            node_id=node_id,
            parent=parent,
            vlan_id=vlan_id,
            vrf_id=vrf_id,
        )

        models_sub_interface.additional_properties = d
        return models_sub_interface

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
