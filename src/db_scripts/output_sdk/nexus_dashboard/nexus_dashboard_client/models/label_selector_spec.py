from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label_selector_match_expression import LabelSelectorMatchExpression


T = TypeVar("T", bound="LabelSelectorSpec")


@_attrs_define
class LabelSelectorSpec:
    """
    Attributes:
        match_expression (Union[Unset, list['LabelSelectorMatchExpression']]):
    """

    match_expression: Union[Unset, list["LabelSelectorMatchExpression"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        match_expression: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.match_expression, Unset):
            match_expression = []
            for match_expression_item_data in self.match_expression:
                match_expression_item = match_expression_item_data.to_dict()
                match_expression.append(match_expression_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if match_expression is not UNSET:
            field_dict["matchExpression"] = match_expression

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label_selector_match_expression import LabelSelectorMatchExpression

        d = dict(src_dict)
        match_expression = []
        _match_expression = d.pop("matchExpression", UNSET)
        for match_expression_item_data in _match_expression or []:
            match_expression_item = LabelSelectorMatchExpression.from_dict(match_expression_item_data)

            match_expression.append(match_expression_item)

        label_selector_spec = cls(
            match_expression=match_expression,
        )

        label_selector_spec.additional_properties = d
        return label_selector_spec

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
