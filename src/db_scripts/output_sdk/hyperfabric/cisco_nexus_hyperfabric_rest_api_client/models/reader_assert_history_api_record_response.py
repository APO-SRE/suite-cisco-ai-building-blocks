from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.common_pagination_response import CommonPaginationResponse
    from ..models.reader_assert_history_api_record import ReaderAssertHistoryApiRecord


T = TypeVar("T", bound="ReaderAssertHistoryApiRecordResponse")


@_attrs_define
class ReaderAssertHistoryApiRecordResponse:
    """AssertHistoryRecordResponseSchemaProto holds the Assertion record time series query result in the message format
    defined in schema.proto.

        Attributes:
            assertions (Union[Unset, list['ReaderAssertHistoryApiRecord']]): Description not available
            pagination (Union[Unset, CommonPaginationResponse]): PaginationResponse defines common pagination properties
                that all GET gRPC responses should have. PaginationResponse is to be embedded in all GET gRPC response messages.
    """

    assertions: Union[Unset, list["ReaderAssertHistoryApiRecord"]] = UNSET
    pagination: Union[Unset, "CommonPaginationResponse"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assertions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.assertions, Unset):
            assertions = []
            for assertions_item_data in self.assertions:
                assertions_item = assertions_item_data.to_dict()
                assertions.append(assertions_item)

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assertions is not UNSET:
            field_dict["assertions"] = assertions
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.common_pagination_response import CommonPaginationResponse
        from ..models.reader_assert_history_api_record import ReaderAssertHistoryApiRecord

        d = dict(src_dict)
        assertions = []
        _assertions = d.pop("assertions", UNSET)
        for assertions_item_data in _assertions or []:
            assertions_item = ReaderAssertHistoryApiRecord.from_dict(assertions_item_data)

            assertions.append(assertions_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, CommonPaginationResponse]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = CommonPaginationResponse.from_dict(_pagination)

        reader_assert_history_api_record_response = cls(
            assertions=assertions,
            pagination=pagination,
        )

        reader_assert_history_api_record_response.additional_properties = d
        return reader_assert_history_api_record_response

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
