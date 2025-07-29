from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BrScErrorForbidden")


@_attrs_define
class BrScErrorForbidden:
    """
    Attributes:
        error (Union[Unset, str]): Error message (empty if no error)
        host_key (Union[Unset, str]): Set when error is 'Host key must be validated'
        old_host_key (Union[Unset, str]): Set when error is 'Host key must be validated' and an older key exists
    """

    error: Union[Unset, str] = UNSET
    host_key: Union[Unset, str] = UNSET
    old_host_key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        host_key = self.host_key

        old_host_key = self.old_host_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if host_key is not UNSET:
            field_dict["hostKey"] = host_key
        if old_host_key is not UNSET:
            field_dict["oldHostKey"] = old_host_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error", UNSET)

        host_key = d.pop("hostKey", UNSET)

        old_host_key = d.pop("oldHostKey", UNSET)

        br_sc_error_forbidden = cls(
            error=error,
            host_key=host_key,
            old_host_key=old_host_key,
        )

        br_sc_error_forbidden.additional_properties = d
        return br_sc_error_forbidden

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
