from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.state_sensor import StateSensor


T = TypeVar("T", bound="StateSensorsResponse")


@_attrs_define
class StateSensorsResponse:
    """Description not available

    Attributes:
        sensors (Union[Unset, list['StateSensor']]): Description not available
    """

    sensors: Union[Unset, list["StateSensor"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sensors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sensors, Unset):
            sensors = []
            for sensors_item_data in self.sensors:
                sensors_item = sensors_item_data.to_dict()
                sensors.append(sensors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sensors is not UNSET:
            field_dict["sensors"] = sensors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.state_sensor import StateSensor

        d = dict(src_dict)
        sensors = []
        _sensors = d.pop("sensors", UNSET)
        for sensors_item_data in _sensors or []:
            sensors_item = StateSensor.from_dict(sensors_item_data)

            sensors.append(sensors_item)

        state_sensors_response = cls(
            sensors=sensors,
        )

        state_sensors_response.additional_properties = d
        return state_sensors_response

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
