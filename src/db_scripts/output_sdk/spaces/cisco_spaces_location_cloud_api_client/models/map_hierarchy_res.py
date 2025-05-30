from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_hierarchy_item import MapHierarchyItem


T = TypeVar("T", bound="MapHierarchyRes")


@_attrs_define
class MapHierarchyRes:
    """
    Attributes:
        map_ (Union[Unset, list['MapHierarchyItem']]):
    """

    map_: Union[Unset, list["MapHierarchyItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        map_: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.map_, Unset):
            map_ = []
            for map_item_data in self.map_:
                map_item = map_item_data.to_dict()
                map_.append(map_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if map_ is not UNSET:
            field_dict["map"] = map_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_hierarchy_item import MapHierarchyItem

        d = dict(src_dict)
        map_ = []
        _map_ = d.pop("map", UNSET)
        for map_item_data in _map_ or []:
            map_item = MapHierarchyItem.from_dict(map_item_data)

            map_.append(map_item)

        map_hierarchy_res = cls(
            map_=map_,
        )

        map_hierarchy_res.additional_properties = d
        return map_hierarchy_res

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
