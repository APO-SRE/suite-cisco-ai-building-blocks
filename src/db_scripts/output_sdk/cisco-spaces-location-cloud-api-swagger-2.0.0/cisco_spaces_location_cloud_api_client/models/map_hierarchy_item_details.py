from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_res_image import MapResImage


T = TypeVar("T", bound="MapHierarchyItemDetails")


@_attrs_define
class MapHierarchyItemDetails:
    """
    Attributes:
        width (Union[Unset, int]): The level's map width. Example: 500.
        height (Union[Unset, int]): The level's map height. Example: 10.
        length (Union[Unset, int]): The level's map length. Example: 500.
        image (Union[Unset, MapResImage]):
    """

    width: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    length: Union[Unset, int] = UNSET
    image: Union[Unset, "MapResImage"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        width = self.width

        height = self.height

        length = self.length

        image: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if length is not UNSET:
            field_dict["length"] = length
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_res_image import MapResImage

        d = dict(src_dict)
        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        length = d.pop("length", UNSET)

        _image = d.pop("image", UNSET)
        image: Union[Unset, MapResImage]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = MapResImage.from_dict(_image)

        map_hierarchy_item_details = cls(
            width=width,
            height=height,
            length=length,
            image=image,
        )

        map_hierarchy_item_details.additional_properties = d
        return map_hierarchy_item_details

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
