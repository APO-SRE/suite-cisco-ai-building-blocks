from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetentionPolicyV1EventmonitoringGET")


@_attrs_define
class RetentionPolicyV1EventmonitoringGET:
    """Retention policy for the generated event records as part of the parent event configuration

    Attributes:
        count (Union[Unset, int]): Total number of most recent event records to retain
        duration (Union[Unset, str]): Duration for which event records should be retained
        size (Union[Unset, str]): Upper limit on the size of the event records to retain. Units in d (days), m (minutes)
            or s (seconds). For example - 20m will retain event records for 20 minutes
    """

    count: Union[Unset, int] = UNSET
    duration: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        duration = self.duration

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if duration is not UNSET:
            field_dict["duration"] = duration
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        duration = d.pop("duration", UNSET)

        size = d.pop("size", UNSET)

        retention_policy_v1_eventmonitoring_get = cls(
            count=count,
            duration=duration,
            size=size,
        )

        retention_policy_v1_eventmonitoring_get.additional_properties = d
        return retention_policy_v1_eventmonitoring_get

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
