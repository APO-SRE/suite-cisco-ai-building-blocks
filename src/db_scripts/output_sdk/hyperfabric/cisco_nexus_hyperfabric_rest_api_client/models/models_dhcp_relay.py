from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_annotation import ModelsAnnotation
    from ..models.models_metadata import ModelsMetadata
    from ..models.models_vni_dhcp import ModelsVniDhcp


T = TypeVar("T", bound="ModelsDhcpRelay")


@_attrs_define
class ModelsDhcpRelay:
    """DhcpRelay encapsulates properties of a DHCP relay object. DhcpRelay are specific to Vrf objects, and all interfaces
    in a DhcpRelay must be in the Vrf. A DhcpRelay must have IP addresses of the DHCP server, and a set of VNI objects
    that need DHCP relay feature.

        Attributes:
            annotations (Union[Unset, list['ModelsAnnotation']]): A set of annotations to store user-defined data.
            description (Union[Unset, str]): A user-defined description of DhcpRelay.
            enabled (Union[Unset, bool]): Indicates if DhcpRelay is enabled or disabled.
            fabric_id (Union[Unset, str]): The identifier of Fabric to which this DhcpRelay belong. Fabric identifier is
                mandatory, and immutable once set.
            id (Union[Unset, str]): The unique identifier of DhcpRelay. Identifier is required to update an existing
                DhcpRelay. If identifier is missing, then set operation defaults to CREATE mode.
            ipv_4_addresses (Union[Unset, list[str]]): IPv4 addresses of DHCP server. May provided a maximum of 2 IPv4
                addresses.
            ipv_6_addresses (Union[Unset, list[str]]): IPv6 addresses of DHCP server. May provided a maximum of 2 IPv6
                addresses.
            labels (Union[Unset, list[str]]): A set of user-defined labels for searching and locating objects.
            metadata (Union[Unset, ModelsMetadata]): Metadata defines metadata of all objects in the service.
            name (Union[Unset, str]): The user-defined name of the DhcpRelay. DhcpRelay name is unique, and is case-
                insensitive.
            vnis (Union[Unset, list['ModelsVniDhcp']]): DHCP relay specification on a per VNI basis. User may specify a
                maximum of 30 VNIs.
            vrf_id (Union[Unset, str]): The identifier of Vrf to which this DhcpRelay belong. Vrf identifier is mandatory,
                and immutable once set.
    """

    annotations: Union[Unset, list["ModelsAnnotation"]] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    ipv_4_addresses: Union[Unset, list[str]] = UNSET
    ipv_6_addresses: Union[Unset, list[str]] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    name: Union[Unset, str] = UNSET
    vnis: Union[Unset, list["ModelsVniDhcp"]] = UNSET
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

        ipv_4_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ipv_4_addresses, Unset):
            ipv_4_addresses = self.ipv_4_addresses

        ipv_6_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ipv_6_addresses, Unset):
            ipv_6_addresses = self.ipv_6_addresses

        labels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        vnis: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vnis, Unset):
            vnis = []
            for vnis_item_data in self.vnis:
                vnis_item = vnis_item_data.to_dict()
                vnis.append(vnis_item)

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
        if ipv_4_addresses is not UNSET:
            field_dict["ipv4Addresses"] = ipv_4_addresses
        if ipv_6_addresses is not UNSET:
            field_dict["ipv6Addresses"] = ipv_6_addresses
        if labels is not UNSET:
            field_dict["labels"] = labels
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if vnis is not UNSET:
            field_dict["vnis"] = vnis
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_annotation import ModelsAnnotation
        from ..models.models_metadata import ModelsMetadata
        from ..models.models_vni_dhcp import ModelsVniDhcp

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

        ipv_4_addresses = cast(list[str], d.pop("ipv4Addresses", UNSET))

        ipv_6_addresses = cast(list[str], d.pop("ipv6Addresses", UNSET))

        labels = cast(list[str], d.pop("labels", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        vnis = []
        _vnis = d.pop("vnis", UNSET)
        for vnis_item_data in _vnis or []:
            vnis_item = ModelsVniDhcp.from_dict(vnis_item_data)

            vnis.append(vnis_item)

        vrf_id = d.pop("vrfId", UNSET)

        models_dhcp_relay = cls(
            annotations=annotations,
            description=description,
            enabled=enabled,
            fabric_id=fabric_id,
            id=id,
            ipv_4_addresses=ipv_4_addresses,
            ipv_6_addresses=ipv_6_addresses,
            labels=labels,
            metadata=metadata,
            name=name,
            vnis=vnis,
            vrf_id=vrf_id,
        )

        models_dhcp_relay.additional_properties = d
        return models_dhcp_relay

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
