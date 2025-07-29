from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DefaultAuthSpecWrapperV4AaaPUT")


@_attrs_define
class DefaultAuthSpecWrapperV4AaaPUT:
    """
    Attributes:
        default_domain (Union[Unset, str]): Default auth domain object
        domain_name (Union[Unset, str]): Login domain name
    """

    default_domain: Union[Unset, str] = UNSET
    domain_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_domain = self.default_domain

        domain_name = self.domain_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_domain is not UNSET:
            field_dict["defaultDomain"] = default_domain
        if domain_name is not UNSET:
            field_dict["domainName"] = domain_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_domain = d.pop("defaultDomain", UNSET)

        domain_name = d.pop("domainName", UNSET)

        default_auth_spec_wrapper_v4_aaa_put = cls(
            default_domain=default_domain,
            domain_name=domain_name,
        )

        default_auth_spec_wrapper_v4_aaa_put.additional_properties = d
        return default_auth_spec_wrapper_v4_aaa_put

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
