from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.login_domain_spec_v4_aaa_get_realm import LoginDomainSpecV4AaaGETRealm
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_data_v4_aaa_get_type_0 import ProviderDataV4AaaGETType0
    from ..models.provider_data_v4_aaa_get_type_1 import ProviderDataV4AaaGETType1
    from ..models.provider_data_v4_aaa_get_type_2 import ProviderDataV4AaaGETType2
    from ..models.provider_data_v4_aaa_get_type_3 import ProviderDataV4AaaGETType3
    from ..models.provider_data_v4_aaa_get_type_4 import ProviderDataV4AaaGETType4


T = TypeVar("T", bound="LoginDomainSpecV4AaaGET")


@_attrs_define
class LoginDomainSpecV4AaaGET:
    """
    Attributes:
        description (Union[Unset, str]): Description about the login domain
        domain (Union[Unset, str]): Login domain name
        realm (Union[Unset, LoginDomainSpecV4AaaGETRealm]): Login domain realm type
        servers (Union['ProviderDataV4AaaGETType0', 'ProviderDataV4AaaGETType1', 'ProviderDataV4AaaGETType2',
            'ProviderDataV4AaaGETType3', 'ProviderDataV4AaaGETType4', Unset]):
    """

    description: Union[Unset, str] = UNSET
    domain: Union[Unset, str] = UNSET
    realm: Union[Unset, LoginDomainSpecV4AaaGETRealm] = UNSET
    servers: Union[
        "ProviderDataV4AaaGETType0",
        "ProviderDataV4AaaGETType1",
        "ProviderDataV4AaaGETType2",
        "ProviderDataV4AaaGETType3",
        "ProviderDataV4AaaGETType4",
        Unset,
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_data_v4_aaa_get_type_0 import ProviderDataV4AaaGETType0
        from ..models.provider_data_v4_aaa_get_type_1 import ProviderDataV4AaaGETType1
        from ..models.provider_data_v4_aaa_get_type_2 import ProviderDataV4AaaGETType2
        from ..models.provider_data_v4_aaa_get_type_3 import ProviderDataV4AaaGETType3

        description = self.description

        domain = self.domain

        realm: Union[Unset, str] = UNSET
        if not isinstance(self.realm, Unset):
            realm = self.realm.value

        servers: Union[Unset, dict[str, Any]]
        if isinstance(self.servers, Unset):
            servers = UNSET
        elif isinstance(self.servers, ProviderDataV4AaaGETType0):
            servers = self.servers.to_dict()
        elif isinstance(self.servers, ProviderDataV4AaaGETType1):
            servers = self.servers.to_dict()
        elif isinstance(self.servers, ProviderDataV4AaaGETType2):
            servers = self.servers.to_dict()
        elif isinstance(self.servers, ProviderDataV4AaaGETType3):
            servers = self.servers.to_dict()
        else:
            servers = self.servers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if domain is not UNSET:
            field_dict["domain"] = domain
        if realm is not UNSET:
            field_dict["realm"] = realm
        if servers is not UNSET:
            field_dict["servers"] = servers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_data_v4_aaa_get_type_0 import ProviderDataV4AaaGETType0
        from ..models.provider_data_v4_aaa_get_type_1 import ProviderDataV4AaaGETType1
        from ..models.provider_data_v4_aaa_get_type_2 import ProviderDataV4AaaGETType2
        from ..models.provider_data_v4_aaa_get_type_3 import ProviderDataV4AaaGETType3
        from ..models.provider_data_v4_aaa_get_type_4 import ProviderDataV4AaaGETType4

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        domain = d.pop("domain", UNSET)

        _realm = d.pop("realm", UNSET)
        realm: Union[Unset, LoginDomainSpecV4AaaGETRealm]
        if isinstance(_realm, Unset):
            realm = UNSET
        else:
            realm = LoginDomainSpecV4AaaGETRealm(_realm)

        def _parse_servers(
            data: object,
        ) -> Union[
            "ProviderDataV4AaaGETType0",
            "ProviderDataV4AaaGETType1",
            "ProviderDataV4AaaGETType2",
            "ProviderDataV4AaaGETType3",
            "ProviderDataV4AaaGETType4",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_provider_data_v_4_aaa_get_type_0 = ProviderDataV4AaaGETType0.from_dict(data)

                return componentsschemas_provider_data_v_4_aaa_get_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_provider_data_v_4_aaa_get_type_1 = ProviderDataV4AaaGETType1.from_dict(data)

                return componentsschemas_provider_data_v_4_aaa_get_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_provider_data_v_4_aaa_get_type_2 = ProviderDataV4AaaGETType2.from_dict(data)

                return componentsschemas_provider_data_v_4_aaa_get_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_provider_data_v_4_aaa_get_type_3 = ProviderDataV4AaaGETType3.from_dict(data)

                return componentsschemas_provider_data_v_4_aaa_get_type_3
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_provider_data_v_4_aaa_get_type_4 = ProviderDataV4AaaGETType4.from_dict(data)

            return componentsschemas_provider_data_v_4_aaa_get_type_4

        servers = _parse_servers(d.pop("servers", UNSET))

        login_domain_spec_v4_aaa_get = cls(
            description=description,
            domain=domain,
            realm=realm,
            servers=servers,
        )

        login_domain_spec_v4_aaa_get.additional_properties = d
        return login_domain_spec_v4_aaa_get

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
