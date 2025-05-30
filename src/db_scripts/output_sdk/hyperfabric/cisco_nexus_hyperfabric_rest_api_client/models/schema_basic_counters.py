from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaBasicCounters")


@_attrs_define
class SchemaBasicCounters:
    """Universal counters for L2/L3 entities

    Attributes:
        bytes_in (Union[Unset, int]): Description not available
        bytes_out (Union[Unset, int]): Description not available
        err_pkts_in (Union[Unset, int]): Description not available
        err_pkts_out (Union[Unset, int]): Description not available
        pkts_in (Union[Unset, int]): Description not available
        pkts_out (Union[Unset, int]): Description not available
    """

    bytes_in: Union[Unset, int] = UNSET
    bytes_out: Union[Unset, int] = UNSET
    err_pkts_in: Union[Unset, int] = UNSET
    err_pkts_out: Union[Unset, int] = UNSET
    pkts_in: Union[Unset, int] = UNSET
    pkts_out: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bytes_in = self.bytes_in

        bytes_out = self.bytes_out

        err_pkts_in = self.err_pkts_in

        err_pkts_out = self.err_pkts_out

        pkts_in = self.pkts_in

        pkts_out = self.pkts_out

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bytes_in is not UNSET:
            field_dict["bytesIn"] = bytes_in
        if bytes_out is not UNSET:
            field_dict["bytesOut"] = bytes_out
        if err_pkts_in is not UNSET:
            field_dict["errPktsIn"] = err_pkts_in
        if err_pkts_out is not UNSET:
            field_dict["errPktsOut"] = err_pkts_out
        if pkts_in is not UNSET:
            field_dict["pktsIn"] = pkts_in
        if pkts_out is not UNSET:
            field_dict["pktsOut"] = pkts_out

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bytes_in = d.pop("bytesIn", UNSET)

        bytes_out = d.pop("bytesOut", UNSET)

        err_pkts_in = d.pop("errPktsIn", UNSET)

        err_pkts_out = d.pop("errPktsOut", UNSET)

        pkts_in = d.pop("pktsIn", UNSET)

        pkts_out = d.pop("pktsOut", UNSET)

        schema_basic_counters = cls(
            bytes_in=bytes_in,
            bytes_out=bytes_out,
            err_pkts_in=err_pkts_in,
            err_pkts_out=err_pkts_out,
            pkts_in=pkts_in,
            pkts_out=pkts_out,
        )

        schema_basic_counters.additional_properties = d
        return schema_basic_counters

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
