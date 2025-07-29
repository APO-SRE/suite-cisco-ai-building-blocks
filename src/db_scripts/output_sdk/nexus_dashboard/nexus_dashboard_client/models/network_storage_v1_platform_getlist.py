from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_storage_v1_platform_get import NetworkStorageV1PlatformGET
    from ..models.network_storage_v1_platform_getlist_metadata import NetworkStorageV1PlatformGETLISTMetadata


T = TypeVar("T", bound="NetworkStorageV1PlatformGETLIST")


@_attrs_define
class NetworkStorageV1PlatformGETLIST:
    """Network attached storage config

    Attributes:
        items (Union[Unset, list['NetworkStorageV1PlatformGET']]):
        metadata (Union[Unset, NetworkStorageV1PlatformGETLISTMetadata]):
    """

    items: Union[Unset, list["NetworkStorageV1PlatformGET"]] = UNSET
    metadata: Union[Unset, "NetworkStorageV1PlatformGETLISTMetadata"] = UNSET
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
        from ..models.network_storage_v1_platform_get import NetworkStorageV1PlatformGET
        from ..models.network_storage_v1_platform_getlist_metadata import NetworkStorageV1PlatformGETLISTMetadata

        d = dict(src_dict)
        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = NetworkStorageV1PlatformGET.from_dict(items_item_data)

            items.append(items_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, NetworkStorageV1PlatformGETLISTMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = NetworkStorageV1PlatformGETLISTMetadata.from_dict(_metadata)

        network_storage_v1_platform_getlist = cls(
            items=items,
            metadata=metadata,
        )

        network_storage_v1_platform_getlist.additional_properties = d
        return network_storage_v1_platform_getlist

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
