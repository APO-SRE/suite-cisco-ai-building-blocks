from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.network_storage_spec_wrapper_v1_platform_post_access_mode import (
    NetworkStorageSpecWrapperV1PlatformPOSTAccessMode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkStorageSpecWrapperV1PlatformPOST")


@_attrs_define
class NetworkStorageSpecWrapperV1PlatformPOST:
    """
    Attributes:
        name (str): Configuration name
        access_mode (Union[Unset, NetworkStorageSpecWrapperV1PlatformPOSTAccessMode]): Allowed accessmode of storage
        alert_threshold (Union[Unset, int]): Alert Threshold for storage size usage
        allowed_apps (Union[Unset, list[str]]): Applications allowed to use this config
        description (Union[Unset, str]): Description about this config
        export_path (Union[Unset, str]): Export Path
        limit (Union[Unset, str]): Limit size for pvs allocated on this storage
        port (Union[Unset, int]): Server Port
        server_address (Union[Unset, str]): Server Address
    """

    name: str
    access_mode: Union[Unset, NetworkStorageSpecWrapperV1PlatformPOSTAccessMode] = UNSET
    alert_threshold: Union[Unset, int] = UNSET
    allowed_apps: Union[Unset, list[str]] = UNSET
    description: Union[Unset, str] = UNSET
    export_path: Union[Unset, str] = UNSET
    limit: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    server_address: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        access_mode: Union[Unset, str] = UNSET
        if not isinstance(self.access_mode, Unset):
            access_mode = self.access_mode.value

        alert_threshold = self.alert_threshold

        allowed_apps: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_apps, Unset):
            allowed_apps = self.allowed_apps

        description = self.description

        export_path = self.export_path

        limit = self.limit

        port = self.port

        server_address = self.server_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if access_mode is not UNSET:
            field_dict["accessMode"] = access_mode
        if alert_threshold is not UNSET:
            field_dict["alertThreshold"] = alert_threshold
        if allowed_apps is not UNSET:
            field_dict["allowedApps"] = allowed_apps
        if description is not UNSET:
            field_dict["description"] = description
        if export_path is not UNSET:
            field_dict["exportPath"] = export_path
        if limit is not UNSET:
            field_dict["limit"] = limit
        if port is not UNSET:
            field_dict["port"] = port
        if server_address is not UNSET:
            field_dict["serverAddress"] = server_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _access_mode = d.pop("accessMode", UNSET)
        access_mode: Union[Unset, NetworkStorageSpecWrapperV1PlatformPOSTAccessMode]
        if isinstance(_access_mode, Unset):
            access_mode = UNSET
        else:
            access_mode = NetworkStorageSpecWrapperV1PlatformPOSTAccessMode(_access_mode)

        alert_threshold = d.pop("alertThreshold", UNSET)

        allowed_apps = cast(list[str], d.pop("allowedApps", UNSET))

        description = d.pop("description", UNSET)

        export_path = d.pop("exportPath", UNSET)

        limit = d.pop("limit", UNSET)

        port = d.pop("port", UNSET)

        server_address = d.pop("serverAddress", UNSET)

        network_storage_spec_wrapper_v1_platform_post = cls(
            name=name,
            access_mode=access_mode,
            alert_threshold=alert_threshold,
            allowed_apps=allowed_apps,
            description=description,
            export_path=export_path,
            limit=limit,
            port=port,
            server_address=server_address,
        )

        network_storage_spec_wrapper_v1_platform_post.additional_properties = d
        return network_storage_spec_wrapper_v1_platform_post

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
