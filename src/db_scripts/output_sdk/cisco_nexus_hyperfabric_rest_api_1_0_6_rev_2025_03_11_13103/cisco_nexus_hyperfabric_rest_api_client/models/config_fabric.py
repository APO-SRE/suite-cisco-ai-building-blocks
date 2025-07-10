from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_fabric_topology import ModelsFabricTopology
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_annotation import ModelsAnnotation
    from ..models.models_metadata import ModelsMetadata


T = TypeVar("T", bound="ConfigFabric")


@_attrs_define
class ConfigFabric:
    """A Fabric is a collection of nodes, connections that represents the interconnections between the nodes, the
    configuration of the ports of the nodes and the logical constructs deployed across the fabric such as VRFs, logical
    networks named VNIs and other services.

        Attributes:
            name (str): The user-defined name of the fabric.
            address (Union[Unset, str]): The physical street address where the fabric is located (E.g. 320 My Street).
            annotations (Union[Unset, list['ModelsAnnotation']]): A list of name-value annotations to store user-defined
                data including complex data such as JSON associated with the fabric.
            city (Union[Unset, str]): The city in which the fabric is located (E.g. San Jose).
            country (Union[Unset, str]): The country code in which the fabric is located (E.g. US).
            description (Union[Unset, str]): The description is a user-defined field to store notes about the fabric.
            fabric_id (Union[Unset, str]): This is a read-only field. The unique identifier of the fabric.
            labels (Union[Unset, list[str]]): A list of user-defined labels that can be used for grouping and filtering
                fabrics.
            location (Union[Unset, str]): The location is a user-defined field to store information about the location of
                the fabric (E.g. SJC01).
            metadata (Union[Unset, ModelsMetadata]): Metadata defines a map of attributes related to the lifecycle of the
                object.
            topology (Union[Unset, ModelsFabricTopology]): FabricTopology defines an enumeration of types of fabric
                topologies.
    """

    name: str
    address: Union[Unset, str] = UNSET
    annotations: Union[Unset, list["ModelsAnnotation"]] = UNSET
    city: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    location: Union[Unset, str] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    topology: Union[Unset, ModelsFabricTopology] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        address = self.address

        annotations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = []
            for annotations_item_data in self.annotations:
                annotations_item = annotations_item_data.to_dict()
                annotations.append(annotations_item)

        city = self.city

        country = self.country

        description = self.description

        fabric_id = self.fabric_id

        labels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        location = self.location

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        topology: Union[Unset, str] = UNSET
        if not isinstance(self.topology, Unset):
            topology = self.topology.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if description is not UNSET:
            field_dict["description"] = description
        if fabric_id is not UNSET:
            field_dict["fabricId"] = fabric_id
        if labels is not UNSET:
            field_dict["labels"] = labels
        if location is not UNSET:
            field_dict["location"] = location
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if topology is not UNSET:
            field_dict["topology"] = topology

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_annotation import ModelsAnnotation
        from ..models.models_metadata import ModelsMetadata

        d = dict(src_dict)
        name = d.pop("name")

        address = d.pop("address", UNSET)

        annotations = []
        _annotations = d.pop("annotations", UNSET)
        for annotations_item_data in _annotations or []:
            annotations_item = ModelsAnnotation.from_dict(annotations_item_data)

            annotations.append(annotations_item)

        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        description = d.pop("description", UNSET)

        fabric_id = d.pop("fabricId", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        location = d.pop("location", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        _topology = d.pop("topology", UNSET)
        topology: Union[Unset, ModelsFabricTopology]
        if isinstance(_topology, Unset):
            topology = UNSET
        else:
            topology = ModelsFabricTopology(_topology)

        config_fabric = cls(
            name=name,
            address=address,
            annotations=annotations,
            city=city,
            country=country,
            description=description,
            fabric_id=fabric_id,
            labels=labels,
            location=location,
            metadata=metadata,
            topology=topology,
        )

        config_fabric.additional_properties = d
        return config_fabric

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
