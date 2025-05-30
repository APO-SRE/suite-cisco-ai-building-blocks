from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_hierarchy_item_ralationship_children_details_inclusion_exclusion_region_item import (
        MapHierarchyItemRalationshipChildrenDetailsInclusionExclusionRegionItem,
    )
    from ..models.map_res_image import MapResImage


T = TypeVar("T", bound="MapHierarchyItemRalationshipChildrenDetails")


@_attrs_define
class MapHierarchyItemRalationshipChildrenDetails:
    """
    Attributes:
        image (Union[Unset, MapResImage]):
        width (Union[Unset, float]):  Example: 85.
        height (Union[Unset, float]):  Example: 10.
        length (Union[Unset, float]):  Example: 58.1.
        offset_x (Union[Unset, float]):
        offset_y (Union[Unset, float]):
        obstacles (Union[Unset, list[str]]):
        gps_markers (Union[Unset, list[str]]):
        floor_number (Union[Unset, int]):  Example: 1.
        calibration_model_ref (Union[Unset, str]):  Example: 28078b6654084fdb9a09b93d8d8a3371.
        inclusion_exclusion_region (Union[Unset,
            list['MapHierarchyItemRalationshipChildrenDetailsInclusionExclusionRegionItem']]):
    """

    image: Union[Unset, "MapResImage"] = UNSET
    width: Union[Unset, float] = UNSET
    height: Union[Unset, float] = UNSET
    length: Union[Unset, float] = UNSET
    offset_x: Union[Unset, float] = UNSET
    offset_y: Union[Unset, float] = UNSET
    obstacles: Union[Unset, list[str]] = UNSET
    gps_markers: Union[Unset, list[str]] = UNSET
    floor_number: Union[Unset, int] = UNSET
    calibration_model_ref: Union[Unset, str] = UNSET
    inclusion_exclusion_region: Union[
        Unset, list["MapHierarchyItemRalationshipChildrenDetailsInclusionExclusionRegionItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        width = self.width

        height = self.height

        length = self.length

        offset_x = self.offset_x

        offset_y = self.offset_y

        obstacles: Union[Unset, list[str]] = UNSET
        if not isinstance(self.obstacles, Unset):
            obstacles = self.obstacles

        gps_markers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.gps_markers, Unset):
            gps_markers = self.gps_markers

        floor_number = self.floor_number

        calibration_model_ref = self.calibration_model_ref

        inclusion_exclusion_region: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.inclusion_exclusion_region, Unset):
            inclusion_exclusion_region = []
            for inclusion_exclusion_region_item_data in self.inclusion_exclusion_region:
                inclusion_exclusion_region_item = inclusion_exclusion_region_item_data.to_dict()
                inclusion_exclusion_region.append(inclusion_exclusion_region_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image is not UNSET:
            field_dict["image"] = image
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if length is not UNSET:
            field_dict["length"] = length
        if offset_x is not UNSET:
            field_dict["offsetX"] = offset_x
        if offset_y is not UNSET:
            field_dict["offsetY"] = offset_y
        if obstacles is not UNSET:
            field_dict["obstacles"] = obstacles
        if gps_markers is not UNSET:
            field_dict["gpsMarkers"] = gps_markers
        if floor_number is not UNSET:
            field_dict["floorNumber"] = floor_number
        if calibration_model_ref is not UNSET:
            field_dict["calibrationModelRef"] = calibration_model_ref
        if inclusion_exclusion_region is not UNSET:
            field_dict["inclusionExclusionRegion"] = inclusion_exclusion_region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_hierarchy_item_ralationship_children_details_inclusion_exclusion_region_item import (
            MapHierarchyItemRalationshipChildrenDetailsInclusionExclusionRegionItem,
        )
        from ..models.map_res_image import MapResImage

        d = dict(src_dict)
        _image = d.pop("image", UNSET)
        image: Union[Unset, MapResImage]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = MapResImage.from_dict(_image)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        length = d.pop("length", UNSET)

        offset_x = d.pop("offsetX", UNSET)

        offset_y = d.pop("offsetY", UNSET)

        obstacles = cast(list[str], d.pop("obstacles", UNSET))

        gps_markers = cast(list[str], d.pop("gpsMarkers", UNSET))

        floor_number = d.pop("floorNumber", UNSET)

        calibration_model_ref = d.pop("calibrationModelRef", UNSET)

        inclusion_exclusion_region = []
        _inclusion_exclusion_region = d.pop("inclusionExclusionRegion", UNSET)
        for inclusion_exclusion_region_item_data in _inclusion_exclusion_region or []:
            inclusion_exclusion_region_item = (
                MapHierarchyItemRalationshipChildrenDetailsInclusionExclusionRegionItem.from_dict(
                    inclusion_exclusion_region_item_data
                )
            )

            inclusion_exclusion_region.append(inclusion_exclusion_region_item)

        map_hierarchy_item_ralationship_children_details = cls(
            image=image,
            width=width,
            height=height,
            length=length,
            offset_x=offset_x,
            offset_y=offset_y,
            obstacles=obstacles,
            gps_markers=gps_markers,
            floor_number=floor_number,
            calibration_model_ref=calibration_model_ref,
            inclusion_exclusion_region=inclusion_exclusion_region,
        )

        map_hierarchy_item_ralationship_children_details.additional_properties = d
        return map_hierarchy_item_ralationship_children_details

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
