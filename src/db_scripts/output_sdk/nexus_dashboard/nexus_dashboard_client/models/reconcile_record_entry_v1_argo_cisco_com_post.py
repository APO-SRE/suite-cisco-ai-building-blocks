from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReconcileRecordEntryV1ArgoCiscoComPOST")


@_attrs_define
class ReconcileRecordEntryV1ArgoCiscoComPOST:
    """
    Attributes:
        observed_version (Union[Unset, int]):
    """

    observed_version: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        observed_version = self.observed_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if observed_version is not UNSET:
            field_dict["observedVersion"] = observed_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        observed_version = d.pop("observedVersion", UNSET)

        reconcile_record_entry_v1_argo_cisco_com_post = cls(
            observed_version=observed_version,
        )

        reconcile_record_entry_v1_argo_cisco_com_post.additional_properties = d
        return reconcile_record_entry_v1_argo_cisco_com_post

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
