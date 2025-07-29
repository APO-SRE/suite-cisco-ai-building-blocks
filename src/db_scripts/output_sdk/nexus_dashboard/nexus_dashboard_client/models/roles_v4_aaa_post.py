from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roles_v4_aaa_post_roles import RolesV4AaaPOSTRoles


T = TypeVar("T", bound="RolesV4AaaPOST")


@_attrs_define
class RolesV4AaaPOST:
    """
    Attributes:
        roles (Union[Unset, RolesV4AaaPOSTRoles]): Mapping of ND Roles and Read/Write Privileges
    """

    roles: Union[Unset, "RolesV4AaaPOSTRoles"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        roles: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roles_v4_aaa_post_roles import RolesV4AaaPOSTRoles

        d = dict(src_dict)
        _roles = d.pop("roles", UNSET)
        roles: Union[Unset, RolesV4AaaPOSTRoles]
        if isinstance(_roles, Unset):
            roles = UNSET
        else:
            roles = RolesV4AaaPOSTRoles.from_dict(_roles)

        roles_v4_aaa_post = cls(
            roles=roles,
        )

        roles_v4_aaa_post.additional_properties = d
        return roles_v4_aaa_post

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
