import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.br_backup_info_status import BrBackupInfoStatus
from ..models.br_type import BrType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.br_status_service_details_items import BrStatusServiceDetailsItems


T = TypeVar("T", bound="BrBackupInfo")


@_attrs_define
class BrBackupInfo:
    """
    Attributes:
        name (Union[Unset, str]): Backup name
        services (Union[Unset, list[str]]): List of services
        type_ (Union[Unset, BrType]): Operation type
        start_time (Union[Unset, datetime.datetime]): Backup start time
        end_time (Union[Unset, datetime.datetime]): Backup end time
        status (Union[Unset, BrBackupInfoStatus]): Status of this backup
        destination (Union[Unset, str]): Remote location where the backup is stored or empty if local
        path (Union[Unset, str]): Path to the backup file (remote backups only)
        user (Union[Unset, str]): ID of user triggering the backup
        schedule (Union[Unset, str]): Name of the schedule that created this backup
        details (Union[Unset, BrStatusServiceDetailsItems]):
    """

    name: Union[Unset, str] = UNSET
    services: Union[Unset, list[str]] = UNSET
    type_: Union[Unset, BrType] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    end_time: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, BrBackupInfoStatus] = UNSET
    destination: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    user: Union[Unset, str] = UNSET
    schedule: Union[Unset, str] = UNSET
    details: Union[Unset, "BrStatusServiceDetailsItems"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        services: Union[Unset, list[str]] = UNSET
        if not isinstance(self.services, Unset):
            services = self.services

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        destination = self.destination

        path = self.path

        user = self.user

        schedule = self.schedule

        details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if services is not UNSET:
            field_dict["services"] = services
        if type_ is not UNSET:
            field_dict["type"] = type_
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if status is not UNSET:
            field_dict["status"] = status
        if destination is not UNSET:
            field_dict["destination"] = destination
        if path is not UNSET:
            field_dict["path"] = path
        if user is not UNSET:
            field_dict["user"] = user
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.br_status_service_details_items import BrStatusServiceDetailsItems

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        services = cast(list[str], d.pop("services", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BrType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BrType(_type_)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BrBackupInfoStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BrBackupInfoStatus(_status)

        destination = d.pop("destination", UNSET)

        path = d.pop("path", UNSET)

        user = d.pop("user", UNSET)

        schedule = d.pop("schedule", UNSET)

        _details = d.pop("details", UNSET)
        details: Union[Unset, BrStatusServiceDetailsItems]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = BrStatusServiceDetailsItems.from_dict(_details)

        br_backup_info = cls(
            name=name,
            services=services,
            type_=type_,
            start_time=start_time,
            end_time=end_time,
            status=status,
            destination=destination,
            path=path,
            user=user,
            schedule=schedule,
            details=details,
        )

        br_backup_info.additional_properties = d
        return br_backup_info

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
