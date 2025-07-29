from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.br_restore_request_type import BrRestoreRequestType

T = TypeVar("T", bound="BrRestoreRequest")


@_attrs_define
class BrRestoreRequest:
    """
    Attributes:
        type_ (BrRestoreRequestType): Type of restore to perform
        ignore_persistent_i_ps (bool): Whether to ignore persistent IPs during restore
    """

    type_: BrRestoreRequestType
    ignore_persistent_i_ps: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        ignore_persistent_i_ps = self.ignore_persistent_i_ps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "ignorePersistentIPs": ignore_persistent_i_ps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = BrRestoreRequestType(d.pop("type"))

        ignore_persistent_i_ps = d.pop("ignorePersistentIPs")

        br_restore_request = cls(
            type_=type_,
            ignore_persistent_i_ps=ignore_persistent_i_ps,
        )

        br_restore_request.additional_properties = d
        return br_restore_request

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
