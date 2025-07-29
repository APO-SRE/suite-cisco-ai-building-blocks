from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.classification import Classification
from ..models.rule_object_rule_name import RuleObjectRuleName
from ..types import UNSET, Unset

T = TypeVar("T", bound="RuleObject")


@_attrs_define
class RuleObject:
    """The available rule names in AI Defense. One of rule_name or rule_id must be provided.

    Attributes:
        rule_name (RuleObjectRuleName): The canonical name of the rule
        entity_types (Union[Unset, list[str]]):
        rule_id (Union[Unset, int]): The unique identifier corresponding to the rule as defined by the AI Defense
            product.
        classification (Union[Unset, Classification]):
    """

    rule_name: RuleObjectRuleName
    entity_types: Union[Unset, list[str]] = UNSET
    rule_id: Union[Unset, int] = UNSET
    classification: Union[Unset, Classification] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_name = self.rule_name.value

        entity_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.entity_types, Unset):
            entity_types = self.entity_types

        rule_id = self.rule_id

        classification: Union[Unset, str] = UNSET
        if not isinstance(self.classification, Unset):
            classification = self.classification.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_name": rule_name,
            }
        )
        if entity_types is not UNSET:
            field_dict["entity_types"] = entity_types
        if rule_id is not UNSET:
            field_dict["rule_id"] = rule_id
        if classification is not UNSET:
            field_dict["classification"] = classification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule_name = RuleObjectRuleName(d.pop("rule_name"))

        entity_types = cast(list[str], d.pop("entity_types", UNSET))

        rule_id = d.pop("rule_id", UNSET)

        _classification = d.pop("classification", UNSET)
        classification: Union[Unset, Classification]
        if isinstance(_classification, Unset):
            classification = UNSET
        else:
            classification = Classification(_classification)

        rule_object = cls(
            rule_name=rule_name,
            entity_types=entity_types,
            rule_id=rule_id,
            classification=classification,
        )

        rule_object.additional_properties = d
        return rule_object

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
