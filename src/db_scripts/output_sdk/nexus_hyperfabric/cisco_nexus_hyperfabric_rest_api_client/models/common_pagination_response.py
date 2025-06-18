from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommonPaginationResponse")


@_attrs_define
class CommonPaginationResponse:
    """PaginationResponse defines common pagination properties that all GET gRPC responses should have. PaginationResponse
    is to be embedded in all GET gRPC response messages.

        Attributes:
            cursor (Union[Unset, str]): Last used search cursor. Next pagination will start after this.
            final (Union[Unset, bool]): Indicates an end of query results.
            total (Union[Unset, int]): Total number of objects found by query.
    """

    cursor: Union[Unset, str] = UNSET
    final: Union[Unset, bool] = UNSET
    total: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursor = self.cursor

        final = self.final

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if final is not UNSET:
            field_dict["final"] = final
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cursor = d.pop("cursor", UNSET)

        final = d.pop("final", UNSET)

        total = d.pop("total", UNSET)

        common_pagination_response = cls(
            cursor=cursor,
            final=final,
            total=total,
        )

        common_pagination_response.additional_properties = d
        return common_pagination_response

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
