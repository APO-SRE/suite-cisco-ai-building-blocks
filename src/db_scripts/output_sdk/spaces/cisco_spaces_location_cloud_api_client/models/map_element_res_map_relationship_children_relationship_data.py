from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MapElementResMapRelationshipChildrenRelationshipData")


@_attrs_define
class MapElementResMapRelationshipChildrenRelationshipData:
    """
    Attributes:
        ancestors (Union[Unset, list[str]]): The acestors of the child.
        ancestor_ids (Union[Unset, list[str]]): The acestors of the child.
    """

    ancestors: Union[Unset, list[str]] = UNSET
    ancestor_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ancestors: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ancestors, Unset):
            ancestors = self.ancestors

        ancestor_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ancestor_ids, Unset):
            ancestor_ids = self.ancestor_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ancestors is not UNSET:
            field_dict["ancestors"] = ancestors
        if ancestor_ids is not UNSET:
            field_dict["ancestorIds"] = ancestor_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ancestors = cast(list[str], d.pop("ancestors", UNSET))

        ancestor_ids = cast(list[str], d.pop("ancestorIds", UNSET))

        map_element_res_map_relationship_children_relationship_data = cls(
            ancestors=ancestors,
            ancestor_ids=ancestor_ids,
        )

        map_element_res_map_relationship_children_relationship_data.additional_properties = d
        return map_element_res_map_relationship_children_relationship_data

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
