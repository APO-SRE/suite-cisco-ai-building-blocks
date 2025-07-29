from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterSpecNTPServerV2PlatformPOST")


@_attrs_define
class ClusterSpecNTPServerV2PlatformPOST:
    """Cluster NTP Server

    Attributes:
        host (Union[Unset, str]): Cluster NTP server ip/fqdn
        key_id (Union[Unset, str]): Cluster NTP server symmetrical key ID
        prefer (Union[Unset, bool]): Cluster NTP server is preferred
    """

    host: Union[Unset, str] = UNSET
    key_id: Union[Unset, str] = UNSET
    prefer: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        key_id = self.key_id

        prefer = self.prefer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if key_id is not UNSET:
            field_dict["keyID"] = key_id
        if prefer is not UNSET:
            field_dict["prefer"] = prefer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host = d.pop("host", UNSET)

        key_id = d.pop("keyID", UNSET)

        prefer = d.pop("prefer", UNSET)

        cluster_spec_ntp_server_v2_platform_post = cls(
            host=host,
            key_id=key_id,
            prefer=prefer,
        )

        cluster_spec_ntp_server_v2_platform_post.additional_properties = d
        return cluster_spec_ntp_server_v2_platform_post

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
