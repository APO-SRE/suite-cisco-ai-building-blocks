from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrustedCASpecWrapperV4CertmanagementPOST")


@_attrs_define
class TrustedCASpecWrapperV4CertmanagementPOST:
    """
    Attributes:
        name (str):
        cert (Union[Unset, str]):
    """

    name: str
    cert: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        cert = self.cert

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if cert is not UNSET:
            field_dict["cert"] = cert

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        cert = d.pop("cert", UNSET)

        trusted_ca_spec_wrapper_v4_certmanagement_post = cls(
            name=name,
            cert=cert,
        )

        trusted_ca_spec_wrapper_v4_certmanagement_post.additional_properties = d
        return trusted_ca_spec_wrapper_v4_certmanagement_post

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
