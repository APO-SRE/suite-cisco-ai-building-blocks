from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ldap_provider_v4_aaa_post import LDAPProviderV4AaaPOST


T = TypeVar("T", bound="LDAPConfigV4AaaPOSTProviders")


@_attrs_define
class LDAPConfigV4AaaPOSTProviders:
    """LDAP login domain provider servers"""

    additional_properties: dict[str, "LDAPProviderV4AaaPOST"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_provider_v4_aaa_post import LDAPProviderV4AaaPOST

        d = dict(src_dict)
        ldap_config_v4_aaa_post_providers = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = LDAPProviderV4AaaPOST.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        ldap_config_v4_aaa_post_providers.additional_properties = additional_properties
        return ldap_config_v4_aaa_post_providers

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "LDAPProviderV4AaaPOST":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "LDAPProviderV4AaaPOST") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
