from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsInterfaceStp")


@_attrs_define
class ModelsInterfaceStp:
    """The Spanning Tree Protocol (STP) interface configuration for the port. The configuration is only used when a VLAN is
    deployed on the port.

        Attributes:
            bpdu_guard (Union[Unset, bool]): BPDU guard enforces that the connected device does not send STP BPDUs on the
                port. If STP BPDUs are received on the port where BPDU guard is enabled the port will be automatically shutdown.
                User can re-enable the port administratively after ensuring the BPDUs have stopped coming on the port.
            enabled (Union[Unset, bool]): The enabled state of the Spanning-Tree Protocol (STP) which indicates if STP is
                enabled or disabled on the port. Requires at least one of the other properties to also be enabled.
            port_fast (Union[Unset, bool]): PortFast allows ports to move to forwarding state quickly when the connected
                device that is not participating in spanning-tree. PortFast is enabled by default on all ports.
            root_guard (Union[Unset, bool]): Root guard enforces the root bridge placement in the network and allows STP to
                interoperate with user network bridges while still maintaining the bridged network topology that the
                administrator requires. When BPDUs are received on a root guard enabled port, the STP state will be moved to
                "Root inconsistent" state to indicate this condition. Once the port stops receiving superior BPDUs, root guard
                will automatically set the port back to a FORWARDING state after the timeout period has expired.
            uplink_fast (Union[Unset, bool]): UplinkFast feature enhances STP performance for switches with redundant
                uplinks. Using the default value for the standard STP forward delay, convergence following a transition from an
                active link to a redundant link can take up to 30 seconds; 15 seconds for listening and an additional 15 seconds
                for learning. UplinkFast maintains a list of backup path to the root bridge and immediately move one of the
                backup paths to forwarding state to speed up the network recovery.
    """

    bpdu_guard: Union[Unset, bool] = UNSET
    enabled: Union[Unset, bool] = UNSET
    port_fast: Union[Unset, bool] = UNSET
    root_guard: Union[Unset, bool] = UNSET
    uplink_fast: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bpdu_guard = self.bpdu_guard

        enabled = self.enabled

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

        port_fast = d.pop("portFast", UNSET)

        root_guard = d.pop("rootGuard", UNSET)

        uplink_fast = d.pop("uplinkFast", UNSET)

        models_interface_stp = cls(
            bpdu_guard=bpdu_guard,
            enabled=enabled,
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
