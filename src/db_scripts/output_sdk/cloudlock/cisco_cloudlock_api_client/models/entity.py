from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_extra import EntityExtra
    from ..models.vendor import Vendor


T = TypeVar("T", bound="Entity")


@_attrs_define
class Entity:
    """The information about the object relating to this incident.

    Attributes:
        direct_url (Union[Unset, str]): The URL to the object.
        extra (Union[Unset, EntityExtra]): The additional information related to the incident.
        id (Union[Unset, str]): This is Cloudlock Internal Identifier for an entity.
        mime_type (Union[Unset, str]): The mime type of the object/document (if any)
        name (Union[Unset, str]): The name of the underlying object represented by this entity.
        origin_id (Union[Unset, str]): This is the identifier of the object in the vendor system.
        origin_type (Union[Unset, str]): The object type (i.e. document, post, app, event).
        owner_email (Union[Unset, str]): Object owner's email address (e.g. user@cloudlock.com).
        owner_name (Union[Unset, str]): Object owner's name (i.e. John Q. User).
        vendor (Union[Unset, Vendor]):
    """

    direct_url: Union[Unset, str] = UNSET
    extra: Union[Unset, "EntityExtra"] = UNSET
    id: Union[Unset, str] = UNSET
    mime_type: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    origin_id: Union[Unset, str] = UNSET
    origin_type: Union[Unset, str] = UNSET
    owner_email: Union[Unset, str] = UNSET
    owner_name: Union[Unset, str] = UNSET
    vendor: Union[Unset, "Vendor"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        direct_url = self.direct_url

        extra: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.extra, Unset):
            extra = self.extra.to_dict()

        id = self.id

        mime_type = self.mime_type

        name = self.name

        origin_id = self.origin_id

        origin_type = self.origin_type

        owner_email = self.owner_email

        owner_name = self.owner_name

        vendor: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vendor, Unset):
            vendor = self.vendor.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if direct_url is not UNSET:
            field_dict["direct_url"] = direct_url
        if extra is not UNSET:
            field_dict["extra"] = extra
        if id is not UNSET:
            field_dict["id"] = id
        if mime_type is not UNSET:
            field_dict["mime_type"] = mime_type
        if name is not UNSET:
            field_dict["name"] = name
        if origin_id is not UNSET:
            field_dict["origin_id"] = origin_id
        if origin_type is not UNSET:
            field_dict["origin_type"] = origin_type
        if owner_email is not UNSET:
            field_dict["owner_email"] = owner_email
        if owner_name is not UNSET:
            field_dict["owner_name"] = owner_name
        if vendor is not UNSET:
            field_dict["vendor"] = vendor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_extra import EntityExtra
        from ..models.vendor import Vendor

        d = dict(src_dict)
        direct_url = d.pop("direct_url", UNSET)

        _extra = d.pop("extra", UNSET)
        extra: Union[Unset, EntityExtra]
        if isinstance(_extra, Unset):
            extra = UNSET
        else:
            extra = EntityExtra.from_dict(_extra)

        id = d.pop("id", UNSET)

        mime_type = d.pop("mime_type", UNSET)

        name = d.pop("name", UNSET)

        origin_id = d.pop("origin_id", UNSET)

        origin_type = d.pop("origin_type", UNSET)

        owner_email = d.pop("owner_email", UNSET)

        owner_name = d.pop("owner_name", UNSET)

        _vendor = d.pop("vendor", UNSET)
        vendor: Union[Unset, Vendor]
        if isinstance(_vendor, Unset):
            vendor = UNSET
        else:
            vendor = Vendor.from_dict(_vendor)

        entity = cls(
            direct_url=direct_url,
            extra=extra,
            id=id,
            mime_type=mime_type,
            name=name,
            origin_id=origin_id,
            origin_type=origin_type,
            owner_email=owner_email,
            owner_name=owner_name,
            vendor=vendor,
        )

        entity.additional_properties = d
        return entity

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
