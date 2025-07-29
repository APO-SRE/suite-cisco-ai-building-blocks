from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventDomainSpecWrapperV1EventmonitoringPOST")


@_attrs_define
class EventDomainSpecWrapperV1EventmonitoringPOST:
    """
    Attributes:
        meta_name (str): Unique Domain name
        event_configs (Union[Unset, list[str]]): List of child event configurations
    """

    meta_name: str
    event_configs: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta_name = self.meta_name

        event_configs: Union[Unset, list[str]] = UNSET
        if not isinstance(self.event_configs, Unset):
            event_configs = self.event_configs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metaName": meta_name,
            }
        )
        if event_configs is not UNSET:
            field_dict["eventConfigs"] = event_configs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        meta_name = d.pop("metaName")

        event_configs = cast(list[str], d.pop("eventConfigs", UNSET))

        event_domain_spec_wrapper_v1_eventmonitoring_post = cls(
            meta_name=meta_name,
            event_configs=event_configs,
        )

        event_domain_spec_wrapper_v1_eventmonitoring_post.additional_properties = d
        return event_domain_spec_wrapper_v1_eventmonitoring_post

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
