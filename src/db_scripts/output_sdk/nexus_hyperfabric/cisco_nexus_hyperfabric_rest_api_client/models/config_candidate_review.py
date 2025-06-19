import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.models_operation import ModelsOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigCandidateReview")


@_attrs_define
class ConfigCandidateReview:
    """CandidateReview represents a candidate review record. CandidateReview records are created when users add review
    comments.

        Attributes:
            comments (Union[Unset, str]): Transaction comments.
            created_at (Union[Unset, datetime.datetime]): Description not available
            created_by (Union[Unset, str]): UserId of the user who added the comments.
            operation (Union[Unset, ModelsOperation]): Operation defines an enumeration of the types of operations or
                actions.
    """

    comments: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    operation: Union[Unset, ModelsOperation] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comments = self.comments

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by = self.created_by

        operation: Union[Unset, str] = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comments is not UNSET:
            field_dict["comments"] = comments
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if operation is not UNSET:
            field_dict["operation"] = operation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comments = d.pop("comments", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        created_by = d.pop("createdBy", UNSET)

        _operation = d.pop("operation", UNSET)
        operation: Union[Unset, ModelsOperation]
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = ModelsOperation(_operation)

        config_candidate_review = cls(
            comments=comments,
            created_at=created_at,
            created_by=created_by,
            operation=operation,
        )

        config_candidate_review.additional_properties = d
        return config_candidate_review

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
