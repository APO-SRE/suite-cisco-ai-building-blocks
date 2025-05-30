import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.schema_env_led_status import SchemaEnvLedStatus
from ..models.schema_env_status import SchemaEnvStatus
from ..models.schema_fan_direction import SchemaFanDirection
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_path_path_id import SchemaPathPathId


T = TypeVar("T", bound="SchemaFan")


@_attrs_define
class SchemaFan:
    """Description not available

    Attributes:
        collected_at (Union[Unset, datetime.datetime]): Description not available
        deprecated_direction (Union[Unset, str]): Description not available
        direction (Union[Unset, SchemaFanDirection]): Description not available
        drawer (Union[Unset, str]): Description not available
        id (Union[Unset, SchemaPathPathId]): PathId identifies the specific "schema coordinates" identifier of an object
            in the schema tree.
        led_status (Union[Unset, SchemaEnvLedStatus]): Description not available
        model (Union[Unset, str]): Description not available
        name (Union[Unset, str]): Description not available
        serial (Union[Unset, str]): Description not available
        speed (Union[Unset, int]): Fan speed as a percentage of the maximum rated speed
        status (Union[Unset, SchemaEnvStatus]): Description not available
    """

    collected_at: Union[Unset, datetime.datetime] = UNSET
    deprecated_direction: Union[Unset, str] = UNSET
    direction: Union[Unset, SchemaFanDirection] = UNSET
    drawer: Union[Unset, str] = UNSET
    id: Union[Unset, "SchemaPathPathId"] = UNSET
    led_status: Union[Unset, SchemaEnvLedStatus] = UNSET
    model: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    serial: Union[Unset, str] = UNSET
    speed: Union[Unset, int] = UNSET
    status: Union[Unset, SchemaEnvStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collected_at: Union[Unset, str] = UNSET
        if not isinstance(self.collected_at, Unset):
            collected_at = self.collected_at.isoformat()

        deprecated_direction = self.deprecated_direction

        direction: Union[Unset, str] = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        drawer = self.drawer

        id: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        led_status: Union[Unset, str] = UNSET
        if not isinstance(self.led_status, Unset):
            led_status = self.led_status.value

        model = self.model

        name = self.name

        serial = self.serial

        speed = self.speed

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collected_at is not UNSET:
            field_dict["collectedAt"] = collected_at
        if deprecated_direction is not UNSET:
            field_dict["deprecatedDirection"] = deprecated_direction
        if direction is not UNSET:
            field_dict["direction"] = direction
        if drawer is not UNSET:
            field_dict["drawer"] = drawer
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
        if speed is not UNSET:
            field_dict["speed"] = speed
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_path_path_id import SchemaPathPathId

        d = dict(src_dict)
        _collected_at = d.pop("collectedAt", UNSET)
        collected_at: Union[Unset, datetime.datetime]
        if isinstance(_collected_at, Unset):
            collected_at = UNSET
        else:
            collected_at = isoparse(_collected_at)

        deprecated_direction = d.pop("deprecatedDirection", UNSET)

        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, SchemaFanDirection]
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = SchemaFanDirection(_direction)

        drawer = d.pop("drawer", UNSET)

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

        speed = d.pop("speed", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SchemaEnvStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SchemaEnvStatus(_status)

        schema_fan = cls(
            collected_at=collected_at,
            deprecated_direction=deprecated_direction,
            direction=direction,
            drawer=drawer,
            id=id,
            led_status=led_status,
            model=model,
            name=name,
            serial=serial,
            speed=speed,
            status=status,
        )

        schema_fan.additional_properties = d
        return schema_fan

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
