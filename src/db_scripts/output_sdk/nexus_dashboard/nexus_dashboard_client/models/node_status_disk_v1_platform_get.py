from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_status_disk_v1_platform_get_storage_controller import NodeStatusDiskV1PlatformGETStorageController
from ..models.node_status_disk_v1_platform_get_type import NodeStatusDiskV1PlatformGETType
from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeStatusDiskV1PlatformGET")


@_attrs_define
class NodeStatusDiskV1PlatformGET:
    """Node Disk Stats

    Attributes:
        capacity (Union[Unset, int]): Total size (Bytes)
        name (Union[Unset, str]): Disk name
        storage_controller (Union[Unset, NodeStatusDiskV1PlatformGETStorageController]):
        type_ (Union[Unset, NodeStatusDiskV1PlatformGETType]): Disk type
    """

    capacity: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    storage_controller: Union[Unset, NodeStatusDiskV1PlatformGETStorageController] = UNSET
    type_: Union[Unset, NodeStatusDiskV1PlatformGETType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        capacity = self.capacity

        name = self.name

        storage_controller: Union[Unset, str] = UNSET
        if not isinstance(self.storage_controller, Unset):
            storage_controller = self.storage_controller.value

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if name is not UNSET:
            field_dict["name"] = name
        if storage_controller is not UNSET:
            field_dict["storageController"] = storage_controller
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        capacity = d.pop("capacity", UNSET)

        name = d.pop("name", UNSET)

        _storage_controller = d.pop("storageController", UNSET)
        storage_controller: Union[Unset, NodeStatusDiskV1PlatformGETStorageController]
        if isinstance(_storage_controller, Unset):
            storage_controller = UNSET
        else:
            storage_controller = NodeStatusDiskV1PlatformGETStorageController(_storage_controller)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, NodeStatusDiskV1PlatformGETType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = NodeStatusDiskV1PlatformGETType(_type_)

        node_status_disk_v1_platform_get = cls(
            capacity=capacity,
            name=name,
            storage_controller=storage_controller,
            type_=type_,
        )

        node_status_disk_v1_platform_get.additional_properties = d
        return node_status_disk_v1_platform_get

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
