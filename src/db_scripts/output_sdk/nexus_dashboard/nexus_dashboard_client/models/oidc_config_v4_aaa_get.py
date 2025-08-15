from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identity_provider_v4_aaa_get import IdentityProviderV4AaaGET


T = TypeVar("T", bound="OIDCConfigV4AaaGET")


@_attrs_define
class OIDCConfigV4AaaGET:
    """
    Attributes:
        identity_provider (Union[Unset, IdentityProviderV4AaaGET]):
    """

    identity_provider: Union[Unset, "IdentityProviderV4AaaGET"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identity_provider: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.identity_provider, Unset):
            identity_provider = self.identity_provider.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identity_provider is not UNSET:
            field_dict["identityProvider"] = identity_provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identity_provider_v4_aaa_get import IdentityProviderV4AaaGET

        d = dict(src_dict)
        _identity_provider = d.pop("identityProvider", UNSET)
        identity_provider: Union[Unset, IdentityProviderV4AaaGET]
        if isinstance(_identity_provider, Unset):
            identity_provider = UNSET
        else:
            identity_provider = IdentityProviderV4AaaGET.from_dict(_identity_provider)

        oidc_config_v4_aaa_get = cls(
            identity_provider=identity_provider,
        )

        oidc_config_v4_aaa_get.additional_properties = d
        return oidc_config_v4_aaa_get

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
