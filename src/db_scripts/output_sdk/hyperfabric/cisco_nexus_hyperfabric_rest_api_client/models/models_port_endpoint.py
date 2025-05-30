from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsPortEndpoint")


@_attrs_define
class ModelsPortEndpoint:
    """PortEndpoint defines a globally unique port location or endpoint.

    Attributes:
        node_id (Union[Unset, str]): The external identifier of the node.
        node_name (Union[Unset, str]): User defined name of the node.
        port_name (Union[Unset, str]): The canonical name of port (E.g. Ethernet1_1).
    """

    node_id: Union[Unset, str] = UNSET
    node_name: Union[Unset, str] = UNSET
    port_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_id = self.node_id

        node_name = self.node_name

        port_name = self.port_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if node_name is not UNSET:
            field_dict["nodeName"] = node_name
        if port_name is not UNSET:
            field_dict["portName"] = port_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        node_id = d.pop("nodeId", UNSET)

        node_name = d.pop("nodeName", UNSET)

        port_name = d.pop("portName", UNSET)

        models_port_endpoint = cls(
            node_id=node_id,
            node_name=node_name,
            port_name=port_name,
        )

        models_port_endpoint.additional_properties = d
        return models_port_endpoint

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
