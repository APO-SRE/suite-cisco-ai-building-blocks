from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schema_env_led_status import SchemaEnvLedStatus
from ..models.schema_env_status import SchemaEnvStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_path_path_id import SchemaPathPathId


T = TypeVar("T", bound="SchemaPsu")


@_attrs_define
class SchemaPsu:
    """Description not available

    Attributes:
        current (Union[Unset, float]): Description not available
        fan_speed (Union[Unset, int]): Fan speed as a percentage of the maximum rated speed
        id (Union[Unset, SchemaPathPathId]): PathId identifies the specific "schema coordinates" identifier of an object
            in the schema tree.
        led_status (Union[Unset, SchemaEnvLedStatus]): Description not available
        model (Union[Unset, str]): Description not available
        name (Union[Unset, str]): Description not available
        serial (Union[Unset, str]): Description not available
        status (Union[Unset, SchemaEnvStatus]): Description not available
        voltage (Union[Unset, float]): Description not available
        watts (Union[Unset, int]): Description not available
    """

    current: Union[Unset, float] = UNSET
    fan_speed: Union[Unset, int] = UNSET
    id: Union[Unset, "SchemaPathPathId"] = UNSET
    led_status: Union[Unset, SchemaEnvLedStatus] = UNSET
    model: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    serial: Union[Unset, str] = UNSET
    status: Union[Unset, SchemaEnvStatus] = UNSET
    voltage: Union[Unset, float] = UNSET
    watts: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current = self.current

        fan_speed = self.fan_speed

        id: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        led_status: Union[Unset, str] = UNSET
        if not isinstance(self.led_status, Unset):
            led_status = self.led_status.value

        model = self.model

        name = self.name

        serial = self.serial

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        voltage = self.voltage

        watts = self.watts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current is not UNSET:
            field_dict["current"] = current
        if fan_speed is not UNSET:
            field_dict["fanSpeed"] = fan_speed
        if id is not UNSET:
            field_dict["id"] = id
        if led_status is not UNSET:
            field_dict["ledStatus"] = led_status
        if model is not UNSET:
            field_dict["model"] = model
        if name is not UNSET:
            field_dict["name"] = name
        if serial is not UNSET:
            field_dict["serial"] = serial
        if status is not UNSET:
            field_dict["status"] = status
        if voltage is not UNSET:
            field_dict["voltage"] = voltage
        if watts is not UNSET:
            field_dict["watts"] = watts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_path_path_id import SchemaPathPathId

        d = dict(src_dict)
        current = d.pop("current", UNSET)

        fan_speed = d.pop("fanSpeed", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, SchemaPathPathId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = SchemaPathPathId.from_dict(_id)

        _led_status = d.pop("ledStatus", UNSET)
        led_status: Union[Unset, SchemaEnvLedStatus]
        if isinstance(_led_status, Unset):
            led_status = UNSET
        else:
            led_status = SchemaEnvLedStatus(_led_status)

        model = d.pop("model", UNSET)

        name = d.pop("name", UNSET)

        serial = d.pop("serial", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SchemaEnvStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SchemaEnvStatus(_status)

        voltage = d.pop("voltage", UNSET)

        watts = d.pop("watts", UNSET)

        schema_psu = cls(
            current=current,
            fan_speed=fan_speed,
            id=id,
            led_status=led_status,
            model=model,
            name=name,
            serial=serial,
            status=status,
            voltage=voltage,
            watts=watts,
        )

        schema_psu.additional_properties = d
        return schema_psu

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
