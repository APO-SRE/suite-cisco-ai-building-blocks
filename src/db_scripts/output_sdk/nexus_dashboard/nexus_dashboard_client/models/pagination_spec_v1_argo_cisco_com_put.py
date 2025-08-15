from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaginationSpecV1ArgoCiscoComPUT")


@_attrs_define
class PaginationSpecV1ArgoCiscoComPUT:
    """
    Attributes:
        key (Union[Unset, str]):
        kind (Union[Unset, str]):
    """

    key: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        kind = self.kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        kind = d.pop("kind", UNSET)

        pagination_spec_v1_argo_cisco_com_put = cls(
            key=key,
            kind=kind,
        )

        pagination_spec_v1_argo_cisco_com_put.additional_properties = d
        return pagination_spec_v1_argo_cisco_com_put

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
