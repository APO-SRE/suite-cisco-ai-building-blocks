from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_config_v4_aaa_post_option import LDAPConfigV4AaaPOSTOption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_config_v4_aaa_post_ad_group import LDAPConfigV4AaaPOSTAdGroup
    from ..models.ldap_config_v4_aaa_post_providers import LDAPConfigV4AaaPOSTProviders


T = TypeVar("T", bound="LDAPConfigV4AaaPOST")


@_attrs_define
class LDAPConfigV4AaaPOST:
    """LDAP login domain configuration

    Attributes:
        ad_group (Union[Unset, LDAPConfigV4AaaPOSTAdGroup]): LDAP login domain AD group map
        option (Union[Unset, LDAPConfigV4AaaPOSTOption]): LDAP login domain authentication mechanism
        providers (Union[Unset, LDAPConfigV4AaaPOSTProviders]): LDAP login domain provider servers
    """

    ad_group: Union[Unset, "LDAPConfigV4AaaPOSTAdGroup"] = UNSET
    option: Union[Unset, LDAPConfigV4AaaPOSTOption] = UNSET
    providers: Union[Unset, "LDAPConfigV4AaaPOSTProviders"] = UNSET
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
        from ..models.ldap_config_v4_aaa_post_ad_group import LDAPConfigV4AaaPOSTAdGroup
        from ..models.ldap_config_v4_aaa_post_providers import LDAPConfigV4AaaPOSTProviders

        d = dict(src_dict)
        _ad_group = d.pop("adGroup", UNSET)
        ad_group: Union[Unset, LDAPConfigV4AaaPOSTAdGroup]
        if isinstance(_ad_group, Unset):
            ad_group = UNSET
        else:
            ad_group = LDAPConfigV4AaaPOSTAdGroup.from_dict(_ad_group)

        _option = d.pop("option", UNSET)
        option: Union[Unset, LDAPConfigV4AaaPOSTOption]
        if isinstance(_option, Unset):
            option = UNSET
        else:
            option = LDAPConfigV4AaaPOSTOption(_option)

        _providers = d.pop("providers", UNSET)
        providers: Union[Unset, LDAPConfigV4AaaPOSTProviders]
        if isinstance(_providers, Unset):
            providers = UNSET
        else:
            providers = LDAPConfigV4AaaPOSTProviders.from_dict(_providers)

        ldap_config_v4_aaa_post = cls(
            ad_group=ad_group,
            option=option,
            providers=providers,
        )

        ldap_config_v4_aaa_post.additional_properties = d
        return ldap_config_v4_aaa_post

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
