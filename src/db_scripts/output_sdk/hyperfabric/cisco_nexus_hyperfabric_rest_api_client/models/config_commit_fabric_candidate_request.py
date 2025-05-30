from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigCommitFabricCandidateRequest")


@_attrs_define
class ConfigCommitFabricCandidateRequest:
    """CommitFabricCandidateRequest encapsulates properties to commit a pending fabric candidate. Candidates commit may
    require special user privileges.

        Attributes:
            comments (Union[Unset, str]): The reason for commit.
            fabric_id (Union[Unset, str]): The fabric identifier. Fabric identifier is mandatory.
            name (Union[Unset, str]): The candidate name.
            revision_id (Union[Unset, str]): The candidate revision identifier.
    """

    comments: Union[Unset, str] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    revision_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comments = self.comments

        fabric_id = self.fabric_id

        name = self.name

        revision_id = self.revision_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comments is not UNSET:
            field_dict["comments"] = comments
        if fabric_id is not UNSET:
            field_dict["fabricId"] = fabric_id
        if name is not UNSET:
            field_dict["name"] = name
        if revision_id is not UNSET:
            field_dict["revisionId"] = revision_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comments = d.pop("comments", UNSET)

        fabric_id = d.pop("fabricId", UNSET)

        name = d.pop("name", UNSET)

        revision_id = d.pop("revisionId", UNSET)

        config_commit_fabric_candidate_request = cls(
            comments=comments,
            fabric_id=fabric_id,
            name=name,
            revision_id=revision_id,
        )

        config_commit_fabric_candidate_request.additional_properties = d
        return config_commit_fabric_candidate_request

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
