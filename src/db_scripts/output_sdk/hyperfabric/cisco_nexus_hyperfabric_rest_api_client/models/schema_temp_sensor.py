from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_path_path_id import SchemaPathPathId


T = TypeVar("T", bound="SchemaTempSensor")


@_attrs_define
class SchemaTempSensor:
    """Description not available

    Attributes:
        deg_c (Union[Unset, int]): Description not available
        deg_celsius (Union[Unset, int]): Description not available
        high_threshold (Union[Unset, int]): Description not available
        id (Union[Unset, SchemaPathPathId]): PathId identifies the specific "schema coordinates" identifier of an object
            in the schema tree.
        low_threshold (Union[Unset, int]): Description not available
    """

    deg_c: Union[Unset, int] = UNSET
    deg_celsius: Union[Unset, int] = UNSET
    high_threshold: Union[Unset, int] = UNSET
    id: Union[Unset, "SchemaPathPathId"] = UNSET
    low_threshold: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deg_c = self.deg_c

        deg_celsius = self.deg_celsius

        high_threshold = self.high_threshold

        id: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        low_threshold = self.low_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deg_c is not UNSET:
            field_dict["degC"] = deg_c
        if deg_celsius is not UNSET:
            field_dict["degCelsius"] = deg_celsius
        if high_threshold is not UNSET:
            field_dict["highThreshold"] = high_threshold
        if id is not UNSET:
            field_dict["id"] = id
        if low_threshold is not UNSET:
            field_dict["lowThreshold"] = low_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_path_path_id import SchemaPathPathId

        d = dict(src_dict)
        deg_c = d.pop("degC", UNSET)

        deg_celsius = d.pop("degCelsius", UNSET)

        high_threshold = d.pop("highThreshold", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, SchemaPathPathId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = SchemaPathPathId.from_dict(_id)

        low_threshold = d.pop("lowThreshold", UNSET)

        schema_temp_sensor = cls(
            deg_c=deg_c,
            deg_celsius=deg_celsius,
            high_threshold=high_threshold,
            id=id,
            low_threshold=low_threshold,
        )

        schema_temp_sensor.additional_properties = d
        return schema_temp_sensor

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
