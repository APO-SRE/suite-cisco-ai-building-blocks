from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_node_role import ModelsNodeRole
from ..models.models_node_type import ModelsNodeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigDevice")


@_attrs_define
class ConfigDevice:
    """A Device is a physical device such as a Cisco 6000 switch managed by Cisco Nexus Hyperfabric that can be bound to a
    node in a fabric.

        Attributes:
            device_id (Union[Unset, str]): This is a read-only field. The device identifier of the device.
            fabric_id (Union[Unset, str]): This is a read-only field. The unique identifier of the fabric of the node to
                which the device is bound.
            fabric_name (Union[Unset, str]): This is a read-only field. The name of the fabric that the devices belongs to.
            model_name (Union[Unset, str]): This is a read-only field. The model name of the device.
            name (Union[Unset, str]): This is a read-only field. The name of the device.
            node_id (Union[Unset, str]): This is a read-only field. The unique identifier of the node to which the device is
                bound.
            node_type (Union[Unset, ModelsNodeType]): NodeType defines an enumeration of node types.
            roles (Union[Unset, list[ModelsNodeRole]]): This is a read-only field. A list of roles associated with the node
                to which the device is bound.
            serial_number (Union[Unset, str]): This is a read-only field. The serial number of the device.
    """

    device_id: Union[Unset, str] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    fabric_name: Union[Unset, str] = UNSET
    model_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    node_type: Union[Unset, ModelsNodeType] = UNSET
    roles: Union[Unset, list[ModelsNodeRole]] = UNSET
    serial_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        fabric_id = self.fabric_id

        fabric_name = self.fabric_name

        model_name = self.model_name

        name = self.name

        node_id = self.node_id

        node_type: Union[Unset, str] = UNSET
        if not isinstance(self.node_type, Unset):
            node_type = self.node_type.value

        roles: Union[Unset, list[str]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.value
                roles.append(roles_item)

        serial_number = self.serial_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if fabric_id is not UNSET:
            field_dict["fabricId"] = fabric_id
        if fabric_name is not UNSET:
            field_dict["fabricName"] = fabric_name
        if model_name is not UNSET:
            field_dict["modelName"] = model_name
        if name is not UNSET:
            field_dict["name"] = name
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type
        if roles is not UNSET:
            field_dict["roles"] = roles
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device_id = d.pop("deviceId", UNSET)

        fabric_id = d.pop("fabricId", UNSET)

        fabric_name = d.pop("fabricName", UNSET)

        model_name = d.pop("modelName", UNSET)

        name = d.pop("name", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _node_type = d.pop("nodeType", UNSET)
        node_type: Union[Unset, ModelsNodeType]
        if isinstance(_node_type, Unset):
            node_type = UNSET
        else:
            node_type = ModelsNodeType(_node_type)

        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = ModelsNodeRole(roles_item_data)

            roles.append(roles_item)

        serial_number = d.pop("serialNumber", UNSET)

        config_device = cls(
            device_id=device_id,
            fabric_id=fabric_id,
            fabric_name=fabric_name,
            model_name=model_name,
            name=name,
            node_id=node_id,
            node_type=node_type,
            roles=roles,
            serial_number=serial_number,
        )

        config_device.additional_properties = d
        return config_device

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
