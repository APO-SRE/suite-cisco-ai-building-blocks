from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.any_patch_item_type_0_op import AnyPATCHItemType0Op

T = TypeVar("T", bound="AnyPATCHItemType0")


@_attrs_define
class AnyPATCHItemType0:
    """
    Attributes:
        op (AnyPATCHItemType0Op): The type of operation to perform Example: replace.
        path (str): A JSON Pointer string specifying the part of the document to operate on Example: spec.favPet.age.
        value (Any): A JSON value used in "add", "replace", and "test" operations Example: 38.
    """

    op: AnyPATCHItemType0Op
    path: str
    value: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        op = self.op.value

        path = self.path

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "op": op,
                "path": path,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        op = AnyPATCHItemType0Op(d.pop("op"))

        path = d.pop("path")

        value = d.pop("value")

        any_patch_item_type_0 = cls(
            op=op,
            path=path,
            value=value,
        )

        any_patch_item_type_0.additional_properties = d
        return any_patch_item_type_0

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
