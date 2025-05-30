from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MissingAPsListItem")


@_attrs_define
class MissingAPsListItem:
    """
    Attributes:
        ap_mac (Union[Unset, str]):  Example: 00:08:f6:d9:08:a0.
        count (Union[Unset, int]): The message count received. Example: 51.
        m_1_rate (Union[Unset, float]): The message rate in 1 min. Example: 0.13455241481625685.
        m_5_rate (Union[Unset, float]): The message rate in 5 min. Example: 2.953704047942261.
        m_15_rate (Union[Unset, float]): The message rate in 15 min. Example: 4.945645924551671.
    """

    ap_mac: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    m_1_rate: Union[Unset, float] = UNSET
    m_5_rate: Union[Unset, float] = UNSET
    m_15_rate: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ap_mac = self.ap_mac

        count = self.count

        m_1_rate = self.m_1_rate

        m_5_rate = self.m_5_rate

        m_15_rate = self.m_15_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ap_mac is not UNSET:
            field_dict["apMac"] = ap_mac
        if count is not UNSET:
            field_dict["count"] = count
        if m_1_rate is not UNSET:
            field_dict["m1Rate"] = m_1_rate
        if m_5_rate is not UNSET:
            field_dict["m5Rate"] = m_5_rate
        if m_15_rate is not UNSET:
            field_dict["m15Rate"] = m_15_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ap_mac = d.pop("apMac", UNSET)

        count = d.pop("count", UNSET)

        m_1_rate = d.pop("m1Rate", UNSET)

        m_5_rate = d.pop("m5Rate", UNSET)

        m_15_rate = d.pop("m15Rate", UNSET)

        missing_a_ps_list_item = cls(
            ap_mac=ap_mac,
            count=count,
            m_1_rate=m_1_rate,
            m_5_rate=m_5_rate,
            m_15_rate=m_15_rate,
        )

        missing_a_ps_list_item.additional_properties = d
        return missing_a_ps_list_item

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
