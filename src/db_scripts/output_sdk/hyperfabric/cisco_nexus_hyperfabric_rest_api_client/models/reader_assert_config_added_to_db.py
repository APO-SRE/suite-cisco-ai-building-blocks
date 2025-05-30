import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReaderAssertConfigAddedToDb")


@_attrs_define
class ReaderAssertConfigAddedToDb:
    """Description not available

    Attributes:
        child_id (Union[Unset, str]): Description not available
        modified_at (Union[Unset, datetime.datetime]): Description not available
        object_id (Union[Unset, str]): Description not available
        object_name (Union[Unset, str]): Description not available
        object_type (Union[Unset, str]): Description not available
        operation (Union[Unset, str]): Description not available
        org_id (Union[Unset, str]): Description not available
        parent_id (Union[Unset, str]): Description not available
        txn_id (Union[Unset, str]): Description not available
        username (Union[Unset, str]): Description not available
    """

    child_id: Union[Unset, str] = UNSET
    modified_at: Union[Unset, datetime.datetime] = UNSET
    object_id: Union[Unset, str] = UNSET
    object_name: Union[Unset, str] = UNSET
    object_type: Union[Unset, str] = UNSET
    operation: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    parent_id: Union[Unset, str] = UNSET
    txn_id: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        child_id = self.child_id

        modified_at: Union[Unset, str] = UNSET
        if not isinstance(self.modified_at, Unset):
            modified_at = self.modified_at.isoformat()

        object_id = self.object_id

        object_name = self.object_name

        object_type = self.object_type

        operation = self.operation

        org_id = self.org_id

        parent_id = self.parent_id

        txn_id = self.txn_id

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if child_id is not UNSET:
            field_dict["childId"] = child_id
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if object_name is not UNSET:
            field_dict["objectName"] = object_name
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if operation is not UNSET:
            field_dict["operation"] = operation
        if org_id is not UNSET:
            field_dict["orgId"] = org_id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if txn_id is not UNSET:
            field_dict["txnId"] = txn_id
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        child_id = d.pop("childId", UNSET)

        _modified_at = d.pop("modifiedAt", UNSET)
        modified_at: Union[Unset, datetime.datetime]
        if isinstance(_modified_at, Unset):
            modified_at = UNSET
        else:
            modified_at = isoparse(_modified_at)

        object_id = d.pop("objectId", UNSET)

        object_name = d.pop("objectName", UNSET)

        object_type = d.pop("objectType", UNSET)

        operation = d.pop("operation", UNSET)

        org_id = d.pop("orgId", UNSET)

        parent_id = d.pop("parentId", UNSET)

        txn_id = d.pop("txnId", UNSET)

        username = d.pop("username", UNSET)

        reader_assert_config_added_to_db = cls(
            child_id=child_id,
            modified_at=modified_at,
            object_id=object_id,
            object_name=object_name,
            object_type=object_type,
            operation=operation,
            org_id=org_id,
            parent_id=parent_id,
            txn_id=txn_id,
            username=username,
        )

        reader_assert_config_added_to_db.additional_properties = d
        return reader_assert_config_added_to_db

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
