from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity import Entity
    from ..models.incident_entity_acl_item import IncidentEntityAclItem


T = TypeVar("T", bound="IncidentEntity")


@_attrs_define
class IncidentEntity:
    """The information about the object relating to this incident.

    Attributes:
        acl (Union[Unset, list['IncidentEntityAclItem']]):
        entity (Union[Unset, Entity]): The information about the object relating to this incident.
    """

    acl: Union[Unset, list["IncidentEntityAclItem"]] = UNSET
    entity: Union[Unset, "Entity"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acl: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.acl, Unset):
            acl = []
            for acl_item_data in self.acl:
                acl_item = acl_item_data.to_dict()
                acl.append(acl_item)

        entity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entity, Unset):
            entity = self.entity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acl is not UNSET:
            field_dict["acl"] = acl
        if entity is not UNSET:
            field_dict["entity"] = entity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity import Entity
        from ..models.incident_entity_acl_item import IncidentEntityAclItem

        d = dict(src_dict)
        acl = []
        _acl = d.pop("acl", UNSET)
        for acl_item_data in _acl or []:
            acl_item = IncidentEntityAclItem.from_dict(acl_item_data)

            acl.append(acl_item)

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, Entity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = Entity.from_dict(_entity)

        incident_entity = cls(
            acl=acl,
            entity=entity,
        )

        incident_entity.additional_properties = d
        return incident_entity

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
