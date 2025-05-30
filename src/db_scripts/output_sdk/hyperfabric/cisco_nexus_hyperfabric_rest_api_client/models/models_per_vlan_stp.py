from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_metadata import ModelsMetadata


T = TypeVar("T", bound="ModelsPerVlanStp")


@_attrs_define
class ModelsPerVlanStp:
    """PerVlanStp encapsulates properties of a Per-Vlan spanning tree protocol config object. There can be only one
    PerVlanStp config for a fabric.

        Attributes:
            enabled (Union[Unset, bool]): Indicates if PerVlanStp is enabled or disabled.
            fabric_id (Union[Unset, str]): The identifier of Fabric to which this PerVlanStp belong. Fabric identifier is
                mandatory, and immutable once set.
            forward_delay (Union[Unset, int]): Packet forward delay time in seconds. Default value is 15s, and range is
                4-30s.
            hello_interval (Union[Unset, int]): Hello interval in seconds for transmission of BPDUs. Default values is 2s,
                and range is 1-10s.
            max_age (Union[Unset, int]): Maximum time to listen for root bridge in seconds. Default value is 20s, and range
                is 6-40s.
            metadata (Union[Unset, ModelsMetadata]): Metadata defines metadata of all objects in the service.
            priority (Union[Unset, int]): Bridge priority value as a multiple of 4096. Default is 32768, and range is
                4096-61440.
            root_guard_timeout (Union[Unset, int]): Switch waits for timeout duration before moving the port to forwarding
                state when superior BPDUs (Bridge Protocol Data Unit) stop coming to the port. Default value is 30s, and range
                is 5-600s.
            stp_mac (Union[Unset, str]): Bridge MAC address. User is expected to set the lowest MAC address to make this
                Fabric as the root of spanning tree.
    """

    enabled: Union[Unset, bool] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    forward_delay: Union[Unset, int] = UNSET
    hello_interval: Union[Unset, int] = UNSET
    max_age: Union[Unset, int] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    priority: Union[Unset, int] = UNSET
    root_guard_timeout: Union[Unset, int] = UNSET
    stp_mac: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        fabric_id = self.fabric_id

        forward_delay = self.forward_delay

        hello_interval = self.hello_interval

        max_age = self.max_age

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        priority = self.priority

        root_guard_timeout = self.root_guard_timeout

        stp_mac = self.stp_mac

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if fabric_id is not UNSET:
            field_dict["fabricId"] = fabric_id
        if forward_delay is not UNSET:
            field_dict["forwardDelay"] = forward_delay
        if hello_interval is not UNSET:
            field_dict["helloInterval"] = hello_interval
        if max_age is not UNSET:
            field_dict["maxAge"] = max_age
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if priority is not UNSET:
            field_dict["priority"] = priority
        if root_guard_timeout is not UNSET:
            field_dict["rootGuardTimeout"] = root_guard_timeout
        if stp_mac is not UNSET:
            field_dict["stpMac"] = stp_mac

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_metadata import ModelsMetadata

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        fabric_id = d.pop("fabricId", UNSET)

        forward_delay = d.pop("forwardDelay", UNSET)

        hello_interval = d.pop("helloInterval", UNSET)

        max_age = d.pop("maxAge", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        priority = d.pop("priority", UNSET)

        root_guard_timeout = d.pop("rootGuardTimeout", UNSET)

        stp_mac = d.pop("stpMac", UNSET)

        models_per_vlan_stp = cls(
            enabled=enabled,
            fabric_id=fabric_id,
            forward_delay=forward_delay,
            hello_interval=hello_interval,
            max_age=max_age,
            metadata=metadata,
            priority=priority,
            root_guard_timeout=root_guard_timeout,
            stp_mac=stp_mac,
        )

        models_per_vlan_stp.additional_properties = d
        return models_per_vlan_stp

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
