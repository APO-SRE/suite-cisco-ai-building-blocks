from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CertificateMetadataV4AaaGET")


@_attrs_define
class CertificateMetadataV4AaaGET:
    """
    Attributes:
        certificate (Union[Unset, str]): RSA Certificate
        domain_name (Union[Unset, str]): Domain Name
        intermediate_ca (Union[Unset, str]): Intermediate Certificate
        key (Union[Unset, str]): Base64 encoded RSA Key
        not_after (Union[Unset, str]): Certificate Validity in RFC3339 format
        not_before (Union[Unset, str]): Certificate Validity in RFC3339 format
        root_ca (Union[Unset, str]): Root Certificate
    """

    certificate: Union[Unset, str] = UNSET
    domain_name: Union[Unset, str] = UNSET
    intermediate_ca: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    not_after: Union[Unset, str] = UNSET
    not_before: Union[Unset, str] = UNSET
    root_ca: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        certificate = self.certificate

        domain_name = self.domain_name

        intermediate_ca = self.intermediate_ca

        key = self.key

        not_after = self.not_after

        not_before = self.not_before

        root_ca = self.root_ca

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificate is not UNSET:
            field_dict["certificate"] = certificate
        if domain_name is not UNSET:
            field_dict["domainName"] = domain_name
        if intermediate_ca is not UNSET:
            field_dict["intermediateCA"] = intermediate_ca
        if key is not UNSET:
            field_dict["key"] = key
        if not_after is not UNSET:
            field_dict["notAfter"] = not_after
        if not_before is not UNSET:
            field_dict["notBefore"] = not_before
        if root_ca is not UNSET:
            field_dict["rootCA"] = root_ca

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        certificate = d.pop("certificate", UNSET)

        domain_name = d.pop("domainName", UNSET)

        intermediate_ca = d.pop("intermediateCA", UNSET)

        key = d.pop("key", UNSET)

        not_after = d.pop("notAfter", UNSET)

        not_before = d.pop("notBefore", UNSET)

        root_ca = d.pop("rootCA", UNSET)

        certificate_metadata_v4_aaa_get = cls(
            certificate=certificate,
            domain_name=domain_name,
            intermediate_ca=intermediate_ca,
            key=key,
            not_after=not_after,
            not_before=not_before,
            root_ca=root_ca,
        )

        certificate_metadata_v4_aaa_get.additional_properties = d
        return certificate_metadata_v4_aaa_get

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
