from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_fan import SchemaFan
    from ..models.schema_psu import SchemaPsu
    from ..models.schema_temp_sensor import SchemaTempSensor


T = TypeVar("T", bound="StateSensor")


@_attrs_define
class StateSensor:
    """Description not available

    Attributes:
        fan (Union[Unset, SchemaFan]): Description not available
        power (Union[Unset, SchemaPsu]): Description not available
        temperature (Union[Unset, SchemaTempSensor]): Description not available
    """

    fan: Union[Unset, "SchemaFan"] = UNSET
    power: Union[Unset, "SchemaPsu"] = UNSET
    temperature: Union[Unset, "SchemaTempSensor"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fan, Unset):
            fan = self.fan.to_dict()

        power: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.power, Unset):
            power = self.power.to_dict()

        temperature: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.temperature, Unset):
            temperature = self.temperature.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fan is not UNSET:
            field_dict["fan"] = fan
        if power is not UNSET:
            field_dict["power"] = power
        if temperature is not UNSET:
            field_dict["temperature"] = temperature

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_fan import SchemaFan
        from ..models.schema_psu import SchemaPsu
        from ..models.schema_temp_sensor import SchemaTempSensor

        d = dict(src_dict)
        _fan = d.pop("fan", UNSET)
        fan: Union[Unset, SchemaFan]
        if isinstance(_fan, Unset):
            fan = UNSET
        else:
            fan = SchemaFan.from_dict(_fan)

        _power = d.pop("power", UNSET)
        power: Union[Unset, SchemaPsu]
        if isinstance(_power, Unset):
            power = UNSET
        else:
            power = SchemaPsu.from_dict(_power)

        _temperature = d.pop("temperature", UNSET)
        temperature: Union[Unset, SchemaTempSensor]
        if isinstance(_temperature, Unset):
            temperature = UNSET
        else:
            temperature = SchemaTempSensor.from_dict(_temperature)

        state_sensor = cls(
            fan=fan,
            power=power,
            temperature=temperature,
        )

        state_sensor.additional_properties = d
        return state_sensor

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
