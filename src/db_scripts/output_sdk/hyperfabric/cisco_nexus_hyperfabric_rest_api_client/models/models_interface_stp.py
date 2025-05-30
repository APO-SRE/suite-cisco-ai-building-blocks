from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsInterfaceStp")


@_attrs_define
class ModelsInterfaceStp:
    """InterfaceStp encapsulates configurable STP parameters of a single interface. Interface/Port must be a member of a
    Vlan for the config to be applied.

        Attributes:
            bpdu_guard (Union[Unset, bool]): BPDU Guard feature enables/disables the connected device's ability to initiate
                or participate in STP on edge ports. When STP BPDUs are received on the port where BPDU guard is enabled the
                port will be shutdown. User can re-enable the port administratively after ensuring the BPDUs have stopped coming
                on the port.
            enabled (Union[Unset, bool]): Enable/Disable spanning-tree protocol config for the port. Spanning-tree is
                enabled only when at least one of the properties is also enabled.
            name (Union[Unset, str]): The name of the NetworkPort or PortChannel.
            port_fast (Union[Unset, bool]): Port-fast command is enabled by default on all ports, port-fast allows edge
                ports to move to forwarding state quickly when the connected device is not participating in spanning-tree.
            root_guard (Union[Unset, bool]): Enforce the root bridge placement in the network and allows STP to interoperate
                with user network bridges while still maintaining the bridged network topology that the administrator requires.
                When BPDUs are received on a root guard enabled port, the STP state will be moved to "Root inconsistent" state
                to indicate this condition. Once the port stops receiving superior BPDUs, Root Guard will automatically set the
                port back to a FORWARDING state after the timeout period has expired.
            uplink_fast (Union[Unset, bool]): Uplink fast feature enhances STP performance for switches with redundant
                uplinks. Using the default value for the standard STP forward delay, convergence following a transition from an
                active link to a redundant link can take 30 seconds; 15 seconds for listening and an additional 15 seconds for
                learning.
    """

    bpdu_guard: Union[Unset, bool] = UNSET
    enabled: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    port_fast: Union[Unset, bool] = UNSET
    root_guard: Union[Unset, bool] = UNSET
    uplink_fast: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bpdu_guard = self.bpdu_guard

        enabled = self.enabled

        name = self.name

        port_fast = self.port_fast

        root_guard = self.root_guard

        uplink_fast = self.uplink_fast

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bpdu_guard is not UNSET:
            field_dict["bpduGuard"] = bpdu_guard
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if name is not UNSET:
            field_dict["name"] = name
        if port_fast is not UNSET:
            field_dict["portFast"] = port_fast
        if root_guard is not UNSET:
            field_dict["rootGuard"] = root_guard
        if uplink_fast is not UNSET:
            field_dict["uplinkFast"] = uplink_fast

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bpdu_guard = d.pop("bpduGuard", UNSET)

        enabled = d.pop("enabled", UNSET)

        name = d.pop("name", UNSET)

        port_fast = d.pop("portFast", UNSET)

        root_guard = d.pop("rootGuard", UNSET)

        uplink_fast = d.pop("uplinkFast", UNSET)

        models_interface_stp = cls(
            bpdu_guard=bpdu_guard,
            enabled=enabled,
            name=name,
            port_fast=port_fast,
            root_guard=root_guard,
            uplink_fast=uplink_fast,
        )

        models_interface_stp.additional_properties = d
        return models_interface_stp

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
