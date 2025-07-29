from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.selector_status_error import SelectorStatusError


T = TypeVar("T", bound="SelectorStatus")


@_attrs_define
class SelectorStatus:
    """
    Attributes:
        error (Union[Unset, SelectorStatusError]):
        resolved_i_ds (Union[Unset, list[str]]):
    """

    error: Union[Unset, "SelectorStatusError"] = UNSET
    resolved_i_ds: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        resolved_i_ds: Union[Unset, list[str]] = UNSET
        if not isinstance(self.resolved_i_ds, Unset):
            resolved_i_ds = self.resolved_i_ds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if resolved_i_ds is not UNSET:
            field_dict["resolvedIDs"] = resolved_i_ds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.selector_status_error import SelectorStatusError

        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: Union[Unset, SelectorStatusError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = SelectorStatusError.from_dict(_error)

        resolved_i_ds = cast(list[str], d.pop("resolvedIDs", UNSET))

        selector_status = cls(
            error=error,
            resolved_i_ds=resolved_i_ds,
        )

        selector_status.additional_properties = d
        return selector_status

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
