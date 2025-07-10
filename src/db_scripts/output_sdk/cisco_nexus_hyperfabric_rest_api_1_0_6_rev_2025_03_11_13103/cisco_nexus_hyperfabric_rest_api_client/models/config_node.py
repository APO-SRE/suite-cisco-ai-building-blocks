from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_node_role import ModelsNodeRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_annotation import ModelsAnnotation
    from ..models.models_metadata import ModelsMetadata
    from ..models.models_psu_airflow import ModelsPsuAirflow


T = TypeVar("T", bound="ConfigNode")


@_attrs_define
class ConfigNode:
    """A Node is a logical representation of a device in a fabric that allows the separation to the logical configuration
    from the actual physical device simplifying RMA and hardware replacements. When associated or bound to a node, a
    device assumes the node identity and all its associated configuration. A node can be pre-configured and referenced
    in other fabric level constructs such as VRFs, VNIs and Link Aggregation Groups (LAGs) before a device is bound to
    it allowing for pre-configuration of a complete fabric.

        Attributes:
            annotations (Union[Unset, list['ModelsAnnotation']]): A list of name-value annotations to store user-defined
                data including complex data such as JSON associated with the node.
            description (Union[Unset, str]): The description is a user-defined field to store notes about the node.
            device_id (Union[Unset, str]): The unique identifier of the device associated with the node.
            enabled (Union[Unset, bool]): This is a read-only field. The enabled state of the node which indicates if the
                node is enabled or disabled.
            labels (Union[Unset, list[str]]): A list of user-defined labels that can be used for grouping and filtering
                nodes.
            location (Union[Unset, str]): The location is a user-defined field to store information about the location of
                the node (E.g. SJC01).
            metadata (Union[Unset, ModelsMetadata]): Metadata defines a map of attributes related to the lifecycle of the
                object.
            model_name (Union[Unset, str]): The name of the hardware model of the node.
            name (Union[Unset, str]): The user-defined name of the node. The name is used as hostname for the node and need
                to comply with DNS restrictions, is case-insensitive and must be unique in the organization.
            node_id (Union[Unset, str]): This is a read-only field. The unique identifier of the node.
            psu_airflows (Union[Unset, list['ModelsPsuAirflow']]): Airflows and corresponding psu models of the node.
            roles (Union[Unset, list[ModelsNodeRole]]): A list of roles for the node.
            serial_number (Union[Unset, str]): The serial number of the device associated with the node.
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
    psu_airflows: Union[Unset, list["ModelsPsuAirflow"]] = UNSET
    roles: Union[Unset, list[ModelsNodeRole]] = UNSET
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

        psu_airflows: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.psu_airflows, Unset):
            psu_airflows = []
            for psu_airflows_item_data in self.psu_airflows:
                psu_airflows_item = psu_airflows_item_data.to_dict()
                psu_airflows.append(psu_airflows_item)

        roles: Union[Unset, list[str]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.value
                roles.append(roles_item)

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
        if psu_airflows is not UNSET:
            field_dict["psuAirflows"] = psu_airflows
        if roles is not UNSET:
            field_dict["roles"] = roles
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_annotation import ModelsAnnotation
        from ..models.models_metadata import ModelsMetadata
        from ..models.models_psu_airflow import ModelsPsuAirflow

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

        psu_airflows = []
        _psu_airflows = d.pop("psuAirflows", UNSET)
        for psu_airflows_item_data in _psu_airflows or []:
            psu_airflows_item = ModelsPsuAirflow.from_dict(psu_airflows_item_data)

            psu_airflows.append(psu_airflows_item)

        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = ModelsNodeRole(roles_item_data)

            roles.append(roles_item)

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
            psu_airflows=psu_airflows,
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
