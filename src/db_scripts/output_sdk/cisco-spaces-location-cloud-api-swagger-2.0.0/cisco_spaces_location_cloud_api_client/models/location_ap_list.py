from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocationAPList")


@_attrs_define
class LocationAPList:
    """
    Attributes:
        ap_mac_address (Union[Unset, str]): The AP's mac address. Example: 3c:08:f6:fb:29:50.
        bands (Union[Unset, list[str]]): The wifi band the AP supports. Example: ['IEEE_802_11_A'].
    """

    ap_mac_address: Union[Unset, str] = UNSET
    bands: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ap_mac_address = self.ap_mac_address

        bands: Union[Unset, list[str]] = UNSET
        if not isinstance(self.bands, Unset):
            bands = self.bands

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ap_mac_address is not UNSET:
            field_dict["apMacAddress"] = ap_mac_address
        if bands is not UNSET:
            field_dict["bands"] = bands

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ap_mac_address = d.pop("apMacAddress", UNSET)

        bands = cast(list[str], d.pop("bands", UNSET))

        location_ap_list = cls(
            ap_mac_address=ap_mac_address,
            bands=bands,
        )

        location_ap_list.additional_properties = d
        return location_ap_list

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
