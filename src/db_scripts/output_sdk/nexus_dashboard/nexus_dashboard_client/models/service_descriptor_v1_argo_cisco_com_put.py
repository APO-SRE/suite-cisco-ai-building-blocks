from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceDescriptorV1ArgoCiscoComPUT")


@_attrs_define
class ServiceDescriptorV1ArgoCiscoComPUT:
    """
    Attributes:
        database_name (Union[Unset, str]):
        endpoint (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    database_name: Union[Unset, str] = UNSET
    endpoint: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database_name = self.database_name

        endpoint = self.endpoint

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if database_name is not UNSET:
            field_dict["databaseName"] = database_name
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        database_name = d.pop("databaseName", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        name = d.pop("name", UNSET)

        service_descriptor_v1_argo_cisco_com_put = cls(
            database_name=database_name,
            endpoint=endpoint,
            name=name,
        )

        service_descriptor_v1_argo_cisco_com_put.additional_properties = d
        return service_descriptor_v1_argo_cisco_com_put

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
