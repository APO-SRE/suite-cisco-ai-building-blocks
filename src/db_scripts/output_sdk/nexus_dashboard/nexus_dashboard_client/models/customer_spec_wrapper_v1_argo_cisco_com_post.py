from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerSpecWrapperV1ArgoCiscoComPOST")


@_attrs_define
class CustomerSpecWrapperV1ArgoCiscoComPOST:
    """
    Attributes:
        description (Union[Unset, str]):
        identity (Union[Unset, str]):
        realm (Union[Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    identity: Union[Unset, str] = UNSET
    realm: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        identity = self.identity

        realm = self.realm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if identity is not UNSET:
            field_dict["identity"] = identity
        if realm is not UNSET:
            field_dict["realm"] = realm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        identity = d.pop("identity", UNSET)

        realm = d.pop("realm", UNSET)

        customer_spec_wrapper_v1_argo_cisco_com_post = cls(
            description=description,
            identity=identity,
            realm=realm,
        )

        customer_spec_wrapper_v1_argo_cisco_com_post.additional_properties = d
        return customer_spec_wrapper_v1_argo_cisco_com_post

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
