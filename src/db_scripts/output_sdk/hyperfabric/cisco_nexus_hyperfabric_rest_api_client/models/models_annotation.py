from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_data_type import ModelsDataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsAnnotation")


@_attrs_define
class ModelsAnnotation:
    """Annotation defines a typed name/value pair.

    Attributes:
        data_type (Union[Unset, ModelsDataType]): Data type enumeration.
        name (Union[Unset, str]): Name defines a user-defined name of annotation.
        value (Union[Unset, str]): Value defines annotation value expressed as string.
    """

    data_type: Union[Unset, ModelsDataType] = UNSET
    name: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_type: Union[Unset, str] = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        name = self.name

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _data_type = d.pop("dataType", UNSET)
        data_type: Union[Unset, ModelsDataType]
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = ModelsDataType(_data_type)

        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        models_annotation = cls(
            data_type=data_type,
            name=name,
            value=value,
        )

        models_annotation.additional_properties = d
        return models_annotation

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
