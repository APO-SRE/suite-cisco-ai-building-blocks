from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.br_type import BrType

T = TypeVar("T", bound="PostApiActionClassBackuprestoreBackupBody")


@_attrs_define
class PostApiActionClassBackuprestoreBackupBody:
    """
    Attributes:
        name (str): Name of the backup to create
        type_ (BrType): Operation type
        destination (str): Name of the remote location where the file will be saved or empty for local backup
        encryption_key (str): Backup file encryption key
    """

    name: str
    type_: BrType
    destination: str
    encryption_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        destination = self.destination

        encryption_key = self.encryption_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "destination": destination,
                "encryptionKey": encryption_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = BrType(d.pop("type"))

        destination = d.pop("destination")

        encryption_key = d.pop("encryptionKey")

        post_api_action_class_backuprestore_backup_body = cls(
            name=name,
            type_=type_,
            destination=destination,
            encryption_key=encryption_key,
        )

        post_api_action_class_backuprestore_backup_body.additional_properties = d
        return post_api_action_class_backuprestore_backup_body

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
