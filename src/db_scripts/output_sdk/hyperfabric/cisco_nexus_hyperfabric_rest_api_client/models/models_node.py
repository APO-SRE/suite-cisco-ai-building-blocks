from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_node_type import ModelsNodeType
from ..models.models_os_type import ModelsOsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_annotation import ModelsAnnotation
    from ..models.models_management_port import ModelsManagementPort
    from ..models.models_metadata import ModelsMetadata
    from ..models.models_network_port import ModelsNetworkPort
    from ..models.models_port_breakout import ModelsPortBreakout
    from ..models.models_port_connection import ModelsPortConnection


T = TypeVar("T", bound="ModelsNode")


@_attrs_define
class ModelsNode:
    """Node encapsulates properties of a blueprint fabric node. A node has the following properties and child objects.  -
    roles: A set of roles that defines what the node is for.  - ports: Physical ports of node. If a port is in break-out
    mode,   then the break-out ports are treated as physical ports of the node.  - routerId: The service allocated
    router identifier meant for BGP sessions.

        Attributes:
            annotations (Union[Unset, list['ModelsAnnotation']]): A set of annotations to store user-defined data.
            breakouts (Union[Unset, list['ModelsPortBreakout']]): Port breakout configs of the node. Breakouts are set only
                when entire Fabric config is queried.
            connections (Union[Unset, list['ModelsPortConnection']]): Fabric connection objects of the node. Note that
                connection list do not have host (endpoint) connections.
            description (Union[Unset, str]): A user-defined description of the node.
            device_id (Union[Unset, str]): The identifier of bound (attached) physical device. Device identifier is
                readonly.
            enabled (Union[Unset, bool]): Indicates if node is enabled or disabled.
            fabric_id (Union[Unset, str]): The identifier of Fabric to which the node belongs. Fabric identifier is
                readonly.
            id (Union[Unset, str]): The unique identifier of the Node. Identifier is required to update an existing node. If
                identifier is missing, then set operation defaults to CREATE mode.
            labels (Union[Unset, list[str]]): A set of user-defined labels for searching and locating objects.
            location (Union[Unset, str]): A user-defined location string (E.g. SJC20).
            management_ports (Union[Unset, list['ModelsManagementPort']]): Management ports for the node.
            metadata (Union[Unset, ModelsMetadata]): Metadata defines metadata of all objects in the service.
            model_name (Union[Unset, str]): Hardware model name of the node. Model name cannot be nullified.
            name (Union[Unset, str]): The user-defined name of the Node. Node name is unique, and must be a FQDN compliant,
                single label hostname.
            node_type (Union[Unset, ModelsNodeType]): NodeType defines an enumeration of node types.
            os_type (Union[Unset, ModelsOsType]): OsType lists various device operating system types.
            ports (Union[Unset, list['ModelsNetworkPort']]): NetworkPort objects of the node. Ports are optional for node
                updates.
            position (Union[Unset, int]): Position of Node in the fabric's node list. Position is readonly.
            roles (Union[Unset, list[int]]): A set of roles of the Node. Node roles are mandatory. A Node can have either
                LEAF or SPINE role, but not both.
            serial_number (Union[Unset, str]): Serial number of the node. Serial number cannot be nullified.
    """

    annotations: Union[Unset, list["ModelsAnnotation"]] = UNSET
    breakouts: Union[Unset, list["ModelsPortBreakout"]] = UNSET
    connections: Union[Unset, list["ModelsPortConnection"]] = UNSET
    description: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    location: Union[Unset, str] = UNSET
    management_ports: Union[Unset, list["ModelsManagementPort"]] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    model_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    node_type: Union[Unset, ModelsNodeType] = UNSET
    os_type: Union[Unset, ModelsOsType] = UNSET
    ports: Union[Unset, list["ModelsNetworkPort"]] = UNSET
    position: Union[Unset, int] = UNSET
    roles: Union[Unset, list[int]] = UNSET
    serial_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = []
            for annotations_item_data in self.annotations:
                annotations_item = annotations_item_data.to_dict()
                annotations.append(annotations_item)

        breakouts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.breakouts, Unset):
            breakouts = []
            for breakouts_item_data in self.breakouts:
                breakouts_item = breakouts_item_data.to_dict()
                breakouts.append(breakouts_item)

        connections: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.connections, Unset):
            connections = []
            for connections_item_data in self.connections:
                connections_item = connections_item_data.to_dict()
                connections.append(connections_item)

        description = self.description

        device_id = self.device_id

        enabled = self.enabled

        fabric_id = self.fabric_id

        id = self.id

        labels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        location = self.location

        management_ports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.management_ports, Unset):
            management_ports = []
            for management_ports_item_data in self.management_ports:
                management_ports_item = management_ports_item_data.to_dict()
                management_ports.append(management_ports_item)

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        model_name = self.model_name

        name = self.name

        node_type: Union[Unset, str] = UNSET
        if not isinstance(self.node_type, Unset):
            node_type = self.node_type.value

        os_type: Union[Unset, str] = UNSET
        if not isinstance(self.os_type, Unset):
            os_type = self.os_type.value

        ports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        position = self.position

        roles: Union[Unset, list[int]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        serial_number = self.serial_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if breakouts is not UNSET:
            field_dict["breakouts"] = breakouts
        if connections is not UNSET:
            field_dict["connections"] = connections
        if description is not UNSET:
            field_dict["description"] = description
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if fabric_id is not UNSET:
            field_dict["fabricId"] = fabric_id
        if id is not UNSET:
            field_dict["id"] = id
        if labels is not UNSET:
            field_dict["labels"] = labels
        if location is not UNSET:
            field_dict["location"] = location
        if management_ports is not UNSET:
            field_dict["managementPorts"] = management_ports
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if model_name is not UNSET:
            field_dict["modelName"] = model_name
        if name is not UNSET:
            field_dict["name"] = name
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type
        if os_type is not UNSET:
            field_dict["osType"] = os_type
        if ports is not UNSET:
            field_dict["ports"] = ports
        if position is not UNSET:
            field_dict["position"] = position
        if roles is not UNSET:
            field_dict["roles"] = roles
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_annotation import ModelsAnnotation
        from ..models.models_management_port import ModelsManagementPort
        from ..models.models_metadata import ModelsMetadata
        from ..models.models_network_port import ModelsNetworkPort
        from ..models.models_port_breakout import ModelsPortBreakout
        from ..models.models_port_connection import ModelsPortConnection

        d = dict(src_dict)
        annotations = []
        _annotations = d.pop("annotations", UNSET)
        for annotations_item_data in _annotations or []:
            annotations_item = ModelsAnnotation.from_dict(annotations_item_data)

            annotations.append(annotations_item)

        breakouts = []
        _breakouts = d.pop("breakouts", UNSET)
        for breakouts_item_data in _breakouts or []:
            breakouts_item = ModelsPortBreakout.from_dict(breakouts_item_data)

            breakouts.append(breakouts_item)

        connections = []
        _connections = d.pop("connections", UNSET)
        for connections_item_data in _connections or []:
            connections_item = ModelsPortConnection.from_dict(connections_item_data)

            connections.append(connections_item)

        description = d.pop("description", UNSET)

        device_id = d.pop("deviceId", UNSET)

        enabled = d.pop("enabled", UNSET)

        fabric_id = d.pop("fabricId", UNSET)

        id = d.pop("id", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        location = d.pop("location", UNSET)

        management_ports = []
        _management_ports = d.pop("managementPorts", UNSET)
        for management_ports_item_data in _management_ports or []:
            management_ports_item = ModelsManagementPort.from_dict(management_ports_item_data)

            management_ports.append(management_ports_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        model_name = d.pop("modelName", UNSET)

        name = d.pop("name", UNSET)

        _node_type = d.pop("nodeType", UNSET)
        node_type: Union[Unset, ModelsNodeType]
        if isinstance(_node_type, Unset):
            node_type = UNSET
        else:
            node_type = ModelsNodeType(_node_type)

        _os_type = d.pop("osType", UNSET)
        os_type: Union[Unset, ModelsOsType]
        if isinstance(_os_type, Unset):
            os_type = UNSET
        else:
            os_type = ModelsOsType(_os_type)

        ports = []
        _ports = d.pop("ports", UNSET)
        for ports_item_data in _ports or []:
            ports_item = ModelsNetworkPort.from_dict(ports_item_data)

            ports.append(ports_item)

        position = d.pop("position", UNSET)

        roles = cast(list[int], d.pop("roles", UNSET))

        serial_number = d.pop("serialNumber", UNSET)

        models_node = cls(
            annotations=annotations,
            breakouts=breakouts,
            connections=connections,
            description=description,
            device_id=device_id,
            enabled=enabled,
            fabric_id=fabric_id,
            id=id,
            labels=labels,
            location=location,
            management_ports=management_ports,
            metadata=metadata,
            model_name=model_name,
            name=name,
            node_type=node_type,
            os_type=os_type,
            ports=ports,
            position=position,
            roles=roles,
            serial_number=serial_number,
        )

        models_node.additional_properties = d
        return models_node

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
