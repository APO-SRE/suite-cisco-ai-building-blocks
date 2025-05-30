from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_bgp_match_group import ModelsBgpMatchGroup
    from ..models.models_bgp_set_group import ModelsBgpSetGroup


T = TypeVar("T", bound="ModelsBgpRule")


@_attrs_define
class ModelsBgpRule:
    """BgpRule encapsulates properties of a BGP rule.

    Attributes:
        accept (Union[Unset, bool]): Accept or reject (permit or deny).
        action (Union[Unset, str]): Extended action (E.g. on-match next or on-match goto <ruleId>
        description (Union[Unset, str]): The user-defined description of rule.
        id (Union[Unset, int]): The identifier of the rule. Id is also the sequence number of rule within the rule list.
            User may set the identifier, Maximum value may not exceed 100.
        match_group (Union[Unset, ModelsBgpMatchGroup]): BgpMatchGroup encapsulates "MATCH" part of a BgpRule. E.g.
            match community <COMMUNITY_LIST>. Note that prefixes are mutually exclusive for matching. That means caller must
            not provide both IPv4 and IPv6 prefixes.
        set_group (Union[Unset, ModelsBgpSetGroup]): BgpSetGroup encapsulates "SET" part of a BgpRule. E.g. set tag 5000
    """

    accept: Union[Unset, bool] = UNSET
    action: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    match_group: Union[Unset, "ModelsBgpMatchGroup"] = UNSET
    set_group: Union[Unset, "ModelsBgpSetGroup"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accept = self.accept

        action = self.action

        description = self.description

        id = self.id

        match_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.match_group, Unset):
            match_group = self.match_group.to_dict()

        set_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.set_group, Unset):
            set_group = self.set_group.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accept is not UNSET:
            field_dict["accept"] = accept
        if action is not UNSET:
            field_dict["action"] = action
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if match_group is not UNSET:
            field_dict["matchGroup"] = match_group
        if set_group is not UNSET:
            field_dict["setGroup"] = set_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_bgp_match_group import ModelsBgpMatchGroup
        from ..models.models_bgp_set_group import ModelsBgpSetGroup

        d = dict(src_dict)
        accept = d.pop("accept", UNSET)

        action = d.pop("action", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        _match_group = d.pop("matchGroup", UNSET)
        match_group: Union[Unset, ModelsBgpMatchGroup]
        if isinstance(_match_group, Unset):
            match_group = UNSET
        else:
            match_group = ModelsBgpMatchGroup.from_dict(_match_group)

        _set_group = d.pop("setGroup", UNSET)
        set_group: Union[Unset, ModelsBgpSetGroup]
        if isinstance(_set_group, Unset):
            set_group = UNSET
        else:
            set_group = ModelsBgpSetGroup.from_dict(_set_group)

        models_bgp_rule = cls(
            accept=accept,
            action=action,
            description=description,
            id=id,
            match_group=match_group,
            set_group=set_group,
        )

        models_bgp_rule.additional_properties = d
        return models_bgp_rule

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
