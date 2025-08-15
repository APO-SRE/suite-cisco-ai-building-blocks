from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_config_data_v4_sitemanagement_get_type_0 import SiteConfigDataV4SitemanagementGETType0
    from ..models.site_config_data_v4_sitemanagement_get_type_1 import SiteConfigDataV4SitemanagementGETType1
    from ..models.site_config_data_v4_sitemanagement_get_type_2 import SiteConfigDataV4SitemanagementGETType2
    from ..models.site_config_data_v4_sitemanagement_get_type_3 import SiteConfigDataV4SitemanagementGETType3
    from ..models.site_spec_wrapper_v4_sitemanagement_get_annotation import SiteSpecWrapperV4SitemanagementGETAnnotation


T = TypeVar("T", bound="SiteSpecWrapperV4SitemanagementGET")


@_attrs_define
class SiteSpecWrapperV4SitemanagementGET:
    """
    Attributes:
        annotation (Union[Unset, SiteSpecWrapperV4SitemanagementGETAnnotation]): annotation for the site
        host (Union[Unset, str]): IP/Hostname of used to on-board the site
        latitude (Union[Unset, str]): geo location for the site being added
        login_domain (Union[Unset, str]): login domain of the controller
        longitude (Union[Unset, str]): geo location for the site being added
        name (Union[Unset, str]): name of the site
        password (Union[Unset, str]): login password of the controller
        secure_verify (Union[Unset, bool]): enable certificate verification for the site
        security_domains (Union[Unset, list[str]]):
        site_config (Union['SiteConfigDataV4SitemanagementGETType0', 'SiteConfigDataV4SitemanagementGETType1',
            'SiteConfigDataV4SitemanagementGETType2', 'SiteConfigDataV4SitemanagementGETType3', Unset]):
        site_type (Union[Unset, str]): site type - ACI/cloudACI/DCNM/NDFC
        use_proxy (Union[Unset, bool]): need proxy to reach the controller
        user_name (Union[Unset, str]): login username for the controller
    """

    annotation: Union[Unset, "SiteSpecWrapperV4SitemanagementGETAnnotation"] = UNSET
    host: Union[Unset, str] = UNSET
    latitude: Union[Unset, str] = UNSET
    login_domain: Union[Unset, str] = UNSET
    longitude: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    secure_verify: Union[Unset, bool] = UNSET
    security_domains: Union[Unset, list[str]] = UNSET
    site_config: Union[
        "SiteConfigDataV4SitemanagementGETType0",
        "SiteConfigDataV4SitemanagementGETType1",
        "SiteConfigDataV4SitemanagementGETType2",
        "SiteConfigDataV4SitemanagementGETType3",
        Unset,
    ] = UNSET
    site_type: Union[Unset, str] = UNSET
    use_proxy: Union[Unset, bool] = UNSET
    user_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.site_config_data_v4_sitemanagement_get_type_0 import SiteConfigDataV4SitemanagementGETType0
        from ..models.site_config_data_v4_sitemanagement_get_type_1 import SiteConfigDataV4SitemanagementGETType1
        from ..models.site_config_data_v4_sitemanagement_get_type_2 import SiteConfigDataV4SitemanagementGETType2

        annotation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.annotation, Unset):
            annotation = self.annotation.to_dict()

        host = self.host

        latitude = self.latitude

        login_domain = self.login_domain

        longitude = self.longitude

        name = self.name

        password = self.password

        secure_verify = self.secure_verify

        security_domains: Union[Unset, list[str]] = UNSET
        if not isinstance(self.security_domains, Unset):
            security_domains = self.security_domains

        site_config: Union[Unset, dict[str, Any]]
        if isinstance(self.site_config, Unset):
            site_config = UNSET
        elif isinstance(self.site_config, SiteConfigDataV4SitemanagementGETType0):
            site_config = self.site_config.to_dict()
        elif isinstance(self.site_config, SiteConfigDataV4SitemanagementGETType1):
            site_config = self.site_config.to_dict()
        elif isinstance(self.site_config, SiteConfigDataV4SitemanagementGETType2):
            site_config = self.site_config.to_dict()
        else:
            site_config = self.site_config.to_dict()

        site_type = self.site_type

        use_proxy = self.use_proxy

        user_name = self.user_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if host is not UNSET:
            field_dict["host"] = host
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if login_domain is not UNSET:
            field_dict["loginDomain"] = login_domain
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if name is not UNSET:
            field_dict["name"] = name
        if password is not UNSET:
            field_dict["password"] = password
        if secure_verify is not UNSET:
            field_dict["secureVerify"] = secure_verify
        if security_domains is not UNSET:
            field_dict["securityDomains"] = security_domains
        if site_config is not UNSET:
            field_dict["siteConfig"] = site_config
        if site_type is not UNSET:
            field_dict["siteType"] = site_type
        if use_proxy is not UNSET:
            field_dict["useProxy"] = use_proxy
        if user_name is not UNSET:
            field_dict["userName"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.site_config_data_v4_sitemanagement_get_type_0 import SiteConfigDataV4SitemanagementGETType0
        from ..models.site_config_data_v4_sitemanagement_get_type_1 import SiteConfigDataV4SitemanagementGETType1
        from ..models.site_config_data_v4_sitemanagement_get_type_2 import SiteConfigDataV4SitemanagementGETType2
        from ..models.site_config_data_v4_sitemanagement_get_type_3 import SiteConfigDataV4SitemanagementGETType3
        from ..models.site_spec_wrapper_v4_sitemanagement_get_annotation import (
            SiteSpecWrapperV4SitemanagementGETAnnotation,
        )

        d = dict(src_dict)
        _annotation = d.pop("annotation", UNSET)
        annotation: Union[Unset, SiteSpecWrapperV4SitemanagementGETAnnotation]
        if isinstance(_annotation, Unset):
            annotation = UNSET
        else:
            annotation = SiteSpecWrapperV4SitemanagementGETAnnotation.from_dict(_annotation)

        host = d.pop("host", UNSET)

        latitude = d.pop("latitude", UNSET)

        login_domain = d.pop("loginDomain", UNSET)

        longitude = d.pop("longitude", UNSET)

        name = d.pop("name", UNSET)

        password = d.pop("password", UNSET)

        secure_verify = d.pop("secureVerify", UNSET)

        security_domains = cast(list[str], d.pop("securityDomains", UNSET))

        def _parse_site_config(
            data: object,
        ) -> Union[
            "SiteConfigDataV4SitemanagementGETType0",
            "SiteConfigDataV4SitemanagementGETType1",
            "SiteConfigDataV4SitemanagementGETType2",
            "SiteConfigDataV4SitemanagementGETType3",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_site_config_data_v_4_sitemanagement_get_type_0 = (
                    SiteConfigDataV4SitemanagementGETType0.from_dict(data)
                )

                return componentsschemas_site_config_data_v_4_sitemanagement_get_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_site_config_data_v_4_sitemanagement_get_type_1 = (
                    SiteConfigDataV4SitemanagementGETType1.from_dict(data)
                )

                return componentsschemas_site_config_data_v_4_sitemanagement_get_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_site_config_data_v_4_sitemanagement_get_type_2 = (
                    SiteConfigDataV4SitemanagementGETType2.from_dict(data)
                )

                return componentsschemas_site_config_data_v_4_sitemanagement_get_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_site_config_data_v_4_sitemanagement_get_type_3 = (
                SiteConfigDataV4SitemanagementGETType3.from_dict(data)
            )

            return componentsschemas_site_config_data_v_4_sitemanagement_get_type_3

        site_config = _parse_site_config(d.pop("siteConfig", UNSET))

        site_type = d.pop("siteType", UNSET)

        use_proxy = d.pop("useProxy", UNSET)

        user_name = d.pop("userName", UNSET)

        site_spec_wrapper_v4_sitemanagement_get = cls(
            annotation=annotation,
            host=host,
            latitude=latitude,
            login_domain=login_domain,
            longitude=longitude,
            name=name,
            password=password,
            secure_verify=secure_verify,
            security_domains=security_domains,
            site_config=site_config,
            site_type=site_type,
            use_proxy=use_proxy,
            user_name=user_name,
        )

        site_spec_wrapper_v4_sitemanagement_get.additional_properties = d
        return site_spec_wrapper_v4_sitemanagement_get

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
