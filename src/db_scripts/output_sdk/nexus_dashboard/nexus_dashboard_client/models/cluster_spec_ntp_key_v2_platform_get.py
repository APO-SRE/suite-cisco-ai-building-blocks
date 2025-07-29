from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cluster_spec_ntp_key_v2_platform_get_auth_type import ClusterSpecNTPKeyV2PlatformGETAuthType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterSpecNTPKeyV2PlatformGET")


@_attrs_define
class ClusterSpecNTPKeyV2PlatformGET:
    """Cluster NTP key

    Attributes:
        auth_type (Union[Unset, ClusterSpecNTPKeyV2PlatformGETAuthType]): Cluster NTP server key hash type
        id (Union[Unset, int]): Cluster NTP server key ID
        key (Union[Unset, str]): Cluster NTP server symmetrical key
        trusted (Union[Unset, bool]): Cluster NTP server key is trusted
    """

    auth_type: Union[Unset, ClusterSpecNTPKeyV2PlatformGETAuthType] = UNSET
    id: Union[Unset, int] = UNSET
    key: Union[Unset, str] = UNSET
    trusted: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_type: Union[Unset, str] = UNSET
        if not isinstance(self.auth_type, Unset):
            auth_type = self.auth_type.value

        id = self.id

        key = self.key

        trusted = self.trusted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if trusted is not UNSET:
            field_dict["trusted"] = trusted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _auth_type = d.pop("authType", UNSET)
        auth_type: Union[Unset, ClusterSpecNTPKeyV2PlatformGETAuthType]
        if isinstance(_auth_type, Unset):
            auth_type = UNSET
        else:
            auth_type = ClusterSpecNTPKeyV2PlatformGETAuthType(_auth_type)

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        trusted = d.pop("trusted", UNSET)

        cluster_spec_ntp_key_v2_platform_get = cls(
            auth_type=auth_type,
            id=id,
            key=key,
            trusted=trusted,
        )

        cluster_spec_ntp_key_v2_platform_get.additional_properties = d
        return cluster_spec_ntp_key_v2_platform_get

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
