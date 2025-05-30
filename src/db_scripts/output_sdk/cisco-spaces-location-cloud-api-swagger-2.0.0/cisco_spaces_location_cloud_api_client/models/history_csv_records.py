from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HistoryCsvRecords")


@_attrs_define
class HistoryCsvRecords:
    """
    Attributes:
        sample_response (Union[Unset, str]):  Example: ['tenantid,macaddress,devicetype,campusid,buildingid,floorid,floo
            rhierarchy,coordinatex,coordinatey,sourcetimestamp,manufacturer,associated,ssid,username,associatedapmac,compute
            type,sourcetype,hierarchy_id,ipaddress', '51111,4c:aa:d6:af:aa:ac,CLIENT,f7dcaab0-26aa-4a70-8aa7-
            7dec1aa7c603,d2aa932f-aebe-44aa-92aa-297aaa37aac1,316aa6e6-faa8-43a7-aa1d-c1aa7c40aa9b,SS->SS1->Level
            1,116.7,321.3,1705435087291,Esif
            Inc.,true,Fort,,fa:da:aa:a7:a6:20,RSSI,Compute,5d474aaa-8883-44ab-90bb-f321daaa1568', '51111,4c:eb:aa:af:a0:1c,C
            LIENT,f7dcaab0-2aa1-4a70-aa37-7dec1bc7aa03,daa0932f-aeaa-441e-92aa-2aaa85137c3c1,316aa6e6-f848-4aa7-aa1d-
            c13f7caa8b9b,SS->SS1->Level 1,116.7,321.3,1705435087291,Esif
            Inc.,true,Fort,,f4:db:e6:a7:aa:aa,RSSI,Compute,aa474c3a-8883-44ab-90bb-f321daa81568'].
        tenant_id (Union[Unset, Any]):  Example: Represents account unique identifier..
        mac_address (Union[Unset, Any]):  Example: Represents Device mac..
        device_type (Union[Unset, Any]):  Example: Represents type of a device. Possible types are CLIENT, TAG, BLE_TAG,
            ROGUE_AP, ROGUE_CLIENT and INTERFERER..
        campus_id (Union[Unset, Any]):  Example: Represents campus where device is located..
        floor_id (Union[Unset, Any]):  Example: Represents floor where device is located..
        floor_hierarchy (Union[Unset, Any]):  Example: Hierarchy of the device starting from campus, building, floor and
            zone. We support single zone in the hierarchy when the device is detected in multiple zones..
        coordinatex (Union[Unset, Any]):  Example: x coordinate of the device..
        coordinatey (Union[Unset, Any]):  Example: y coordinate of the device.
        sourcetimestamp (Union[Unset, Any]):  Example: Timestamp when the device is processed by Location Engine. For
            e.g. when the location is computed..
        maxdetectedapmac (Union[Unset, Any]):  Example: Represents AP mac which provides max RSSI in the RSSI probe
            packet..
        maxdetectedband (Union[Unset, Any]):  Example: Represents AP band which provides max RSSI in the RSSI probe
            packet..
        detectingcontrollers (Union[Unset, Any]):  Example: Controller reporting this device..
        firstactiveat (Union[Unset, Any]):  Example: When this device is first seen active in the network..
        locatedsinceactivecount (Union[Unset, Any]):  Example: This refers to how many times this device has location
            computed after its active..
        changedon (Union[Unset, Any]):  Example: History database record insertion time..
        manufacturer (Union[Unset, Any]):  Example: Manufacturer of the device..
        associated (Union[Unset, Any]):  Example: Represents IEEE 802.11 packet status, applicable for Clients when they
            connect to WIFI network..
        maxdetectedrssi (Union[Unset, Any]):  Example: Represents max RSSI in the RSSI probe packet..
        ssid (Union[Unset, Any]):  Example: Represents wireless network device is connected to..
        username (Union[Unset, Any]):  Example: Represents device username used for connecting to SSID..
        associatedapmac (Union[Unset, Any]):  Example: Represents device associated AP after connecting to SSID..
        associatedaprssi (Union[Unset, Any]):  Example: Represents associated AP RSSI in the probe packet..
        maxdetectedslot (Union[Unset, Any]):  Example: Represents max RSSI is reported from which AP slot..
        ipaddress (Union[Unset, Any]):  Example: Represents device IP address..
        staticdevice (Union[Unset, Any]):  Example: Represents whether device is marked as static device..
        recordtype (Union[Unset, Any]):  Example: For internal use..
        computetype (Union[Unset, Any]):  Example: Represents device location done on which dataset. Possible values
            are: 1.RSSI (1) - RSSI probe packets are reported by non-fast locate aps on NMSP channel  2.FASTLOCATE-RSSI (2)
            - Fast locate enabled Aps have contributed to send RSSI probe packets on UDP channel  3.AoA (3) - Reported
            Hyperlocation data  4. Associated-AP (8) - When device location is done using Associated AP location on the map
            .
        source (Union[Unset, Any]):  Example: Represents device location is done on Cloud or CMX tethered. Possible
            values are: 1. Compute (1) - for cloud location  2. Notification (2) - for cmx tethered  3. Meraki (3)  - for
            Meraki devices.
        machashed (Union[Unset, Any]):  Example: Represents whether the device mac is hashed from Connector..
        policyname (Union[Unset, Any]):  Example: For internal use..
        udid (Union[Unset, Any]):  Example: For internal use..
        hierarchy_id (Union[Unset, Any]):  Example: For internal use..
    """

    sample_response: Union[Unset, str] = UNSET
    tenant_id: Union[Unset, Any] = UNSET
    mac_address: Union[Unset, Any] = UNSET
    device_type: Union[Unset, Any] = UNSET
    campus_id: Union[Unset, Any] = UNSET
    floor_id: Union[Unset, Any] = UNSET
    floor_hierarchy: Union[Unset, Any] = UNSET
    coordinatex: Union[Unset, Any] = UNSET
    coordinatey: Union[Unset, Any] = UNSET
    sourcetimestamp: Union[Unset, Any] = UNSET
    maxdetectedapmac: Union[Unset, Any] = UNSET
    maxdetectedband: Union[Unset, Any] = UNSET
    detectingcontrollers: Union[Unset, Any] = UNSET
    firstactiveat: Union[Unset, Any] = UNSET
    locatedsinceactivecount: Union[Unset, Any] = UNSET
    changedon: Union[Unset, Any] = UNSET
    manufacturer: Union[Unset, Any] = UNSET
    associated: Union[Unset, Any] = UNSET
    maxdetectedrssi: Union[Unset, Any] = UNSET
    ssid: Union[Unset, Any] = UNSET
    username: Union[Unset, Any] = UNSET
    associatedapmac: Union[Unset, Any] = UNSET
    associatedaprssi: Union[Unset, Any] = UNSET
    maxdetectedslot: Union[Unset, Any] = UNSET
    ipaddress: Union[Unset, Any] = UNSET
    staticdevice: Union[Unset, Any] = UNSET
    recordtype: Union[Unset, Any] = UNSET
    computetype: Union[Unset, Any] = UNSET
    source: Union[Unset, Any] = UNSET
    machashed: Union[Unset, Any] = UNSET
    policyname: Union[Unset, Any] = UNSET
    udid: Union[Unset, Any] = UNSET
    hierarchy_id: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sample_response = self.sample_response

        tenant_id = self.tenant_id

        mac_address = self.mac_address

        device_type = self.device_type

        campus_id = self.campus_id

        floor_id = self.floor_id

        floor_hierarchy = self.floor_hierarchy

        coordinatex = self.coordinatex

        coordinatey = self.coordinatey

        sourcetimestamp = self.sourcetimestamp

        maxdetectedapmac = self.maxdetectedapmac

        maxdetectedband = self.maxdetectedband

        detectingcontrollers = self.detectingcontrollers

        firstactiveat = self.firstactiveat

        locatedsinceactivecount = self.locatedsinceactivecount

        changedon = self.changedon

        manufacturer = self.manufacturer

        associated = self.associated

        maxdetectedrssi = self.maxdetectedrssi

        ssid = self.ssid

        username = self.username

        associatedapmac = self.associatedapmac

        associatedaprssi = self.associatedaprssi

        maxdetectedslot = self.maxdetectedslot

        ipaddress = self.ipaddress

        staticdevice = self.staticdevice

        recordtype = self.recordtype

        computetype = self.computetype

        source = self.source

        machashed = self.machashed

        policyname = self.policyname

        udid = self.udid

        hierarchy_id = self.hierarchy_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sample_response is not UNSET:
            field_dict["Sample Response"] = sample_response
        if tenant_id is not UNSET:
            field_dict["tenantId "] = tenant_id
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if campus_id is not UNSET:
            field_dict["campusId"] = campus_id
        if floor_id is not UNSET:
            field_dict["floorId"] = floor_id
        if floor_hierarchy is not UNSET:
            field_dict["floorHierarchy"] = floor_hierarchy
        if coordinatex is not UNSET:
            field_dict["coordinatex"] = coordinatex
        if coordinatey is not UNSET:
            field_dict["coordinatey"] = coordinatey
        if sourcetimestamp is not UNSET:
            field_dict["sourcetimestamp "] = sourcetimestamp
        if maxdetectedapmac is not UNSET:
            field_dict["maxdetectedapmac"] = maxdetectedapmac
        if maxdetectedband is not UNSET:
            field_dict["maxdetectedband"] = maxdetectedband
        if detectingcontrollers is not UNSET:
            field_dict["detectingcontrollers"] = detectingcontrollers
        if firstactiveat is not UNSET:
            field_dict["firstactiveat"] = firstactiveat
        if locatedsinceactivecount is not UNSET:
            field_dict["locatedsinceactivecount"] = locatedsinceactivecount
        if changedon is not UNSET:
            field_dict["changedon"] = changedon
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if associated is not UNSET:
            field_dict["associated"] = associated
        if maxdetectedrssi is not UNSET:
            field_dict["maxdetectedrssi"] = maxdetectedrssi
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if username is not UNSET:
            field_dict["username"] = username
        if associatedapmac is not UNSET:
            field_dict["associatedapmac"] = associatedapmac
        if associatedaprssi is not UNSET:
            field_dict["associatedaprssi"] = associatedaprssi
        if maxdetectedslot is not UNSET:
            field_dict["maxdetectedslot"] = maxdetectedslot
        if ipaddress is not UNSET:
            field_dict["ipaddress"] = ipaddress
        if staticdevice is not UNSET:
            field_dict["staticdevice"] = staticdevice
        if recordtype is not UNSET:
            field_dict["recordtype"] = recordtype
        if computetype is not UNSET:
            field_dict["computetype"] = computetype
        if source is not UNSET:
            field_dict["source"] = source
        if machashed is not UNSET:
            field_dict["machashed "] = machashed
        if policyname is not UNSET:
            field_dict["policyname"] = policyname
        if udid is not UNSET:
            field_dict["udid"] = udid
        if hierarchy_id is not UNSET:
            field_dict["hierarchy_id"] = hierarchy_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sample_response = d.pop("Sample Response", UNSET)

        tenant_id = d.pop("tenantId ", UNSET)

        mac_address = d.pop("macAddress", UNSET)

        device_type = d.pop("deviceType", UNSET)

        campus_id = d.pop("campusId", UNSET)

        floor_id = d.pop("floorId", UNSET)

        floor_hierarchy = d.pop("floorHierarchy", UNSET)

        coordinatex = d.pop("coordinatex", UNSET)

        coordinatey = d.pop("coordinatey", UNSET)

        sourcetimestamp = d.pop("sourcetimestamp ", UNSET)

        maxdetectedapmac = d.pop("maxdetectedapmac", UNSET)

        maxdetectedband = d.pop("maxdetectedband", UNSET)

        detectingcontrollers = d.pop("detectingcontrollers", UNSET)

        firstactiveat = d.pop("firstactiveat", UNSET)

        locatedsinceactivecount = d.pop("locatedsinceactivecount", UNSET)

        changedon = d.pop("changedon", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        associated = d.pop("associated", UNSET)

        maxdetectedrssi = d.pop("maxdetectedrssi", UNSET)

        ssid = d.pop("ssid", UNSET)

        username = d.pop("username", UNSET)

        associatedapmac = d.pop("associatedapmac", UNSET)

        associatedaprssi = d.pop("associatedaprssi", UNSET)

        maxdetectedslot = d.pop("maxdetectedslot", UNSET)

        ipaddress = d.pop("ipaddress", UNSET)

        staticdevice = d.pop("staticdevice", UNSET)

        recordtype = d.pop("recordtype", UNSET)

        computetype = d.pop("computetype", UNSET)

        source = d.pop("source", UNSET)

        machashed = d.pop("machashed ", UNSET)

        policyname = d.pop("policyname", UNSET)

        udid = d.pop("udid", UNSET)

        hierarchy_id = d.pop("hierarchy_id", UNSET)

        history_csv_records = cls(
            sample_response=sample_response,
            tenant_id=tenant_id,
            mac_address=mac_address,
            device_type=device_type,
            campus_id=campus_id,
            floor_id=floor_id,
            floor_hierarchy=floor_hierarchy,
            coordinatex=coordinatex,
            coordinatey=coordinatey,
            sourcetimestamp=sourcetimestamp,
            maxdetectedapmac=maxdetectedapmac,
            maxdetectedband=maxdetectedband,
            detectingcontrollers=detectingcontrollers,
            firstactiveat=firstactiveat,
            locatedsinceactivecount=locatedsinceactivecount,
            changedon=changedon,
            manufacturer=manufacturer,
            associated=associated,
            maxdetectedrssi=maxdetectedrssi,
            ssid=ssid,
            username=username,
            associatedapmac=associatedapmac,
            associatedaprssi=associatedaprssi,
            maxdetectedslot=maxdetectedslot,
            ipaddress=ipaddress,
            staticdevice=staticdevice,
            recordtype=recordtype,
            computetype=computetype,
            source=source,
            machashed=machashed,
            policyname=policyname,
            udid=udid,
            hierarchy_id=hierarchy_id,
        )

        history_csv_records.additional_properties = d
        return history_csv_records

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
