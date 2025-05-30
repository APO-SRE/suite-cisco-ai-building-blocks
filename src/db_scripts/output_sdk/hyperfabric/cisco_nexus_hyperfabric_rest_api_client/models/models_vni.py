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


T = TypeVar("T", bound="ModelsVni")


@_attrs_define
class ModelsVni:
    """Vni encapsulates properties of a L2/L3 logical network (VNI). Vni has two distinct modes - L2VNI and L3VNI. In L3VNI
    mode, Vni allows bidirectional flow of traffic between a Layer-2 bridged network and a Layer-3 routed network.
    Whereas, in L2VNI mode, Vni allows traffic between all participating ports through a subnet.

        Attributes:
            annotations (Union[Unset, list['ModelsAnnotation']]): A set of annotations to store user-defined data.
            description (Union[Unset, str]): A user-defined description of Vni.
            enabled (Union[Unset, bool]): Indicates if Vni is enabled or disabled.
            fabric_id (Union[Unset, str]): The identifier of Fabric to which this Vni belongs to. Fabric identifier or
                fabric name must be provided.
            id (Union[Unset, str]): The unique object identifier of Vni. Identifier is required to update an existing Vni.
                If identifier is missing, then set operation defaults to CREATE mode.
            is_default (Union[Unset, bool]): Indicates that Vni is a default (aut-created) VNI (readonly).
            is_l3 (Union[Unset, bool]): Indicates that Vni is in L3VNI mode. The service will create A VRF in L3VNI mode.
                Once set, user may not change mode from L3VNI to L2VNI or vice versa.
            labels (Union[Unset, list[str]]): A set of user-defined labels for searching and locating objects.
            members (Union[Unset, list['ModelsVlanMember']]): The member network ports of Vni. Must provide member ports
                during Vni creation.
            metadata (Union[Unset, ModelsMetadata]): Metadata defines metadata of all objects in the service.
            mtu (Union[Unset, int]): Maximum transfer unit of Vni. Value must be between 1500 and 9600. MTU of all member
                network ports will inherit this MTU.
            name (Union[Unset, str]): The user-defined name of the Vni. Vni name is unique, and is case-insensitive.
            svis (Union[Unset, list['ModelsSvi']]): The switch virtual interfaces (SVI) of Vni in L3VNI mode or static-
                anycast-gateway of Vni in L2VNI mode. L2VNI rules:  1) There must be exactly one SAG enabled SVI entry.  2)
                NodeId attribute of SVI must be empty. L3VNI rules:  1) There must be one SVI per node per Vlan.  2) NodeId
                attribute of SVI must be set to the node where SVI should be active.
            vni (Union[Unset, int]): The Vxlan network identifier (VNI). The service allocates a VNI if not provided. If VNI
                is provided, then the value must be between 2 and 6000000. The service reserves VNI values above 6000000 (6M).
            vrf_id (Union[Unset, str]): The Vrf associated with the Vni. L2VNI:  1) Vrf belongs to a separate L3VNI object.
                2) User may link SVI of VNI with an existing VRF.  3) If Vrf is present in setVnis request, then the service
                will link SVI to VRF.  4) The service will not update or delete any other VRF interfaces. L3VNI:  1) Vrf belongs
                to the L3VNI itself.  2) Vni automatically creates a VRF.  3) All SVIs of L3VNI are automatically added to the
                VRF.
    """

    annotations: Union[Unset, list["ModelsAnnotation"]] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    is_default: Union[Unset, bool] = UNSET
    is_l3: Union[Unset, bool] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    members: Union[Unset, list["ModelsVlanMember"]] = UNSET
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

        is_default = self.is_default

        is_l3 = self.is_l3

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
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if is_l3 is not UNSET:
            field_dict["isL3"] = is_l3
        if labels is not UNSET:
            field_dict["labels"] = labels
        if members is not UNSET:
            field_dict["members"] = members
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

        is_default = d.pop("isDefault", UNSET)

        is_l3 = d.pop("isL3", UNSET)

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
            is_default=is_default,
            is_l3=is_l3,
            labels=labels,
            members=members,
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
