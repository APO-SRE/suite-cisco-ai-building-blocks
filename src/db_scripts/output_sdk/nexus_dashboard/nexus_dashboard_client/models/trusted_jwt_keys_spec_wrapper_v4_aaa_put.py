from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrustedJWTKeysSpecWrapperV4AaaPUT")


@_attrs_define
class TrustedJWTKeysSpecWrapperV4AaaPUT:
    """
    Attributes:
        key_id (Union[Unset, str]): JWT Key ID
        public_key (Union[Unset, str]): JWT Public Key in base64 format
        remote_id_claim (Union[Unset, str]): Claim to check while verifying OTP request using this key
    """

    key_id: Union[Unset, str] = UNSET
    public_key: Union[Unset, str] = UNSET
    remote_id_claim: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key_id = self.key_id

        public_key = self.public_key

        remote_id_claim = self.remote_id_claim

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key_id is not UNSET:
            field_dict["keyID"] = key_id
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if remote_id_claim is not UNSET:
            field_dict["remoteIDClaim"] = remote_id_claim

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key_id = d.pop("keyID", UNSET)

        public_key = d.pop("publicKey", UNSET)

        remote_id_claim = d.pop("remoteIDClaim", UNSET)

        trusted_jwt_keys_spec_wrapper_v4_aaa_put = cls(
            key_id=key_id,
            public_key=public_key,
            remote_id_claim=remote_id_claim,
        )

        trusted_jwt_keys_spec_wrapper_v4_aaa_put.additional_properties = d
        return trusted_jwt_keys_spec_wrapper_v4_aaa_put

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
