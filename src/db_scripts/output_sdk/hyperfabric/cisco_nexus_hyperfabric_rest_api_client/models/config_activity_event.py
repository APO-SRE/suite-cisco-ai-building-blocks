import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.models_object_type import ModelsObjectType
from ..models.models_operation import ModelsOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigActivityEvent")


@_attrs_define
class ConfigActivityEvent:
    """ActivityEvent encapsulates an activity log event.

    Attributes:
        event_id (Union[Unset, str]): The monotonically increasing event identifier.
        object_id (Union[Unset, str]): The object identifier.
        object_name (Union[Unset, str]): The object name (maybe empty).
        object_type (Union[Unset, ModelsObjectType]): Object type enumeration. By convention, ObjectType must have exact
            same string name (in uppercase) as Go type name. For example, Go type Fabric must have an object type of FABRIC.
        operation (Union[Unset, ModelsOperation]): Operation type enumeration.
        parent_id (Union[Unset, str]): The object identifier of parent object.
        parent_type (Union[Unset, ModelsObjectType]): Object type enumeration. By convention, ObjectType must have exact
            same string name (in uppercase) as Go type name. For example, Go type Fabric must have an object type of FABRIC.
        timestamp (Union[Unset, datetime.datetime]): The activity event timestamp.
        username (Union[Unset, str]): The user who triggered the activity event.
    """

    event_id: Union[Unset, str] = UNSET
    object_id: Union[Unset, str] = UNSET
    object_name: Union[Unset, str] = UNSET
    object_type: Union[Unset, ModelsObjectType] = UNSET
    operation: Union[Unset, ModelsOperation] = UNSET
    parent_id: Union[Unset, str] = UNSET
    parent_type: Union[Unset, ModelsObjectType] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_id = self.event_id

        object_id = self.object_id

        object_name = self.object_name

        object_type: Union[Unset, str] = UNSET
        if not isinstance(self.object_type, Unset):
            object_type = self.object_type.value

        operation: Union[Unset, str] = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        parent_id = self.parent_id

        parent_type: Union[Unset, str] = UNSET
        if not isinstance(self.parent_type, Unset):
            parent_type = self.parent_type.value

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if object_name is not UNSET:
            field_dict["objectName"] = object_name
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if operation is not UNSET:
            field_dict["operation"] = operation
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if parent_type is not UNSET:
            field_dict["parentType"] = parent_type
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_id = d.pop("eventId", UNSET)

        object_id = d.pop("objectId", UNSET)

        object_name = d.pop("objectName", UNSET)

        _object_type = d.pop("objectType", UNSET)
        object_type: Union[Unset, ModelsObjectType]
        if isinstance(_object_type, Unset):
            object_type = UNSET
        else:
            object_type = ModelsObjectType(_object_type)

        _operation = d.pop("operation", UNSET)
        operation: Union[Unset, ModelsOperation]
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = ModelsOperation(_operation)

        parent_id = d.pop("parentId", UNSET)

        _parent_type = d.pop("parentType", UNSET)
        parent_type: Union[Unset, ModelsObjectType]
        if isinstance(_parent_type, Unset):
            parent_type = UNSET
        else:
            parent_type = ModelsObjectType(_parent_type)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        username = d.pop("username", UNSET)

        config_activity_event = cls(
            event_id=event_id,
            object_id=object_id,
            object_name=object_name,
            object_type=object_type,
            operation=operation,
            parent_id=parent_id,
            parent_type=parent_type,
            timestamp=timestamp,
            username=username,
        )

        config_activity_event.additional_properties = d
        return config_activity_event

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
