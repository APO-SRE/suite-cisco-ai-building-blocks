from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_store_v1_eventmonitoring_put import EventStoreV1EventmonitoringPUT


T = TypeVar("T", bound="EventConfigStatusWrapperV1EventmonitoringPUT")


@_attrs_define
class EventConfigStatusWrapperV1EventmonitoringPUT:
    """
    Attributes:
        error (Union[Unset, str]): Last observed error, if any.
        event_store (Union[Unset, EventStoreV1EventmonitoringPUT]): Store of event records with currently active
            lifecycle
    """

    error: Union[Unset, str] = UNSET
    event_store: Union[Unset, "EventStoreV1EventmonitoringPUT"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        event_store: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_store, Unset):
            event_store = self.event_store.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if event_store is not UNSET:
            field_dict["eventStore"] = event_store

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_store_v1_eventmonitoring_put import EventStoreV1EventmonitoringPUT

        d = dict(src_dict)
        error = d.pop("error", UNSET)

        _event_store = d.pop("eventStore", UNSET)
        event_store: Union[Unset, EventStoreV1EventmonitoringPUT]
        if isinstance(_event_store, Unset):
            event_store = UNSET
        else:
            event_store = EventStoreV1EventmonitoringPUT.from_dict(_event_store)

        event_config_status_wrapper_v1_eventmonitoring_put = cls(
            error=error,
            event_store=event_store,
        )

        event_config_status_wrapper_v1_eventmonitoring_put.additional_properties = d
        return event_config_status_wrapper_v1_eventmonitoring_put

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
