from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.any_patch_item_type_2_op import AnyPATCHItemType2Op

T = TypeVar("T", bound="AnyPATCHItemType2")


@_attrs_define
class AnyPATCHItemType2:
    """
    Attributes:
        from_ (str): A JSON Pointer string specifying the part of the document to operate on Example: spec.favPet.name.
        op (AnyPATCHItemType2Op): The type of operation to perform Example: move.
        path (str): A JSON Pointer string specifying the part of the document to operate on Example: spec.favPet.name.
    """

    from_: str
    op: AnyPATCHItemType2Op
    path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        op = self.op.value

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "op": op,
                "path": path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = d.pop("from")

        op = AnyPATCHItemType2Op(d.pop("op"))

        path = d.pop("path")

        any_patch_item_type_2 = cls(
            from_=from_,
            op=op,
            path=path,
        )

        any_patch_item_type_2.additional_properties = d
        return any_patch_item_type_2

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
