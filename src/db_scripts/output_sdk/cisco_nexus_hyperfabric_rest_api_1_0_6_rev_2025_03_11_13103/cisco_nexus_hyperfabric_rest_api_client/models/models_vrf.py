from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_annotation import ModelsAnnotation
    from ..models.models_metadata import ModelsMetadata
    from ..models.models_network_interface import ModelsNetworkInterface


T = TypeVar("T", bound="ModelsVrf")


@_attrs_define
class ModelsVrf:
    """A VRF is a virtual-routing-and-forwarding instance that represents a routing table deployed across nodes in the
    fabric to implement VRF-lite and the ability to have multiple routing tables on a single device. A VRF can be
    associated to multiple VNIs configured with an Anycast Gateway SVI.

        Attributes:
            annotations (Union[Unset, list['ModelsAnnotation']]): A list of name-value annotations to store user-defined
                data including complex data such as JSON associated with the VRF.
            asn (Union[Unset, int]): The Autonomous System Number (ASN) used for the VRF external BGP peering.
            description (Union[Unset, str]): The description is a user-defined field to store notes about the VRF.
            enabled (Union[Unset, bool]): This is a read-only field. The enabled state of the VRF which indicates if the VRF
                is enabled or disabled.
            fabric_id (Union[Unset, str]): This is a read-only field. The unique identifier of the fabric to which this VRF
                belongs to.
            id (Union[Unset, str]): This is a read-only field. The unique identifier of the VRF.
            interfaces (Union[Unset, list['ModelsNetworkInterface']]): This is a read-only field. A list of interfaces that
                are associated with the VRF.
            is_default (Union[Unset, bool]): This is a read-only field. The flag that indicates if the VRF is the default
                (auto-created) VRF or not.
            labels (Union[Unset, list[str]]): A list of user-defined labels that can be used for grouping and filtering
                VRFs.
            metadata (Union[Unset, ModelsMetadata]): Metadata defines a map of attributes related to the lifecycle of the
                object.
            name (Union[Unset, str]): The user-defined name of the VRF. The VRF name has to be unique, and is case-
                insensitive. The name should start with `Vrf`, `VRF`, `VRf` or `VrF`, followed by an optional `-` separator and
                end with an alpha-numeric string of 1 to 16 character.
            vni (Union[Unset, int]): The VXLAN Network Identifier (VNI) used for the VRF.
    """

    annotations: Union[Unset, list["ModelsAnnotation"]] = UNSET
    asn: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    interfaces: Union[Unset, list["ModelsNetworkInterface"]] = UNSET
    is_default: Union[Unset, bool] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    name: Union[Unset, str] = UNSET
    vni: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = []
            for annotations_item_data in self.annotations:
                annotations_item = annotations_item_data.to_dict()
                annotations.append(annotations_item)

        asn = self.asn

        description = self.description

        enabled = self.enabled

        fabric_id = self.fabric_id

        id = self.id

        interfaces: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        is_default = self.is_default

        labels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        vni = self.vni

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if asn is not UNSET:
            field_dict["asn"] = asn
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if fabric_id is not UNSET:
            field_dict["fabricId"] = fabric_id
        if id is not UNSET:
            field_dict["id"] = id
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if labels is not UNSET:
            field_dict["labels"] = labels
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if vni is not UNSET:
            field_dict["vni"] = vni

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_annotation import ModelsAnnotation
        from ..models.models_metadata import ModelsMetadata
        from ..models.models_network_interface import ModelsNetworkInterface

        d = dict(src_dict)
        annotations = []
        _annotations = d.pop("annotations", UNSET)
        for annotations_item_data in _annotations or []:
            annotations_item = ModelsAnnotation.from_dict(annotations_item_data)

            annotations.append(annotations_item)

        asn = d.pop("asn", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        fabric_id = d.pop("fabricId", UNSET)

        id = d.pop("id", UNSET)

        interfaces = []
        _interfaces = d.pop("interfaces", UNSET)
        for interfaces_item_data in _interfaces or []:
            interfaces_item = ModelsNetworkInterface.from_dict(interfaces_item_data)

            interfaces.append(interfaces_item)

        is_default = d.pop("isDefault", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        vni = d.pop("vni", UNSET)

        models_vrf = cls(
            annotations=annotations,
            asn=asn,
            description=description,
            enabled=enabled,
            fabric_id=fabric_id,
            id=id,
            interfaces=interfaces,
            is_default=is_default,
            labels=labels,
            metadata=metadata,
            name=name,
            vni=vni,
        )

        models_vrf.additional_properties = d
        return models_vrf

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
