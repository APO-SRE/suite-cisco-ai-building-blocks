from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.field_selector_match_expression_operator import FieldSelectorMatchExpressionOperator
from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldSelectorMatchExpression")


@_attrs_define
class FieldSelectorMatchExpression:
    """
    Attributes:
        field (Union[Unset, str]):
        operator (Union[Unset, FieldSelectorMatchExpressionOperator]):
        value (Union[Unset, Any]):
        values (Union[Unset, list[Any]]):
    """

    field: Union[Unset, str] = UNSET
    operator: Union[Unset, FieldSelectorMatchExpressionOperator] = UNSET
    value: Union[Unset, Any] = UNSET
    values: Union[Unset, list[Any]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        operator: Union[Unset, str] = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        value = self.value

        values: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if operator is not UNSET:
            field_dict["operator"] = operator
        if value is not UNSET:
            field_dict["value"] = value
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field", UNSET)

        _operator = d.pop("operator", UNSET)
        operator: Union[Unset, FieldSelectorMatchExpressionOperator]
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = FieldSelectorMatchExpressionOperator(_operator)

        value = d.pop("value", UNSET)

        values = cast(list[Any], d.pop("values", UNSET))

        field_selector_match_expression = cls(
            field=field,
            operator=operator,
            value=value,
            values=values,
        )

        field_selector_match_expression.additional_properties = d
        return field_selector_match_expression

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
