from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DirectoryEntrySpecV1ArgoCiscoComPUT")


@_attrs_define
class DirectoryEntrySpecV1ArgoCiscoComPUT:
    """
    Attributes:
        application (Union[Unset, str]):
        category (Union[Unset, str]):
        database_name (Union[Unset, str]):
        endpoint (Union[Unset, str]):
        kind (Union[Unset, str]):
        name (Union[Unset, str]):
        operations (Union[Unset, list[str]]):
        owner (Union[Unset, str]):
        realm (Union[Unset, str]):
    """

    application: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    database_name: Union[Unset, str] = UNSET
    endpoint: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    operations: Union[Unset, list[str]] = UNSET
    owner: Union[Unset, str] = UNSET
    realm: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application = self.application

        category = self.category

        database_name = self.database_name

        endpoint = self.endpoint

        kind = self.kind

        name = self.name

        operations: Union[Unset, list[str]] = UNSET
        if not isinstance(self.operations, Unset):
            operations = self.operations

        owner = self.owner

        realm = self.realm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application is not UNSET:
            field_dict["application"] = application
        if category is not UNSET:
            field_dict["category"] = category
        if database_name is not UNSET:
            field_dict["databaseName"] = database_name
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if kind is not UNSET:
            field_dict["kind"] = kind
        if name is not UNSET:
            field_dict["name"] = name
        if operations is not UNSET:
            field_dict["operations"] = operations
        if owner is not UNSET:
            field_dict["owner"] = owner
        if realm is not UNSET:
            field_dict["realm"] = realm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        application = d.pop("application", UNSET)

        category = d.pop("category", UNSET)

        database_name = d.pop("databaseName", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        kind = d.pop("kind", UNSET)

        name = d.pop("name", UNSET)

        operations = cast(list[str], d.pop("operations", UNSET))

        owner = d.pop("owner", UNSET)

        realm = d.pop("realm", UNSET)

        directory_entry_spec_v1_argo_cisco_com_put = cls(
            application=application,
            category=category,
            database_name=database_name,
            endpoint=endpoint,
            kind=kind,
            name=name,
            operations=operations,
            owner=owner,
            realm=realm,
        )

        directory_entry_spec_v1_argo_cisco_com_put.additional_properties = d
        return directory_entry_spec_v1_argo_cisco_com_put

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
