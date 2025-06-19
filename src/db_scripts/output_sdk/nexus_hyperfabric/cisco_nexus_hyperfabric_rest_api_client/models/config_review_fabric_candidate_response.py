from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigReviewFabricCandidateResponse")


@_attrs_define
class ConfigReviewFabricCandidateResponse:
    """The response to a request to add review comments to a specific candidate configuration of a fabric.

    Attributes:
        fabric_id (Union[Unset, str]): The fabric identifier.
    """

    fabric_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fabric_id = self.fabric_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fabric_id is not UNSET:
            field_dict["fabricId"] = fabric_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fabric_id = d.pop("fabricId", UNSET)

        config_review_fabric_candidate_response = cls(
            fabric_id=fabric_id,
        )

        config_review_fabric_candidate_response.additional_properties = d
        return config_review_fabric_candidate_response

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
