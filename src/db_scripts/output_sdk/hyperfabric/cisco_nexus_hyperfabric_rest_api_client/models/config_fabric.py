from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_annotation import ModelsAnnotation
    from ..models.models_metadata import ModelsMetadata


T = TypeVar("T", bound="ConfigFabric")


@_attrs_define
class ConfigFabric:
    """Add a new or update an existing fabric. Note that the fabricId is read-only.

    Attributes:
        name (str): The name of the fabric.
        address (Union[Unset, str]): Physical address line (E.g. 320 My Street)
        annotations (Union[Unset, list['ModelsAnnotation']]): One or more annotations for the fabric.
        city (Union[Unset, str]): City name (E.g. San Jose)
        country (Union[Unset, str]): Country code (E.g. US)
        description (Union[Unset, str]): A description of the fabric.
        fabric_id (Union[Unset, str]): The unique id of the fabric. This is a read-only attribute.
        labels (Union[Unset, list[str]]): One or more labels for the fabric.
        location (Union[Unset, str]): A user-defined location string (E.g. SJC20).
        metadata (Union[Unset, ModelsMetadata]): Metadata defines metadata of all objects in the service.
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
