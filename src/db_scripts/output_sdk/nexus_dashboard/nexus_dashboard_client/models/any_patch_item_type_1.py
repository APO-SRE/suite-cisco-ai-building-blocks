from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.any_patch_item_type_1_op import AnyPATCHItemType1Op

T = TypeVar("T", bound="AnyPATCHItemType1")


@_attrs_define
class AnyPATCHItemType1:
    """
    Attributes:
        op (AnyPATCHItemType1Op): The type of operation to perform Example: remove.
        path (str): A JSON Pointer string specifying the part of the document to operate on Example: spec.favPet.name.
    """

    op: AnyPATCHItemType1Op
    path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        op = self.op.value

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "op": op,
                "path": path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        op = AnyPATCHItemType1Op(d.pop("op"))

        path = d.pop("path")

        any_patch_item_type_1 = cls(
            op=op,
            path=path,
        )

        any_patch_item_type_1.additional_properties = d
        return any_patch_item_type_1

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
