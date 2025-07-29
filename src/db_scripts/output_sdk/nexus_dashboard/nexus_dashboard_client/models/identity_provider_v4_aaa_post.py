from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.identity_provider_v4_aaa_post_auth_type import IdentityProviderV4AaaPOSTAuthType
from ..types import UNSET, Unset

T = TypeVar("T", bound="IdentityProviderV4AaaPOST")


@_attrs_define
class IdentityProviderV4AaaPOST:
    """
    Attributes:
        auth_type (Union[Unset, IdentityProviderV4AaaPOSTAuthType]): OIDC authentication mechanism
        client_id (Union[Unset, str]): OIDC Identity Provider Client ID
        client_secret (Union[Unset, str]): Base64 encoded OIDC Identity Provider Client Secret
        gui_banner_message (Union[Unset, str]): GUI Banner Message Page URL
        issuer (Union[Unset, str]): OIDC Identity Provider Issuer URL
        scopes (Union[Unset, list[str]]): OIDC Identity Provider Scopes
        use_proxy (Union[Unset, bool]): Flag to determine whether to use system proxy for OIDC Identity Provider
        username_attribute (Union[Unset, str]): Username attribute to be searched in claims
    """

    auth_type: Union[Unset, IdentityProviderV4AaaPOSTAuthType] = UNSET
    client_id: Union[Unset, str] = UNSET
    client_secret: Union[Unset, str] = UNSET
    gui_banner_message: Union[Unset, str] = UNSET
    issuer: Union[Unset, str] = UNSET
    scopes: Union[Unset, list[str]] = UNSET
    use_proxy: Union[Unset, bool] = UNSET
    username_attribute: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_type: Union[Unset, str] = UNSET
        if not isinstance(self.auth_type, Unset):
            auth_type = self.auth_type.value

        client_id = self.client_id

        client_secret = self.client_secret

        gui_banner_message = self.gui_banner_message

        issuer = self.issuer

        scopes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = self.scopes

        use_proxy = self.use_proxy

        username_attribute = self.username_attribute

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type
        if client_id is not UNSET:
            field_dict["clientID"] = client_id
        if client_secret is not UNSET:
            field_dict["clientSecret"] = client_secret
        if gui_banner_message is not UNSET:
            field_dict["guiBannerMessage"] = gui_banner_message
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if use_proxy is not UNSET:
            field_dict["useProxy"] = use_proxy
        if username_attribute is not UNSET:
            field_dict["usernameAttribute"] = username_attribute

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _auth_type = d.pop("authType", UNSET)
        auth_type: Union[Unset, IdentityProviderV4AaaPOSTAuthType]
        if isinstance(_auth_type, Unset):
            auth_type = UNSET
        else:
            auth_type = IdentityProviderV4AaaPOSTAuthType(_auth_type)

        client_id = d.pop("clientID", UNSET)

        client_secret = d.pop("clientSecret", UNSET)

        gui_banner_message = d.pop("guiBannerMessage", UNSET)

        issuer = d.pop("issuer", UNSET)

        scopes = cast(list[str], d.pop("scopes", UNSET))

        use_proxy = d.pop("useProxy", UNSET)

        username_attribute = d.pop("usernameAttribute", UNSET)

        identity_provider_v4_aaa_post = cls(
            auth_type=auth_type,
            client_id=client_id,
            client_secret=client_secret,
            gui_banner_message=gui_banner_message,
            issuer=issuer,
            scopes=scopes,
            use_proxy=use_proxy,
            username_attribute=username_attribute,
        )

        identity_provider_v4_aaa_post.additional_properties = d
        return identity_provider_v4_aaa_post

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
