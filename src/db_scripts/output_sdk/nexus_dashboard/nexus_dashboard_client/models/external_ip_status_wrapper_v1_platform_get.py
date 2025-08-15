from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_ip_status_error_v1_platform_get import ExternalIpStatusErrorV1PlatformGET
    from ..models.external_ip_status_wrapper_v1_platform_get_external_ip_allocation import (
        ExternalIpStatusWrapperV1PlatformGETExternalIpAllocation,
    )


T = TypeVar("T", bound="ExternalIpStatusWrapperV1PlatformGET")


@_attrs_define
class ExternalIpStatusWrapperV1PlatformGET:
    """
    Attributes:
        error (Union[Unset, ExternalIpStatusErrorV1PlatformGET]): error is the last observed error, if any.
        external_ip_allocation (Union[Unset, ExternalIpStatusWrapperV1PlatformGETExternalIpAllocation]): Map of external
            IPs and the service they are allocated to
    """

    error: Union[Unset, "ExternalIpStatusErrorV1PlatformGET"] = UNSET
    external_ip_allocation: Union[Unset, "ExternalIpStatusWrapperV1PlatformGETExternalIpAllocation"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        external_ip_allocation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.external_ip_allocation, Unset):
            external_ip_allocation = self.external_ip_allocation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if external_ip_allocation is not UNSET:
            field_dict["externalIpAllocation"] = external_ip_allocation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_ip_status_error_v1_platform_get import ExternalIpStatusErrorV1PlatformGET
        from ..models.external_ip_status_wrapper_v1_platform_get_external_ip_allocation import (
            ExternalIpStatusWrapperV1PlatformGETExternalIpAllocation,
        )

        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: Union[Unset, ExternalIpStatusErrorV1PlatformGET]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ExternalIpStatusErrorV1PlatformGET.from_dict(_error)

        _external_ip_allocation = d.pop("externalIpAllocation", UNSET)
        external_ip_allocation: Union[Unset, ExternalIpStatusWrapperV1PlatformGETExternalIpAllocation]
        if isinstance(_external_ip_allocation, Unset):
            external_ip_allocation = UNSET
        else:
            external_ip_allocation = ExternalIpStatusWrapperV1PlatformGETExternalIpAllocation.from_dict(
                _external_ip_allocation
            )

        external_ip_status_wrapper_v1_platform_get = cls(
            error=error,
            external_ip_allocation=external_ip_allocation,
        )

        external_ip_status_wrapper_v1_platform_get.additional_properties = d
        return external_ip_status_wrapper_v1_platform_get

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
