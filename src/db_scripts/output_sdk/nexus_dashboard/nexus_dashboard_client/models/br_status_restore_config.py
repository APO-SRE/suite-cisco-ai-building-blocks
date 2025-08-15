from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.br_type import BrType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BrStatusRestoreConfig")


@_attrs_define
class BrStatusRestoreConfig:
    """Configuration used for restore operations

    Attributes:
        type_ (Union[Unset, BrType]): Operation type
        services (Union[Unset, list[str]]): Running services
        source (Union[Unset, str]): remote location where backup file is stored. Empty for local backups
        path (Union[Unset, str]): File path to import from the remote location or file name imported via
            /api/action/class/backuprestore/file-upload
    """

    type_: Union[Unset, BrType] = UNSET
    services: Union[Unset, list[str]] = UNSET
    source: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        services: Union[Unset, list[str]] = UNSET
        if not isinstance(self.services, Unset):
            services = self.services

        source = self.source

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if services is not UNSET:
            field_dict["services"] = services
        if source is not UNSET:
            field_dict["source"] = source
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BrType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BrType(_type_)

        services = cast(list[str], d.pop("services", UNSET))

        source = d.pop("source", UNSET)

        path = d.pop("path", UNSET)

        br_status_restore_config = cls(
            type_=type_,
            services=services,
            source=source,
            path=path,
        )

        br_status_restore_config.additional_properties = d
        return br_status_restore_config

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
