from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_config_v4_aaa_get_option import LDAPConfigV4AaaGETOption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_config_v4_aaa_get_ad_group import LDAPConfigV4AaaGETAdGroup
    from ..models.ldap_config_v4_aaa_get_providers import LDAPConfigV4AaaGETProviders


T = TypeVar("T", bound="LDAPConfigV4AaaGET")


@_attrs_define
class LDAPConfigV4AaaGET:
    """LDAP login domain configuration

    Attributes:
        ad_group (Union[Unset, LDAPConfigV4AaaGETAdGroup]): LDAP login domain AD group map
        option (Union[Unset, LDAPConfigV4AaaGETOption]): LDAP login domain authentication mechanism
        providers (Union[Unset, LDAPConfigV4AaaGETProviders]): LDAP login domain provider servers
    """

    ad_group: Union[Unset, "LDAPConfigV4AaaGETAdGroup"] = UNSET
    option: Union[Unset, LDAPConfigV4AaaGETOption] = UNSET
    providers: Union[Unset, "LDAPConfigV4AaaGETProviders"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ad_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ad_group, Unset):
            ad_group = self.ad_group.to_dict()

        option: Union[Unset, str] = UNSET
        if not isinstance(self.option, Unset):
            option = self.option.value

        providers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.providers, Unset):
            providers = self.providers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ad_group is not UNSET:
            field_dict["adGroup"] = ad_group
        if option is not UNSET:
            field_dict["option"] = option
        if providers is not UNSET:
            field_dict["providers"] = providers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_config_v4_aaa_get_ad_group import LDAPConfigV4AaaGETAdGroup
        from ..models.ldap_config_v4_aaa_get_providers import LDAPConfigV4AaaGETProviders

        d = dict(src_dict)
        _ad_group = d.pop("adGroup", UNSET)
        ad_group: Union[Unset, LDAPConfigV4AaaGETAdGroup]
        if isinstance(_ad_group, Unset):
            ad_group = UNSET
        else:
            ad_group = LDAPConfigV4AaaGETAdGroup.from_dict(_ad_group)

        _option = d.pop("option", UNSET)
        option: Union[Unset, LDAPConfigV4AaaGETOption]
        if isinstance(_option, Unset):
            option = UNSET
        else:
            option = LDAPConfigV4AaaGETOption(_option)

        _providers = d.pop("providers", UNSET)
        providers: Union[Unset, LDAPConfigV4AaaGETProviders]
        if isinstance(_providers, Unset):
            providers = UNSET
        else:
            providers = LDAPConfigV4AaaGETProviders.from_dict(_providers)

        ldap_config_v4_aaa_get = cls(
            ad_group=ad_group,
            option=option,
            providers=providers,
        )

        ldap_config_v4_aaa_get.additional_properties = d
        return ldap_config_v4_aaa_get

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
