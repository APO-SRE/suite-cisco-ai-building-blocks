from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activities_collection_client_location import ActivitiesCollectionClientLocation
    from ..models.activities_collection_extra import ActivitiesCollectionExtra
    from ..models.activities_collection_raw import ActivitiesCollectionRaw
    from ..models.activities_collection_user import ActivitiesCollectionUser
    from ..models.activities_collection_vendor import ActivitiesCollectionVendor


T = TypeVar("T", bound="ActivitiesCollection")


@_attrs_define
class ActivitiesCollection:
    """
    Attributes:
        event_id (Union[Unset, str]): This is CloudLock Internal Identifier for an activity. Example:
            -6285966971996490902#0.
        client_ip (Union[Unset, str]): The client's IP address. Example: 86.176.87.160.
        event_type (Union[Unset, str]): The type of the event. Example: login, other, user_settings.
        created_at (Union[Unset, str]): When the activity took place, in UTC. Example: 2015-03-19T09:00:17.602482+00:00.
        operation_successful (Union[Unset, bool]): Specifies whether the activity succeeded. Example: True.
        client_location (Union[Unset, ActivitiesCollectionClientLocation]): The client location information.
        event_category (Union[Unset, str]): The event category type. Example: auth.
        origin_id (Union[Unset, str]): The origin ID. Example: -6285966971996490902.
        user (Union[Unset, ActivitiesCollectionUser]): The user information.
        user_agent (Union[Unset, str]):
        vendor (Union[Unset, ActivitiesCollectionVendor]): The platform information.
        extra (Union[Unset, ActivitiesCollectionExtra]): Additional information related to the activity
        raw (Union[Unset, ActivitiesCollectionRaw]): The raw information for the activity.
    """

    event_id: Union[Unset, str] = UNSET
    client_ip: Union[Unset, str] = UNSET
    event_type: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    operation_successful: Union[Unset, bool] = UNSET
    client_location: Union[Unset, "ActivitiesCollectionClientLocation"] = UNSET
    event_category: Union[Unset, str] = UNSET
    origin_id: Union[Unset, str] = UNSET
    user: Union[Unset, "ActivitiesCollectionUser"] = UNSET
    user_agent: Union[Unset, str] = UNSET
    vendor: Union[Unset, "ActivitiesCollectionVendor"] = UNSET
    extra: Union[Unset, "ActivitiesCollectionExtra"] = UNSET
    raw: Union[Unset, "ActivitiesCollectionRaw"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_id = self.event_id

        client_ip = self.client_ip

        event_type = self.event_type

        created_at = self.created_at

        operation_successful = self.operation_successful

        client_location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.client_location, Unset):
            client_location = self.client_location.to_dict()

        event_category = self.event_category

        origin_id = self.origin_id

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        user_agent = self.user_agent

        vendor: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vendor, Unset):
            vendor = self.vendor.to_dict()

        extra: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.extra, Unset):
            extra = self.extra.to_dict()

        raw: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.raw, Unset):
            raw = self.raw.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_id is not UNSET:
            field_dict["event_id"] = event_id
        if client_ip is not UNSET:
            field_dict["client_ip"] = client_ip
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if operation_successful is not UNSET:
            field_dict["operation_successful"] = operation_successful
        if client_location is not UNSET:
            field_dict["client_location"] = client_location
        if event_category is not UNSET:
            field_dict["event_category"] = event_category
        if origin_id is not UNSET:
            field_dict["origin_id"] = origin_id
        if user is not UNSET:
            field_dict["user"] = user
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if extra is not UNSET:
            field_dict["extra"] = extra
        if raw is not UNSET:
            field_dict["raw"] = raw

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activities_collection_client_location import ActivitiesCollectionClientLocation
        from ..models.activities_collection_extra import ActivitiesCollectionExtra
        from ..models.activities_collection_raw import ActivitiesCollectionRaw
        from ..models.activities_collection_user import ActivitiesCollectionUser
        from ..models.activities_collection_vendor import ActivitiesCollectionVendor

        d = dict(src_dict)
        event_id = d.pop("event_id", UNSET)

        client_ip = d.pop("client_ip", UNSET)

        event_type = d.pop("event_type", UNSET)

        created_at = d.pop("created_at", UNSET)

        operation_successful = d.pop("operation_successful", UNSET)

        _client_location = d.pop("client_location", UNSET)
        client_location: Union[Unset, ActivitiesCollectionClientLocation]
        if isinstance(_client_location, Unset):
            client_location = UNSET
        else:
            client_location = ActivitiesCollectionClientLocation.from_dict(_client_location)

        event_category = d.pop("event_category", UNSET)

        origin_id = d.pop("origin_id", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, ActivitiesCollectionUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ActivitiesCollectionUser.from_dict(_user)

        user_agent = d.pop("user_agent", UNSET)

        _vendor = d.pop("vendor", UNSET)
        vendor: Union[Unset, ActivitiesCollectionVendor]
        if isinstance(_vendor, Unset):
            vendor = UNSET
        else:
            vendor = ActivitiesCollectionVendor.from_dict(_vendor)

        _extra = d.pop("extra", UNSET)
        extra: Union[Unset, ActivitiesCollectionExtra]
        if isinstance(_extra, Unset):
            extra = UNSET
        else:
            extra = ActivitiesCollectionExtra.from_dict(_extra)

        _raw = d.pop("raw", UNSET)
        raw: Union[Unset, ActivitiesCollectionRaw]
        if isinstance(_raw, Unset):
            raw = UNSET
        else:
            raw = ActivitiesCollectionRaw.from_dict(_raw)

        activities_collection = cls(
            event_id=event_id,
            client_ip=client_ip,
            event_type=event_type,
            created_at=created_at,
            operation_successful=operation_successful,
            client_location=client_location,
            event_category=event_category,
            origin_id=origin_id,
            user=user,
            user_agent=user_agent,
            vendor=vendor,
            extra=extra,
            raw=raw,
        )

        activities_collection.additional_properties = d
        return activities_collection

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
