from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocationDeviceMaxDetectedRssi")


@_attrs_define
class LocationDeviceMaxDetectedRssi:
    """
    Attributes:
        ap_mac_address (Union[Unset, str]): AP mac address Example: f0:7f:06:35:8d:00.
        band (Union[Unset, str]): The WiFi band the device is in. Example: IEEE_802_11_B.
        slot (Union[Unset, int]): The wifi slot Example: 2.
        rssi (Union[Unset, int]): Wifi service set identifier. Available for associated clients only. Example: -81.
        antenna_index (Union[Unset, int]): The natenna index, start from 0.
        last_heard (Union[Unset, int]):  Example: 1.
    """

    ap_mac_address: Union[Unset, str] = UNSET
    band: Union[Unset, str] = UNSET
    slot: Union[Unset, int] = UNSET
    rssi: Union[Unset, int] = UNSET
    antenna_index: Union[Unset, int] = UNSET
    last_heard: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ap_mac_address = self.ap_mac_address

        band = self.band

        slot = self.slot

        rssi = self.rssi

        antenna_index = self.antenna_index

        last_heard = self.last_heard

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ap_mac_address is not UNSET:
            field_dict["apMacAddress"] = ap_mac_address
        if band is not UNSET:
            field_dict["band"] = band
        if slot is not UNSET:
            field_dict["slot"] = slot
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
        if antenna_index is not UNSET:
            field_dict["antennaIndex"] = antenna_index
        if last_heard is not UNSET:
            field_dict["lastHeard"] = last_heard

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ap_mac_address = d.pop("apMacAddress", UNSET)

        band = d.pop("band", UNSET)

        slot = d.pop("slot", UNSET)

        rssi = d.pop("rssi", UNSET)

        antenna_index = d.pop("antennaIndex", UNSET)

        last_heard = d.pop("lastHeard", UNSET)

        location_device_max_detected_rssi = cls(
            ap_mac_address=ap_mac_address,
            band=band,
            slot=slot,
            rssi=rssi,
            antenna_index=antenna_index,
            last_heard=last_heard,
        )

        location_device_max_detected_rssi.additional_properties = d
        return location_device_max_detected_rssi

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
