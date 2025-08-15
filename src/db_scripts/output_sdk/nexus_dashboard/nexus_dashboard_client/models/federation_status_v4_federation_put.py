from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.federation_status_v4_federation_put_manager_reachability import (
    FederationStatusV4FederationPUTManagerReachability,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FederationStatusV4FederationPUT")


@_attrs_define
class FederationStatusV4FederationPUT:
    """
    Attributes:
        federation_id (Union[Unset, str]): Federation ID
        manager_reachability (Union[Unset, FederationStatusV4FederationPUTManagerReachability]):
    """

    federation_id: Union[Unset, str] = UNSET
    manager_reachability: Union[Unset, FederationStatusV4FederationPUTManagerReachability] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        federation_id = self.federation_id

        manager_reachability: Union[Unset, str] = UNSET
        if not isinstance(self.manager_reachability, Unset):
            manager_reachability = self.manager_reachability.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if federation_id is not UNSET:
            field_dict["federationID"] = federation_id
        if manager_reachability is not UNSET:
            field_dict["managerReachability"] = manager_reachability

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        federation_id = d.pop("federationID", UNSET)

        _manager_reachability = d.pop("managerReachability", UNSET)
        manager_reachability: Union[Unset, FederationStatusV4FederationPUTManagerReachability]
        if isinstance(_manager_reachability, Unset):
            manager_reachability = UNSET
        else:
            manager_reachability = FederationStatusV4FederationPUTManagerReachability(_manager_reachability)

        federation_status_v4_federation_put = cls(
            federation_id=federation_id,
            manager_reachability=manager_reachability,
        )

        federation_status_v4_federation_put.additional_properties = d
        return federation_status_v4_federation_put

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
