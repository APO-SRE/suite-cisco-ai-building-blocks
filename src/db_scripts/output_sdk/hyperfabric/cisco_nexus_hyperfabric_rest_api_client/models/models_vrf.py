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
    """Vrf encapsulates properties of a virtual-routing-and-forwarding object. Vrf allows having more than one routing
    tables on a single switch. Vrf implements VRF-lite (IP VRF), or VRF without MPLS.
    1) A Vrf is a tenant object, and is inactive until it is attached to a Vni.  2) There is a one-to-one relationship
    between Vrf and a L3VNI.  3) A Vrf maybe attached to several L2VNI objects.

        Attributes:
            annotations (Union[Unset, list['ModelsAnnotation']]): A set of annotations to store user-defined data.
            asn (Union[Unset, int]): Optional ASN of the VRF. ASN, if provided, is used for BGP peering.
            description (Union[Unset, str]): A user-defined description of Vrf.
            enabled (Union[Unset, bool]): Indicates if Vrf is enabled or disabled.
            fabric_id (Union[Unset, str]): The identifier of Fabric to which this Vrf belong. Fabric identifier is
                mandatory.
            id (Union[Unset, str]): The unique identifier of Vrf. Identifier is required to update an existing Vrf. If
                identifier is missing, then set operation defaults to CREATE mode.
            interfaces (Union[Unset, list['ModelsNetworkInterface']]): A set of interfaces that are part of Vrf.
            ipv_4_loopbacks (Union[Unset, list[str]]): IPv4 address range of DHCP relay Loopbacks. Loopbacks are created
                when DHCP relays are attached to a VRF. Loopbacks may also be created for other purposes. Caller must provide an
                IP range in CIDR format (E.g. 10.10.2.1/24) or a distinct set of IP addresses (E.g. 10.10.1.1, 10.10.1.5.
                10.10.2.3 etc.). IP range should be large enough to create Loopbacks on all switches in the fabric. E.g.
                10.10.10.1/24
            ipv_6_loopbacks (Union[Unset, list[str]]): IPv6 address range of DHCP relay Loopbacks. Caller must provide an IP
                range in CIDR format. CIDR range should be large enough to create Loopbacks on all switches in the fabric. E.g.
                3000::1/112
            is_default (Union[Unset, bool]): Indicates that Vrf is a default (aut-created) VRF (readonly).
            labels (Union[Unset, list[str]]): A set of user-defined labels for searching and locating objects.
            metadata (Union[Unset, ModelsMetadata]): Metadata defines metadata of all objects in the service.
            name (Union[Unset, str]): The user-defined name of the Vrf. Vrf name is unique, and is case-insensitive.
            route_target (Union[Unset, str]): Globally unique route-target of VRF. RouteTarget is readonly. FIXME: This
                field should not be exposed via REST API.
            vni (Union[Unset, int]): VNI of the parent L3VNI (readonly).
    """

    annotations: Union[Unset, list["ModelsAnnotation"]] = UNSET
    asn: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    interfaces: Union[Unset, list["ModelsNetworkInterface"]] = UNSET
    ipv_4_loopbacks: Union[Unset, list[str]] = UNSET
    ipv_6_loopbacks: Union[Unset, list[str]] = UNSET
    is_default: Union[Unset, bool] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    name: Union[Unset, str] = UNSET
    route_target: Union[Unset, str] = UNSET
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

        ipv_4_loopbacks: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ipv_4_loopbacks, Unset):
            ipv_4_loopbacks = self.ipv_4_loopbacks

        ipv_6_loopbacks: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ipv_6_loopbacks, Unset):
            ipv_6_loopbacks = self.ipv_6_loopbacks

        is_default = self.is_default

        labels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        route_target = self.route_target

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
        if ipv_4_loopbacks is not UNSET:
            field_dict["ipv4Loopbacks"] = ipv_4_loopbacks
        if ipv_6_loopbacks is not UNSET:
            field_dict["ipv6Loopbacks"] = ipv_6_loopbacks
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if labels is not UNSET:
            field_dict["labels"] = labels
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if route_target is not UNSET:
            field_dict["routeTarget"] = route_target
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

        ipv_4_loopbacks = cast(list[str], d.pop("ipv4Loopbacks", UNSET))

        ipv_6_loopbacks = cast(list[str], d.pop("ipv6Loopbacks", UNSET))

        is_default = d.pop("isDefault", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        route_target = d.pop("routeTarget", UNSET)

        vni = d.pop("vni", UNSET)

        models_vrf = cls(
            annotations=annotations,
            asn=asn,
            description=description,
            enabled=enabled,
            fabric_id=fabric_id,
            id=id,
            interfaces=interfaces,
            ipv_4_loopbacks=ipv_4_loopbacks,
            ipv_6_loopbacks=ipv_6_loopbacks,
            is_default=is_default,
            labels=labels,
            metadata=metadata,
            name=name,
            route_target=route_target,
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
