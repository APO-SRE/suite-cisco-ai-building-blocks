from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_status_v1_platform_put_machine_type import NodeStatusV1PlatformPUTMachineType
from ..models.node_status_v1_platform_put_platform_type import NodeStatusV1PlatformPUTPlatformType
from ..models.node_status_v1_platform_put_state import NodeStatusV1PlatformPUTState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_hardware_v1_platform_put import NodeHardwareV1PlatformPUT
    from ..models.node_status_error_v1_platform_put import NodeStatusErrorV1PlatformPUT


T = TypeVar("T", bound="NodeStatusV1PlatformPUT")


@_attrs_define
class NodeStatusV1PlatformPUT:
    """Node status information

    Attributes:
        boot_time (Union[Unset, str]): Node's last boot time
        cluster_name (Union[Unset, str]): Cluster name
        error (Union[Unset, NodeStatusErrorV1PlatformPUT]): error is the last observed error, if any.
        firmware_upgrade_time (Union[Unset, str]): Node's last firmware upgrade time
        hardware_status (Union[Unset, NodeHardwareV1PlatformPUT]): Hardware specs of the node
        k_8_s_status (Union[Unset, str]): Node's K8 status
        machine_type (Union[Unset, NodeStatusV1PlatformPUTMachineType]): Node hardware type
        model (Union[Unset, str]): Node model
        platform_type (Union[Unset, NodeStatusV1PlatformPUTPlatformType]): Node platform type
        serf_status (Union[Unset, str]): Node's Serf status
        state (Union[Unset, NodeStatusV1PlatformPUTState]): Node operational Status
        uuid (Union[Unset, str]): Node id
        version (Union[Unset, str]): Node version
    """

    boot_time: Union[Unset, str] = UNSET
    cluster_name: Union[Unset, str] = UNSET
    error: Union[Unset, "NodeStatusErrorV1PlatformPUT"] = UNSET
    firmware_upgrade_time: Union[Unset, str] = UNSET
    hardware_status: Union[Unset, "NodeHardwareV1PlatformPUT"] = UNSET
    k_8_s_status: Union[Unset, str] = UNSET
    machine_type: Union[Unset, NodeStatusV1PlatformPUTMachineType] = UNSET
    model: Union[Unset, str] = UNSET
    platform_type: Union[Unset, NodeStatusV1PlatformPUTPlatformType] = UNSET
    serf_status: Union[Unset, str] = UNSET
    state: Union[Unset, NodeStatusV1PlatformPUTState] = UNSET
    uuid: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        boot_time = self.boot_time

        cluster_name = self.cluster_name

        error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        firmware_upgrade_time = self.firmware_upgrade_time

        hardware_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.hardware_status, Unset):
            hardware_status = self.hardware_status.to_dict()

        k_8_s_status = self.k_8_s_status

        machine_type: Union[Unset, str] = UNSET
        if not isinstance(self.machine_type, Unset):
            machine_type = self.machine_type.value

        model = self.model

        platform_type: Union[Unset, str] = UNSET
        if not isinstance(self.platform_type, Unset):
            platform_type = self.platform_type.value

        serf_status = self.serf_status

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        uuid = self.uuid

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if boot_time is not UNSET:
            field_dict["bootTime"] = boot_time
        if cluster_name is not UNSET:
            field_dict["clusterName"] = cluster_name
        if error is not UNSET:
            field_dict["error"] = error
        if firmware_upgrade_time is not UNSET:
            field_dict["firmwareUpgradeTime"] = firmware_upgrade_time
        if hardware_status is not UNSET:
            field_dict["hardwareStatus"] = hardware_status
        if k_8_s_status is not UNSET:
            field_dict["k8sStatus"] = k_8_s_status
        if machine_type is not UNSET:
            field_dict["machineType"] = machine_type
        if model is not UNSET:
            field_dict["model"] = model
        if platform_type is not UNSET:
            field_dict["platformType"] = platform_type
        if serf_status is not UNSET:
            field_dict["serfStatus"] = serf_status
        if state is not UNSET:
            field_dict["state"] = state
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node_hardware_v1_platform_put import NodeHardwareV1PlatformPUT
        from ..models.node_status_error_v1_platform_put import NodeStatusErrorV1PlatformPUT

        d = dict(src_dict)
        boot_time = d.pop("bootTime", UNSET)

        cluster_name = d.pop("clusterName", UNSET)

        _error = d.pop("error", UNSET)
        error: Union[Unset, NodeStatusErrorV1PlatformPUT]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = NodeStatusErrorV1PlatformPUT.from_dict(_error)

        firmware_upgrade_time = d.pop("firmwareUpgradeTime", UNSET)

        _hardware_status = d.pop("hardwareStatus", UNSET)
        hardware_status: Union[Unset, NodeHardwareV1PlatformPUT]
        if isinstance(_hardware_status, Unset):
            hardware_status = UNSET
        else:
            hardware_status = NodeHardwareV1PlatformPUT.from_dict(_hardware_status)

        k_8_s_status = d.pop("k8sStatus", UNSET)

        _machine_type = d.pop("machineType", UNSET)
        machine_type: Union[Unset, NodeStatusV1PlatformPUTMachineType]
        if isinstance(_machine_type, Unset):
            machine_type = UNSET
        else:
            machine_type = NodeStatusV1PlatformPUTMachineType(_machine_type)

        model = d.pop("model", UNSET)

        _platform_type = d.pop("platformType", UNSET)
        platform_type: Union[Unset, NodeStatusV1PlatformPUTPlatformType]
        if isinstance(_platform_type, Unset):
            platform_type = UNSET
        else:
            platform_type = NodeStatusV1PlatformPUTPlatformType(_platform_type)

        serf_status = d.pop("serfStatus", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, NodeStatusV1PlatformPUTState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = NodeStatusV1PlatformPUTState(_state)

        uuid = d.pop("uuid", UNSET)

        version = d.pop("version", UNSET)

        node_status_v1_platform_put = cls(
            boot_time=boot_time,
            cluster_name=cluster_name,
            error=error,
            firmware_upgrade_time=firmware_upgrade_time,
            hardware_status=hardware_status,
            k_8_s_status=k_8_s_status,
            machine_type=machine_type,
            model=model,
            platform_type=platform_type,
            serf_status=serf_status,
            state=state,
            uuid=uuid,
            version=version,
        )

        node_status_v1_platform_put.additional_properties = d
        return node_status_v1_platform_put

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
