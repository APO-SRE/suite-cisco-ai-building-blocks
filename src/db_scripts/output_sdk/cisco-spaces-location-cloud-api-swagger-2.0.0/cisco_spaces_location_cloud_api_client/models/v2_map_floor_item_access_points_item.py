from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v2_map_floor_item_access_points_item_interfaces_item import (
        V2MapFloorItemAccessPointsItemInterfacesItem,
    )


T = TypeVar("T", bound="V2MapFloorItemAccessPointsItem")


@_attrs_define
class V2MapFloorItemAccessPointsItem:
    """
    Attributes:
        mac_address (Union[Unset, str]): Access point MAC address Example: 00:08:f6:d9:08:a0.
        is_planned_ap (Union[Unset, str]): Boolean for planned AP Example: false.
        map_position (Union[Unset, str]): Map's position coordinates Example: 116.66606,109.5864,10.0.
        name (Union[Unset, str]): Access point name either queried from controller or defined in maps Example: AP-
            SJC-10-3-23.
        id (Union[Unset, str]): Unique AccessPoint ID Example: a8da11de-c901-4f20-862d-2bf63dde00f4.
        make (Union[Unset, str]): AP make name Example: CISCO_TRADITIONAL.
        level (Union[Unset, str]): Level type Example: AP.
        display_name (Union[Unset, str]): Access point display name defined in maps Example: AP-SJC-10-3-23.
        num_of_slots (Union[Unset, float]): Number of slots of the access point defined in map Example: 3.
        ap_type (Union[Unset, float]): Access point type Example: 2.
        model (Union[Unset, str]): Access point model Example: AP3800I.
        x (Union[Unset, float]): X coordinate of the access point Example: 67.95191.
        y (Union[Unset, float]): Y coordinate of the access point Example: 148.05374.
        z (Union[Unset, float]): Z coordinate of the access point Example: 10.
        angle (Union[Unset, float]): Angle of the access point defined in map Example: 1.57.
        interfaces (Union[Unset, list['V2MapFloorItemAccessPointsItemInterfacesItem']]):
    """

    mac_address: Union[Unset, str] = UNSET
    is_planned_ap: Union[Unset, str] = UNSET
    map_position: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    make: Union[Unset, str] = UNSET
    level: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    num_of_slots: Union[Unset, float] = UNSET
    ap_type: Union[Unset, float] = UNSET
    model: Union[Unset, str] = UNSET
    x: Union[Unset, float] = UNSET
    y: Union[Unset, float] = UNSET
    z: Union[Unset, float] = UNSET
    angle: Union[Unset, float] = UNSET
    interfaces: Union[Unset, list["V2MapFloorItemAccessPointsItemInterfacesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac_address = self.mac_address

        is_planned_ap = self.is_planned_ap

        map_position = self.map_position

        name = self.name

        id = self.id

        make = self.make

        level = self.level

        display_name = self.display_name

        num_of_slots = self.num_of_slots

        ap_type = self.ap_type

        model = self.model

        x = self.x

        y = self.y

        z = self.z

        angle = self.angle

        interfaces: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if is_planned_ap is not UNSET:
            field_dict["isPlannedAP"] = is_planned_ap
        if map_position is not UNSET:
            field_dict["mapPosition"] = map_position
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if make is not UNSET:
            field_dict["make"] = make
        if level is not UNSET:
            field_dict["level"] = level
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if num_of_slots is not UNSET:
            field_dict["numOfSlots"] = num_of_slots
        if ap_type is not UNSET:
            field_dict["apType"] = ap_type
        if model is not UNSET:
            field_dict["model"] = model
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if z is not UNSET:
            field_dict["z"] = z
        if angle is not UNSET:
            field_dict["angle"] = angle
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v2_map_floor_item_access_points_item_interfaces_item import (
            V2MapFloorItemAccessPointsItemInterfacesItem,
        )

        d = dict(src_dict)
        mac_address = d.pop("macAddress", UNSET)

        is_planned_ap = d.pop("isPlannedAP", UNSET)

        map_position = d.pop("mapPosition", UNSET)

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        make = d.pop("make", UNSET)

        level = d.pop("level", UNSET)

        display_name = d.pop("displayName", UNSET)

        num_of_slots = d.pop("numOfSlots", UNSET)

        ap_type = d.pop("apType", UNSET)

        model = d.pop("model", UNSET)

        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        z = d.pop("z", UNSET)

        angle = d.pop("angle", UNSET)

        interfaces = []
        _interfaces = d.pop("interfaces", UNSET)
        for interfaces_item_data in _interfaces or []:
            interfaces_item = V2MapFloorItemAccessPointsItemInterfacesItem.from_dict(interfaces_item_data)

            interfaces.append(interfaces_item)

        v2_map_floor_item_access_points_item = cls(
            mac_address=mac_address,
            is_planned_ap=is_planned_ap,
            map_position=map_position,
            name=name,
            id=id,
            make=make,
            level=level,
            display_name=display_name,
            num_of_slots=num_of_slots,
            ap_type=ap_type,
            model=model,
            x=x,
            y=y,
            z=z,
            angle=angle,
            interfaces=interfaces,
        )

        v2_map_floor_item_access_points_item.additional_properties = d
        return v2_map_floor_item_access_points_item

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
