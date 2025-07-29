from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credential_spec_wrapper_v4_credmgr_put_credentials import CredentialSpecWrapperV4CredmgrPUTCredentials


T = TypeVar("T", bound="CredentialSpecWrapperV4CredmgrPUT")


@_attrs_define
class CredentialSpecWrapperV4CredmgrPUT:
    """
    Attributes:
        credentials (Union[Unset, CredentialSpecWrapperV4CredmgrPUTCredentials]):
        name (Union[Unset, str]):
    """

    credentials: Union[Unset, "CredentialSpecWrapperV4CredmgrPUTCredentials"] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credentials: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_spec_wrapper_v4_credmgr_put_credentials import (
            CredentialSpecWrapperV4CredmgrPUTCredentials,
        )

        d = dict(src_dict)
        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, CredentialSpecWrapperV4CredmgrPUTCredentials]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = CredentialSpecWrapperV4CredmgrPUTCredentials.from_dict(_credentials)

        name = d.pop("name", UNSET)

        credential_spec_wrapper_v4_credmgr_put = cls(
            credentials=credentials,
            name=name,
        )

        credential_spec_wrapper_v4_credmgr_put.additional_properties = d
        return credential_spec_wrapper_v4_credmgr_put

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
