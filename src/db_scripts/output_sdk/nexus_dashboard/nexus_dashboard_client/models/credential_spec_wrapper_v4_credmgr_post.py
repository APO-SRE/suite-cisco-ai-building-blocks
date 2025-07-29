from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credential_spec_wrapper_v4_credmgr_post_credentials import (
        CredentialSpecWrapperV4CredmgrPOSTCredentials,
    )


T = TypeVar("T", bound="CredentialSpecWrapperV4CredmgrPOST")


@_attrs_define
class CredentialSpecWrapperV4CredmgrPOST:
    """
    Attributes:
        name (str):
        credentials (Union[Unset, CredentialSpecWrapperV4CredmgrPOSTCredentials]):
    """

    name: str
    credentials: Union[Unset, "CredentialSpecWrapperV4CredmgrPOSTCredentials"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        credentials: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if credentials is not UNSET:
            field_dict["credentials"] = credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_spec_wrapper_v4_credmgr_post_credentials import (
            CredentialSpecWrapperV4CredmgrPOSTCredentials,
        )

        d = dict(src_dict)
        name = d.pop("name")

        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, CredentialSpecWrapperV4CredmgrPOSTCredentials]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = CredentialSpecWrapperV4CredmgrPOSTCredentials.from_dict(_credentials)

        credential_spec_wrapper_v4_credmgr_post = cls(
            name=name,
            credentials=credentials,
        )

        credential_spec_wrapper_v4_credmgr_post.additional_properties = d
        return credential_spec_wrapper_v4_credmgr_post

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
