import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_element_res_map_details import MapElementResMapDetails
    from ..models.map_element_res_map_relationship import MapElementResMapRelationship


T = TypeVar("T", bound="MapElementResMap")


@_attrs_define
class MapElementResMap:
    """
    Attributes:
        id (Union[Unset, str]): The element unique identifier. Example: 2616615914b2433c83e33f404ca59aa6.
        name (Union[Unset, str]): The element name. Example: jkp-build.
        level (Union[Unset, str]): The level in the map hierarchy. Example: BUILDING.
        imported_id (Union[Unset, str]):  Example: -6047456030286152000.
        created_on (Union[Unset, datetime.datetime]): The item creation time. Example: 2018-04-04T16:50:48.334Z.
        details (Union[Unset, MapElementResMapDetails]):
        relationship_data (Union[Unset, MapElementResMapRelationship]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    level: Union[Unset, str] = UNSET
    imported_id: Union[Unset, str] = UNSET
    created_on: Union[Unset, datetime.datetime] = UNSET
    details: Union[Unset, "MapElementResMapDetails"] = UNSET
    relationship_data: Union[Unset, "MapElementResMapRelationship"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        level = self.level

        imported_id = self.imported_id

        created_on: Union[Unset, str] = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

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
        from ..models.map_element_res_map_details import MapElementResMapDetails
        from ..models.map_element_res_map_relationship import MapElementResMapRelationship

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        level = d.pop("level", UNSET)

        imported_id = d.pop("importedId", UNSET)

        _created_on = d.pop("createdOn", UNSET)
        created_on: Union[Unset, datetime.datetime]
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        _details = d.pop("details", UNSET)
        details: Union[Unset, MapElementResMapDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = MapElementResMapDetails.from_dict(_details)

        _relationship_data = d.pop("relationshipData", UNSET)
        relationship_data: Union[Unset, MapElementResMapRelationship]
        if isinstance(_relationship_data, Unset):
            relationship_data = UNSET
        else:
            relationship_data = MapElementResMapRelationship.from_dict(_relationship_data)

        map_element_res_map = cls(
            id=id,
            name=name,
            level=level,
            imported_id=imported_id,
            created_on=created_on,
            details=details,
            relationship_data=relationship_data,
        )

        map_element_res_map.additional_properties = d
        return map_element_res_map

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
