from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_user import ModelsUser


T = TypeVar("T", bound="AuthSetUsersRequest")


@_attrs_define
class AuthSetUsersRequest:
    """SetUsersRequest creates or updates the specified users in the context of this tenant.

    Attributes:
        tenant_id (Union[Unset, str]): Identify a specific tenant, optional. If not specified, the tenant associated
            with the current user session making the request is used. Users will be created or updated in the resulting
            tenant. This parameter allows an admin of the default-tenant to create or update users in a non-default tenant
            of the organization.
        users (Union[Unset, list['ModelsUser']]): A list of users, each one representing a user to be created or updated
            in the tenant.
    """

    tenant_id: Union[Unset, str] = UNSET
    users: Union[Unset, list["ModelsUser"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tenant_id = self.tenant_id

        users: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_user import ModelsUser

        d = dict(src_dict)
        tenant_id = d.pop("tenantId", UNSET)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = ModelsUser.from_dict(users_item_data)

            users.append(users_item)

        auth_set_users_request = cls(
            tenant_id=tenant_id,
            users=users,
        )

        auth_set_users_request.additional_properties = d
        return auth_set_users_request

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
