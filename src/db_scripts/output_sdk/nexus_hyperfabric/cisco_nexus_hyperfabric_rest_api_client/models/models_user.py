import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.models_user_role import ModelsUserRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_metadata import ModelsMetadata


T = TypeVar("T", bound="ModelsUser")


@_attrs_define
class ModelsUser:
    """A User is a Cisco.com account, identified by email, authorized to access a specific Cisco Nexus Hyperfabric
    Organization with a specific role that represents the level of privilege of the user. Only a user with
    administrative privileges may modify another user's user record.

        Attributes:
            email (Union[Unset, str]): The email address of the user.
            enabled (Union[Unset, bool]): The enabled state of the user which indicates if the user is enabled or disabled.
            id (Union[Unset, str]): This is a read-only field. The unique identifier of a user.
            labels (Union[Unset, list[str]]): A list of user-defined labels that can be used for grouping and filtering
                users.
            last_login (Union[Unset, datetime.datetime]): This is a read-only field. The last recorded web interface login
                time of the user in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (e.g. `YYYY-MM-
                DDTHH:MM:SSZ`).
            metadata (Union[Unset, ModelsMetadata]): Metadata defines a map of attributes related to the lifecycle of the
                object.
            role (Union[Unset, ModelsUserRole]): UserRole defines an enumeration of roles that represents different level of
                privileges that can be associated with a user.
    """

    email: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    last_login: Union[Unset, datetime.datetime] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    role: Union[Unset, ModelsUserRole] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        enabled = self.enabled

        id = self.id

        labels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        last_login: Union[Unset, str] = UNSET
        if not isinstance(self.last_login, Unset):
            last_login = self.last_login.isoformat()

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if labels is not UNSET:
            field_dict["labels"] = labels
        if last_login is not UNSET:
            field_dict["lastLogin"] = last_login
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_metadata import ModelsMetadata

        d = dict(src_dict)
        email = d.pop("email", UNSET)

        enabled = d.pop("enabled", UNSET)

        id = d.pop("id", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        _last_login = d.pop("lastLogin", UNSET)
        last_login: Union[Unset, datetime.datetime]
        if isinstance(_last_login, Unset):
            last_login = UNSET
        else:
            last_login = isoparse(_last_login)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        _role = d.pop("role", UNSET)
        role: Union[Unset, ModelsUserRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = ModelsUserRole(_role)

        models_user = cls(
            email=email,
            enabled=enabled,
            id=id,
            labels=labels,
            last_login=last_login,
            metadata=metadata,
            role=role,
        )

        models_user.additional_properties = d
        return models_user

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
