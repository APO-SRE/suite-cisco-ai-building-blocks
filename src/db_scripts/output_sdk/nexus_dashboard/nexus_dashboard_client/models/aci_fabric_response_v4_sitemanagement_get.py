from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ACIFabricResponseV4SitemanagementGET")


@_attrs_define
class ACIFabricResponseV4SitemanagementGET:
    """
    Attributes:
        inbepgdn (Union[Unset, list[str]]):
        name (Union[Unset, str]):
    """

    inbepgdn: Union[Unset, list[str]] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inbepgdn: Union[Unset, list[str]] = UNSET
        if not isinstance(self.inbepgdn, Unset):
            inbepgdn = self.inbepgdn

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inbepgdn is not UNSET:
            field_dict["inbepgdn"] = inbepgdn
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inbepgdn = cast(list[str], d.pop("inbepgdn", UNSET))

        name = d.pop("name", UNSET)

        aci_fabric_response_v4_sitemanagement_get = cls(
            inbepgdn=inbepgdn,
            name=name,
        )

        aci_fabric_response_v4_sitemanagement_get.additional_properties = d
        return aci_fabric_response_v4_sitemanagement_get

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
