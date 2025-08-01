from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.classification import Classification
from ..models.inspect_response_severity import InspectResponseSeverity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rule_object import RuleObject


T = TypeVar("T", bound="InspectResponse")


@_attrs_define
class InspectResponse:
    """
    Attributes:
        classifications (Union[Unset, list[Classification]]): The classification of the prompt or completion
        is_safe (Union[Unset, bool]): Whether the prompt or completion is safe or unsafe
        severity (Union[Unset, InspectResponseSeverity]): The severity of the prompt or completion
        rules (Union[Unset, list['RuleObject']]): The rules that the prompt or completion violates
        attack_technique (Union[Unset, str]): The attack techniques that the prompt or completion falls under
        explanation (Union[Unset, str]): The explanation of the attack technique and the rule
        client_transaction_id (Union[Unset, str]): The client transaction ID received in the request if any
        event_id (Union[Unset, str]): The event ID if any generated by AI Defense, post inspection if there is a
            violation
    """

    classifications: Union[Unset, list[Classification]] = UNSET
    is_safe: Union[Unset, bool] = UNSET
    severity: Union[Unset, InspectResponseSeverity] = UNSET
    rules: Union[Unset, list["RuleObject"]] = UNSET
    attack_technique: Union[Unset, str] = UNSET
    explanation: Union[Unset, str] = UNSET
    client_transaction_id: Union[Unset, str] = UNSET
    event_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        classifications: Union[Unset, list[str]] = UNSET
        if not isinstance(self.classifications, Unset):
            classifications = []
            for classifications_item_data in self.classifications:
                classifications_item = classifications_item_data.value
                classifications.append(classifications_item)

        is_safe = self.is_safe

        severity: Union[Unset, str] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        attack_technique = self.attack_technique

        explanation = self.explanation

        client_transaction_id = self.client_transaction_id

        event_id = self.event_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if classifications is not UNSET:
            field_dict["classifications"] = classifications
        if is_safe is not UNSET:
            field_dict["is_safe"] = is_safe
        if severity is not UNSET:
            field_dict["severity"] = severity
        if rules is not UNSET:
            field_dict["rules"] = rules
        if attack_technique is not UNSET:
            field_dict["attack_technique"] = attack_technique
        if explanation is not UNSET:
            field_dict["explanation"] = explanation
        if client_transaction_id is not UNSET:
            field_dict["client_transaction_id"] = client_transaction_id
        if event_id is not UNSET:
            field_dict["event_id"] = event_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rule_object import RuleObject

        d = dict(src_dict)
        classifications = []
        _classifications = d.pop("classifications", UNSET)
        for classifications_item_data in _classifications or []:
            classifications_item = Classification(classifications_item_data)

            classifications.append(classifications_item)

        is_safe = d.pop("is_safe", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, InspectResponseSeverity]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = InspectResponseSeverity(_severity)

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = RuleObject.from_dict(rules_item_data)

            rules.append(rules_item)

        attack_technique = d.pop("attack_technique", UNSET)

        explanation = d.pop("explanation", UNSET)

        client_transaction_id = d.pop("client_transaction_id", UNSET)

        event_id = d.pop("event_id", UNSET)

        inspect_response = cls(
            classifications=classifications,
            is_safe=is_safe,
            severity=severity,
            rules=rules,
            attack_technique=attack_technique,
            explanation=explanation,
            client_transaction_id=client_transaction_id,
            event_id=event_id,
        )

        inspect_response.additional_properties = d
        return inspect_response

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
