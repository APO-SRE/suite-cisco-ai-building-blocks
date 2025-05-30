import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_activity_event import ConfigActivityEvent
    from ..models.config_candidate_review import ConfigCandidateReview


T = TypeVar("T", bound="ConfigFabricCandidate")


@_attrs_define
class ConfigFabricCandidate:
    """FabricCandidate represents a single fabric candidate record.

    Attributes:
        active (Union[Unset, bool]): Indicates that there are pending changes.
        created_at (Union[Unset, datetime.datetime]): Description not available
        created_by (Union[Unset, str]): The user who created the candidate.
        events (Union[Unset, list['ConfigActivityEvent']]): Activity events.
        fabric_id (Union[Unset, str]): The fabric identifier.
        modified_at (Union[Unset, datetime.datetime]): The last modification timestamp.
        modified_by (Union[Unset, str]): The user who modified candidate.
        name (Union[Unset, str]): The candidate name.
        reviews (Union[Unset, list['ConfigCandidateReview']]): A set of review logs.
        revision_id (Union[Unset, str]): The revision identifier of the candidate.
        txn_id (Union[Unset, str]): The transaction sequence number.
    """

    active: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    events: Union[Unset, list["ConfigActivityEvent"]] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    modified_at: Union[Unset, datetime.datetime] = UNSET
    modified_by: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    reviews: Union[Unset, list["ConfigCandidateReview"]] = UNSET
    revision_id: Union[Unset, str] = UNSET
    txn_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by = self.created_by

        events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        fabric_id = self.fabric_id

        modified_at: Union[Unset, str] = UNSET
        if not isinstance(self.modified_at, Unset):
            modified_at = self.modified_at.isoformat()

        modified_by = self.modified_by

        name = self.name

        reviews: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.reviews, Unset):
            reviews = []
            for reviews_item_data in self.reviews:
                reviews_item = reviews_item_data.to_dict()
                reviews.append(reviews_item)

        revision_id = self.revision_id

        txn_id = self.txn_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if events is not UNSET:
            field_dict["events"] = events
        if fabric_id is not UNSET:
            field_dict["fabricId"] = fabric_id
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if name is not UNSET:
            field_dict["name"] = name
        if reviews is not UNSET:
            field_dict["reviews"] = reviews
        if revision_id is not UNSET:
            field_dict["revisionId"] = revision_id
        if txn_id is not UNSET:
            field_dict["txnId"] = txn_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_activity_event import ConfigActivityEvent
        from ..models.config_candidate_review import ConfigCandidateReview

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        created_by = d.pop("createdBy", UNSET)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = ConfigActivityEvent.from_dict(events_item_data)

            events.append(events_item)

        fabric_id = d.pop("fabricId", UNSET)

        _modified_at = d.pop("modifiedAt", UNSET)
        modified_at: Union[Unset, datetime.datetime]
        if isinstance(_modified_at, Unset):
            modified_at = UNSET
        else:
            modified_at = isoparse(_modified_at)

        modified_by = d.pop("modifiedBy", UNSET)

        name = d.pop("name", UNSET)

        reviews = []
        _reviews = d.pop("reviews", UNSET)
        for reviews_item_data in _reviews or []:
            reviews_item = ConfigCandidateReview.from_dict(reviews_item_data)

            reviews.append(reviews_item)

        revision_id = d.pop("revisionId", UNSET)

        txn_id = d.pop("txnId", UNSET)

        config_fabric_candidate = cls(
            active=active,
            created_at=created_at,
            created_by=created_by,
            events=events,
            fabric_id=fabric_id,
            modified_at=modified_at,
            modified_by=modified_by,
            name=name,
            reviews=reviews,
            revision_id=revision_id,
            txn_id=txn_id,
        )

        config_fabric_candidate.additional_properties = d
        return config_fabric_candidate

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
