from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.http_server_options_v4_aaa_post_min_version import HTTPServerOptionsV4AaaPOSTMinVersion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.certificate_metadata_v4_aaa_post import CertificateMetadataV4AaaPOST


T = TypeVar("T", bound="HTTPServerOptionsV4AaaPOST")


@_attrs_define
class HTTPServerOptionsV4AaaPOST:
    """
    Attributes:
        certificate_metadata (Union[Unset, CertificateMetadataV4AaaPOST]):
        min_version (Union[Unset, HTTPServerOptionsV4AaaPOSTMinVersion]): SSL Min Version
        server_name (Union[Unset, str]): Server Name
    """

    certificate_metadata: Union[Unset, "CertificateMetadataV4AaaPOST"] = UNSET
    min_version: Union[Unset, HTTPServerOptionsV4AaaPOSTMinVersion] = UNSET
    server_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        certificate_metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.certificate_metadata, Unset):
            certificate_metadata = self.certificate_metadata.to_dict()

        min_version: Union[Unset, str] = UNSET
        if not isinstance(self.min_version, Unset):
            min_version = self.min_version.value

        server_name = self.server_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificate_metadata is not UNSET:
            field_dict["certificateMetadata"] = certificate_metadata
        if min_version is not UNSET:
            field_dict["minVersion"] = min_version
        if server_name is not UNSET:
            field_dict["serverName"] = server_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.certificate_metadata_v4_aaa_post import CertificateMetadataV4AaaPOST

        d = dict(src_dict)
        _certificate_metadata = d.pop("certificateMetadata", UNSET)
        certificate_metadata: Union[Unset, CertificateMetadataV4AaaPOST]
        if isinstance(_certificate_metadata, Unset):
            certificate_metadata = UNSET
        else:
            certificate_metadata = CertificateMetadataV4AaaPOST.from_dict(_certificate_metadata)

        _min_version = d.pop("minVersion", UNSET)
        min_version: Union[Unset, HTTPServerOptionsV4AaaPOSTMinVersion]
        if isinstance(_min_version, Unset):
            min_version = UNSET
        else:
            min_version = HTTPServerOptionsV4AaaPOSTMinVersion(_min_version)

        server_name = d.pop("serverName", UNSET)

        http_server_options_v4_aaa_post = cls(
            certificate_metadata=certificate_metadata,
            min_version=min_version,
            server_name=server_name,
        )

        http_server_options_v4_aaa_post.additional_properties = d
        return http_server_options_v4_aaa_post

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
