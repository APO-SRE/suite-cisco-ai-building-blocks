from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_config_v4_aaa_get import LDAPConfigV4AaaGET


T = TypeVar("T", bound="ProviderDataV4AaaGETType0")


@_attrs_define
class ProviderDataV4AaaGETType0:
    """
    Attributes:
        ldap (Union[Unset, LDAPConfigV4AaaGET]): LDAP login domain configuration
    """

    ldap: Union[Unset, "LDAPConfigV4AaaGET"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ldap: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ldap, Unset):
            ldap = self.ldap.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ldap is not UNSET:
            field_dict["ldap"] = ldap

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_config_v4_aaa_get import LDAPConfigV4AaaGET

        d = dict(src_dict)
        _ldap = d.pop("ldap", UNSET)
        ldap: Union[Unset, LDAPConfigV4AaaGET]
        if isinstance(_ldap, Unset):
            ldap = UNSET
        else:
            ldap = LDAPConfigV4AaaGET.from_dict(_ldap)

        provider_data_v4_aaa_get_type_0 = cls(
            ldap=ldap,
        )

        provider_data_v4_aaa_get_type_0.additional_properties = d
        return provider_data_v4_aaa_get_type_0

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
