import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_path_path_id import SchemaPathPathId


T = TypeVar("T", bound="SchemaSystemStats")


@_attrs_define
class SchemaSystemStats:
    """Description not available

    Attributes:
        collected_at (Union[Unset, datetime.datetime]): Description not available
        cpu_idle (Union[Unset, float]): Description not available
        cpu_used (Union[Unset, float]): Description not available
        disk_free (Union[Unset, str]): Description not available
        disk_total (Union[Unset, str]): Description not available
        disk_used (Union[Unset, str]): Description not available
        id (Union[Unset, SchemaPathPathId]): PathId identifies the specific "schema coordinates" identifier of an object
            in the schema tree.
        mem_free (Union[Unset, str]): Description not available
        mem_total (Union[Unset, str]): Description not available
        mem_used (Union[Unset, str]): Description not available
    """

    collected_at: Union[Unset, datetime.datetime] = UNSET
    cpu_idle: Union[Unset, float] = UNSET
    cpu_used: Union[Unset, float] = UNSET
    disk_free: Union[Unset, str] = UNSET
    disk_total: Union[Unset, str] = UNSET
    disk_used: Union[Unset, str] = UNSET
    id: Union[Unset, "SchemaPathPathId"] = UNSET
    mem_free: Union[Unset, str] = UNSET
    mem_total: Union[Unset, str] = UNSET
    mem_used: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collected_at: Union[Unset, str] = UNSET
        if not isinstance(self.collected_at, Unset):
            collected_at = self.collected_at.isoformat()

        cpu_idle = self.cpu_idle

        cpu_used = self.cpu_used

        disk_free = self.disk_free

        disk_total = self.disk_total

        disk_used = self.disk_used

        id: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        mem_free = self.mem_free

        mem_total = self.mem_total

        mem_used = self.mem_used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collected_at is not UNSET:
            field_dict["collectedAt"] = collected_at
        if cpu_idle is not UNSET:
            field_dict["cpuIdle"] = cpu_idle
        if cpu_used is not UNSET:
            field_dict["cpuUsed"] = cpu_used
        if disk_free is not UNSET:
            field_dict["diskFree"] = disk_free
        if disk_total is not UNSET:
            field_dict["diskTotal"] = disk_total
        if disk_used is not UNSET:
            field_dict["diskUsed"] = disk_used
        if id is not UNSET:
            field_dict["id"] = id
        if mem_free is not UNSET:
            field_dict["memFree"] = mem_free
        if mem_total is not UNSET:
            field_dict["memTotal"] = mem_total
        if mem_used is not UNSET:
            field_dict["memUsed"] = mem_used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_path_path_id import SchemaPathPathId

        d = dict(src_dict)
        _collected_at = d.pop("collectedAt", UNSET)
        collected_at: Union[Unset, datetime.datetime]
        if isinstance(_collected_at, Unset):
            collected_at = UNSET
        else:
            collected_at = isoparse(_collected_at)

        cpu_idle = d.pop("cpuIdle", UNSET)

        cpu_used = d.pop("cpuUsed", UNSET)

        disk_free = d.pop("diskFree", UNSET)

        disk_total = d.pop("diskTotal", UNSET)

        disk_used = d.pop("diskUsed", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, SchemaPathPathId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = SchemaPathPathId.from_dict(_id)

        mem_free = d.pop("memFree", UNSET)

        mem_total = d.pop("memTotal", UNSET)

        mem_used = d.pop("memUsed", UNSET)

        schema_system_stats = cls(
            collected_at=collected_at,
            cpu_idle=cpu_idle,
            cpu_used=cpu_used,
            disk_free=disk_free,
            disk_total=disk_total,
            disk_used=disk_used,
            id=id,
            mem_free=mem_free,
            mem_total=mem_total,
            mem_used=mem_used,
        )

        schema_system_stats.additional_properties = d
        return schema_system_stats

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
