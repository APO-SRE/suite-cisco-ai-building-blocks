from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_user import ModelsUser


T = TypeVar("T", bound="AuthUsersResponse")


@_attrs_define
class AuthUsersResponse:
    """The response to a request for a list of users.

    Attributes:
        users (Union[Unset, list['ModelsUser']]): A list of users.
    """

    users: Union[Unset, list["ModelsUser"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_user import ModelsUser

        d = dict(src_dict)
        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = ModelsUser.from_dict(users_item_data)

            users.append(users_item)

        auth_users_response = cls(
            users=users,
        )

        auth_users_response.additional_properties = d
        return auth_users_response

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
