from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_annotation import ModelsAnnotation
    from ..models.models_metadata import ModelsMetadata
    from ..models.models_svi import ModelsSvi
    from ..models.models_vlan_member import ModelsVlanMember


T = TypeVar("T", bound="ModelsVlan")


@_attrs_define
class ModelsVlan:
    """Vlan represents a Vlan in a tenancy. Vlan encapsulates a VLAN identifier, and a set of network ports from leaf node.
    Vlan is locally significant, meaning a Vlan is meaningful only within the switch. The service allows creating
    "global" Vlan, however it is meaningful only in the context of a switch.
    VLAN-ID   Ports     ---------  ------- Leaf0:      10     [Ethernet1_1, Ethernet1_8]      20     [Ethernet1_4,
    Ethernet1_12] Leaf1:      10     [Ethernet1_16, Ethernet1_32]      20     [Ethernet1_1, Ethernet1_12]
    NOTES: Vlan always belong to a Vni.

        Attributes:
            annotations (Union[Unset, list['ModelsAnnotation']]): A set of annotations to store user-defined data.
            description (Union[Unset, str]): A user-defined description of Vlan.
            enabled (Union[Unset, bool]): Indicates if Vlan is enabled or disabled.
            fabric_id (Union[Unset, str]): The identifier of Fabric to which this Vlan belong.
            id (Union[Unset, str]): The unique identifier of Vlan. Identifier is required to update an existing Vlan. If
                identifier is missing, then set operation defaults to CREATE mode.
            labels (Union[Unset, list[str]]): A set of user-defined labels for searching and locating objects.
            members (Union[Unset, list['ModelsVlanMember']]): A set of NetworkPort objects that are members of this Vlan.
            metadata (Union[Unset, ModelsMetadata]): Metadata defines metadata of all objects in the service.
            name (Union[Unset, str]): The user-defined name of the Vlan. Vlan name is unique, and is case-insensitive.
            svis (Union[Unset, list['ModelsSvi']]): Vlan's SVI objects. SVI objects are optional for Vlan updates. However,
                if SVI objects are supplied, then it must be a full set.
            vlan_id (Union[Unset, int]): The Vlan identifier. Vlan identifier must be between 2 and 3600. The service
                reserves Vlan identifier between 3601 and 4096.
            vni (Union[Unset, int]): Vni to which this Vlan is attached to. Vni is readonly.
            vrf_id (Union[Unset, str]): Vrf object attached to this Vlan. Vrf identifier is readonly.
    """

    annotations: Union[Unset, list["ModelsAnnotation"]] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    members: Union[Unset, list["ModelsVlanMember"]] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    name: Union[Unset, str] = UNSET
    svis: Union[Unset, list["ModelsSvi"]] = UNSET
    vlan_id: Union[Unset, int] = UNSET
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

        members: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        svis: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.svis, Unset):
            svis = []
            for svis_item_data in self.svis:
                svis_item = svis_item_data.to_dict()
                svis.append(svis_item)

        vlan_id = self.vlan_id

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
        if members is not UNSET:
            field_dict["members"] = members
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if svis is not UNSET:
            field_dict["svis"] = svis
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id
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
        from ..models.models_vlan_member import ModelsVlanMember

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

        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in _members or []:
            members_item = ModelsVlanMember.from_dict(members_item_data)

            members.append(members_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        svis = []
        _svis = d.pop("svis", UNSET)
        for svis_item_data in _svis or []:
            svis_item = ModelsSvi.from_dict(svis_item_data)

            svis.append(svis_item)

        vlan_id = d.pop("vlanId", UNSET)

        vni = d.pop("vni", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        models_vlan = cls(
            annotations=annotations,
            description=description,
            enabled=enabled,
            fabric_id=fabric_id,
            id=id,
            labels=labels,
            members=members,
            metadata=metadata,
            name=name,
            svis=svis,
            vlan_id=vlan_id,
            vni=vni,
            vrf_id=vrf_id,
        )

        models_vlan.additional_properties = d
        return models_vlan

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
