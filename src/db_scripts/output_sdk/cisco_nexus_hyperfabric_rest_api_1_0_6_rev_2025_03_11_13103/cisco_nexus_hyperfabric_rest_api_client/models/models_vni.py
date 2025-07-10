from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_annotation import ModelsAnnotation
    from ..models.models_metadata import ModelsMetadata
    from ..models.models_svi import ModelsSvi


T = TypeVar("T", bound="ModelsVni")


@_attrs_define
class ModelsVni:
    """A VNI represents a Layer 2 or Layer 3 logical network that can be extended across the fabric and mapped to a VLAN ID
    on specific ports and port channels. A VNI can be mapped to a VRF and configured with an SVI to serve as an Anycast
    Gateway.

        Attributes:
            annotations (Union[Unset, list['ModelsAnnotation']]): A list of name-value annotations to store user-defined
                data including complex data such as JSON associated with the VNI.
            description (Union[Unset, str]): The description is a user-defined field to store notes about the VNI.
            enabled (Union[Unset, bool]): This is a read-only field. The enabled state of the VNI which indicates if the VNI
                is enabled or disabled.
            fabric_id (Union[Unset, str]): This is a read-only field. The unique identifier of the fabric to which this VNI
                belongs to.
            id (Union[Unset, str]): This is a read-only field. The unique identifier of the VNI.
            labels (Union[Unset, list[str]]): A list of user-defined labels that can be used for grouping and filtering
                VNIs.
            metadata (Union[Unset, ModelsMetadata]): Metadata defines a map of attributes related to the lifecycle of the
                object.
            mtu (Union[Unset, int]): The Maximum Transfer Unit (MTU) of the SVI of the VNI. The value must be between 1500
                and 9600.
            name (Union[Unset, str]): The user-defined name of the VNI. The VNI name has to be unique, and is case-
                insensitive.
            svis (Union[Unset, list['ModelsSvi']]): A list of Switch Virtual Interfaces (SVIs) for the VNI.
            vni (Union[Unset, int]): The VXLAN Network Identifier (VNI) used for the VNI. The value must be between 2 and
                6000000.
            vrf_id (Union[Unset, str]): The unique identifier of the VRF associated with the VNI.
    """

    annotations: Union[Unset, list["ModelsAnnotation"]] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    mtu: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    svis: Union[Unset, list["ModelsSvi"]] = UNSET
    vni: Union[Unset, int] = UNSET
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

        labels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        mtu = self.mtu

        name = self.name

        svis: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.svis, Unset):
            svis = []
            for svis_item_data in self.svis:
                svis_item = svis_item_data.to_dict()
                svis.append(svis_item)

        vni = self.vni

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
        if labels is not UNSET:
            field_dict["labels"] = labels
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if name is not UNSET:
            field_dict["name"] = name
        if svis is not UNSET:
            field_dict["svis"] = svis
        if vni is not UNSET:
            field_dict["vni"] = vni
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_annotation import ModelsAnnotation
        from ..models.models_metadata import ModelsMetadata
        from ..models.models_svi import ModelsSvi

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

        labels = cast(list[str], d.pop("labels", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        mtu = d.pop("mtu", UNSET)

        name = d.pop("name", UNSET)

        svis = []
        _svis = d.pop("svis", UNSET)
        for svis_item_data in _svis or []:
            svis_item = ModelsSvi.from_dict(svis_item_data)

            svis.append(svis_item)

        vni = d.pop("vni", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        models_vni = cls(
            annotations=annotations,
            description=description,
            enabled=enabled,
            fabric_id=fabric_id,
            id=id,
            labels=labels,
            metadata=metadata,
            mtu=mtu,
            name=name,
            svis=svis,
            vni=vni,
            vrf_id=vrf_id,
        )

        models_vni.additional_properties = d
        return models_vni

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
