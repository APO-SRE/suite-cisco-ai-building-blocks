from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.network_storage_status_wrapper_v1_platform_get_health_state import (
    NetworkStorageStatusWrapperV1PlatformGETHealthState,
)
from ..models.network_storage_status_wrapper_v1_platform_get_usage_state import (
    NetworkStorageStatusWrapperV1PlatformGETUsageState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkStorageStatusWrapperV1PlatformGET")


@_attrs_define
class NetworkStorageStatusWrapperV1PlatformGET:
    """
    Attributes:
        health_state (Union[Unset, NetworkStorageStatusWrapperV1PlatformGETHealthState]): Current health of the storage
        message (Union[Unset, str]): Status message about this storage's health
        usage (Union[Unset, int]): Current storage usage %
        usage_state (Union[Unset, NetworkStorageStatusWrapperV1PlatformGETUsageState]): Current usage state of the
            storage
        user_apps (Union[Unset, list[str]]): Applications currently using this config
    """

    health_state: Union[Unset, NetworkStorageStatusWrapperV1PlatformGETHealthState] = UNSET
    message: Union[Unset, str] = UNSET
    usage: Union[Unset, int] = UNSET
    usage_state: Union[Unset, NetworkStorageStatusWrapperV1PlatformGETUsageState] = UNSET
    user_apps: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        health_state: Union[Unset, str] = UNSET
        if not isinstance(self.health_state, Unset):
            health_state = self.health_state.value

        message = self.message

        usage = self.usage

        usage_state: Union[Unset, str] = UNSET
        if not isinstance(self.usage_state, Unset):
            usage_state = self.usage_state.value

        user_apps: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_apps, Unset):
            user_apps = self.user_apps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if health_state is not UNSET:
            field_dict["healthState"] = health_state
        if message is not UNSET:
            field_dict["message"] = message
        if usage is not UNSET:
            field_dict["usage"] = usage
        if usage_state is not UNSET:
            field_dict["usageState"] = usage_state
        if user_apps is not UNSET:
            field_dict["userApps"] = user_apps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _health_state = d.pop("healthState", UNSET)
        health_state: Union[Unset, NetworkStorageStatusWrapperV1PlatformGETHealthState]
        if isinstance(_health_state, Unset):
            health_state = UNSET
        else:
            health_state = NetworkStorageStatusWrapperV1PlatformGETHealthState(_health_state)

        message = d.pop("message", UNSET)

        usage = d.pop("usage", UNSET)

        _usage_state = d.pop("usageState", UNSET)
        usage_state: Union[Unset, NetworkStorageStatusWrapperV1PlatformGETUsageState]
        if isinstance(_usage_state, Unset):
            usage_state = UNSET
        else:
            usage_state = NetworkStorageStatusWrapperV1PlatformGETUsageState(_usage_state)

        user_apps = cast(list[str], d.pop("userApps", UNSET))

        network_storage_status_wrapper_v1_platform_get = cls(
            health_state=health_state,
            message=message,
            usage=usage,
            usage_state=usage_state,
            user_apps=user_apps,
        )

        network_storage_status_wrapper_v1_platform_get.additional_properties = d
        return network_storage_status_wrapper_v1_platform_get

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
