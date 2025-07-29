from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentAggregatesAgg")


@_attrs_define
class IncidentAggregatesAgg:
    """The aggregates object.

    Attributes:
        info (Union[Unset, int]): The number of `info` severity incidents.
        total (Union[Unset, int]): The overall number of incidents.
        warning (Union[Unset, int]): The number of `warning` severity incidents.
        critical (Union[Unset, int]): The number of `critical` severity incidents.'
        alert (Union[Unset, int]): The number of `alert` severity incidents.
    """

    info: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET
    warning: Union[Unset, int] = UNSET
    critical: Union[Unset, int] = UNSET
    alert: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        info = self.info

        total = self.total

        warning = self.warning

        critical = self.critical

        alert = self.alert

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if info is not UNSET:
            field_dict["info"] = info
        if total is not UNSET:
            field_dict["total"] = total
        if warning is not UNSET:
            field_dict["warning"] = warning
        if critical is not UNSET:
            field_dict["critical"] = critical
        if alert is not UNSET:
            field_dict["alert"] = alert

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        info = d.pop("info", UNSET)

        total = d.pop("total", UNSET)

        warning = d.pop("warning", UNSET)

        critical = d.pop("critical", UNSET)

        alert = d.pop("alert", UNSET)

        incident_aggregates_agg = cls(
            info=info,
            total=total,
            warning=warning,
            critical=critical,
            alert=alert,
        )

        incident_aggregates_agg.additional_properties = d
        return incident_aggregates_agg

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
