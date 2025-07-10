from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_user_role import ModelsUserRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthUpdateUser")


@_attrs_define
class AuthUpdateUser:
    """Update a specific user.
    Update a specific user associated with the organization.

        Attributes:
            enabled (Union[Unset, bool]): Enable/disable the user.
            labels (Union[Unset, list[str]]): A list of user-defined labels that can be used for grouping and filtering
                Users.
            role (Union[Unset, ModelsUserRole]): UserRole defines an enumeration of roles that represents different level of
                privileges that can be associated with a user.
    """

    enabled: Union[Unset, bool] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    role: Union[Unset, ModelsUserRole] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        labels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if labels is not UNSET:
            field_dict["labels"] = labels
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        _role = d.pop("role", UNSET)
        role: Union[Unset, ModelsUserRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = ModelsUserRole(_role)

        auth_update_user = cls(
            enabled=enabled,
            labels=labels,
            role=role,
        )

        auth_update_user.additional_properties = d
        return auth_update_user

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
