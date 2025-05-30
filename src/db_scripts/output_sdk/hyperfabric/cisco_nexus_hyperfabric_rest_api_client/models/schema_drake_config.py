from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaDrakeConfig")


@_attrs_define
class SchemaDrakeConfig:
    """Description not available

    Attributes:
        cloud_base_url_list (Union[Unset, list[str]]): Description not available
    """

    cloud_base_url_list: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_base_url_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cloud_base_url_list, Unset):
            cloud_base_url_list = self.cloud_base_url_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloud_base_url_list is not UNSET:
            field_dict["cloudBaseUrlList"] = cloud_base_url_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cloud_base_url_list = cast(list[str], d.pop("cloudBaseUrlList", UNSET))

        schema_drake_config = cls(
            cloud_base_url_list=cloud_base_url_list,
        )

        schema_drake_config.additional_properties = d
        return schema_drake_config

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
