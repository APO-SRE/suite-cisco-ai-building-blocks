from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaginatedObjectDescriptorV1ArgoCiscoComPOST")


@_attrs_define
class PaginatedObjectDescriptorV1ArgoCiscoComPOST:
    """
    Attributes:
        id_key (Union[Unset, str]):
        vals (Union[Unset, list[str]]):
    """

    id_key: Union[Unset, str] = UNSET
    vals: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id_key = self.id_key

        vals: Union[Unset, list[str]] = UNSET
        if not isinstance(self.vals, Unset):
            vals = self.vals

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id_key is not UNSET:
            field_dict["idKey"] = id_key
        if vals is not UNSET:
            field_dict["vals"] = vals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id_key = d.pop("idKey", UNSET)

        vals = cast(list[str], d.pop("vals", UNSET))

        paginated_object_descriptor_v1_argo_cisco_com_post = cls(
            id_key=id_key,
            vals=vals,
        )

        paginated_object_descriptor_v1_argo_cisco_com_post.additional_properties = d
        return paginated_object_descriptor_v1_argo_cisco_com_post

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
