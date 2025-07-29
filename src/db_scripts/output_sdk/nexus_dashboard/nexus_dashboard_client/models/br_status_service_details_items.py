from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BrStatusServiceDetailsItems")


@_attrs_define
class BrStatusServiceDetailsItems:
    """
    Attributes:
        name (Union[Unset, str]): Task name
        timeout (Union[Unset, int]): Overall timeout in seconds
        progress_weight (Union[Unset, int]): Progress weight of task in overall context.
        current_progress (Union[Unset, int]): Current progress for this task
        failure_reason (Union[Unset, str]): Failure reason if the operation failed for some reason
        success_message (Union[Unset, str]): Additional success message for users
    """

    name: Union[Unset, str] = UNSET
    timeout: Union[Unset, int] = UNSET
    progress_weight: Union[Unset, int] = UNSET
    current_progress: Union[Unset, int] = UNSET
    failure_reason: Union[Unset, str] = UNSET
    success_message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        timeout = self.timeout

        progress_weight = self.progress_weight

        current_progress = self.current_progress

        failure_reason = self.failure_reason

        success_message = self.success_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if progress_weight is not UNSET:
            field_dict["progressWeight"] = progress_weight
        if current_progress is not UNSET:
            field_dict["currentProgress"] = current_progress
        if failure_reason is not UNSET:
            field_dict["failureReason"] = failure_reason
        if success_message is not UNSET:
            field_dict["successMessage"] = success_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        timeout = d.pop("timeout", UNSET)

        progress_weight = d.pop("progressWeight", UNSET)

        current_progress = d.pop("currentProgress", UNSET)

        failure_reason = d.pop("failureReason", UNSET)

        success_message = d.pop("successMessage", UNSET)

        br_status_service_details_items = cls(
            name=name,
            timeout=timeout,
            progress_weight=progress_weight,
            current_progress=current_progress,
            failure_reason=failure_reason,
            success_message=success_message,
        )

        br_status_service_details_items.additional_properties = d
        return br_status_service_details_items

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
