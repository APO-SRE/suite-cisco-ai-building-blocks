from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_spec_wrapper_v1_platform_post_role import NodeSpecWrapperV1PlatformPOSTRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_spec_bgp_config_v1_platform_post import NodeSpecBgpConfigV1PlatformPOST
    from ..models.node_spec_network_v1_platform_post import NodeSpecNetworkV1PlatformPOST


T = TypeVar("T", bound="NodeSpecWrapperV1PlatformPOST")


@_attrs_define
class NodeSpecWrapperV1PlatformPOST:
    """
    Attributes:
        name (str): Node name
        bgp_config (Union[Unset, NodeSpecBgpConfigV1PlatformPOST]): Node BGP config
        cimc_ip (Union[Unset, str]): Node cimc IP (physical only)
        inb_network (Union[Unset, NodeSpecNetworkV1PlatformPOST]): Node Network config. Inband represents cluster
            internal network information, OOB represents user-accessible network information
        oob_network (Union[Unset, NodeSpecNetworkV1PlatformPOST]): Node Network config. Inband represents cluster
            internal network information, OOB represents user-accessible network information
        registered (Union[Unset, bool]): Node registered flag
        role (Union[Unset, NodeSpecWrapperV1PlatformPOSTRole]): Node role
        serial_number (Union[Unset, str]): Node serial number
    """

    name: str
    bgp_config: Union[Unset, "NodeSpecBgpConfigV1PlatformPOST"] = UNSET
    cimc_ip: Union[Unset, str] = UNSET
    inb_network: Union[Unset, "NodeSpecNetworkV1PlatformPOST"] = UNSET
    oob_network: Union[Unset, "NodeSpecNetworkV1PlatformPOST"] = UNSET
    registered: Union[Unset, bool] = UNSET
    role: Union[Unset, NodeSpecWrapperV1PlatformPOSTRole] = UNSET
    serial_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        bgp_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bgp_config, Unset):
            bgp_config = self.bgp_config.to_dict()

        cimc_ip = self.cimc_ip

        inb_network: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.inb_network, Unset):
            inb_network = self.inb_network.to_dict()

        oob_network: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.oob_network, Unset):
            oob_network = self.oob_network.to_dict()

        registered = self.registered

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        serial_number = self.serial_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if bgp_config is not UNSET:
            field_dict["bgpConfig"] = bgp_config
        if cimc_ip is not UNSET:
            field_dict["cimcIP"] = cimc_ip
        if inb_network is not UNSET:
            field_dict["inbNetwork"] = inb_network
        if oob_network is not UNSET:
            field_dict["oobNetwork"] = oob_network
        if registered is not UNSET:
            field_dict["registered"] = registered
        if role is not UNSET:
            field_dict["role"] = role
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node_spec_bgp_config_v1_platform_post import NodeSpecBgpConfigV1PlatformPOST
        from ..models.node_spec_network_v1_platform_post import NodeSpecNetworkV1PlatformPOST

        d = dict(src_dict)
        name = d.pop("name")

        _bgp_config = d.pop("bgpConfig", UNSET)
        bgp_config: Union[Unset, NodeSpecBgpConfigV1PlatformPOST]
        if isinstance(_bgp_config, Unset):
            bgp_config = UNSET
        else:
            bgp_config = NodeSpecBgpConfigV1PlatformPOST.from_dict(_bgp_config)

        cimc_ip = d.pop("cimcIP", UNSET)

        _inb_network = d.pop("inbNetwork", UNSET)
        inb_network: Union[Unset, NodeSpecNetworkV1PlatformPOST]
        if isinstance(_inb_network, Unset):
            inb_network = UNSET
        else:
            inb_network = NodeSpecNetworkV1PlatformPOST.from_dict(_inb_network)

        _oob_network = d.pop("oobNetwork", UNSET)
        oob_network: Union[Unset, NodeSpecNetworkV1PlatformPOST]
        if isinstance(_oob_network, Unset):
            oob_network = UNSET
        else:
            oob_network = NodeSpecNetworkV1PlatformPOST.from_dict(_oob_network)

        registered = d.pop("registered", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, NodeSpecWrapperV1PlatformPOSTRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = NodeSpecWrapperV1PlatformPOSTRole(_role)

        serial_number = d.pop("serialNumber", UNSET)

        node_spec_wrapper_v1_platform_post = cls(
            name=name,
            bgp_config=bgp_config,
            cimc_ip=cimc_ip,
            inb_network=inb_network,
            oob_network=oob_network,
            registered=registered,
            role=role,
            serial_number=serial_number,
        )

        node_spec_wrapper_v1_platform_post.additional_properties = d
        return node_spec_wrapper_v1_platform_post

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
