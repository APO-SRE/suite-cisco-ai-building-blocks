from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCommunity")


@_attrs_define
class ModelsCommunity:
    """Community encapsulates properties of a BGP community.

    Attributes:
        accept (Union[Unset, bool]): Accept or reject (permit or deny).
        community (Union[Unset, str]): The BGP community tag. Maybe in wildcard format; e.g. *:100 or 1000:*.
        description (Union[Unset, str]): A short description for the community.
    """

    accept: Union[Unset, bool] = UNSET
    community: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accept = self.accept

        community = self.community

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accept is not UNSET:
            field_dict["accept"] = accept
        if community is not UNSET:
            field_dict["community"] = community
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accept = d.pop("accept", UNSET)

        community = d.pop("community", UNSET)

        description = d.pop("description", UNSET)

        models_community = cls(
            accept=accept,
            community=community,
            description=description,
        )

        models_community.additional_properties = d
        return models_community

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
