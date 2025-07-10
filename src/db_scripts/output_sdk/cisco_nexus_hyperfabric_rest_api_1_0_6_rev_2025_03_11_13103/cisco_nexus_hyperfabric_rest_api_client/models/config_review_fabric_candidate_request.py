from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigReviewFabricCandidateRequest")


@_attrs_define
class ConfigReviewFabricCandidateRequest:
    """The request to add review comments to a specific candidate configuration of a fabric.

    Attributes:
        comments (Union[Unset, str]): The comments to be added as a review to the candidate configuration.
        fabric_id (Union[Unset, str]): The fabric id or name.
        name (Union[Unset, str]): The candidate configuration name.
    """

    comments: Union[Unset, str] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comments = self.comments

        fabric_id = self.fabric_id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comments is not UNSET:
            field_dict["comments"] = comments
        if fabric_id is not UNSET:
            field_dict["fabricId"] = fabric_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comments = d.pop("comments", UNSET)

        fabric_id = d.pop("fabricId", UNSET)

        name = d.pop("name", UNSET)

        config_review_fabric_candidate_request = cls(
            comments=comments,
            fabric_id=fabric_id,
            name=name,
        )

        config_review_fabric_candidate_request.additional_properties = d
        return config_review_fabric_candidate_request

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
