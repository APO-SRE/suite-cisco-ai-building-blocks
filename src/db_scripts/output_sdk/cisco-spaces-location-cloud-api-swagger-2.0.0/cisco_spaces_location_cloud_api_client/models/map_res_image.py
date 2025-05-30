from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MapResImage")


@_attrs_define
class MapResImage:
    """
    Attributes:
        size (Union[Unset, int]):  Example: 2801.
        width (Union[Unset, int]):  Example: 2801.
        height (Union[Unset, int]):  Example: 1912.
        image_name (Union[Unset, str]): The image for the map. Example: domain_0_1488923984353.jpg.
        zoom_level (Union[Unset, int]):  Example: 4.
        color_depth (Union[Unset, int]):  Example: 8.
        source_file (Union[Unset, str]):  Example: domain_0_1488923984353.jpg.
        max_resolution (Union[Unset, int]):  Example: 16.
        valid_image_supplied (Union[Unset, bool]): Indicate if the source image is valid(true) or not(false). Example:
            True.
    """

    size: Union[Unset, int] = UNSET
    width: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    image_name: Union[Unset, str] = UNSET
    zoom_level: Union[Unset, int] = UNSET
    color_depth: Union[Unset, int] = UNSET
    source_file: Union[Unset, str] = UNSET
    max_resolution: Union[Unset, int] = UNSET
    valid_image_supplied: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        size = self.size

        width = self.width

        height = self.height

        image_name = self.image_name

        zoom_level = self.zoom_level

        color_depth = self.color_depth

        source_file = self.source_file

        max_resolution = self.max_resolution

        valid_image_supplied = self.valid_image_supplied

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if size is not UNSET:
            field_dict["size"] = size
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if image_name is not UNSET:
            field_dict["imageName"] = image_name
        if zoom_level is not UNSET:
            field_dict["zoomLevel"] = zoom_level
        if color_depth is not UNSET:
            field_dict["colorDepth"] = color_depth
        if source_file is not UNSET:
            field_dict["sourceFile"] = source_file
        if max_resolution is not UNSET:
            field_dict["maxResolution"] = max_resolution
        if valid_image_supplied is not UNSET:
            field_dict["validImageSupplied"] = valid_image_supplied

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        size = d.pop("size", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        image_name = d.pop("imageName", UNSET)

        zoom_level = d.pop("zoomLevel", UNSET)

        color_depth = d.pop("colorDepth", UNSET)

        source_file = d.pop("sourceFile", UNSET)

        max_resolution = d.pop("maxResolution", UNSET)

        valid_image_supplied = d.pop("validImageSupplied", UNSET)

        map_res_image = cls(
            size=size,
            width=width,
            height=height,
            image_name=image_name,
            zoom_level=zoom_level,
            color_depth=color_depth,
            source_file=source_file,
            max_resolution=max_resolution,
            valid_image_supplied=valid_image_supplied,
        )

        map_res_image.additional_properties = d
        return map_res_image

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
