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


T = TypeVar("T", bound="V2LocationDevice")


@_attrs_define
class V2LocationDevice:
    """
    Attributes:
        tenant_id (Union[Unset, str]): the tenant unique identifier Example: 200.
        mac_address (Union[Unset, str]): mac address of the device. Example: 00:12:b8:0a:c6:20.
        device_type (Union[Unset, str]): CLIENT, TAG, ROGUE_AP, ROGUE_CLIENT, INTERFERER AND BLE_TAG Example: TAG.
        campus_id (Union[Unset, str]): unique identifier for a campus from the map import process Example:
            5cb06b3ba1d943669963417c4330c6c7.
        building_id (Union[Unset, str]): unique identifier for a building from the map import process Example:
            98c86b09665a4ffab9647709d966f3a6.
        floor_id (Union[Unset, str]): unique identifier for a floor from the map import process Example:
            3b3aad61352e4bc09cdea0119ee3d9f3.
        lhfloor_id (Union[Unset, str]): location hierarchy unique identifier for a floor from the map import process
            Example: 3b3aad61352e4bc09cdea0119ee3d9f3.
        hierarchy (Union[Unset, str]): Location hierarchy displayed in string format Example: San Jose->SJC-17->1st
            Floor.
        location_hierarchy (Union[Unset, str]): Location hierarchy from root level displayed in string format Example:
            root-node->San Jose->SJC-17->1st Floor.
        hierarchy_ids (Union[Unset, list[Any]]): array of hierarchy level ids from root to floor or zone Example:
            ["0c872fbb-0545-45fd-b7e2-6ce6ff6f08af","2d3da06b-f4f2-4b3e-9e56-492665ae78ac"].
        source (Union[Unset, str]): Device source like Meraki (data from Meraki Cloud), Notification (tethered data from
            CMX) and Compute (data from Connector) Example: NOTIFICATION.
        is_mac_hashed (Union[Unset, bool]): states where the mac address is hash value
        device_id (Union[Unset, str]): Unique device id assigned to device on Controller. Mainly used for randomised
            devices. When there is no unique device id available, Mac address is populated. Example: 00:24:b1:02:e7:10.
        coordinates (Union[Unset, list[float]]): The coordinates represents cartesian location (x,y) of device which is
            always relative to a given floor Example: [33.401928, 101.87378].
        geo_coordinates (Union[Unset, list[float]]): Latitude and Longitude coordinates of a device. Example:
            [49.26188380661546, -123.24809010788138].
        confidence_factor (Union[Unset, int]): With every calculated location (x,y) a confidence factor (error feet) is
            returned. Example: 120.
        compute_type (Union[Unset, str]): The compute type, possible values are RSSI, FASTLOCATE-RSSI and AOA. Example:
            RSSI.
        first_located_at (Union[Unset, datetime.datetime]): The first time of the device location being detected.
            Example: 2018-05-25T17:30:12.403Z.
        last_located_at (Union[Unset, datetime.datetime]): The last time of the location being detected. Example:
            2018-05-27T21:14:44.005Z.
        changed_on (Union[Unset, str]): The UTC time the device state changed. Example: 1527456440322.
        associated (Union[Unset, bool]): true|false.  Whether or not a device has connected to a network.
        manufacturer (Union[Unset, str]): Manufacturer of the device. Example: Aeroscout Ltd..
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
    lhfloor_id: Union[Unset, str] = UNSET
    hierarchy: Union[Unset, str] = UNSET
    location_hierarchy: Union[Unset, str] = UNSET
    hierarchy_ids: Union[Unset, list[Any]] = UNSET
    source: Union[Unset, str] = UNSET
    is_mac_hashed: Union[Unset, bool] = UNSET
    device_id: Union[Unset, str] = UNSET
    coordinates: Union[Unset, list[float]] = UNSET
    geo_coordinates: Union[Unset, list[float]] = UNSET
    confidence_factor: Union[Unset, int] = UNSET
    compute_type: Union[Unset, str] = UNSET
    first_located_at: Union[Unset, datetime.datetime] = UNSET
    last_located_at: Union[Unset, datetime.datetime] = UNSET
    changed_on: Union[Unset, str] = UNSET
    associated: Union[Unset, bool] = UNSET
    manufacturer: Union[Unset, str] = UNSET
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

        lhfloor_id = self.lhfloor_id

        hierarchy = self.hierarchy

        location_hierarchy = self.location_hierarchy

        hierarchy_ids: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.hierarchy_ids, Unset):
            hierarchy_ids = self.hierarchy_ids

        source = self.source

        is_mac_hashed = self.is_mac_hashed

        device_id = self.device_id

        coordinates: Union[Unset, list[float]] = UNSET
        if not isinstance(self.coordinates, Unset):
            coordinates = self.coordinates

        geo_coordinates: Union[Unset, list[float]] = UNSET
        if not isinstance(self.geo_coordinates, Unset):
            geo_coordinates = self.geo_coordinates

        confidence_factor = self.confidence_factor

        compute_type = self.compute_type

        first_located_at: Union[Unset, str] = UNSET
        if not isinstance(self.first_located_at, Unset):
            first_located_at = self.first_located_at.isoformat()

        last_located_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_located_at, Unset):
            last_located_at = self.last_located_at.isoformat()

        changed_on = self.changed_on

        associated = self.associated

        manufacturer = self.manufacturer

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
        if lhfloor_id is not UNSET:
            field_dict["lhfloorId"] = lhfloor_id
        if hierarchy is not UNSET:
            field_dict["hierarchy"] = hierarchy
        if location_hierarchy is not UNSET:
            field_dict["locationHierarchy"] = location_hierarchy
        if hierarchy_ids is not UNSET:
            field_dict["hierarchyIds"] = hierarchy_ids
        if source is not UNSET:
            field_dict["source"] = source
        if is_mac_hashed is not UNSET:
            field_dict["isMacHashed"] = is_mac_hashed
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if geo_coordinates is not UNSET:
            field_dict["geoCoordinates"] = geo_coordinates
        if confidence_factor is not UNSET:
            field_dict["confidenceFactor"] = confidence_factor
        if compute_type is not UNSET:
            field_dict["computeType"] = compute_type
        if first_located_at is not UNSET:
            field_dict["firstLocatedAt"] = first_located_at
        if last_located_at is not UNSET:
            field_dict["lastLocatedAt"] = last_located_at
        if changed_on is not UNSET:
            field_dict["changedOn"] = changed_on
        if associated is not UNSET:
            field_dict["associated"] = associated
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
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

        lhfloor_id = d.pop("lhfloorId", UNSET)

        hierarchy = d.pop("hierarchy", UNSET)

        location_hierarchy = d.pop("locationHierarchy", UNSET)

        hierarchy_ids = cast(list[Any], d.pop("hierarchyIds", UNSET))

        source = d.pop("source", UNSET)

        is_mac_hashed = d.pop("isMacHashed", UNSET)

        device_id = d.pop("deviceId", UNSET)

        coordinates = cast(list[float], d.pop("coordinates", UNSET))

        geo_coordinates = cast(list[float], d.pop("geoCoordinates", UNSET))

        confidence_factor = d.pop("confidenceFactor", UNSET)

        compute_type = d.pop("computeType", UNSET)

        _first_located_at = d.pop("firstLocatedAt", UNSET)
        first_located_at: Union[Unset, datetime.datetime]
        if isinstance(_first_located_at, Unset):
            first_located_at = UNSET
        else:
            first_located_at = isoparse(_first_located_at)

        _last_located_at = d.pop("lastLocatedAt", UNSET)
        last_located_at: Union[Unset, datetime.datetime]
        if isinstance(_last_located_at, Unset):
            last_located_at = UNSET
        else:
            last_located_at = isoparse(_last_located_at)

        changed_on = d.pop("changedOn", UNSET)

        associated = d.pop("associated", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

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

        v2_location_device = cls(
            tenant_id=tenant_id,
            mac_address=mac_address,
            device_type=device_type,
            campus_id=campus_id,
            building_id=building_id,
            floor_id=floor_id,
            lhfloor_id=lhfloor_id,
            hierarchy=hierarchy,
            location_hierarchy=location_hierarchy,
            hierarchy_ids=hierarchy_ids,
            source=source,
            is_mac_hashed=is_mac_hashed,
            device_id=device_id,
            coordinates=coordinates,
            geo_coordinates=geo_coordinates,
            confidence_factor=confidence_factor,
            compute_type=compute_type,
            first_located_at=first_located_at,
            last_located_at=last_located_at,
            changed_on=changed_on,
            associated=associated,
            manufacturer=manufacturer,
            max_detected_rssi=max_detected_rssi,
            num_detecting_aps=num_detecting_aps,
            ap_list=ap_list,
        )

        v2_location_device.additional_properties = d
        return v2_location_device

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
