from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.login_domain_spec_wrapper_v4_aaa_post_realm import LoginDomainSpecWrapperV4AaaPOSTRealm
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_data_v4_aaa_post_type_0 import ProviderDataV4AaaPOSTType0
    from ..models.provider_data_v4_aaa_post_type_1 import ProviderDataV4AaaPOSTType1
    from ..models.provider_data_v4_aaa_post_type_2 import ProviderDataV4AaaPOSTType2
    from ..models.provider_data_v4_aaa_post_type_3 import ProviderDataV4AaaPOSTType3
    from ..models.provider_data_v4_aaa_post_type_4 import ProviderDataV4AaaPOSTType4


T = TypeVar("T", bound="LoginDomainSpecWrapperV4AaaPOST")


@_attrs_define
class LoginDomainSpecWrapperV4AaaPOST:
    """
    Attributes:
        domain (str): Login domain name
        description (Union[Unset, str]): Description about the login domain
        realm (Union[Unset, LoginDomainSpecWrapperV4AaaPOSTRealm]): Login domain realm type
        servers (Union['ProviderDataV4AaaPOSTType0', 'ProviderDataV4AaaPOSTType1', 'ProviderDataV4AaaPOSTType2',
            'ProviderDataV4AaaPOSTType3', 'ProviderDataV4AaaPOSTType4', Unset]):
    """

    domain: str
    description: Union[Unset, str] = UNSET
    realm: Union[Unset, LoginDomainSpecWrapperV4AaaPOSTRealm] = UNSET
    servers: Union[
        "ProviderDataV4AaaPOSTType0",
        "ProviderDataV4AaaPOSTType1",
        "ProviderDataV4AaaPOSTType2",
        "ProviderDataV4AaaPOSTType3",
        "ProviderDataV4AaaPOSTType4",
        Unset,
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_data_v4_aaa_post_type_0 import ProviderDataV4AaaPOSTType0
        from ..models.provider_data_v4_aaa_post_type_1 import ProviderDataV4AaaPOSTType1
        from ..models.provider_data_v4_aaa_post_type_2 import ProviderDataV4AaaPOSTType2
        from ..models.provider_data_v4_aaa_post_type_3 import ProviderDataV4AaaPOSTType3

        domain = self.domain

        description = self.description

        realm: Union[Unset, str] = UNSET
        if not isinstance(self.realm, Unset):
            realm = self.realm.value

        servers: Union[Unset, dict[str, Any]]
        if isinstance(self.servers, Unset):
            servers = UNSET
        elif isinstance(self.servers, ProviderDataV4AaaPOSTType0):
            servers = self.servers.to_dict()
        elif isinstance(self.servers, ProviderDataV4AaaPOSTType1):
            servers = self.servers.to_dict()
        elif isinstance(self.servers, ProviderDataV4AaaPOSTType2):
            servers = self.servers.to_dict()
        elif isinstance(self.servers, ProviderDataV4AaaPOSTType3):
            servers = self.servers.to_dict()
        else:
            servers = self.servers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if realm is not UNSET:
            field_dict["realm"] = realm
        if servers is not UNSET:
            field_dict["servers"] = servers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_data_v4_aaa_post_type_0 import ProviderDataV4AaaPOSTType0
        from ..models.provider_data_v4_aaa_post_type_1 import ProviderDataV4AaaPOSTType1
        from ..models.provider_data_v4_aaa_post_type_2 import ProviderDataV4AaaPOSTType2
        from ..models.provider_data_v4_aaa_post_type_3 import ProviderDataV4AaaPOSTType3
        from ..models.provider_data_v4_aaa_post_type_4 import ProviderDataV4AaaPOSTType4

        d = dict(src_dict)
        domain = d.pop("domain")

        description = d.pop("description", UNSET)

        _realm = d.pop("realm", UNSET)
        realm: Union[Unset, LoginDomainSpecWrapperV4AaaPOSTRealm]
        if isinstance(_realm, Unset):
            realm = UNSET
        else:
            realm = LoginDomainSpecWrapperV4AaaPOSTRealm(_realm)

        def _parse_servers(
            data: object,
        ) -> Union[
            "ProviderDataV4AaaPOSTType0",
            "ProviderDataV4AaaPOSTType1",
            "ProviderDataV4AaaPOSTType2",
            "ProviderDataV4AaaPOSTType3",
            "ProviderDataV4AaaPOSTType4",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_provider_data_v_4_aaa_post_type_0 = ProviderDataV4AaaPOSTType0.from_dict(data)

                return componentsschemas_provider_data_v_4_aaa_post_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_provider_data_v_4_aaa_post_type_1 = ProviderDataV4AaaPOSTType1.from_dict(data)

                return componentsschemas_provider_data_v_4_aaa_post_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_provider_data_v_4_aaa_post_type_2 = ProviderDataV4AaaPOSTType2.from_dict(data)

                return componentsschemas_provider_data_v_4_aaa_post_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_provider_data_v_4_aaa_post_type_3 = ProviderDataV4AaaPOSTType3.from_dict(data)

                return componentsschemas_provider_data_v_4_aaa_post_type_3
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_provider_data_v_4_aaa_post_type_4 = ProviderDataV4AaaPOSTType4.from_dict(data)

            return componentsschemas_provider_data_v_4_aaa_post_type_4

        servers = _parse_servers(d.pop("servers", UNSET))

        login_domain_spec_wrapper_v4_aaa_post = cls(
            domain=domain,
            description=description,
            realm=realm,
            servers=servers,
        )

        login_domain_spec_wrapper_v4_aaa_post.additional_properties = d
        return login_domain_spec_wrapper_v4_aaa_post

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
