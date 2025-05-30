from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_element_res_map import MapElementResMap


T = TypeVar("T", bound="MapElementRes")


@_attrs_define
class MapElementRes:
    """
    Attributes:
        success (Union[Unset, bool]):  Example: True.
        map_ (Union[Unset, MapElementResMap]):
    """

    success: Union[Unset, bool] = UNSET
    map_: Union[Unset, "MapElementResMap"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        map_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.map_, Unset):
            map_ = self.map_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if map_ is not UNSET:
            field_dict["map"] = map_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_element_res_map import MapElementResMap

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        _map_ = d.pop("map", UNSET)
        map_: Union[Unset, MapElementResMap]
        if isinstance(_map_, Unset):
            map_ = UNSET
        else:
            map_ = MapElementResMap.from_dict(_map_)

        map_element_res = cls(
            success=success,
            map_=map_,
        )

        map_element_res.additional_properties = d
        return map_element_res

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
