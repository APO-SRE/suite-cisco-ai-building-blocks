from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V2MapFloorItemAccessPointsItemInterfacesItem")


@_attrs_define
class V2MapFloorItemAccessPointsItemInterfacesItem:
    """
    Attributes:
        antenna_pattern (Union[Unset, str]): antenna pattern Example: Internal-3800-5GHz.
        channel_number (Union[Unset, float]): channel number Example: 11.
        antenna_angle (Union[Unset, float]): antenna pattern Example: 1.5707964.
        antenna_gain (Union[Unset, float]): antenna gain Example: 8.
        if_slot_id (Union[Unset, float]): slot number Example: 2.
        antenna_mode (Union[Unset, float]): antenna mode
        dual_band_slot (Union[Unset, bool]): dual band slot Example: True.
        antenna_elev_angle (Union[Unset, float]): antenna elevation pattern
        tx_power_control (Union[Unset, float]): TX power control Example: 1.
        antenna_type (Union[Unset, float]): antenna type Example: 1.
        channel_assignment (Union[Unset, float]): channel assignment Example: 1.
        unit (Union[Unset, str]): unit Example: RADIAN.
        tx_power_level (Union[Unset, float]): TX power level Example: 6.
        band (Union[Unset, str]): 802.11 band Example: IEEE_802_11_A.
        added_by_dnaspaces (Union[Unset, float]): Number of APs added by DNASpaces
        antenna_diversity (Union[Unset, float]): antenna diversity Example: 3.
    """

    antenna_pattern: Union[Unset, str] = UNSET
    channel_number: Union[Unset, float] = UNSET
    antenna_angle: Union[Unset, float] = UNSET
    antenna_gain: Union[Unset, float] = UNSET
    if_slot_id: Union[Unset, float] = UNSET
    antenna_mode: Union[Unset, float] = UNSET
    dual_band_slot: Union[Unset, bool] = UNSET
    antenna_elev_angle: Union[Unset, float] = UNSET
    tx_power_control: Union[Unset, float] = UNSET
    antenna_type: Union[Unset, float] = UNSET
    channel_assignment: Union[Unset, float] = UNSET
    unit: Union[Unset, str] = UNSET
    tx_power_level: Union[Unset, float] = UNSET
    band: Union[Unset, str] = UNSET
    added_by_dnaspaces: Union[Unset, float] = UNSET
    antenna_diversity: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        antenna_pattern = self.antenna_pattern

        channel_number = self.channel_number

        antenna_angle = self.antenna_angle

        antenna_gain = self.antenna_gain

        if_slot_id = self.if_slot_id

        antenna_mode = self.antenna_mode

        dual_band_slot = self.dual_band_slot

        antenna_elev_angle = self.antenna_elev_angle

        tx_power_control = self.tx_power_control

        antenna_type = self.antenna_type

        channel_assignment = self.channel_assignment

        unit = self.unit

        tx_power_level = self.tx_power_level

        band = self.band

        added_by_dnaspaces = self.added_by_dnaspaces

        antenna_diversity = self.antenna_diversity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if antenna_pattern is not UNSET:
            field_dict["antennaPattern"] = antenna_pattern
        if channel_number is not UNSET:
            field_dict["channelNumber"] = channel_number
        if antenna_angle is not UNSET:
            field_dict["antennaAngle"] = antenna_angle
        if antenna_gain is not UNSET:
            field_dict["antennaGain"] = antenna_gain
        if if_slot_id is not UNSET:
            field_dict["ifSlotId"] = if_slot_id
        if antenna_mode is not UNSET:
            field_dict["antennaMode"] = antenna_mode
        if dual_band_slot is not UNSET:
            field_dict["dualBandSlot"] = dual_band_slot
        if antenna_elev_angle is not UNSET:
            field_dict["antennaElevAngle"] = antenna_elev_angle
        if tx_power_control is not UNSET:
            field_dict["txPowerControl"] = tx_power_control
        if antenna_type is not UNSET:
            field_dict["antennaType"] = antenna_type
        if channel_assignment is not UNSET:
            field_dict["channelAssignment"] = channel_assignment
        if unit is not UNSET:
            field_dict["unit"] = unit
        if tx_power_level is not UNSET:
            field_dict["txPowerLevel"] = tx_power_level
        if band is not UNSET:
            field_dict["band"] = band
        if added_by_dnaspaces is not UNSET:
            field_dict["addedByDnaspaces"] = added_by_dnaspaces
        if antenna_diversity is not UNSET:
            field_dict["antennaDiversity"] = antenna_diversity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        antenna_pattern = d.pop("antennaPattern", UNSET)

        channel_number = d.pop("channelNumber", UNSET)

        antenna_angle = d.pop("antennaAngle", UNSET)

        antenna_gain = d.pop("antennaGain", UNSET)

        if_slot_id = d.pop("ifSlotId", UNSET)

        antenna_mode = d.pop("antennaMode", UNSET)

        dual_band_slot = d.pop("dualBandSlot", UNSET)

        antenna_elev_angle = d.pop("antennaElevAngle", UNSET)

        tx_power_control = d.pop("txPowerControl", UNSET)

        antenna_type = d.pop("antennaType", UNSET)

        channel_assignment = d.pop("channelAssignment", UNSET)

        unit = d.pop("unit", UNSET)

        tx_power_level = d.pop("txPowerLevel", UNSET)

        band = d.pop("band", UNSET)

        added_by_dnaspaces = d.pop("addedByDnaspaces", UNSET)

        antenna_diversity = d.pop("antennaDiversity", UNSET)

        v2_map_floor_item_access_points_item_interfaces_item = cls(
            antenna_pattern=antenna_pattern,
            channel_number=channel_number,
            antenna_angle=antenna_angle,
            antenna_gain=antenna_gain,
            if_slot_id=if_slot_id,
            antenna_mode=antenna_mode,
            dual_band_slot=dual_band_slot,
            antenna_elev_angle=antenna_elev_angle,
            tx_power_control=tx_power_control,
            antenna_type=antenna_type,
            channel_assignment=channel_assignment,
            unit=unit,
            tx_power_level=tx_power_level,
            band=band,
            added_by_dnaspaces=added_by_dnaspaces,
            antenna_diversity=antenna_diversity,
        )

        v2_map_floor_item_access_points_item_interfaces_item.additional_properties = d
        return v2_map_floor_item_access_points_item_interfaces_item

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
