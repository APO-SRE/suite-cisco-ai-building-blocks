from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rbacv4_aaa_put_domains import RBACV4AaaPUTDomains


T = TypeVar("T", bound="RBACV4AaaPUT")


@_attrs_define
class RBACV4AaaPUT:
    """
    Attributes:
        domains (Union[Unset, RBACV4AaaPUTDomains]): Mapping of ND Security Domains and Roles
    """

    domains: Union[Unset, "RBACV4AaaPUTDomains"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domains: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.domains, Unset):
            domains = self.domains.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domains is not UNSET:
            field_dict["domains"] = domains

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rbacv4_aaa_put_domains import RBACV4AaaPUTDomains

        d = dict(src_dict)
        _domains = d.pop("domains", UNSET)
        domains: Union[Unset, RBACV4AaaPUTDomains]
        if isinstance(_domains, Unset):
            domains = UNSET
        else:
            domains = RBACV4AaaPUTDomains.from_dict(_domains)

        rbacv4_aaa_put = cls(
            domains=domains,
        )

        rbacv4_aaa_put.additional_properties = d
        return rbacv4_aaa_put

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
