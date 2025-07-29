from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.roles_v4_aaa_put import RolesV4AaaPUT


T = TypeVar("T", bound="RBACV4AaaPUTDomains")


@_attrs_define
class RBACV4AaaPUTDomains:
    """Mapping of ND Security Domains and Roles"""

    additional_properties: dict[str, "RolesV4AaaPUT"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roles_v4_aaa_put import RolesV4AaaPUT

        d = dict(src_dict)
        rbacv4_aaa_put_domains = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = RolesV4AaaPUT.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        rbacv4_aaa_put_domains.additional_properties = additional_properties
        return rbacv4_aaa_put_domains

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "RolesV4AaaPUT":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "RolesV4AaaPUT") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
