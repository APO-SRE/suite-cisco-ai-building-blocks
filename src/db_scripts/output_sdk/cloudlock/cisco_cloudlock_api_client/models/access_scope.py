from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scope_category import ScopeCategory


T = TypeVar("T", bound="AccessScope")


@_attrs_define
class AccessScope:
    """
    Attributes:
        category (Union[Unset, ScopeCategory]): The scope categories resource returns information on the access scopes,
            which exist per each category.
            Scope category strings: `FDATA` (full data access), `BINFO` (basic info), `LACES` (limited access to data and
            files),
            `PINFO` (payment information), and `INBO`X (access inbox or contact information).
        id (Union[Unset, str]): The internal Cloudlock ID for the access scope.
        description (Union[Unset, str]): A verbose description of the access scope, for example: `View your email
            address`.
        friendly_name (Union[Unset, str]): The name of the access scope. In the UI this is the `ACCESS SCOPE` in the
            Access Scopes table. For example: `Userinfo - Email`.
        url (Union[Unset, str]): The url to the access scope. For example:
            'https://www.googleapis.com/auth/userinfo.email'.
    """

    category: Union[Unset, "ScopeCategory"] = UNSET
    id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    friendly_name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        id = self.id

        description = self.description

        friendly_name = self.friendly_name

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if friendly_name is not UNSET:
            field_dict["friendly_name"] = friendly_name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scope_category import ScopeCategory

        d = dict(src_dict)
        _category = d.pop("category", UNSET)
        category: Union[Unset, ScopeCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ScopeCategory.from_dict(_category)

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        friendly_name = d.pop("friendly_name", UNSET)

        url = d.pop("url", UNSET)

        access_scope = cls(
            category=category,
            id=id,
            description=description,
            friendly_name=friendly_name,
            url=url,
        )

        access_scope.additional_properties = d
        return access_scope

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
