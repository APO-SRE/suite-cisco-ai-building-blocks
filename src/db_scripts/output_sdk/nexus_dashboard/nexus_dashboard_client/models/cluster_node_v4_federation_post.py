from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cluster_node_v4_federation_post_current_state import ClusterNodeV4FederationPOSTCurrentState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterNodeV4FederationPOST")


@_attrs_define
class ClusterNodeV4FederationPOST:
    """
    Attributes:
        current_state (Union[Unset, ClusterNodeV4FederationPOSTCurrentState]): Current state of the node
        data_ip (Union[Unset, str]): data/in-band IP of the node
        management_ip (Union[Unset, str]): management/out-of-band IP of the node
        management_i_pv_6 (Union[Unset, str]): management/out-of-band IPv6 of the node
        name (Union[Unset, str]): Name of the node
        serial_number (Union[Unset, str]): serial number of the node
        version (Union[Unset, str]): Image version of the node
    """

    current_state: Union[Unset, ClusterNodeV4FederationPOSTCurrentState] = UNSET
    data_ip: Union[Unset, str] = UNSET
    management_ip: Union[Unset, str] = UNSET
    management_i_pv_6: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_state: Union[Unset, str] = UNSET
        if not isinstance(self.current_state, Unset):
            current_state = self.current_state.value

        data_ip = self.data_ip

        management_ip = self.management_ip

        management_i_pv_6 = self.management_i_pv_6

        name = self.name

        serial_number = self.serial_number

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_state is not UNSET:
            field_dict["currentState"] = current_state
        if data_ip is not UNSET:
            field_dict["dataIP"] = data_ip
        if management_ip is not UNSET:
            field_dict["managementIP"] = management_ip
        if management_i_pv_6 is not UNSET:
            field_dict["managementIPv6"] = management_i_pv_6
        if name is not UNSET:
            field_dict["name"] = name
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _current_state = d.pop("currentState", UNSET)
        current_state: Union[Unset, ClusterNodeV4FederationPOSTCurrentState]
        if isinstance(_current_state, Unset):
            current_state = UNSET
        else:
            current_state = ClusterNodeV4FederationPOSTCurrentState(_current_state)

        data_ip = d.pop("dataIP", UNSET)

        management_ip = d.pop("managementIP", UNSET)

        management_i_pv_6 = d.pop("managementIPv6", UNSET)

        name = d.pop("name", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        version = d.pop("version", UNSET)

        cluster_node_v4_federation_post = cls(
            current_state=current_state,
            data_ip=data_ip,
            management_ip=management_ip,
            management_i_pv_6=management_i_pv_6,
            name=name,
            serial_number=serial_number,
            version=version,
        )

        cluster_node_v4_federation_post.additional_properties = d
        return cluster_node_v4_federation_post

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
