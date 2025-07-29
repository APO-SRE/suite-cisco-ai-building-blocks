from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PoliciesCollection")


@_attrs_define
class PoliciesCollection:
    """
    Attributes:
        id (Union[Unset, str]): This is CloudLock Internal Identifier for a policy. Example: G8qz0vb49V.
        name (Union[Unset, str]): The name of the policy. Example: PCI - Alert.
        state (Union[Unset, str]): Indicates if the policy is active or inactive. Example: Active, Inactive.
        description (Union[Unset, str]): The description of the policy. Example: Apps whose authorized access scopes
            present potential security risks.
        created_at (Union[Unset, str]): The policy creation time, specified as a timestamp in UTC. Example:
            2015-03-19T09:00:17.602482+00:00.
        updated_at (Union[Unset, str]): The policy updated time, specified as a timestamp in UTC. Example:
            2015-03-19T09:00:17.602482+00:00.
        severity (Union[Unset, str]): The severity assigned to incidents of this policy. Example:
            CRITICAL,WARNING,INFO,ALERT.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        state = self.state

        description = self.description

        created_at = self.created_at

        updated_at = self.updated_at

        severity = self.severity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if state is not UNSET:
            field_dict["state"] = state
        if description is not UNSET:
            field_dict["description"] = description
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        state = d.pop("state", UNSET)

        description = d.pop("description", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        severity = d.pop("severity", UNSET)

        policies_collection = cls(
            id=id,
            name=name,
            state=state,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            severity=severity,
        )

        policies_collection.additional_properties = d
        return policies_collection

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
