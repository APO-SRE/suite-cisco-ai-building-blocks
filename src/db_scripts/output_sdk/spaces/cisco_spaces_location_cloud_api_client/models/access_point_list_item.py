from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_point_list_item_ap_interfaces_item import AccessPointListItemApInterfacesItem
    from ..models.access_point_list_item_geo_coordinate import AccessPointListItemGeoCoordinate
    from ..models.access_point_list_item_map_coordinates import AccessPointListItemMapCoordinates


T = TypeVar("T", bound="AccessPointListItem")


@_attrs_define
class AccessPointListItem:
    """
    Attributes:
        name (Union[Unset, str]): Access point name either queried from controller or defined in maps Example: AP-
            SJC-10-3-23.
        display_name (Union[Unset, str]): Access point display name defined in maps Example: AP-SJC-10-3-23.
        radio_mac_address (Union[Unset, str]): Access point base radio MAC address Example: 00:08:f6:d9:08:a0.
        eth_mac_address (Union[Unset, str]): Access point ethernet MAC address queried from controller Example:
            00:08:f6:d9:08:a0.
        ip_address (Union[Unset, str]): Access point IP address queried from controller Example: 172.19.28.10.
        ap_type (Union[Unset, float]): Access point type Example: 2.
        ap_mode (Union[Unset, str]): Access point mode, currently not populated Example: null.
        model (Union[Unset, str]): Access point model Example: AP3800I.
        switch_name (Union[Unset, str]): Controller IP address that the access point is associated with Example:
            10.20.200.28.
        floor_id (Union[Unset, str]): ID of the floor that the access point is placed on Example:
            0d8af76120804825a830b12fb7bab43e.
        floor_id_string (Union[Unset, str]): ID of the floor that the access point is placed on Example:
            0d8af76120804825a830b12fb7bab43e.
        floor_name (Union[Unset, str]): Name of the floor that the access point is placed on defined in maps Example:
            Floor 2.
        angle (Union[Unset, float]): Angle of the access point defined in map Example: 1.57.
        num_of_slots (Union[Unset, float]): Number of slots of the access point defined in map Example: 3.
        map_coordinates (Union[Unset, AccessPointListItemMapCoordinates]):
        geo_coordinate (Union[Unset, AccessPointListItemGeoCoordinate]): only computed when there are valid GPS markers
            on the floor
        ap_interfaces (Union[Unset, list['AccessPointListItemApInterfacesItem']]):
    """

    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    radio_mac_address: Union[Unset, str] = UNSET
    eth_mac_address: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    ap_type: Union[Unset, float] = UNSET
    ap_mode: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    switch_name: Union[Unset, str] = UNSET
    floor_id: Union[Unset, str] = UNSET
    floor_id_string: Union[Unset, str] = UNSET
    floor_name: Union[Unset, str] = UNSET
    angle: Union[Unset, float] = UNSET
    num_of_slots: Union[Unset, float] = UNSET
    map_coordinates: Union[Unset, "AccessPointListItemMapCoordinates"] = UNSET
    geo_coordinate: Union[Unset, "AccessPointListItemGeoCoordinate"] = UNSET
    ap_interfaces: Union[Unset, list["AccessPointListItemApInterfacesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        display_name = self.display_name

        radio_mac_address = self.radio_mac_address

        eth_mac_address = self.eth_mac_address

        ip_address = self.ip_address

        ap_type = self.ap_type

        ap_mode = self.ap_mode

        model = self.model

        switch_name = self.switch_name

        floor_id = self.floor_id

        floor_id_string = self.floor_id_string

        floor_name = self.floor_name

        angle = self.angle

        num_of_slots = self.num_of_slots

        map_coordinates: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.map_coordinates, Unset):
            map_coordinates = self.map_coordinates.to_dict()

        geo_coordinate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.geo_coordinate, Unset):
            geo_coordinate = self.geo_coordinate.to_dict()

        ap_interfaces: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ap_interfaces, Unset):
            ap_interfaces = []
            for ap_interfaces_item_data in self.ap_interfaces:
                ap_interfaces_item = ap_interfaces_item_data.to_dict()
                ap_interfaces.append(ap_interfaces_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if radio_mac_address is not UNSET:
            field_dict["radioMacAddress"] = radio_mac_address
        if eth_mac_address is not UNSET:
            field_dict["ethMacAddress"] = eth_mac_address
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if ap_type is not UNSET:
            field_dict["apType"] = ap_type
        if ap_mode is not UNSET:
            field_dict["apMode"] = ap_mode
        if model is not UNSET:
            field_dict["model"] = model
        if switch_name is not UNSET:
            field_dict["switchName"] = switch_name
        if floor_id is not UNSET:
            field_dict["floorId"] = floor_id
        if floor_id_string is not UNSET:
            field_dict["floorIdString"] = floor_id_string
        if floor_name is not UNSET:
            field_dict["floorName"] = floor_name
        if angle is not UNSET:
            field_dict["angle"] = angle
        if num_of_slots is not UNSET:
            field_dict["numOfSlots"] = num_of_slots
        if map_coordinates is not UNSET:
            field_dict["mapCoordinates"] = map_coordinates
        if geo_coordinate is not UNSET:
            field_dict["geoCoordinate"] = geo_coordinate
        if ap_interfaces is not UNSET:
            field_dict["apInterfaces"] = ap_interfaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.access_point_list_item_ap_interfaces_item import AccessPointListItemApInterfacesItem
        from ..models.access_point_list_item_geo_coordinate import AccessPointListItemGeoCoordinate
        from ..models.access_point_list_item_map_coordinates import AccessPointListItemMapCoordinates

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        radio_mac_address = d.pop("radioMacAddress", UNSET)

        eth_mac_address = d.pop("ethMacAddress", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        ap_type = d.pop("apType", UNSET)

        ap_mode = d.pop("apMode", UNSET)

        model = d.pop("model", UNSET)

        switch_name = d.pop("switchName", UNSET)

        floor_id = d.pop("floorId", UNSET)

        floor_id_string = d.pop("floorIdString", UNSET)

        floor_name = d.pop("floorName", UNSET)

        angle = d.pop("angle", UNSET)

        num_of_slots = d.pop("numOfSlots", UNSET)

        _map_coordinates = d.pop("mapCoordinates", UNSET)
        map_coordinates: Union[Unset, AccessPointListItemMapCoordinates]
        if isinstance(_map_coordinates, Unset):
            map_coordinates = UNSET
        else:
            map_coordinates = AccessPointListItemMapCoordinates.from_dict(_map_coordinates)

        _geo_coordinate = d.pop("geoCoordinate", UNSET)
        geo_coordinate: Union[Unset, AccessPointListItemGeoCoordinate]
        if isinstance(_geo_coordinate, Unset):
            geo_coordinate = UNSET
        else:
            geo_coordinate = AccessPointListItemGeoCoordinate.from_dict(_geo_coordinate)

        ap_interfaces = []
        _ap_interfaces = d.pop("apInterfaces", UNSET)
        for ap_interfaces_item_data in _ap_interfaces or []:
            ap_interfaces_item = AccessPointListItemApInterfacesItem.from_dict(ap_interfaces_item_data)

            ap_interfaces.append(ap_interfaces_item)

        access_point_list_item = cls(
            name=name,
            display_name=display_name,
            radio_mac_address=radio_mac_address,
            eth_mac_address=eth_mac_address,
            ip_address=ip_address,
            ap_type=ap_type,
            ap_mode=ap_mode,
            model=model,
            switch_name=switch_name,
            floor_id=floor_id,
            floor_id_string=floor_id_string,
            floor_name=floor_name,
            angle=angle,
            num_of_slots=num_of_slots,
            map_coordinates=map_coordinates,
            geo_coordinate=geo_coordinate,
            ap_interfaces=ap_interfaces,
        )

        access_point_list_item.additional_properties = d
        return access_point_list_item

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
