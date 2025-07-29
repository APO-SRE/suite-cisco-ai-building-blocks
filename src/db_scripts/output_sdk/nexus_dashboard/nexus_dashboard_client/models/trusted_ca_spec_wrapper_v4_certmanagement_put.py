from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrustedCASpecWrapperV4CertmanagementPUT")


@_attrs_define
class TrustedCASpecWrapperV4CertmanagementPUT:
    """
    Attributes:
        cert (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    cert: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cert = self.cert

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cert is not UNSET:
            field_dict["cert"] = cert
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cert = d.pop("cert", UNSET)

        name = d.pop("name", UNSET)

        trusted_ca_spec_wrapper_v4_certmanagement_put = cls(
            cert=cert,
            name=name,
        )

        trusted_ca_spec_wrapper_v4_certmanagement_put.additional_properties = d
        return trusted_ca_spec_wrapper_v4_certmanagement_put

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
