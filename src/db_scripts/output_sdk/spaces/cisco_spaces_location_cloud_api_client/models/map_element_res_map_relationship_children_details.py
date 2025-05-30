from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_res_image import MapResImage


T = TypeVar("T", bound="MapElementResMapRelationshipChildrenDetails")


@_attrs_define
class MapElementResMapRelationshipChildrenDetails:
    """
    Attributes:
        width (Union[Unset, float]): the element width on map. Example: 91.8.
        length (Union[Unset, float]): the element length on map. Example: 91.8.
        offset_x (Union[Unset, float]):
        offset_y (Union[Unset, float]):
        floor_number (Union[Unset, int]):  Example: 1.
        image (Union[Unset, MapResImage]):
    """

    width: Union[Unset, float] = UNSET
    length: Union[Unset, float] = UNSET
    offset_x: Union[Unset, float] = UNSET
    offset_y: Union[Unset, float] = UNSET
    floor_number: Union[Unset, int] = UNSET
    image: Union[Unset, "MapResImage"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        width = self.width

        length = self.length

        offset_x = self.offset_x

        offset_y = self.offset_y

        floor_number = self.floor_number

        image: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if width is not UNSET:
            field_dict["width"] = width
        if length is not UNSET:
            field_dict["length"] = length
        if offset_x is not UNSET:
            field_dict["offsetX"] = offset_x
        if offset_y is not UNSET:
            field_dict["offsetY"] = offset_y
        if floor_number is not UNSET:
            field_dict["floorNumber"] = floor_number
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_res_image import MapResImage

        d = dict(src_dict)
        width = d.pop("width", UNSET)

        length = d.pop("length", UNSET)

        offset_x = d.pop("offsetX", UNSET)

        offset_y = d.pop("offsetY", UNSET)

        floor_number = d.pop("floorNumber", UNSET)

        _image = d.pop("image", UNSET)
        image: Union[Unset, MapResImage]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = MapResImage.from_dict(_image)

        map_element_res_map_relationship_children_details = cls(
            width=width,
            length=length,
            offset_x=offset_x,
            offset_y=offset_y,
            floor_number=floor_number,
            image=image,
        )

        map_element_res_map_relationship_children_details.additional_properties = d
        return map_element_res_map_relationship_children_details

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
