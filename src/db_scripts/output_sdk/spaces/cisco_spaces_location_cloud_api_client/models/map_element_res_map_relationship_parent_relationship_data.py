from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MapElementResMapRelationshipParentRelationshipData")


@_attrs_define
class MapElementResMapRelationshipParentRelationshipData:
    """
    Attributes:
        ancestors (Union[Unset, list[str]]):
        ancestors_ids (Union[Unset, list[str]]):
    """

    ancestors: Union[Unset, list[str]] = UNSET
    ancestors_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ancestors: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ancestors, Unset):
            ancestors = self.ancestors

        ancestors_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ancestors_ids, Unset):
            ancestors_ids = self.ancestors_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ancestors is not UNSET:
            field_dict["ancestors"] = ancestors
        if ancestors_ids is not UNSET:
            field_dict["ancestorsIds"] = ancestors_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ancestors = cast(list[str], d.pop("ancestors", UNSET))

        ancestors_ids = cast(list[str], d.pop("ancestorsIds", UNSET))

        map_element_res_map_relationship_parent_relationship_data = cls(
            ancestors=ancestors,
            ancestors_ids=ancestors_ids,
        )

        map_element_res_map_relationship_parent_relationship_data.additional_properties = d
        return map_element_res_map_relationship_parent_relationship_data

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
