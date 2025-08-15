from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_config_v1_eventmonitoring_get import EventConfigV1EventmonitoringGET
    from ..models.event_config_v1_eventmonitoring_getlist_metadata import EventConfigV1EventmonitoringGETLISTMetadata


T = TypeVar("T", bound="EventConfigV1EventmonitoringGETLIST")


@_attrs_define
class EventConfigV1EventmonitoringGETLIST:
    """Configuration to monitor a specific or group of resources on ND

    Attributes:
        items (Union[Unset, list['EventConfigV1EventmonitoringGET']]):
        metadata (Union[Unset, EventConfigV1EventmonitoringGETLISTMetadata]):
    """

    items: Union[Unset, list["EventConfigV1EventmonitoringGET"]] = UNSET
    metadata: Union[Unset, "EventConfigV1EventmonitoringGETLISTMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_config_v1_eventmonitoring_get import EventConfigV1EventmonitoringGET
        from ..models.event_config_v1_eventmonitoring_getlist_metadata import (
            EventConfigV1EventmonitoringGETLISTMetadata,
        )

        d = dict(src_dict)
        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = EventConfigV1EventmonitoringGET.from_dict(items_item_data)

            items.append(items_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, EventConfigV1EventmonitoringGETLISTMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = EventConfigV1EventmonitoringGETLISTMetadata.from_dict(_metadata)

        event_config_v1_eventmonitoring_getlist = cls(
            items=items,
            metadata=metadata,
        )

        event_config_v1_eventmonitoring_getlist.additional_properties = d
        return event_config_v1_eventmonitoring_getlist

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
