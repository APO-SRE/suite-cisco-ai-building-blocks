from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_annotation import ModelsAnnotation
    from ..models.models_metadata import ModelsMetadata


T = TypeVar("T", bound="ConfigNode")


@_attrs_define
class ConfigNode:
    """Add a new or update an existing Node. Note that the nodeId is read-only.

    Attributes:
        annotations (Union[Unset, list['ModelsAnnotation']]): A list of one or more annotations associated with the
            Node.
        description (Union[Unset, str]): A user-defined description of Node. Description can be up to 2000 characters.
        device_id (Union[Unset, str]): The mac address of the switch bound to this node.
        enabled (Union[Unset, bool]): Indicates if Node is enabled or disabled.
        labels (Union[Unset, list[str]]): A list of one or more tags associated with the Node.
        location (Union[Unset, str]): A user-defined location string (E.g. SJC20).
        metadata (Union[Unset, ModelsMetadata]): Metadata defines metadata of all objects in the service.
        model_name (Union[Unset, str]): Hardware model name of Node. Model name cannot be nullified.
        name (Union[Unset, str]): The user-defined name of the Node. Node name is unique, and is case-insensitive.
        node_id (Union[Unset, str]): The unique identifier of Node. This is a read-only attribute assigned by the
            service.
        roles (Union[Unset, list[int]]): A Node can have multiple roles.
        serial_number (Union[Unset, str]): Serial number of Node. Serial number cannot be nullified.
    """

    annotations: Union[Unset, list["ModelsAnnotation"]] = UNSET
    description: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    location: Union[Unset, str] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    model_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
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

        description = self.description

        device_id = self.device_id

        enabled = self.enabled

        labels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        location = self.location

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        model_name = self.model_name

        name = self.name

        node_id = self.node_id

        roles: Union[Unset, list[int]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        serial_number = self.serial_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if description is not UNSET:
            field_dict["description"] = description
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if labels is not UNSET:
            field_dict["labels"] = labels
        if location is not UNSET:
            field_dict["location"] = location
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if model_name is not UNSET:
            field_dict["modelName"] = model_name
        if name is not UNSET:
            field_dict["name"] = name
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if roles is not UNSET:
            field_dict["roles"] = roles
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number

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

        device_id = d.pop("deviceId", UNSET)

        enabled = d.pop("enabled", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        location = d.pop("location", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        model_name = d.pop("modelName", UNSET)

        name = d.pop("name", UNSET)

        node_id = d.pop("nodeId", UNSET)

        roles = cast(list[int], d.pop("roles", UNSET))

        serial_number = d.pop("serialNumber", UNSET)

        config_node = cls(
            annotations=annotations,
            description=description,
            device_id=device_id,
            enabled=enabled,
            labels=labels,
            location=location,
            metadata=metadata,
            model_name=model_name,
            name=name,
            node_id=node_id,
            roles=roles,
            serial_number=serial_number,
        )

        config_node.additional_properties = d
        return config_node

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
