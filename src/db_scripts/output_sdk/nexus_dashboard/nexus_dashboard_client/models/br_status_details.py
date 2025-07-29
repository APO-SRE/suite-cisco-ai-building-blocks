from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.br_status_details_service_details import BrStatusDetailsServiceDetails


T = TypeVar("T", bound="BrStatusDetails")


@_attrs_define
class BrStatusDetails:
    """Backup/Restore operation details

    Attributes:
        progress (Union[Unset, int]): Overall progress
        progress_msg (Union[Unset, str]): Overall progress message
        service_details (Union[Unset, BrStatusDetailsServiceDetails]):
    """

    progress: Union[Unset, int] = UNSET
    progress_msg: Union[Unset, str] = UNSET
    service_details: Union[Unset, "BrStatusDetailsServiceDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        progress = self.progress

        progress_msg = self.progress_msg

        service_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.service_details, Unset):
            service_details = self.service_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if progress is not UNSET:
            field_dict["progress"] = progress
        if progress_msg is not UNSET:
            field_dict["progressMsg"] = progress_msg
        if service_details is not UNSET:
            field_dict["serviceDetails"] = service_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.br_status_details_service_details import BrStatusDetailsServiceDetails

        d = dict(src_dict)
        progress = d.pop("progress", UNSET)

        progress_msg = d.pop("progressMsg", UNSET)

        _service_details = d.pop("serviceDetails", UNSET)
        service_details: Union[Unset, BrStatusDetailsServiceDetails]
        if isinstance(_service_details, Unset):
            service_details = UNSET
        else:
            service_details = BrStatusDetailsServiceDetails.from_dict(_service_details)

        br_status_details = cls(
            progress=progress,
            progress_msg=progress_msg,
            service_details=service_details,
        )

        br_status_details.additional_properties = d
        return br_status_details

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
