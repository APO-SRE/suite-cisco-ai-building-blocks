from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_os_type import ModelsOsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigDevice")


@_attrs_define
class ConfigDevice:
    """Metadata about a device.

    Attributes:
        device_id (Union[Unset, str]): The device id.
        fabric_id (Union[Unset, str]): The fabric id that the device belong to.
        model_name (Union[Unset, str]): The device model name.
        name (Union[Unset, str]): The name of the device.
        node_id (Union[Unset, str]): The node id to which the device is bound.
        os_type (Union[Unset, ModelsOsType]): OsType lists various device operating system types.
        rack_id (Union[Unset, str]): The rack id where the device is installed.
        roles (Union[Unset, list[int]]): The roles supported by the device.
        serial_number (Union[Unset, str]): The device serial number.
    """

    device_id: Union[Unset, str] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    model_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    os_type: Union[Unset, ModelsOsType] = UNSET
    rack_id: Union[Unset, str] = UNSET
    roles: Union[Unset, list[int]] = UNSET
    serial_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        fabric_id = self.fabric_id

        model_name = self.model_name

        name = self.name

        node_id = self.node_id

        os_type: Union[Unset, str] = UNSET
        if not isinstance(self.os_type, Unset):
            os_type = self.os_type.value

        rack_id = self.rack_id

        roles: Union[Unset, list[int]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        serial_number = self.serial_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if fabric_id is not UNSET:
            field_dict["fabricId"] = fabric_id
        if model_name is not UNSET:
            field_dict["modelName"] = model_name
        if name is not UNSET:
            field_dict["name"] = name
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if os_type is not UNSET:
            field_dict["osType"] = os_type
        if rack_id is not UNSET:
            field_dict["rackId"] = rack_id
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

        model_name = d.pop("modelName", UNSET)

        name = d.pop("name", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _os_type = d.pop("osType", UNSET)
        os_type: Union[Unset, ModelsOsType]
        if isinstance(_os_type, Unset):
            os_type = UNSET
        else:
            os_type = ModelsOsType(_os_type)

        rack_id = d.pop("rackId", UNSET)

        roles = cast(list[int], d.pop("roles", UNSET))

        serial_number = d.pop("serialNumber", UNSET)

        config_device = cls(
            device_id=device_id,
            fabric_id=fabric_id,
            model_name=model_name,
            name=name,
            node_id=node_id,
            os_type=os_type,
            rack_id=rack_id,
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
