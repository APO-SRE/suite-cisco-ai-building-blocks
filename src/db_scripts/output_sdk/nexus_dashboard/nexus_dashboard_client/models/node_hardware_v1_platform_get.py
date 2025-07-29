from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_status_cpu_v1_platform_get import NodeStatusCpuV1PlatformGET
    from ..models.node_status_disk_v1_platform_get import NodeStatusDiskV1PlatformGET
    from ..models.node_status_memory_v1_platform_get import NodeStatusMemoryV1PlatformGET


T = TypeVar("T", bound="NodeHardwareV1PlatformGET")


@_attrs_define
class NodeHardwareV1PlatformGET:
    """Hardware specs of the node

    Attributes:
        cpu (Union[Unset, NodeStatusCpuV1PlatformGET]): Node Cpu stats
        disks (Union[Unset, list['NodeStatusDiskV1PlatformGET']]): Node disk list
        memory (Union[Unset, NodeStatusMemoryV1PlatformGET]): Node Memory stats
    """

    cpu: Union[Unset, "NodeStatusCpuV1PlatformGET"] = UNSET
    disks: Union[Unset, list["NodeStatusDiskV1PlatformGET"]] = UNSET
    memory: Union[Unset, "NodeStatusMemoryV1PlatformGET"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cpu, Unset):
            cpu = self.cpu.to_dict()

        disks: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.disks, Unset):
            disks = []
            for disks_item_data in self.disks:
                disks_item = disks_item_data.to_dict()
                disks.append(disks_item)

        memory: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.memory, Unset):
            memory = self.memory.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if disks is not UNSET:
            field_dict["disks"] = disks
        if memory is not UNSET:
            field_dict["memory"] = memory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node_status_cpu_v1_platform_get import NodeStatusCpuV1PlatformGET
        from ..models.node_status_disk_v1_platform_get import NodeStatusDiskV1PlatformGET
        from ..models.node_status_memory_v1_platform_get import NodeStatusMemoryV1PlatformGET

        d = dict(src_dict)
        _cpu = d.pop("cpu", UNSET)
        cpu: Union[Unset, NodeStatusCpuV1PlatformGET]
        if isinstance(_cpu, Unset):
            cpu = UNSET
        else:
            cpu = NodeStatusCpuV1PlatformGET.from_dict(_cpu)

        disks = []
        _disks = d.pop("disks", UNSET)
        for disks_item_data in _disks or []:
            disks_item = NodeStatusDiskV1PlatformGET.from_dict(disks_item_data)

            disks.append(disks_item)

        _memory = d.pop("memory", UNSET)
        memory: Union[Unset, NodeStatusMemoryV1PlatformGET]
        if isinstance(_memory, Unset):
            memory = UNSET
        else:
            memory = NodeStatusMemoryV1PlatformGET.from_dict(_memory)

        node_hardware_v1_platform_get = cls(
            cpu=cpu,
            disks=disks,
            memory=memory,
        )

        node_hardware_v1_platform_get.additional_properties = d
        return node_hardware_v1_platform_get

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
