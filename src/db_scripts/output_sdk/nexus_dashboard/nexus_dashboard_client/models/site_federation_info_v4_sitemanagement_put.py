from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteFederationInfoV4SitemanagementPUT")


@_attrs_define
class SiteFederationInfoV4SitemanagementPUT:
    """
    Attributes:
        federation_member_uuid (Union[Unset, str]): Federation member UUID
        local (Union[Unset, bool]): site on-boarded locally, set to true
        name (Union[Unset, str]): Federation member cluster name
        site_fingerprint (Union[Unset, str]): Federation member site fingerprint - not set currently
        site_uuid (Union[Unset, str]): UUID of the site
    """

    federation_member_uuid: Union[Unset, str] = UNSET
    local: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    site_fingerprint: Union[Unset, str] = UNSET
    site_uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        federation_member_uuid = self.federation_member_uuid

        local = self.local

        name = self.name

        site_fingerprint = self.site_fingerprint

        site_uuid = self.site_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if federation_member_uuid is not UNSET:
            field_dict["federationMemberUUID"] = federation_member_uuid
        if local is not UNSET:
            field_dict["local"] = local
        if name is not UNSET:
            field_dict["name"] = name
        if site_fingerprint is not UNSET:
            field_dict["siteFingerprint"] = site_fingerprint
        if site_uuid is not UNSET:
            field_dict["siteUUID"] = site_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        federation_member_uuid = d.pop("federationMemberUUID", UNSET)

        local = d.pop("local", UNSET)

        name = d.pop("name", UNSET)

        site_fingerprint = d.pop("siteFingerprint", UNSET)

        site_uuid = d.pop("siteUUID", UNSET)

        site_federation_info_v4_sitemanagement_put = cls(
            federation_member_uuid=federation_member_uuid,
            local=local,
            name=name,
            site_fingerprint=site_fingerprint,
            site_uuid=site_uuid,
        )

        site_federation_info_v4_sitemanagement_put.additional_properties = d
        return site_federation_info_v4_sitemanagement_put

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
