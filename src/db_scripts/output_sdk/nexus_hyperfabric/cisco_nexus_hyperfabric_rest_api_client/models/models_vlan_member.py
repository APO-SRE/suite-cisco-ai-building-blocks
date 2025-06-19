from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_port_endpoint import ModelsPortEndpoint


T = TypeVar("T", bound="ModelsVlanMember")


@_attrs_define
class ModelsVlanMember:
    """A VNI VLAN Member represents the attachement of a specific VNI to a port or port channel untagged or using a dot1q
    VLAN ID (also known as a trunk). The role of the port or port channel has to be configured as `HOST_PORT`.

        Attributes:
            port (Union[Unset, ModelsPortEndpoint]): PortEndpoint defines a globally unique port location or endpoint.
            untagged (Union[Unset, bool]): The flag that defines if the VNI VLAN member is configured as untagged or not.
            vlan_id (Union[Unset, int]): The VLAN ID to be used as dot1Q encapsulation for the VNI on a port of the node or
                a port channel. The VLAN ID must be between 2 and 3600.
    """

    port: Union[Unset, "ModelsPortEndpoint"] = UNSET
    untagged: Union[Unset, bool] = UNSET
    vlan_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.port, Unset):
            port = self.port.to_dict()

        untagged = self.untagged

        vlan_id = self.vlan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if untagged is not UNSET:
            field_dict["untagged"] = untagged
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_port_endpoint import ModelsPortEndpoint

        d = dict(src_dict)
        _port = d.pop("port", UNSET)
        port: Union[Unset, ModelsPortEndpoint]
        if isinstance(_port, Unset):
            port = UNSET
        else:
            port = ModelsPortEndpoint.from_dict(_port)

        untagged = d.pop("untagged", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        models_vlan_member = cls(
            port=port,
            untagged=untagged,
            vlan_id=vlan_id,
        )

        models_vlan_member.additional_properties = d
        return models_vlan_member

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
