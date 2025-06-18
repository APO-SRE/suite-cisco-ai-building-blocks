from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_management_port import ModelsManagementPort


T = TypeVar("T", bound="ConfigManagementPortsResponse")


@_attrs_define
class ConfigManagementPortsResponse:
    """The response returned to a request for the list of management ports of a specific node in a fabric.

    Attributes:
        ports (Union[Unset, list['ModelsManagementPort']]): The list of management ports of a specific node.
    """

    ports: Union[Unset, list["ModelsManagementPort"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ports is not UNSET:
            field_dict["ports"] = ports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_management_port import ModelsManagementPort

        d = dict(src_dict)
        ports = []
        _ports = d.pop("ports", UNSET)
        for ports_item_data in _ports or []:
            ports_item = ModelsManagementPort.from_dict(ports_item_data)

            ports.append(ports_item)

        config_management_ports_response = cls(
            ports=ports,
        )

        config_management_ports_response.additional_properties = d
        return config_management_ports_response

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
