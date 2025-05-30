from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_annotation import ModelsAnnotation
    from ..models.models_metadata import ModelsMetadata


T = TypeVar("T", bound="ModelsPortBreakout")


@_attrs_define
class ModelsPortBreakout:
    """PortBreakout encapsulates network port breakout policy. PortBreakout does not represent a configurable object. It is
    a policy that gets applied to a switch.

        Attributes:
            annotations (Union[Unset, list['ModelsAnnotation']]): A set of annotations to store user-defined data.
            breakouts (Union[Unset, list[str]]): The output of the port breakout operation (readonly).
            description (Union[Unset, str]): A user-defined description of PortBreakout.
            enabled (Union[Unset, bool]): Indicates if PortBreakout is enabled or disabled.
            fabric_id (Union[Unset, str]): The identifier of Fabric to which this PortBreakout belongs to. FabricId is
                mandatory.
            id (Union[Unset, str]): The unique identifier of PortBreakout. Identifier is required to update an existing
                PortBreakout. If identifier is missing, then set operation defaults to CREATE mode.
            labels (Union[Unset, list[str]]): A set of user-defined labels for searching and locating objects.
            metadata (Union[Unset, ModelsMetadata]): Metadata defines metadata of all objects in the service.
            mode (Union[Unset, str]): Breakout mode. E.g. 2x200G(2)
            name (Union[Unset, str]): The user-defined name of the PortBreakout object.
            node_id (Union[Unset, str]): The identifier of the node for which the PortBreakout is for. NodeId is mandatory.
            pluggable (Union[Unset, str]): User-defined cable model name (PID).
            ports (Union[Unset, list[str]]): The names of base network ports.
    """

    annotations: Union[Unset, list["ModelsAnnotation"]] = UNSET
    breakouts: Union[Unset, list[str]] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    mode: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    pluggable: Union[Unset, str] = UNSET
    ports: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = []
            for annotations_item_data in self.annotations:
                annotations_item = annotations_item_data.to_dict()
                annotations.append(annotations_item)

        breakouts: Union[Unset, list[str]] = UNSET
        if not isinstance(self.breakouts, Unset):
            breakouts = self.breakouts

        description = self.description

        enabled = self.enabled

        fabric_id = self.fabric_id

        id = self.id

        labels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        mode = self.mode

        name = self.name

        node_id = self.node_id

        pluggable = self.pluggable

        ports: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ports, Unset):
            ports = self.ports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if breakouts is not UNSET:
            field_dict["breakouts"] = breakouts
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if fabric_id is not UNSET:
            field_dict["fabricId"] = fabric_id
        if id is not UNSET:
            field_dict["id"] = id
        if labels is not UNSET:
            field_dict["labels"] = labels
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if mode is not UNSET:
            field_dict["mode"] = mode
        if name is not UNSET:
            field_dict["name"] = name
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if pluggable is not UNSET:
            field_dict["pluggable"] = pluggable
        if ports is not UNSET:
            field_dict["ports"] = ports

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

        breakouts = cast(list[str], d.pop("breakouts", UNSET))

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        fabric_id = d.pop("fabricId", UNSET)

        id = d.pop("id", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        mode = d.pop("mode", UNSET)

        name = d.pop("name", UNSET)

        node_id = d.pop("nodeId", UNSET)

        pluggable = d.pop("pluggable", UNSET)

        ports = cast(list[str], d.pop("ports", UNSET))

        models_port_breakout = cls(
            annotations=annotations,
            breakouts=breakouts,
            description=description,
            enabled=enabled,
            fabric_id=fabric_id,
            id=id,
            labels=labels,
            metadata=metadata,
            mode=mode,
            name=name,
            node_id=node_id,
            pluggable=pluggable,
            ports=ports,
        )

        models_port_breakout.additional_properties = d
        return models_port_breakout

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
