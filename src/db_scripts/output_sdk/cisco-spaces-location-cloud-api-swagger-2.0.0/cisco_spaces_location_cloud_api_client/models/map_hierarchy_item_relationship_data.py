from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_hierarchy_item_ralationship_children import MapHierarchyItemRalationshipChildren
    from ..models.map_hierarchy_item_relationship_data_parent import MapHierarchyItemRelationshipDataParent


T = TypeVar("T", bound="MapHierarchyItemRelationshipData")


@_attrs_define
class MapHierarchyItemRelationshipData:
    """
    Attributes:
        ancestors (Union[Unset, list[str]]):
        ancestor_ids (Union[Unset, list[str]]):
        children (Union[Unset, list['MapHierarchyItemRalationshipChildren']]):
        parent (Union[Unset, MapHierarchyItemRelationshipDataParent]):
    """

    ancestors: Union[Unset, list[str]] = UNSET
    ancestor_ids: Union[Unset, list[str]] = UNSET
    children: Union[Unset, list["MapHierarchyItemRalationshipChildren"]] = UNSET
    parent: Union[Unset, "MapHierarchyItemRelationshipDataParent"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ancestors: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ancestors, Unset):
            ancestors = self.ancestors

        ancestor_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ancestor_ids, Unset):
            ancestor_ids = self.ancestor_ids

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
        if ancestor_ids is not UNSET:
            field_dict["ancestorIds"] = ancestor_ids
        if children is not UNSET:
            field_dict["children"] = children
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_hierarchy_item_ralationship_children import MapHierarchyItemRalationshipChildren
        from ..models.map_hierarchy_item_relationship_data_parent import MapHierarchyItemRelationshipDataParent

        d = dict(src_dict)
        ancestors = cast(list[str], d.pop("ancestors", UNSET))

        ancestor_ids = cast(list[str], d.pop("ancestorIds", UNSET))

        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in _children or []:
            children_item = MapHierarchyItemRalationshipChildren.from_dict(children_item_data)

            children.append(children_item)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, MapHierarchyItemRelationshipDataParent]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = MapHierarchyItemRelationshipDataParent.from_dict(_parent)

        map_hierarchy_item_relationship_data = cls(
            ancestors=ancestors,
            ancestor_ids=ancestor_ids,
            children=children,
            parent=parent,
        )

        map_hierarchy_item_relationship_data.additional_properties = d
        return map_hierarchy_item_relationship_data

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
