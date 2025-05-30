from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_match_type import ModelsMatchType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsIpPrefix")


@_attrs_define
class ModelsIpPrefix:
    """IpPrefix encapsulates properties of an IP prefix.

    Attributes:
        accept (Union[Unset, bool]): Accept or reject (permit or deny).
        description (Union[Unset, str]): A short description for the prefix.
        match (Union[Unset, ModelsMatchType]): MatchType enumerates different conditional matching operators.
        prefix (Union[Unset, str]): IPv4 or IPv6 prefix. Must be in CIDR format.
    """

    accept: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    match: Union[Unset, ModelsMatchType] = UNSET
    prefix: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accept = self.accept

        description = self.description

        match: Union[Unset, str] = UNSET
        if not isinstance(self.match, Unset):
            match = self.match.value

        prefix = self.prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accept is not UNSET:
            field_dict["accept"] = accept
        if description is not UNSET:
            field_dict["description"] = description
        if match is not UNSET:
            field_dict["match"] = match
        if prefix is not UNSET:
            field_dict["prefix"] = prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accept = d.pop("accept", UNSET)

        description = d.pop("description", UNSET)

        _match = d.pop("match", UNSET)
        match: Union[Unset, ModelsMatchType]
        if isinstance(_match, Unset):
            match = UNSET
        else:
            match = ModelsMatchType(_match)

        prefix = d.pop("prefix", UNSET)

        models_ip_prefix = cls(
            accept=accept,
            description=description,
            match=match,
            prefix=prefix,
        )

        models_ip_prefix.additional_properties = d
        return models_ip_prefix

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
