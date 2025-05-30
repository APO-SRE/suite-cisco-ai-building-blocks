from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_annotation import ModelsAnnotation
    from ..models.models_metadata import ModelsMetadata


T = TypeVar("T", bound="ModelsLoopback")


@_attrs_define
class ModelsLoopback:
    """Loopback represents a loopback device in a tenancy. Loopback encapsulates an IPv4 address, and an optional IPv6
    address.

        Attributes:
            annotations (Union[Unset, list['ModelsAnnotation']]): A set of annotations to store user-defined data.
            description (Union[Unset, str]): A user-defined description of Loopback.
            enabled (Union[Unset, bool]): Indicates if Loopback is enabled or disabled.
            fabric_id (Union[Unset, str]): The fabric identifier to which this loopback belong to.
            id (Union[Unset, str]): The unique identifier of Loopback. Identifier is required to update an existing
                Loopback. If identifier is missing, then set operation defaults to CREATE mode.
            ipv_4_address (Union[Unset, str]): IPv4 address of Loopback device. IPv4 address must be a host IPv4 address.
            ipv_6_address (Union[Unset, str]): IPv6 address of Loopback device. IPv6 address must be a host IPv6 address.
            labels (Union[Unset, list[str]]): A set of user-defined labels for searching and locating objects.
            metadata (Union[Unset, ModelsMetadata]): Metadata defines metadata of all objects in the service.
            name (Union[Unset, str]): The user-defined name of the Loopback. Loopback name is unique within a node. Loopback
                name has a fixed prefix of Loopback and an integer suffix (Eg. Loopback10).
            node_id (Union[Unset, str]): The node identifier to which this Loopback belong to.
            vrf_id (Union[Unset, str]): Vrf object attached to this Loopback. Vrf identifier is readonly.
    """

    annotations: Union[Unset, list["ModelsAnnotation"]] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    ipv_4_address: Union[Unset, str] = UNSET
    ipv_6_address: Union[Unset, str] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    name: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
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

        ipv_4_address = self.ipv_4_address

        ipv_6_address = self.ipv_6_address

        labels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        node_id = self.node_id

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
        if ipv_4_address is not UNSET:
            field_dict["ipv4Address"] = ipv_4_address
        if ipv_6_address is not UNSET:
            field_dict["ipv6Address"] = ipv_6_address
        if labels is not UNSET:
            field_dict["labels"] = labels
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
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

        ipv_4_address = d.pop("ipv4Address", UNSET)

        ipv_6_address = d.pop("ipv6Address", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        node_id = d.pop("nodeId", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        models_loopback = cls(
            annotations=annotations,
            description=description,
            enabled=enabled,
            fabric_id=fabric_id,
            id=id,
            ipv_4_address=ipv_4_address,
            ipv_6_address=ipv_6_address,
            labels=labels,
            metadata=metadata,
            name=name,
            node_id=node_id,
            vrf_id=vrf_id,
        )

        models_loopback.additional_properties = d
        return models_loopback

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
