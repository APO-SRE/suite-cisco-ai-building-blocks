import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaAssertConfigStaticDefaultRouteExistsData")


@_attrs_define
class SchemaAssertConfigStaticDefaultRouteExistsData:
    """Description not available

    Attributes:
        fabric_id (Union[Unset, str]): Description not available
        generation_id (Union[Unset, str]): Description not available
        implicit (Union[Unset, bool]): Description not available
        latch_time (Union[Unset, str]): Description not available
        latched_at (Union[Unset, datetime.datetime]): Description not available
        org_id (Union[Unset, str]): Description not available
    """

    fabric_id: Union[Unset, str] = UNSET
    generation_id: Union[Unset, str] = UNSET
    implicit: Union[Unset, bool] = UNSET
    latch_time: Union[Unset, str] = UNSET
    latched_at: Union[Unset, datetime.datetime] = UNSET
    org_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fabric_id = self.fabric_id

        generation_id = self.generation_id

        implicit = self.implicit

        latch_time = self.latch_time

        latched_at: Union[Unset, str] = UNSET
        if not isinstance(self.latched_at, Unset):
            latched_at = self.latched_at.isoformat()

        org_id = self.org_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fabric_id is not UNSET:
            field_dict["fabricId"] = fabric_id
        if generation_id is not UNSET:
            field_dict["generationId"] = generation_id
        if implicit is not UNSET:
            field_dict["implicit"] = implicit
        if latch_time is not UNSET:
            field_dict["latchTime"] = latch_time
        if latched_at is not UNSET:
            field_dict["latchedAt"] = latched_at
        if org_id is not UNSET:
            field_dict["orgId"] = org_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fabric_id = d.pop("fabricId", UNSET)

        generation_id = d.pop("generationId", UNSET)

        implicit = d.pop("implicit", UNSET)

        latch_time = d.pop("latchTime", UNSET)

        _latched_at = d.pop("latchedAt", UNSET)
        latched_at: Union[Unset, datetime.datetime]
        if isinstance(_latched_at, Unset):
            latched_at = UNSET
        else:
            latched_at = isoparse(_latched_at)

        org_id = d.pop("orgId", UNSET)

        schema_assert_config_static_default_route_exists_data = cls(
            fabric_id=fabric_id,
            generation_id=generation_id,
            implicit=implicit,
            latch_time=latch_time,
            latched_at=latched_at,
            org_id=org_id,
        )

        schema_assert_config_static_default_route_exists_data.additional_properties = d
        return schema_assert_config_static_default_route_exists_data

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
