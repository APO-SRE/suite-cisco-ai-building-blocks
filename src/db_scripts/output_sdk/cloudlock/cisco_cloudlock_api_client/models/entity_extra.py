from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityExtra")


@_attrs_define
class EntityExtra:
    """The additional information related to the incident.

    Attributes:
        origin_type_label (Union[Unset, str]): This field gives additional info regarding the scanned object that
            triggered the policy violation.
        origin_type_label_plural (Union[Unset, str]): Similar to the origin_type_label but for a plural label
    """

    origin_type_label: Union[Unset, str] = UNSET
    origin_type_label_plural: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        origin_type_label = self.origin_type_label

        origin_type_label_plural = self.origin_type_label_plural

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if origin_type_label is not UNSET:
            field_dict["origin_type_label"] = origin_type_label
        if origin_type_label_plural is not UNSET:
            field_dict["origin_type_label_plural"] = origin_type_label_plural

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        origin_type_label = d.pop("origin_type_label", UNSET)

        origin_type_label_plural = d.pop("origin_type_label_plural", UNSET)

        entity_extra = cls(
            origin_type_label=origin_type_label,
            origin_type_label_plural=origin_type_label_plural,
        )

        entity_extra.additional_properties = d
        return entity_extra

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
