from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_selector_match_expression import FieldSelectorMatchExpression


T = TypeVar("T", bound="FieldSelectorSpec")


@_attrs_define
class FieldSelectorSpec:
    """
    Attributes:
        match_expression (Union[Unset, FieldSelectorMatchExpression]):
    """

    match_expression: Union[Unset, "FieldSelectorMatchExpression"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        match_expression: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.match_expression, Unset):
            match_expression = self.match_expression.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if match_expression is not UNSET:
            field_dict["matchExpression"] = match_expression

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_selector_match_expression import FieldSelectorMatchExpression

        d = dict(src_dict)
        _match_expression = d.pop("matchExpression", UNSET)
        match_expression: Union[Unset, FieldSelectorMatchExpression]
        if isinstance(_match_expression, Unset):
            match_expression = UNSET
        else:
            match_expression = FieldSelectorMatchExpression.from_dict(_match_expression)

        field_selector_spec = cls(
            match_expression=match_expression,
        )

        field_selector_spec.additional_properties = d
        return field_selector_spec

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
