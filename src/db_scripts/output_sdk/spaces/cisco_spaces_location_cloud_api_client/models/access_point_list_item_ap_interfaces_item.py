from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessPointListItemApInterfacesItem")


@_attrs_define
class AccessPointListItemApInterfacesItem:
    """
    Attributes:
        band (Union[Unset, str]): 802.11 band Example: IEEE_802_11_A.
        if_slot_id (Union[Unset, float]): slot ID
        channel_assignment (Union[Unset, float]): channel assignment Example: 1.
        channel_number (Union[Unset, float]): channel number Example: 11.
        tx_power_level (Union[Unset, float]): TX power level Example: 6.
        antenna_pattern (Union[Unset, str]): antenna pattern Example: Internal-3800-5GHz.
        antenna_angle (Union[Unset, float]): antenna pattern Example: 1.5707964.
        antenna_elev_angle (Union[Unset, float]): antenna elevation pattern
        antenna_gain (Union[Unset, float]): antenna gain Example: 8.
        antenna_diversity (Union[Unset, float]): antenna diversity Example: 3.
        antenna_mode (Union[Unset, float]): antenna mode
        antenna_type (Union[Unset, float]): antenna type Example: 1.
        tx_power_control (Union[Unset, float]): TX power control Example: 1.
        unit (Union[Unset, str]): unit Example: RADIAN.
        dual_band_slot (Union[Unset, bool]): dual band slot Example: True.
    """

    band: Union[Unset, str] = UNSET
    if_slot_id: Union[Unset, float] = UNSET
    channel_assignment: Union[Unset, float] = UNSET
    channel_number: Union[Unset, float] = UNSET
    tx_power_level: Union[Unset, float] = UNSET
    antenna_pattern: Union[Unset, str] = UNSET
    antenna_angle: Union[Unset, float] = UNSET
    antenna_elev_angle: Union[Unset, float] = UNSET
    antenna_gain: Union[Unset, float] = UNSET
    antenna_diversity: Union[Unset, float] = UNSET
    antenna_mode: Union[Unset, float] = UNSET
    antenna_type: Union[Unset, float] = UNSET
    tx_power_control: Union[Unset, float] = UNSET
    unit: Union[Unset, str] = UNSET
    dual_band_slot: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        band = self.band

        if_slot_id = self.if_slot_id

        channel_assignment = self.channel_assignment

        channel_number = self.channel_number

        tx_power_level = self.tx_power_level

        antenna_pattern = self.antenna_pattern

        antenna_angle = self.antenna_angle

        antenna_elev_angle = self.antenna_elev_angle

        antenna_gain = self.antenna_gain

        antenna_diversity = self.antenna_diversity

        antenna_mode = self.antenna_mode

        antenna_type = self.antenna_type

        tx_power_control = self.tx_power_control

        unit = self.unit

        dual_band_slot = self.dual_band_slot

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if band is not UNSET:
            field_dict["band"] = band
        if if_slot_id is not UNSET:
            field_dict["ifSlotId"] = if_slot_id
        if channel_assignment is not UNSET:
            field_dict["channelAssignment"] = channel_assignment
        if channel_number is not UNSET:
            field_dict["channelNumber"] = channel_number
        if tx_power_level is not UNSET:
            field_dict["txPowerLevel"] = tx_power_level
        if antenna_pattern is not UNSET:
            field_dict["antennaPattern"] = antenna_pattern
        if antenna_angle is not UNSET:
            field_dict["antennaAngle"] = antenna_angle
        if antenna_elev_angle is not UNSET:
            field_dict["antennaElevAngle"] = antenna_elev_angle
        if antenna_gain is not UNSET:
            field_dict["antennaGain"] = antenna_gain
        if antenna_diversity is not UNSET:
            field_dict["antennaDiversity"] = antenna_diversity
        if antenna_mode is not UNSET:
            field_dict["antennaMode"] = antenna_mode
        if antenna_type is not UNSET:
            field_dict["antennaType"] = antenna_type
        if tx_power_control is not UNSET:
            field_dict["txPowerControl"] = tx_power_control
        if unit is not UNSET:
            field_dict["unit"] = unit
        if dual_band_slot is not UNSET:
            field_dict["dualBandSlot"] = dual_band_slot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        band = d.pop("band", UNSET)

        if_slot_id = d.pop("ifSlotId", UNSET)

        channel_assignment = d.pop("channelAssignment", UNSET)

        channel_number = d.pop("channelNumber", UNSET)

        tx_power_level = d.pop("txPowerLevel", UNSET)

        antenna_pattern = d.pop("antennaPattern", UNSET)

        antenna_angle = d.pop("antennaAngle", UNSET)

        antenna_elev_angle = d.pop("antennaElevAngle", UNSET)

        antenna_gain = d.pop("antennaGain", UNSET)

        antenna_diversity = d.pop("antennaDiversity", UNSET)

        antenna_mode = d.pop("antennaMode", UNSET)

        antenna_type = d.pop("antennaType", UNSET)

        tx_power_control = d.pop("txPowerControl", UNSET)

        unit = d.pop("unit", UNSET)

        dual_band_slot = d.pop("dualBandSlot", UNSET)

        access_point_list_item_ap_interfaces_item = cls(
            band=band,
            if_slot_id=if_slot_id,
            channel_assignment=channel_assignment,
            channel_number=channel_number,
            tx_power_level=tx_power_level,
            antenna_pattern=antenna_pattern,
            antenna_angle=antenna_angle,
            antenna_elev_angle=antenna_elev_angle,
            antenna_gain=antenna_gain,
            antenna_diversity=antenna_diversity,
            antenna_mode=antenna_mode,
            antenna_type=antenna_type,
            tx_power_control=tx_power_control,
            unit=unit,
            dual_band_slot=dual_band_slot,
        )

        access_point_list_item_ap_interfaces_item.additional_properties = d
        return access_point_list_item_ap_interfaces_item

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
