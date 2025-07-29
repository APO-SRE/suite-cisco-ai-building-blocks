from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.br_status_service_details_items import BrStatusServiceDetailsItems


T = TypeVar("T", bound="BrStatusServiceDetails")


@_attrs_define
class BrStatusServiceDetails:
    """Service details

    Attributes:
        progress (Union[Unset, int]): Overall service progress
        details (Union[Unset, list['BrStatusServiceDetailsItems']]): Service-specific details
    """

    progress: Union[Unset, int] = UNSET
    details: Union[Unset, list["BrStatusServiceDetailsItems"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        progress = self.progress

        details: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()
                details.append(details_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if progress is not UNSET:
            field_dict["progress"] = progress
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.br_status_service_details_items import BrStatusServiceDetailsItems

        d = dict(src_dict)
        progress = d.pop("progress", UNSET)

        details = []
        _details = d.pop("details", UNSET)
        for details_item_data in _details or []:
            details_item = BrStatusServiceDetailsItems.from_dict(details_item_data)

            details.append(details_item)

        br_status_service_details = cls(
            progress=progress,
            details=details,
        )

        br_status_service_details.additional_properties = d
        return br_status_service_details

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
