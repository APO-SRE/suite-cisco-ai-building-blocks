from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_annotation import ModelsAnnotation
    from ..models.models_metadata import ModelsMetadata
    from ..models.models_network_interface import ModelsNetworkInterface


T = TypeVar("T", bound="ModelsBgpPeer")


@_attrs_define
class ModelsBgpPeer:
    """BgpPeer encapsulates properties of BGP peer. Vrf on a border Node must have a BGP or OSPF object to talk to external
    routers. BgpPeer provides the config to VRF to peer with external router.

        Attributes:
            annotations (Union[Unset, list['ModelsAnnotation']]): A set of annotations to store user-defined data.
            description (Union[Unset, str]): A user-defined description of BgpPeer. Description can be up to 2000
                characters.
            enabled (Union[Unset, bool]): Indicates if BgpPeer is enabled or disabled.
            export_policy_id (Union[Unset, str]): BGP export policy identifier.
            fabric_id (Union[Unset, str]): The identifier of Fabric to which this BgpPeer belongs. Fabric identifier is
                mandatory, and immutable once set.
            id (Union[Unset, str]): The unique identifier of BgpPeer. Identifier is required to update an existing BgpPeer.
                If identifier is missing, then set operation defaults to CREATE mode.
            import_policy_id (Union[Unset, str]): BGP import policy identifier.
            ipv_4_addresses (Union[Unset, list[str]]): IPv4 addresses of external router. Must not set IPv6 addresses when
                IPv4 addresses are set. User may not provide more than one IPv4 address.
            ipv_6_addresses (Union[Unset, list[str]]): IPv6 addresses of external router. Must not set IPv4 addresses when
                IPv6 addresses are set. User may not provide more than one IPv6 address.
            labels (Union[Unset, list[str]]): A set of user-defined labels for searching and locating objects.
            local_asn (Union[Unset, int]): Local switch/fabric ASN.
            metadata (Union[Unset, ModelsMetadata]): Metadata defines metadata of all objects in the service.
            name (Union[Unset, str]): The user-defined name of BgpPeer. BgpPeer name is unique, and is case-insensitive.
            password (Union[Unset, str]): MD5 password or TCP-AO keychain encryption password in clear text.
            remote_asn (Union[Unset, int]): Asn of the external router.
            source_inf (Union[Unset, ModelsNetworkInterface]): NetworkInterface encapsulates properties of a network
                interface attached to a VRF. A NetworkInterface maybe a NetworkPort, Vlan interface (SVI), Loopback, PortChannel
                or a SubInterface.
            tcp_ao (Union[Unset, bool]): Indicates that authentication is TCP-AO based (not Supported for Beta).
            ttl (Union[Unset, int]): Expected number of hops to the external router.
            vrf_id (Union[Unset, str]): VRF to which this BgpPeer is attached to. VrfId is mandatory. External router's IP
                addresses must be reachable in the VRF.
    """

    annotations: Union[Unset, list["ModelsAnnotation"]] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    export_policy_id: Union[Unset, str] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    import_policy_id: Union[Unset, str] = UNSET
    ipv_4_addresses: Union[Unset, list[str]] = UNSET
    ipv_6_addresses: Union[Unset, list[str]] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    local_asn: Union[Unset, int] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    name: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    remote_asn: Union[Unset, int] = UNSET
    source_inf: Union[Unset, "ModelsNetworkInterface"] = UNSET
    tcp_ao: Union[Unset, bool] = UNSET
    ttl: Union[Unset, int] = UNSET
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

        export_policy_id = self.export_policy_id

        fabric_id = self.fabric_id

        id = self.id

        import_policy_id = self.import_policy_id

        ipv_4_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ipv_4_addresses, Unset):
            ipv_4_addresses = self.ipv_4_addresses

        ipv_6_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ipv_6_addresses, Unset):
            ipv_6_addresses = self.ipv_6_addresses

        labels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        local_asn = self.local_asn

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        password = self.password

        remote_asn = self.remote_asn

        source_inf: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source_inf, Unset):
            source_inf = self.source_inf.to_dict()

        tcp_ao = self.tcp_ao

        ttl = self.ttl

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
        if export_policy_id is not UNSET:
            field_dict["exportPolicyId"] = export_policy_id
        if fabric_id is not UNSET:
            field_dict["fabricId"] = fabric_id
        if id is not UNSET:
            field_dict["id"] = id
        if import_policy_id is not UNSET:
            field_dict["importPolicyId"] = import_policy_id
        if ipv_4_addresses is not UNSET:
            field_dict["ipv4Addresses"] = ipv_4_addresses
        if ipv_6_addresses is not UNSET:
            field_dict["ipv6Addresses"] = ipv_6_addresses
        if labels is not UNSET:
            field_dict["labels"] = labels
        if local_asn is not UNSET:
            field_dict["localAsn"] = local_asn
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if password is not UNSET:
            field_dict["password"] = password
        if remote_asn is not UNSET:
            field_dict["remoteAsn"] = remote_asn
        if source_inf is not UNSET:
            field_dict["sourceInf"] = source_inf
        if tcp_ao is not UNSET:
            field_dict["tcpAo"] = tcp_ao
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id

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

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        export_policy_id = d.pop("exportPolicyId", UNSET)

        fabric_id = d.pop("fabricId", UNSET)

        id = d.pop("id", UNSET)

        import_policy_id = d.pop("importPolicyId", UNSET)

        ipv_4_addresses = cast(list[str], d.pop("ipv4Addresses", UNSET))

        ipv_6_addresses = cast(list[str], d.pop("ipv6Addresses", UNSET))

        labels = cast(list[str], d.pop("labels", UNSET))

        local_asn = d.pop("localAsn", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        password = d.pop("password", UNSET)

        remote_asn = d.pop("remoteAsn", UNSET)

        _source_inf = d.pop("sourceInf", UNSET)
        source_inf: Union[Unset, ModelsNetworkInterface]
        if isinstance(_source_inf, Unset):
            source_inf = UNSET
        else:
            source_inf = ModelsNetworkInterface.from_dict(_source_inf)

        tcp_ao = d.pop("tcpAo", UNSET)

        ttl = d.pop("ttl", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        models_bgp_peer = cls(
            annotations=annotations,
            description=description,
            enabled=enabled,
            export_policy_id=export_policy_id,
            fabric_id=fabric_id,
            id=id,
            import_policy_id=import_policy_id,
            ipv_4_addresses=ipv_4_addresses,
            ipv_6_addresses=ipv_6_addresses,
            labels=labels,
            local_asn=local_asn,
            metadata=metadata,
            name=name,
            password=password,
            remote_asn=remote_asn,
            source_inf=source_inf,
            tcp_ao=tcp_ao,
            ttl=ttl,
            vrf_id=vrf_id,
        )

        models_bgp_peer.additional_properties = d
        return models_bgp_peer

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
