from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScopeCategory")


@_attrs_define
class ScopeCategory:
    """The scope categories resource returns information on the access scopes, which exist per each category.
    Scope category strings: `FDATA` (full data access), `BINFO` (basic info), `LACES` (limited access to data and
    files),
    `PINFO` (payment information), and `INBO`X (access inbox or contact information).

        Attributes:
            title (Union[Unset, str]): The categories title, for example: `Basic Information`.
            category_id (Union[Unset, str]): The category id. For example: `FDATA`, `BINFO`, `LACES`, and `PINFO`. Example:
                FDATA.
    """

    title: Union[Unset, str] = UNSET
    category_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        category_id = self.category_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if category_id is not UNSET:
            field_dict["category_id"] = category_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        category_id = d.pop("category_id", UNSET)

        scope_category = cls(
            title=title,
            category_id=category_id,
        )

        scope_category.additional_properties = d
        return scope_category

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
