from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_hierarchy_item_ralationship_children_details import MapHierarchyItemRalationshipChildrenDetails
    from ..models.map_hierarchy_item_ralationship_children_relationship_data import (
        MapHierarchyItemRalationshipChildrenRelationshipData,
    )


T = TypeVar("T", bound="MapHierarchyItemRalationshipChildren")


@_attrs_define
class MapHierarchyItemRalationshipChildren:
    """
    Attributes:
        id (Union[Unset, str]): Compus unique identifier. Example: ef148ae7277649da885e08ef40f49d27.
        name (Union[Unset, str]): Compus name. Example: Simulator-100-Campus0.
        level (Union[Unset, str]): The level in the hireachy. Example: BUILDING.
        imported_id (Union[Unset, str]): The level in the hireachy. Example: 1721917301.
        created_on (Union[Unset, str]): The date and time of the level being created. Example: 2017-12-18T23:10:16.122Z.
        details (Union[Unset, MapHierarchyItemRalationshipChildrenDetails]):
        relationship_data (Union[Unset, MapHierarchyItemRalationshipChildrenRelationshipData]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    level: Union[Unset, str] = UNSET
    imported_id: Union[Unset, str] = UNSET
    created_on: Union[Unset, str] = UNSET
    details: Union[Unset, "MapHierarchyItemRalationshipChildrenDetails"] = UNSET
    relationship_data: Union[Unset, "MapHierarchyItemRalationshipChildrenRelationshipData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        level = self.level

        imported_id = self.imported_id

        created_on = self.created_on

        details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        relationship_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.relationship_data, Unset):
            relationship_data = self.relationship_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if level is not UNSET:
            field_dict["level"] = level
        if imported_id is not UNSET:
            field_dict["importedId"] = imported_id
        if created_on is not UNSET:
            field_dict["createdOn"] = created_on
        if details is not UNSET:
            field_dict["details"] = details
        if relationship_data is not UNSET:
            field_dict["relationshipData"] = relationship_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_hierarchy_item_ralationship_children_details import (
            MapHierarchyItemRalationshipChildrenDetails,
        )
        from ..models.map_hierarchy_item_ralationship_children_relationship_data import (
            MapHierarchyItemRalationshipChildrenRelationshipData,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        level = d.pop("level", UNSET)

        imported_id = d.pop("importedId", UNSET)

        created_on = d.pop("createdOn", UNSET)

        _details = d.pop("details", UNSET)
        details: Union[Unset, MapHierarchyItemRalationshipChildrenDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = MapHierarchyItemRalationshipChildrenDetails.from_dict(_details)

        _relationship_data = d.pop("relationshipData", UNSET)
        relationship_data: Union[Unset, MapHierarchyItemRalationshipChildrenRelationshipData]
        if isinstance(_relationship_data, Unset):
            relationship_data = UNSET
        else:
            relationship_data = MapHierarchyItemRalationshipChildrenRelationshipData.from_dict(_relationship_data)

        map_hierarchy_item_ralationship_children = cls(
            id=id,
            name=name,
            level=level,
            imported_id=imported_id,
            created_on=created_on,
            details=details,
            relationship_data=relationship_data,
        )

        map_hierarchy_item_ralationship_children.additional_properties = d
        return map_hierarchy_item_ralationship_children

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
