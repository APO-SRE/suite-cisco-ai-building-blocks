from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.common_pagination_response import CommonPaginationResponse
    from ..models.reader_assert_counter_report import ReaderAssertCounterReport


T = TypeVar("T", bound="ReaderAssertCounterReportResponse")


@_attrs_define
class ReaderAssertCounterReportResponse:
    """AssertCounterReportResponse holds the AssertCounter time series query result.

    Attributes:
        counter_report (Union[Unset, list['ReaderAssertCounterReport']]): Description not available
        pagination (Union[Unset, CommonPaginationResponse]): PaginationResponse defines common pagination properties
            that all GET gRPC responses should have. PaginationResponse is to be embedded in all GET gRPC response messages.
    """

    counter_report: Union[Unset, list["ReaderAssertCounterReport"]] = UNSET
    pagination: Union[Unset, "CommonPaginationResponse"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        counter_report: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.counter_report, Unset):
            counter_report = []
            for counter_report_item_data in self.counter_report:
                counter_report_item = counter_report_item_data.to_dict()
                counter_report.append(counter_report_item)

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if counter_report is not UNSET:
            field_dict["counterReport"] = counter_report
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.common_pagination_response import CommonPaginationResponse
        from ..models.reader_assert_counter_report import ReaderAssertCounterReport

        d = dict(src_dict)
        counter_report = []
        _counter_report = d.pop("counterReport", UNSET)
        for counter_report_item_data in _counter_report or []:
            counter_report_item = ReaderAssertCounterReport.from_dict(counter_report_item_data)

            counter_report.append(counter_report_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, CommonPaginationResponse]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = CommonPaginationResponse.from_dict(_pagination)

        reader_assert_counter_report_response = cls(
            counter_report=counter_report,
            pagination=pagination,
        )

        reader_assert_counter_report_response.additional_properties = d
        return reader_assert_counter_report_response

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
