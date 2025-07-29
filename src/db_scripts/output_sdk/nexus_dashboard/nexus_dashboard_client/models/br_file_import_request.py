from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BrFileImportRequest")


@_attrs_define
class BrFileImportRequest:
    """
    Attributes:
        name (str): Name of a known backup to be restored
        source (str): Source of the backup file
        path (str): Path or name of the file to import
        encryption_key (str): Encryption key for the backup
    """

    name: str
    source: str
    path: str
    encryption_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        source = self.source

        path = self.path

        encryption_key = self.encryption_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "source": source,
                "path": path,
                "encryptionKey": encryption_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        source = d.pop("source")

        path = d.pop("path")

        encryption_key = d.pop("encryptionKey")

        br_file_import_request = cls(
            name=name,
            source=source,
            path=path,
            encryption_key=encryption_key,
        )

        br_file_import_request.additional_properties = d
        return br_file_import_request

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
