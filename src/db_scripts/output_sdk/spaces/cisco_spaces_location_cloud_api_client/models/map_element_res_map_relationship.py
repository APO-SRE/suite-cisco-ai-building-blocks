from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_element_res_map_relationship_children import MapElementResMapRelationshipChildren
    from ..models.map_element_res_map_relationship_parent import MapElementResMapRelationshipParent


T = TypeVar("T", bound="MapElementResMapRelationship")


@_attrs_define
class MapElementResMapRelationship:
    """
    Attributes:
        ancestors (Union[Unset, list[str]]):
        ancestors_ids (Union[Unset, list[str]]):
        children (Union[Unset, list['MapElementResMapRelationshipChildren']]):
        parent (Union[Unset, MapElementResMapRelationshipParent]):
    """

    ancestors: Union[Unset, list[str]] = UNSET
    ancestors_ids: Union[Unset, list[str]] = UNSET
    children: Union[Unset, list["MapElementResMapRelationshipChildren"]] = UNSET
    parent: Union[Unset, "MapElementResMapRelationshipParent"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ancestors: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ancestors, Unset):
            ancestors = self.ancestors

        ancestors_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ancestors_ids, Unset):
            ancestors_ids = self.ancestors_ids

        children: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        parent: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ancestors is not UNSET:
            field_dict["ancestors"] = ancestors
        if ancestors_ids is not UNSET:
            field_dict["ancestorsIds"] = ancestors_ids
        if children is not UNSET:
            field_dict["children"] = children
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_element_res_map_relationship_children import MapElementResMapRelationshipChildren
        from ..models.map_element_res_map_relationship_parent import MapElementResMapRelationshipParent

        d = dict(src_dict)
        ancestors = cast(list[str], d.pop("ancestors", UNSET))

        ancestors_ids = cast(list[str], d.pop("ancestorsIds", UNSET))

        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in _children or []:
            children_item = MapElementResMapRelationshipChildren.from_dict(children_item_data)

            children.append(children_item)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, MapElementResMapRelationshipParent]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = MapElementResMapRelationshipParent.from_dict(_parent)

        map_element_res_map_relationship = cls(
            ancestors=ancestors,
            ancestors_ids=ancestors_ids,
            children=children,
            parent=parent,
        )

        map_element_res_map_relationship.additional_properties = d
        return map_element_res_map_relationship

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
