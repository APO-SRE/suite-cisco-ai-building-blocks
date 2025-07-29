from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_policy_criteria import MatchPolicyCriteria


T = TypeVar("T", bound="Match")


@_attrs_define
class Match:
    """A Match represents an occurrence of a content pattern in an object (such as a file).
    The content pattern is defined in a policy.

        Attributes:
            created_at (Union[Unset, str]): The time when this match was detected. Time expressed as a timestamp in UTC.
            ctx_after (Union[Unset, str]): The characters after the match.
            ctx_before (Union[Unset, str]): The characters before the match.
            field_name (Union[Unset, str]): The field or object for this match.
            text (Union[Unset, str]): Provide string to identify object. Relevant for content detection criteria='Custom
                regex criteria' only.
            policy_criteria (Union[Unset, MatchPolicyCriteria]): A description of the policy criteria.
    """

    created_at: Union[Unset, str] = UNSET
    ctx_after: Union[Unset, str] = UNSET
    ctx_before: Union[Unset, str] = UNSET
    field_name: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    policy_criteria: Union[Unset, "MatchPolicyCriteria"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        ctx_after = self.ctx_after

        ctx_before = self.ctx_before

        field_name = self.field_name

        text = self.text

        policy_criteria: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.policy_criteria, Unset):
            policy_criteria = self.policy_criteria.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if ctx_after is not UNSET:
            field_dict["ctx_after"] = ctx_after
        if ctx_before is not UNSET:
            field_dict["ctx_before"] = ctx_before
        if field_name is not UNSET:
            field_dict["field_name"] = field_name
        if text is not UNSET:
            field_dict["text"] = text
        if policy_criteria is not UNSET:
            field_dict["policy_criteria"] = policy_criteria

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.match_policy_criteria import MatchPolicyCriteria

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        ctx_after = d.pop("ctx_after", UNSET)

        ctx_before = d.pop("ctx_before", UNSET)

        field_name = d.pop("field_name", UNSET)

        text = d.pop("text", UNSET)

        _policy_criteria = d.pop("policy_criteria", UNSET)
        policy_criteria: Union[Unset, MatchPolicyCriteria]
        if isinstance(_policy_criteria, Unset):
            policy_criteria = UNSET
        else:
            policy_criteria = MatchPolicyCriteria.from_dict(_policy_criteria)

        match = cls(
            created_at=created_at,
            ctx_after=ctx_after,
            ctx_before=ctx_before,
            field_name=field_name,
            text=text,
            policy_criteria=policy_criteria,
        )

        match.additional_properties = d
        return match

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
