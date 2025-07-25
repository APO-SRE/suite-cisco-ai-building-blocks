from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_fabric_candidate import ConfigFabricCandidate


T = TypeVar("T", bound="ConfigGetFabricCandidatesResponse")


@_attrs_define
class ConfigGetFabricCandidatesResponse:
    """The response to a request for a list of candidate configurations of a specific fabric.

    Attributes:
        candidates (Union[Unset, list['ConfigFabricCandidate']]): A list of candidate configurations of a specific
            fabric
    """

    candidates: Union[Unset, list["ConfigFabricCandidate"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        candidates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.candidates, Unset):
            candidates = []
            for candidates_item_data in self.candidates:
                candidates_item = candidates_item_data.to_dict()
                candidates.append(candidates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if candidates is not UNSET:
            field_dict["candidates"] = candidates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_fabric_candidate import ConfigFabricCandidate

        d = dict(src_dict)
        candidates = []
        _candidates = d.pop("candidates", UNSET)
        for candidates_item_data in _candidates or []:
            candidates_item = ConfigFabricCandidate.from_dict(candidates_item_data)

            candidates.append(candidates_item)

        config_get_fabric_candidates_response = cls(
            candidates=candidates,
        )

        config_get_fabric_candidates_response.additional_properties = d
        return config_get_fabric_candidates_response

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
