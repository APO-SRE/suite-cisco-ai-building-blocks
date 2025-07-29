from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity import Entity
    from ..models.match import Match
    from ..models.policy import Policy


T = TypeVar("T", bound="IncidentsCollection")


@_attrs_define
class IncidentsCollection:
    """
    Attributes:
        id (Union[Unset, str]): The internal CloudLock incident ID, which can be used to
            call or update a specific incident.
        customer_key (Union[Unset, str]): An empty field to be used as a system ID (a customer can set this or leave it
            empty).
        incident_status (Union[Unset, str]): The status of the incident. Possible values: NEW, RESOLVED, IN PROGRESS,
            DISMISSED.
        severity (Union[Unset, str]): The severity of the incident. Possible values: INFO, WARNING, CRITICAL, ALERT.
        created_at (Union[Unset, str]): The incident creation time, in UTC.
        updated_at (Union[Unset, str]): The incident last upate time, in UTC.
        match_count (Union[Unset, int]): The total number of matches."
        entity (Union[Unset, Entity]): The information about the object relating to this incident.
        policy (Union[Unset, Policy]): The policy that triggered the incident.
        matches (Union[Unset, list['Match']]): The list of matches for the incident.
    """

    id: Union[Unset, str] = UNSET
    customer_key: Union[Unset, str] = UNSET
    incident_status: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    match_count: Union[Unset, int] = UNSET
    entity: Union[Unset, "Entity"] = UNSET
    policy: Union[Unset, "Policy"] = UNSET
    matches: Union[Unset, list["Match"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_key = self.customer_key

        incident_status = self.incident_status

        severity = self.severity

        created_at = self.created_at

        updated_at = self.updated_at

        match_count = self.match_count

        entity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entity, Unset):
            entity = self.entity.to_dict()

        policy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        matches: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.matches, Unset):
            matches = []
            for matches_item_data in self.matches:
                matches_item = matches_item_data.to_dict()
                matches.append(matches_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if customer_key is not UNSET:
            field_dict["customer_key"] = customer_key
        if incident_status is not UNSET:
            field_dict["incident_status"] = incident_status
        if severity is not UNSET:
            field_dict["severity"] = severity
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if match_count is not UNSET:
            field_dict["match_count"] = match_count
        if entity is not UNSET:
            field_dict["entity"] = entity
        if policy is not UNSET:
            field_dict["policy"] = policy
        if matches is not UNSET:
            field_dict["matches"] = matches

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity import Entity
        from ..models.match import Match
        from ..models.policy import Policy

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        customer_key = d.pop("customer_key", UNSET)

        incident_status = d.pop("incident_status", UNSET)

        severity = d.pop("severity", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        match_count = d.pop("match_count", UNSET)

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, Entity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = Entity.from_dict(_entity)

        _policy = d.pop("policy", UNSET)
        policy: Union[Unset, Policy]
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = Policy.from_dict(_policy)

        matches = []
        _matches = d.pop("matches", UNSET)
        for matches_item_data in _matches or []:
            matches_item = Match.from_dict(matches_item_data)

            matches.append(matches_item)

        incidents_collection = cls(
            id=id,
            customer_key=customer_key,
            incident_status=incident_status,
            severity=severity,
            created_at=created_at,
            updated_at=updated_at,
            match_count=match_count,
            entity=entity,
            policy=policy,
            matches=matches,
        )

        incidents_collection.additional_properties = d
        return incidents_collection

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
