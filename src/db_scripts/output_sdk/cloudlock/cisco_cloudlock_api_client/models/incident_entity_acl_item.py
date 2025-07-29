from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vendor import Vendor


T = TypeVar("T", bound="IncidentEntityAclItem")


@_attrs_define
class IncidentEntityAclItem:
    """
    Attributes:
        id (Union[Unset, str]):
        value (Union[Unset, str]):
        role (Union[Unset, str]):
        type_ (Union[Unset, str]):
        status (Union[Unset, str]):
        created_on (Union[Unset, str]):
        vendor (Union[Unset, Vendor]):
        origin_id (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    role: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    created_on: Union[Unset, str] = UNSET
    vendor: Union[Unset, "Vendor"] = UNSET
    origin_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        value = self.value

        role = self.role

        type_ = self.type_

        status = self.status

        created_on = self.created_on

        vendor: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vendor, Unset):
            vendor = self.vendor.to_dict()

        origin_id = self.origin_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value
        if role is not UNSET:
            field_dict["role"] = role
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if origin_id is not UNSET:
            field_dict["origin_id"] = origin_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vendor import Vendor

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        value = d.pop("value", UNSET)

        role = d.pop("role", UNSET)

        type_ = d.pop("type", UNSET)

        status = d.pop("status", UNSET)

        created_on = d.pop("created_on", UNSET)

        _vendor = d.pop("vendor", UNSET)
        vendor: Union[Unset, Vendor]
        if isinstance(_vendor, Unset):
            vendor = UNSET
        else:
            vendor = Vendor.from_dict(_vendor)

        origin_id = d.pop("origin_id", UNSET)

        incident_entity_acl_item = cls(
            id=id,
            value=value,
            role=role,
            type_=type_,
            status=status,
            created_on=created_on,
            vendor=vendor,
            origin_id=origin_id,
        )

        incident_entity_acl_item.additional_properties = d
        return incident_entity_acl_item

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
