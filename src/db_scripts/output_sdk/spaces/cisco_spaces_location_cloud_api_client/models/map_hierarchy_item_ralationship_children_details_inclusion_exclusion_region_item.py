from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_hierarchy_item_corner import MapHierarchyItemCorner


T = TypeVar("T", bound="MapHierarchyItemRalationshipChildrenDetailsInclusionExclusionRegionItem")


@_attrs_define
class MapHierarchyItemRalationshipChildrenDetailsInclusionExclusionRegionItem:
    """
    Attributes:
        v0 (Union[Unset, MapHierarchyItemCorner]):
        v1 (Union[Unset, MapHierarchyItemCorner]):
        v2 (Union[Unset, MapHierarchyItemCorner]):
        v3 (Union[Unset, MapHierarchyItemCorner]):
        type_ (Union[Unset, str]): Indicate how to handle the vertices on map. Example: OUTSIDE.
        vertices (Union[Unset, int]): The number of vertices. Example: 4.
    """

    v0: Union[Unset, "MapHierarchyItemCorner"] = UNSET
    v1: Union[Unset, "MapHierarchyItemCorner"] = UNSET
    v2: Union[Unset, "MapHierarchyItemCorner"] = UNSET
    v3: Union[Unset, "MapHierarchyItemCorner"] = UNSET
    type_: Union[Unset, str] = UNSET
    vertices: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        v0: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.v0, Unset):
            v0 = self.v0.to_dict()

        v1: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.v1, Unset):
            v1 = self.v1.to_dict()

        v2: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.v2, Unset):
            v2 = self.v2.to_dict()

        v3: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.v3, Unset):
            v3 = self.v3.to_dict()

        type_ = self.type_

        vertices = self.vertices

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if v0 is not UNSET:
            field_dict["v0"] = v0
        if v1 is not UNSET:
            field_dict["v1"] = v1
        if v2 is not UNSET:
            field_dict["v2"] = v2
        if v3 is not UNSET:
            field_dict["v3"] = v3
        if type_ is not UNSET:
            field_dict["type"] = type_
        if vertices is not UNSET:
            field_dict["vertices"] = vertices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_hierarchy_item_corner import MapHierarchyItemCorner

        d = dict(src_dict)
        _v0 = d.pop("v0", UNSET)
        v0: Union[Unset, MapHierarchyItemCorner]
        if isinstance(_v0, Unset):
            v0 = UNSET
        else:
            v0 = MapHierarchyItemCorner.from_dict(_v0)

        _v1 = d.pop("v1", UNSET)
        v1: Union[Unset, MapHierarchyItemCorner]
        if isinstance(_v1, Unset):
            v1 = UNSET
        else:
            v1 = MapHierarchyItemCorner.from_dict(_v1)

        _v2 = d.pop("v2", UNSET)
        v2: Union[Unset, MapHierarchyItemCorner]
        if isinstance(_v2, Unset):
            v2 = UNSET
        else:
            v2 = MapHierarchyItemCorner.from_dict(_v2)

        _v3 = d.pop("v3", UNSET)
        v3: Union[Unset, MapHierarchyItemCorner]
        if isinstance(_v3, Unset):
            v3 = UNSET
        else:
            v3 = MapHierarchyItemCorner.from_dict(_v3)

        type_ = d.pop("type", UNSET)

        vertices = d.pop("vertices", UNSET)

        map_hierarchy_item_ralationship_children_details_inclusion_exclusion_region_item = cls(
            v0=v0,
            v1=v1,
            v2=v2,
            v3=v3,
            type_=type_,
            vertices=vertices,
        )

        map_hierarchy_item_ralationship_children_details_inclusion_exclusion_region_item.additional_properties = d
        return map_hierarchy_item_ralationship_children_details_inclusion_exclusion_region_item

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
