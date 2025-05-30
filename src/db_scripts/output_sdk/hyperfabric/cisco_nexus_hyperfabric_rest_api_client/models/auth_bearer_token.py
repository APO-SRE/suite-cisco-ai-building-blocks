import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.models_token_scope import ModelsTokenScope
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_metadata import ModelsMetadata


T = TypeVar("T", bound="AuthBearerToken")


@_attrs_define
class AuthBearerToken:
    """Metadata for a bearer token.

    Attributes:
        description (Union[Unset, str]): The user provided description for the token.
        metadata (Union[Unset, ModelsMetadata]): Metadata defines metadata of all objects in the service.
        name (Union[Unset, str]): The user provided name for the token.
        not_after (Union[Unset, datetime.datetime]): The time after which the token cannot be used.
        not_before (Union[Unset, datetime.datetime]): The time at which the token can be used.
        scope (Union[Unset, ModelsTokenScope]): Scope defines scope of tokens and keys used for authorization.
        token (Union[Unset, str]): This is a read-only field. The token, available only when the token is created.
        token_id (Union[Unset, str]): This is a read-only field. A unique id for the token.
    """

    description: Union[Unset, str] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    name: Union[Unset, str] = UNSET
    not_after: Union[Unset, datetime.datetime] = UNSET
    not_before: Union[Unset, datetime.datetime] = UNSET
    scope: Union[Unset, ModelsTokenScope] = UNSET
    token: Union[Unset, str] = UNSET
    token_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        not_after: Union[Unset, str] = UNSET
        if not isinstance(self.not_after, Unset):
            not_after = self.not_after.isoformat()

        not_before: Union[Unset, str] = UNSET
        if not isinstance(self.not_before, Unset):
            not_before = self.not_before.isoformat()

        scope: Union[Unset, str] = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        token = self.token

        token_id = self.token_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if not_after is not UNSET:
            field_dict["notAfter"] = not_after
        if not_before is not UNSET:
            field_dict["notBefore"] = not_before
        if scope is not UNSET:
            field_dict["scope"] = scope
        if token is not UNSET:
            field_dict["token"] = token
        if token_id is not UNSET:
            field_dict["tokenId"] = token_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_metadata import ModelsMetadata

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        _not_after = d.pop("notAfter", UNSET)
        not_after: Union[Unset, datetime.datetime]
        if isinstance(_not_after, Unset):
            not_after = UNSET
        else:
            not_after = isoparse(_not_after)

        _not_before = d.pop("notBefore", UNSET)
        not_before: Union[Unset, datetime.datetime]
        if isinstance(_not_before, Unset):
            not_before = UNSET
        else:
            not_before = isoparse(_not_before)

        _scope = d.pop("scope", UNSET)
        scope: Union[Unset, ModelsTokenScope]
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = ModelsTokenScope(_scope)

        token = d.pop("token", UNSET)

        token_id = d.pop("tokenId", UNSET)

        auth_bearer_token = cls(
            description=description,
            metadata=metadata,
            name=name,
            not_after=not_after,
            not_before=not_before,
            scope=scope,
            token=token,
            token_id=token_id,
        )

        auth_bearer_token.additional_properties = d
        return auth_bearer_token

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
