from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FabricSpecWrapperV4SitemanagementPUT")


@_attrs_define
class FabricSpecWrapperV4SitemanagementPUT:
    """
    Attributes:
        login_domain (Union[Unset, str]): controller login domain
        password (Union[Unset, str]): controller login password - base64 encoded
        site_type (Union[Unset, str]): site type - ACI/cloudACI/DCNM/NDFC
        url (Union[Unset, str]): controller URL
        use_proxy (Union[Unset, bool]): controller reachable via proxy
        user_name (Union[Unset, str]): controller login username
    """

    login_domain: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    site_type: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    use_proxy: Union[Unset, bool] = UNSET
    user_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        login_domain = self.login_domain

        password = self.password

        site_type = self.site_type

        url = self.url

        use_proxy = self.use_proxy

        user_name = self.user_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if login_domain is not UNSET:
            field_dict["loginDomain"] = login_domain
        if password is not UNSET:
            field_dict["password"] = password
        if site_type is not UNSET:
            field_dict["siteType"] = site_type
        if url is not UNSET:
            field_dict["url"] = url
        if use_proxy is not UNSET:
            field_dict["useProxy"] = use_proxy
        if user_name is not UNSET:
            field_dict["userName"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login_domain = d.pop("loginDomain", UNSET)

        password = d.pop("password", UNSET)

        site_type = d.pop("siteType", UNSET)

        url = d.pop("url", UNSET)

        use_proxy = d.pop("useProxy", UNSET)

        user_name = d.pop("userName", UNSET)

        fabric_spec_wrapper_v4_sitemanagement_put = cls(
            login_domain=login_domain,
            password=password,
            site_type=site_type,
            url=url,
            use_proxy=use_proxy,
            user_name=user_name,
        )

        fabric_spec_wrapper_v4_sitemanagement_put.additional_properties = d
        return fabric_spec_wrapper_v4_sitemanagement_put

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
