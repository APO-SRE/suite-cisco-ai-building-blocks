from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_fabric_topology import ModelsFabricTopology
from ..models.models_fabric_type import ModelsFabricType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_annotation import ModelsAnnotation
    from ..models.models_metadata import ModelsMetadata
    from ..models.models_node import ModelsNode
    from ..models.models_port_connection import ModelsPortConnection


T = TypeVar("T", bound="ModelsFabric")


@_attrs_define
class ModelsFabric:
    """Fabric is a collection of nodes and port interconnections.  - nodes: A set of nodes classified as LEAF, SPINE.  -
    connections: Physical port interconnections between nodes.

        Attributes:
            address (Union[Unset, str]): Physical address line (E.g. 320 My Street)
            annotations (Union[Unset, list['ModelsAnnotation']]): A set of annotations to store user-defined data.
            city (Union[Unset, str]): City name (E.g. San Jose)
            connections (Union[Unset, list['ModelsPortConnection']]): A set of Fabric interconnection objects. Connections
                are optional during Fabric modification. If provided, Connections set must be a full set.
            country (Union[Unset, str]): Country code (E.g. US)
            description (Union[Unset, str]): A user-defined description of Fabric.
            enabled (Union[Unset, bool]): Indicates if Fabric is enabled or disabled.
            fabric_type (Union[Unset, ModelsFabricType]): FabricType defines an enumeration of fabric types.
            id (Union[Unset, str]): The unique identifier of Fabric. Identifier is required to update an existing Fabric. If
                identifier is missing, then set operation defaults to CREATE mode.
            labels (Union[Unset, list[str]]): A set of user-defined labels for searching and locating objects.
            location (Union[Unset, str]): A user-defined location string (E.g. SJC20).
            metadata (Union[Unset, ModelsMetadata]): Metadata defines metadata of all objects in the service.
            name (Union[Unset, str]): The user-defined name of Fabric. Fabric name is unique, and is case-insensitive.
            nodes (Union[Unset, list['ModelsNode']]): A set of nodes that are part of Fabric. Nodes are optional during
                Fabric modification. If provided, Nodes set must be a full set.
            num_candidates (Union[Unset, int]): Number of active config candidates. NumCandidates is readonly.
            sag_mac (Union[Unset, str]): Optional static anycast gateway's MAC address.
            topology (Union[Unset, ModelsFabricTopology]): FabricTopology defines an enumeration of fabric topology.
            unrecognized (Union[Unset, list['ModelsNode']]): A set of nodes that are discovered but not unrecognized by the
                service. GetFabrics API does not return unrecognized nodes. However, GetFabricInventories API sets Unrecognized
                nodes when it finds non-service switches.
    """

    address: Union[Unset, str] = UNSET
    annotations: Union[Unset, list["ModelsAnnotation"]] = UNSET
    city: Union[Unset, str] = UNSET
    connections: Union[Unset, list["ModelsPortConnection"]] = UNSET
    country: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    fabric_type: Union[Unset, ModelsFabricType] = UNSET
    id: Union[Unset, str] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    location: Union[Unset, str] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    name: Union[Unset, str] = UNSET
    nodes: Union[Unset, list["ModelsNode"]] = UNSET
    num_candidates: Union[Unset, int] = UNSET
    sag_mac: Union[Unset, str] = UNSET
    topology: Union[Unset, ModelsFabricTopology] = UNSET
    unrecognized: Union[Unset, list["ModelsNode"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        annotations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = []
            for annotations_item_data in self.annotations:
                annotations_item = annotations_item_data.to_dict()
                annotations.append(annotations_item)

        city = self.city

        connections: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.connections, Unset):
            connections = []
            for connections_item_data in self.connections:
                connections_item = connections_item_data.to_dict()
                connections.append(connections_item)

        country = self.country

        description = self.description

        enabled = self.enabled

        fabric_type: Union[Unset, str] = UNSET
        if not isinstance(self.fabric_type, Unset):
            fabric_type = self.fabric_type.value

        id = self.id

        labels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        location = self.location

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        nodes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)

        num_candidates = self.num_candidates

        sag_mac = self.sag_mac

        topology: Union[Unset, str] = UNSET
        if not isinstance(self.topology, Unset):
            topology = self.topology.value

        unrecognized: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.unrecognized, Unset):
            unrecognized = []
            for unrecognized_item_data in self.unrecognized:
                unrecognized_item = unrecognized_item_data.to_dict()
                unrecognized.append(unrecognized_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if city is not UNSET:
            field_dict["city"] = city
        if connections is not UNSET:
            field_dict["connections"] = connections
        if country is not UNSET:
            field_dict["country"] = country
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if fabric_type is not UNSET:
            field_dict["fabricType"] = fabric_type
        if id is not UNSET:
            field_dict["id"] = id
        if labels is not UNSET:
            field_dict["labels"] = labels
        if location is not UNSET:
            field_dict["location"] = location
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if num_candidates is not UNSET:
            field_dict["numCandidates"] = num_candidates
        if sag_mac is not UNSET:
            field_dict["sagMac"] = sag_mac
        if topology is not UNSET:
            field_dict["topology"] = topology
        if unrecognized is not UNSET:
            field_dict["unrecognized"] = unrecognized

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_annotation import ModelsAnnotation
        from ..models.models_metadata import ModelsMetadata
        from ..models.models_node import ModelsNode
        from ..models.models_port_connection import ModelsPortConnection

        d = dict(src_dict)
        address = d.pop("address", UNSET)

        annotations = []
        _annotations = d.pop("annotations", UNSET)
        for annotations_item_data in _annotations or []:
            annotations_item = ModelsAnnotation.from_dict(annotations_item_data)

            annotations.append(annotations_item)

        city = d.pop("city", UNSET)

        connections = []
        _connections = d.pop("connections", UNSET)
        for connections_item_data in _connections or []:
            connections_item = ModelsPortConnection.from_dict(connections_item_data)

            connections.append(connections_item)

        country = d.pop("country", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        _fabric_type = d.pop("fabricType", UNSET)
        fabric_type: Union[Unset, ModelsFabricType]
        if isinstance(_fabric_type, Unset):
            fabric_type = UNSET
        else:
            fabric_type = ModelsFabricType(_fabric_type)

        id = d.pop("id", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        location = d.pop("location", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        nodes = []
        _nodes = d.pop("nodes", UNSET)
        for nodes_item_data in _nodes or []:
            nodes_item = ModelsNode.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        num_candidates = d.pop("numCandidates", UNSET)

        sag_mac = d.pop("sagMac", UNSET)

        _topology = d.pop("topology", UNSET)
        topology: Union[Unset, ModelsFabricTopology]
        if isinstance(_topology, Unset):
            topology = UNSET
        else:
            topology = ModelsFabricTopology(_topology)

        unrecognized = []
        _unrecognized = d.pop("unrecognized", UNSET)
        for unrecognized_item_data in _unrecognized or []:
            unrecognized_item = ModelsNode.from_dict(unrecognized_item_data)

            unrecognized.append(unrecognized_item)

        models_fabric = cls(
            address=address,
            annotations=annotations,
            city=city,
            connections=connections,
            country=country,
            description=description,
            enabled=enabled,
            fabric_type=fabric_type,
            id=id,
            labels=labels,
            location=location,
            metadata=metadata,
            name=name,
            nodes=nodes,
            num_candidates=num_candidates,
            sag_mac=sag_mac,
            topology=topology,
            unrecognized=unrecognized,
        )

        models_fabric.additional_properties = d
        return models_fabric

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
