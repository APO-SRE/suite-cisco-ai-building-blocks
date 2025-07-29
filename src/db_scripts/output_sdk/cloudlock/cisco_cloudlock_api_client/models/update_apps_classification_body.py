from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAppsClassificationBody")


@_attrs_define
class UpdateAppsClassificationBody:
    """
    Example:
        {'other_reason': 'Other Custom Reason', 'reason_id': 4, 'type': 'trusted'}

    Attributes:
        other_reason (Union[Unset, str]):
        reason_id (Union[Unset, float]):
        type_ (Union[Unset, str]):
    """

    other_reason: Union[Unset, str] = UNSET
    reason_id: Union[Unset, float] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        other_reason = self.other_reason

        reason_id = self.reason_id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if other_reason is not UNSET:
            field_dict["other_reason"] = other_reason
        if reason_id is not UNSET:
            field_dict["reason_id"] = reason_id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        other_reason = d.pop("other_reason", UNSET)

        reason_id = d.pop("reason_id", UNSET)

        type_ = d.pop("type", UNSET)

        update_apps_classification_body = cls(
            other_reason=other_reason,
            reason_id=reason_id,
            type_=type_,
        )

        update_apps_classification_body.additional_properties = d
        return update_apps_classification_body

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
