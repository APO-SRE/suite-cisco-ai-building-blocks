import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_ap_list import LocationAPList
    from ..models.location_device_max_detected_rssi import LocationDeviceMaxDetectedRssi


T = TypeVar("T", bound="LocationDevice")


@_attrs_define
class LocationDevice:
    r"""
    Attributes:
        tenant_id (Union[Unset, str]): the tenant unique identifier Example: 200.
        mac_address (Union[Unset, str]): macaddress of the device. Example: 00:12:b8:0a:c6:20.
        device_type (Union[Unset, str]): CLIENT, TAG, ROGUE_AP, or ROGUE_CLIENT Example: TAG.
        campus_id (Union[Unset, str]): unique identifier for a campus from the map import process Example:
            5cb06b3ba1d943669963417c4330c6c7.
        building_id (Union[Unset, str]): unique identifier for a building from the map import process Example:
            98c86b09665a4ffab9647709d966f3a6.
        floor_id (Union[Unset, str]): unique identifier for a floor from the map import process\ Example:
            3b3aad61352e4bc09cdea0119ee3d9f3.
        coordinates (Union[Unset, list[float]]): The coordinates represents cartesian location (x,y) of device which is
            always relative to a given floor Example: [33.401928, 101.87378].
        raw_coordinates (Union[Unset, list[float]]): The raw x and y coordinates of a device. Example: [33.401928,
            101.87378].
        confidence_factor (Union[Unset, int]):  Example: 120.
        compute_type (Union[Unset, str]): The compute type, possible values are RSSI and AOA. Example: RSSI.
        first_located_at (Union[Unset, str]): The first time of the device location being detected. Example:
            2018-05-25T17:30:12.403Z.
        last_location_at (Union[Unset, datetime.datetime]): The last time of the location being detected. Example:
            2018-05-27T21:14:44.005Z.
        changed_on (Union[Unset, str]): The UTC time the device state changed. Example: 1527456440322.
        associated (Union[Unset, bool]): true|false.  Whether or not a device has connected to a network.
        manufacturer (Union[Unset, str]): Manufacturer of the device. Example: Aeroscout Ltd..
        controller (Union[Unset, str]): The controller IP. Example: 10.22.244.27.
        max_detected_rssi (Union[Unset, LocationDeviceMaxDetectedRssi]):
        num_detecting_aps (Union[Unset, int]): The number of detecting APs. Example: 3.
        ap_list (Union[Unset, list['LocationAPList']]): The list of APs.
    """

    tenant_id: Union[Unset, str] = UNSET
    mac_address: Union[Unset, str] = UNSET
    device_type: Union[Unset, str] = UNSET
    campus_id: Union[Unset, str] = UNSET
    building_id: Union[Unset, str] = UNSET
    floor_id: Union[Unset, str] = UNSET
    coordinates: Union[Unset, list[float]] = UNSET
    raw_coordinates: Union[Unset, list[float]] = UNSET
    confidence_factor: Union[Unset, int] = UNSET
    compute_type: Union[Unset, str] = UNSET
    first_located_at: Union[Unset, str] = UNSET
    last_location_at: Union[Unset, datetime.datetime] = UNSET
    changed_on: Union[Unset, str] = UNSET
    associated: Union[Unset, bool] = UNSET
    manufacturer: Union[Unset, str] = UNSET
    controller: Union[Unset, str] = UNSET
    max_detected_rssi: Union[Unset, "LocationDeviceMaxDetectedRssi"] = UNSET
    num_detecting_aps: Union[Unset, int] = UNSET
    ap_list: Union[Unset, list["LocationAPList"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tenant_id = self.tenant_id

        mac_address = self.mac_address

        device_type = self.device_type

        campus_id = self.campus_id

        building_id = self.building_id

        floor_id = self.floor_id

        coordinates: Union[Unset, list[float]] = UNSET
        if not isinstance(self.coordinates, Unset):
            coordinates = self.coordinates

        raw_coordinates: Union[Unset, list[float]] = UNSET
        if not isinstance(self.raw_coordinates, Unset):
            raw_coordinates = self.raw_coordinates

        confidence_factor = self.confidence_factor

        compute_type = self.compute_type

        first_located_at = self.first_located_at

        last_location_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_location_at, Unset):
            last_location_at = self.last_location_at.isoformat()

        changed_on = self.changed_on

        associated = self.associated

        manufacturer = self.manufacturer

        controller = self.controller

        max_detected_rssi: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.max_detected_rssi, Unset):
            max_detected_rssi = self.max_detected_rssi.to_dict()

        num_detecting_aps = self.num_detecting_aps

        ap_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ap_list, Unset):
            ap_list = []
            for ap_list_item_data in self.ap_list:
                ap_list_item = ap_list_item_data.to_dict()
                ap_list.append(ap_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if campus_id is not UNSET:
            field_dict["campusId"] = campus_id
        if building_id is not UNSET:
            field_dict["buildingId"] = building_id
        if floor_id is not UNSET:
            field_dict["floorId"] = floor_id
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if raw_coordinates is not UNSET:
            field_dict["rawCoordinates"] = raw_coordinates
        if confidence_factor is not UNSET:
            field_dict["confidenceFactor"] = confidence_factor
        if compute_type is not UNSET:
            field_dict["computeType"] = compute_type
        if first_located_at is not UNSET:
            field_dict["firstLocatedAt"] = first_located_at
        if last_location_at is not UNSET:
            field_dict["lastLocationAt"] = last_location_at
        if changed_on is not UNSET:
            field_dict["changedOn"] = changed_on
        if associated is not UNSET:
            field_dict["associated"] = associated
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if controller is not UNSET:
            field_dict["controller"] = controller
        if max_detected_rssi is not UNSET:
            field_dict["maxDetectedRssi"] = max_detected_rssi
        if num_detecting_aps is not UNSET:
            field_dict["numDetectingAps"] = num_detecting_aps
        if ap_list is not UNSET:
            field_dict["apList"] = ap_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_ap_list import LocationAPList
        from ..models.location_device_max_detected_rssi import LocationDeviceMaxDetectedRssi

        d = dict(src_dict)
        tenant_id = d.pop("tenantId", UNSET)

        mac_address = d.pop("macAddress", UNSET)

        device_type = d.pop("deviceType", UNSET)

        campus_id = d.pop("campusId", UNSET)

        building_id = d.pop("buildingId", UNSET)

        floor_id = d.pop("floorId", UNSET)

        coordinates = cast(list[float], d.pop("coordinates", UNSET))

        raw_coordinates = cast(list[float], d.pop("rawCoordinates", UNSET))

        confidence_factor = d.pop("confidenceFactor", UNSET)

        compute_type = d.pop("computeType", UNSET)

        first_located_at = d.pop("firstLocatedAt", UNSET)

        _last_location_at = d.pop("lastLocationAt", UNSET)
        last_location_at: Union[Unset, datetime.datetime]
        if isinstance(_last_location_at, Unset):
            last_location_at = UNSET
        else:
            last_location_at = isoparse(_last_location_at)

        changed_on = d.pop("changedOn", UNSET)

        associated = d.pop("associated", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        controller = d.pop("controller", UNSET)

        _max_detected_rssi = d.pop("maxDetectedRssi", UNSET)
        max_detected_rssi: Union[Unset, LocationDeviceMaxDetectedRssi]
        if isinstance(_max_detected_rssi, Unset):
            max_detected_rssi = UNSET
        else:
            max_detected_rssi = LocationDeviceMaxDetectedRssi.from_dict(_max_detected_rssi)

        num_detecting_aps = d.pop("numDetectingAps", UNSET)

        ap_list = []
        _ap_list = d.pop("apList", UNSET)
        for ap_list_item_data in _ap_list or []:
            ap_list_item = LocationAPList.from_dict(ap_list_item_data)

            ap_list.append(ap_list_item)

        location_device = cls(
            tenant_id=tenant_id,
            mac_address=mac_address,
            device_type=device_type,
            campus_id=campus_id,
            building_id=building_id,
            floor_id=floor_id,
            coordinates=coordinates,
            raw_coordinates=raw_coordinates,
            confidence_factor=confidence_factor,
            compute_type=compute_type,
            first_located_at=first_located_at,
            last_location_at=last_location_at,
            changed_on=changed_on,
            associated=associated,
            manufacturer=manufacturer,
            controller=controller,
            max_detected_rssi=max_detected_rssi,
            num_detecting_aps=num_detecting_aps,
            ap_list=ap_list,
        )

        location_device.additional_properties = d
        return location_device

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
