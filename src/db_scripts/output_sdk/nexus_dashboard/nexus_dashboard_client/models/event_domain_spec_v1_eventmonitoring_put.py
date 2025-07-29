from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventDomainSpecV1EventmonitoringPUT")


@_attrs_define
class EventDomainSpecV1EventmonitoringPUT:
    """Spec portion of EventDomain resource

    Attributes:
        event_configs (Union[Unset, list[str]]): List of child event configurations
        meta_name (Union[Unset, str]): Unique Domain name
    """

    event_configs: Union[Unset, list[str]] = UNSET
    meta_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_configs: Union[Unset, list[str]] = UNSET
        if not isinstance(self.event_configs, Unset):
            event_configs = self.event_configs

        meta_name = self.meta_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_configs is not UNSET:
            field_dict["eventConfigs"] = event_configs
        if meta_name is not UNSET:
            field_dict["metaName"] = meta_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_configs = cast(list[str], d.pop("eventConfigs", UNSET))

        meta_name = d.pop("metaName", UNSET)

        event_domain_spec_v1_eventmonitoring_put = cls(
            event_configs=event_configs,
            meta_name=meta_name,
        )

        event_domain_spec_v1_eventmonitoring_put.additional_properties = d
        return event_domain_spec_v1_eventmonitoring_put

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
