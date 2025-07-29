from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_spec_wrapper_v1_platform_get_role import NodeSpecWrapperV1PlatformGETRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_spec_bgp_config_v1_platform_get import NodeSpecBgpConfigV1PlatformGET
    from ..models.node_spec_network_v1_platform_get import NodeSpecNetworkV1PlatformGET


T = TypeVar("T", bound="NodeSpecWrapperV1PlatformGET")


@_attrs_define
class NodeSpecWrapperV1PlatformGET:
    """
    Attributes:
        bgp_config (Union[Unset, NodeSpecBgpConfigV1PlatformGET]): Node BGP config
        cimc_ip (Union[Unset, str]): Node cimc IP (physical only)
        inb_network (Union[Unset, NodeSpecNetworkV1PlatformGET]): Node Network config. Inband represents cluster
            internal network information, OOB represents user-accessible network information
        name (Union[Unset, str]): Node name
        oob_network (Union[Unset, NodeSpecNetworkV1PlatformGET]): Node Network config. Inband represents cluster
            internal network information, OOB represents user-accessible network information
        registered (Union[Unset, bool]): Node registered flag
        role (Union[Unset, NodeSpecWrapperV1PlatformGETRole]): Node role
        serial_number (Union[Unset, str]): Node serial number
    """

    bgp_config: Union[Unset, "NodeSpecBgpConfigV1PlatformGET"] = UNSET
    cimc_ip: Union[Unset, str] = UNSET
    inb_network: Union[Unset, "NodeSpecNetworkV1PlatformGET"] = UNSET
    name: Union[Unset, str] = UNSET
    oob_network: Union[Unset, "NodeSpecNetworkV1PlatformGET"] = UNSET
    registered: Union[Unset, bool] = UNSET
    role: Union[Unset, NodeSpecWrapperV1PlatformGETRole] = UNSET
    serial_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bgp_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bgp_config, Unset):
            bgp_config = self.bgp_config.to_dict()

        cimc_ip = self.cimc_ip

        inb_network: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.inb_network, Unset):
            inb_network = self.inb_network.to_dict()

        name = self.name

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
        field_dict.update({})
        if bgp_config is not UNSET:
            field_dict["bgpConfig"] = bgp_config
        if cimc_ip is not UNSET:
            field_dict["cimcIP"] = cimc_ip
        if inb_network is not UNSET:
            field_dict["inbNetwork"] = inb_network
        if name is not UNSET:
            field_dict["name"] = name
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
        from ..models.node_spec_bgp_config_v1_platform_get import NodeSpecBgpConfigV1PlatformGET
        from ..models.node_spec_network_v1_platform_get import NodeSpecNetworkV1PlatformGET

        d = dict(src_dict)
        _bgp_config = d.pop("bgpConfig", UNSET)
        bgp_config: Union[Unset, NodeSpecBgpConfigV1PlatformGET]
        if isinstance(_bgp_config, Unset):
            bgp_config = UNSET
        else:
            bgp_config = NodeSpecBgpConfigV1PlatformGET.from_dict(_bgp_config)

        cimc_ip = d.pop("cimcIP", UNSET)

        _inb_network = d.pop("inbNetwork", UNSET)
        inb_network: Union[Unset, NodeSpecNetworkV1PlatformGET]
        if isinstance(_inb_network, Unset):
            inb_network = UNSET
        else:
            inb_network = NodeSpecNetworkV1PlatformGET.from_dict(_inb_network)

        name = d.pop("name", UNSET)

        _oob_network = d.pop("oobNetwork", UNSET)
        oob_network: Union[Unset, NodeSpecNetworkV1PlatformGET]
        if isinstance(_oob_network, Unset):
            oob_network = UNSET
        else:
            oob_network = NodeSpecNetworkV1PlatformGET.from_dict(_oob_network)

        registered = d.pop("registered", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, NodeSpecWrapperV1PlatformGETRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = NodeSpecWrapperV1PlatformGETRole(_role)

        serial_number = d.pop("serialNumber", UNSET)

        node_spec_wrapper_v1_platform_get = cls(
            bgp_config=bgp_config,
            cimc_ip=cimc_ip,
            inb_network=inb_network,
            name=name,
            oob_network=oob_network,
            registered=registered,
            role=role,
            serial_number=serial_number,
        )

        node_spec_wrapper_v1_platform_get.additional_properties = d
        return node_spec_wrapper_v1_platform_get

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
