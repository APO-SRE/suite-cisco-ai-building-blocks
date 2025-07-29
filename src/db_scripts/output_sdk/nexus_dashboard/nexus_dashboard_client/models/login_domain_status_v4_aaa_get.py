from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.login_domain_status_v4_aaa_get_provider_status import LoginDomainStatusV4AaaGETProviderStatus


T = TypeVar("T", bound="LoginDomainStatusV4AaaGET")


@_attrs_define
class LoginDomainStatusV4AaaGET:
    """
    Attributes:
        provider_status (Union[Unset, LoginDomainStatusV4AaaGETProviderStatus]): Login domain providers reachability
            status
    """

    provider_status: Union[Unset, "LoginDomainStatusV4AaaGETProviderStatus"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.provider_status, Unset):
            provider_status = self.provider_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider_status is not UNSET:
            field_dict["providerStatus"] = provider_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.login_domain_status_v4_aaa_get_provider_status import LoginDomainStatusV4AaaGETProviderStatus

        d = dict(src_dict)
        _provider_status = d.pop("providerStatus", UNSET)
        provider_status: Union[Unset, LoginDomainStatusV4AaaGETProviderStatus]
        if isinstance(_provider_status, Unset):
            provider_status = UNSET
        else:
            provider_status = LoginDomainStatusV4AaaGETProviderStatus.from_dict(_provider_status)

        login_domain_status_v4_aaa_get = cls(
            provider_status=provider_status,
        )

        login_domain_status_v4_aaa_get.additional_properties = d
        return login_domain_status_v4_aaa_get

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
