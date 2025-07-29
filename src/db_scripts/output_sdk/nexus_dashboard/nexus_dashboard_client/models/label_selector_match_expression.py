from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.label_selector_match_expression_operator import LabelSelectorMatchExpressionOperator
from ..types import UNSET, Unset

T = TypeVar("T", bound="LabelSelectorMatchExpression")


@_attrs_define
class LabelSelectorMatchExpression:
    """
    Attributes:
        key (Union[Unset, str]):
        operator (Union[Unset, LabelSelectorMatchExpressionOperator]):
        values (Union[Unset, list[str]]):
    """

    key: Union[Unset, str] = UNSET
    operator: Union[Unset, LabelSelectorMatchExpressionOperator] = UNSET
    values: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        operator: Union[Unset, str] = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        values: Union[Unset, list[str]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if operator is not UNSET:
            field_dict["operator"] = operator
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        _operator = d.pop("operator", UNSET)
        operator: Union[Unset, LabelSelectorMatchExpressionOperator]
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = LabelSelectorMatchExpressionOperator(_operator)

        values = cast(list[str], d.pop("values", UNSET))

        label_selector_match_expression = cls(
            key=key,
            operator=operator,
            values=values,
        )

        label_selector_match_expression.additional_properties = d
        return label_selector_match_expression

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
