import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_path_path_id import SchemaPathPathId


T = TypeVar("T", bound="SchemaPortCounters")


@_attrs_define
class SchemaPortCounters:
    """Description not available

    Attributes:
        carrier_transitions (Union[Unset, int]): Description not available
        collected_at (Union[Unset, datetime.datetime]): Description not available
        id (Union[Unset, SchemaPathPathId]): PathId identifies the specific "schema coordinates" identifier of an object
            in the schema tree.
        in_bitsps (Union[Unset, float]): bytes per second
        in_broadcast_pkts (Union[Unset, int]): Description not available
        in_discards (Union[Unset, int]): Description not available
        in_errors (Union[Unset, int]): Description not available
        in_fcs_errors (Union[Unset, int]): Description not available
        in_multicast_pkts (Union[Unset, int]): Description not available
        in_octets (Union[Unset, int]): Description not available
        in_pfc_0_pkts (Union[Unset, int]): Description not available
        in_pfc_1_pkts (Union[Unset, int]): Description not available
        in_pfc_2_pkts (Union[Unset, int]): Description not available
        in_pfc_3_pkts (Union[Unset, int]): Description not available
        in_pfc_4_pkts (Union[Unset, int]): Description not available
        in_pfc_5_pkts (Union[Unset, int]): Description not available
        in_pfc_6_pkts (Union[Unset, int]): Description not available
        in_pfc_7_pkts (Union[Unset, int]): Description not available
        in_pfc_pps (Union[Unset, float]): Aggregate packets per second over all PFC counters
        in_pkts (Union[Unset, int]): Description not available
        in_pps (Union[Unset, float]): packets per second
        in_unicast_pkts (Union[Unset, int]): Description not available
        in_unicast_pps (Union[Unset, float]): unicast packets per second
        in_unknown_protos (Union[Unset, int]): Description not available
        last_clear (Union[Unset, datetime.datetime]): Description not available
        out_bitsps (Union[Unset, float]): Description not available
        out_broadcast_pkts (Union[Unset, int]): Description not available
        out_discards (Union[Unset, int]): Description not available
        out_errors (Union[Unset, int]): Description not available
        out_multicast_pkts (Union[Unset, int]): Description not available
        out_octets (Union[Unset, int]): Description not available
        out_pfc_0_pkts (Union[Unset, int]): Description not available
        out_pfc_1_pkts (Union[Unset, int]): Description not available
        out_pfc_2_pkts (Union[Unset, int]): Description not available
        out_pfc_3_pkts (Union[Unset, int]): Description not available
        out_pfc_4_pkts (Union[Unset, int]): Description not available
        out_pfc_5_pkts (Union[Unset, int]): Description not available
        out_pfc_6_pkts (Union[Unset, int]): Description not available
        out_pfc_7_pkts (Union[Unset, int]): Description not available
        out_pfc_pps (Union[Unset, float]): Description not available
        out_pkts (Union[Unset, int]): Description not available
        out_pps (Union[Unset, float]): Description not available
        out_unicast_pkts (Union[Unset, int]): Description not available
        out_unicast_pps (Union[Unset, float]): Description not available
    """

    carrier_transitions: Union[Unset, int] = UNSET
    collected_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, "SchemaPathPathId"] = UNSET
    in_bitsps: Union[Unset, float] = UNSET
    in_broadcast_pkts: Union[Unset, int] = UNSET
    in_discards: Union[Unset, int] = UNSET
    in_errors: Union[Unset, int] = UNSET
    in_fcs_errors: Union[Unset, int] = UNSET
    in_multicast_pkts: Union[Unset, int] = UNSET
    in_octets: Union[Unset, int] = UNSET
    in_pfc_0_pkts: Union[Unset, int] = UNSET
    in_pfc_1_pkts: Union[Unset, int] = UNSET
    in_pfc_2_pkts: Union[Unset, int] = UNSET
    in_pfc_3_pkts: Union[Unset, int] = UNSET
    in_pfc_4_pkts: Union[Unset, int] = UNSET
    in_pfc_5_pkts: Union[Unset, int] = UNSET
    in_pfc_6_pkts: Union[Unset, int] = UNSET
    in_pfc_7_pkts: Union[Unset, int] = UNSET
    in_pfc_pps: Union[Unset, float] = UNSET
    in_pkts: Union[Unset, int] = UNSET
    in_pps: Union[Unset, float] = UNSET
    in_unicast_pkts: Union[Unset, int] = UNSET
    in_unicast_pps: Union[Unset, float] = UNSET
    in_unknown_protos: Union[Unset, int] = UNSET
    last_clear: Union[Unset, datetime.datetime] = UNSET
    out_bitsps: Union[Unset, float] = UNSET
    out_broadcast_pkts: Union[Unset, int] = UNSET
    out_discards: Union[Unset, int] = UNSET
    out_errors: Union[Unset, int] = UNSET
    out_multicast_pkts: Union[Unset, int] = UNSET
    out_octets: Union[Unset, int] = UNSET
    out_pfc_0_pkts: Union[Unset, int] = UNSET
    out_pfc_1_pkts: Union[Unset, int] = UNSET
    out_pfc_2_pkts: Union[Unset, int] = UNSET
    out_pfc_3_pkts: Union[Unset, int] = UNSET
    out_pfc_4_pkts: Union[Unset, int] = UNSET
    out_pfc_5_pkts: Union[Unset, int] = UNSET
    out_pfc_6_pkts: Union[Unset, int] = UNSET
    out_pfc_7_pkts: Union[Unset, int] = UNSET
    out_pfc_pps: Union[Unset, float] = UNSET
    out_pkts: Union[Unset, int] = UNSET
    out_pps: Union[Unset, float] = UNSET
    out_unicast_pkts: Union[Unset, int] = UNSET
    out_unicast_pps: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carrier_transitions = self.carrier_transitions

        collected_at: Union[Unset, str] = UNSET
        if not isinstance(self.collected_at, Unset):
            collected_at = self.collected_at.isoformat()

        id: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        in_bitsps = self.in_bitsps

        in_broadcast_pkts = self.in_broadcast_pkts

        in_discards = self.in_discards

        in_errors = self.in_errors

        in_fcs_errors = self.in_fcs_errors

        in_multicast_pkts = self.in_multicast_pkts

        in_octets = self.in_octets

        in_pfc_0_pkts = self.in_pfc_0_pkts

        in_pfc_1_pkts = self.in_pfc_1_pkts

        in_pfc_2_pkts = self.in_pfc_2_pkts

        in_pfc_3_pkts = self.in_pfc_3_pkts

        in_pfc_4_pkts = self.in_pfc_4_pkts

        in_pfc_5_pkts = self.in_pfc_5_pkts

        in_pfc_6_pkts = self.in_pfc_6_pkts

        in_pfc_7_pkts = self.in_pfc_7_pkts

        in_pfc_pps = self.in_pfc_pps

        in_pkts = self.in_pkts

        in_pps = self.in_pps

        in_unicast_pkts = self.in_unicast_pkts

        in_unicast_pps = self.in_unicast_pps

        in_unknown_protos = self.in_unknown_protos

        last_clear: Union[Unset, str] = UNSET
        if not isinstance(self.last_clear, Unset):
            last_clear = self.last_clear.isoformat()

        out_bitsps = self.out_bitsps

        out_broadcast_pkts = self.out_broadcast_pkts

        out_discards = self.out_discards

        out_errors = self.out_errors

        out_multicast_pkts = self.out_multicast_pkts

        out_octets = self.out_octets

        out_pfc_0_pkts = self.out_pfc_0_pkts

        out_pfc_1_pkts = self.out_pfc_1_pkts

        out_pfc_2_pkts = self.out_pfc_2_pkts

        out_pfc_3_pkts = self.out_pfc_3_pkts

        out_pfc_4_pkts = self.out_pfc_4_pkts

        out_pfc_5_pkts = self.out_pfc_5_pkts

        out_pfc_6_pkts = self.out_pfc_6_pkts

        out_pfc_7_pkts = self.out_pfc_7_pkts

        out_pfc_pps = self.out_pfc_pps

        out_pkts = self.out_pkts

        out_pps = self.out_pps

        out_unicast_pkts = self.out_unicast_pkts

        out_unicast_pps = self.out_unicast_pps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if carrier_transitions is not UNSET:
            field_dict["carrierTransitions"] = carrier_transitions
        if collected_at is not UNSET:
            field_dict["collectedAt"] = collected_at
        if id is not UNSET:
            field_dict["id"] = id
        if in_bitsps is not UNSET:
            field_dict["inBitsps"] = in_bitsps
        if in_broadcast_pkts is not UNSET:
            field_dict["inBroadcastPkts"] = in_broadcast_pkts
        if in_discards is not UNSET:
            field_dict["inDiscards"] = in_discards
        if in_errors is not UNSET:
            field_dict["inErrors"] = in_errors
        if in_fcs_errors is not UNSET:
            field_dict["inFcsErrors"] = in_fcs_errors
        if in_multicast_pkts is not UNSET:
            field_dict["inMulticastPkts"] = in_multicast_pkts
        if in_octets is not UNSET:
            field_dict["inOctets"] = in_octets
        if in_pfc_0_pkts is not UNSET:
            field_dict["inPfc0Pkts"] = in_pfc_0_pkts
        if in_pfc_1_pkts is not UNSET:
            field_dict["inPfc1Pkts"] = in_pfc_1_pkts
        if in_pfc_2_pkts is not UNSET:
            field_dict["inPfc2Pkts"] = in_pfc_2_pkts
        if in_pfc_3_pkts is not UNSET:
            field_dict["inPfc3Pkts"] = in_pfc_3_pkts
        if in_pfc_4_pkts is not UNSET:
            field_dict["inPfc4Pkts"] = in_pfc_4_pkts
        if in_pfc_5_pkts is not UNSET:
            field_dict["inPfc5Pkts"] = in_pfc_5_pkts
        if in_pfc_6_pkts is not UNSET:
            field_dict["inPfc6Pkts"] = in_pfc_6_pkts
        if in_pfc_7_pkts is not UNSET:
            field_dict["inPfc7Pkts"] = in_pfc_7_pkts
        if in_pfc_pps is not UNSET:
            field_dict["inPfcPps"] = in_pfc_pps
        if in_pkts is not UNSET:
            field_dict["inPkts"] = in_pkts
        if in_pps is not UNSET:
            field_dict["inPps"] = in_pps
        if in_unicast_pkts is not UNSET:
            field_dict["inUnicastPkts"] = in_unicast_pkts
        if in_unicast_pps is not UNSET:
            field_dict["inUnicastPps"] = in_unicast_pps
        if in_unknown_protos is not UNSET:
            field_dict["inUnknownProtos"] = in_unknown_protos
        if last_clear is not UNSET:
            field_dict["lastClear"] = last_clear
        if out_bitsps is not UNSET:
            field_dict["outBitsps"] = out_bitsps
        if out_broadcast_pkts is not UNSET:
            field_dict["outBroadcastPkts"] = out_broadcast_pkts
        if out_discards is not UNSET:
            field_dict["outDiscards"] = out_discards
        if out_errors is not UNSET:
            field_dict["outErrors"] = out_errors
        if out_multicast_pkts is not UNSET:
            field_dict["outMulticastPkts"] = out_multicast_pkts
        if out_octets is not UNSET:
            field_dict["outOctets"] = out_octets
        if out_pfc_0_pkts is not UNSET:
            field_dict["outPfc0Pkts"] = out_pfc_0_pkts
        if out_pfc_1_pkts is not UNSET:
            field_dict["outPfc1Pkts"] = out_pfc_1_pkts
        if out_pfc_2_pkts is not UNSET:
            field_dict["outPfc2Pkts"] = out_pfc_2_pkts
        if out_pfc_3_pkts is not UNSET:
            field_dict["outPfc3Pkts"] = out_pfc_3_pkts
        if out_pfc_4_pkts is not UNSET:
            field_dict["outPfc4Pkts"] = out_pfc_4_pkts
        if out_pfc_5_pkts is not UNSET:
            field_dict["outPfc5Pkts"] = out_pfc_5_pkts
        if out_pfc_6_pkts is not UNSET:
            field_dict["outPfc6Pkts"] = out_pfc_6_pkts
        if out_pfc_7_pkts is not UNSET:
            field_dict["outPfc7Pkts"] = out_pfc_7_pkts
        if out_pfc_pps is not UNSET:
            field_dict["outPfcPps"] = out_pfc_pps
        if out_pkts is not UNSET:
            field_dict["outPkts"] = out_pkts
        if out_pps is not UNSET:
            field_dict["outPps"] = out_pps
        if out_unicast_pkts is not UNSET:
            field_dict["outUnicastPkts"] = out_unicast_pkts
        if out_unicast_pps is not UNSET:
            field_dict["outUnicastPps"] = out_unicast_pps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_path_path_id import SchemaPathPathId

        d = dict(src_dict)
        carrier_transitions = d.pop("carrierTransitions", UNSET)

        _collected_at = d.pop("collectedAt", UNSET)
        collected_at: Union[Unset, datetime.datetime]
        if isinstance(_collected_at, Unset):
            collected_at = UNSET
        else:
            collected_at = isoparse(_collected_at)

        _id = d.pop("id", UNSET)
        id: Union[Unset, SchemaPathPathId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = SchemaPathPathId.from_dict(_id)

        in_bitsps = d.pop("inBitsps", UNSET)

        in_broadcast_pkts = d.pop("inBroadcastPkts", UNSET)

        in_discards = d.pop("inDiscards", UNSET)

        in_errors = d.pop("inErrors", UNSET)

        in_fcs_errors = d.pop("inFcsErrors", UNSET)

        in_multicast_pkts = d.pop("inMulticastPkts", UNSET)

        in_octets = d.pop("inOctets", UNSET)

        in_pfc_0_pkts = d.pop("inPfc0Pkts", UNSET)

        in_pfc_1_pkts = d.pop("inPfc1Pkts", UNSET)

        in_pfc_2_pkts = d.pop("inPfc2Pkts", UNSET)

        in_pfc_3_pkts = d.pop("inPfc3Pkts", UNSET)

        in_pfc_4_pkts = d.pop("inPfc4Pkts", UNSET)

        in_pfc_5_pkts = d.pop("inPfc5Pkts", UNSET)

        in_pfc_6_pkts = d.pop("inPfc6Pkts", UNSET)

        in_pfc_7_pkts = d.pop("inPfc7Pkts", UNSET)

        in_pfc_pps = d.pop("inPfcPps", UNSET)

        in_pkts = d.pop("inPkts", UNSET)

        in_pps = d.pop("inPps", UNSET)

        in_unicast_pkts = d.pop("inUnicastPkts", UNSET)

        in_unicast_pps = d.pop("inUnicastPps", UNSET)

        in_unknown_protos = d.pop("inUnknownProtos", UNSET)

        _last_clear = d.pop("lastClear", UNSET)
        last_clear: Union[Unset, datetime.datetime]
        if isinstance(_last_clear, Unset):
            last_clear = UNSET
        else:
            last_clear = isoparse(_last_clear)

        out_bitsps = d.pop("outBitsps", UNSET)

        out_broadcast_pkts = d.pop("outBroadcastPkts", UNSET)

        out_discards = d.pop("outDiscards", UNSET)

        out_errors = d.pop("outErrors", UNSET)

        out_multicast_pkts = d.pop("outMulticastPkts", UNSET)

        out_octets = d.pop("outOctets", UNSET)

        out_pfc_0_pkts = d.pop("outPfc0Pkts", UNSET)

        out_pfc_1_pkts = d.pop("outPfc1Pkts", UNSET)

        out_pfc_2_pkts = d.pop("outPfc2Pkts", UNSET)

        out_pfc_3_pkts = d.pop("outPfc3Pkts", UNSET)

        out_pfc_4_pkts = d.pop("outPfc4Pkts", UNSET)

        out_pfc_5_pkts = d.pop("outPfc5Pkts", UNSET)

        out_pfc_6_pkts = d.pop("outPfc6Pkts", UNSET)

        out_pfc_7_pkts = d.pop("outPfc7Pkts", UNSET)

        out_pfc_pps = d.pop("outPfcPps", UNSET)

        out_pkts = d.pop("outPkts", UNSET)

        out_pps = d.pop("outPps", UNSET)

        out_unicast_pkts = d.pop("outUnicastPkts", UNSET)

        out_unicast_pps = d.pop("outUnicastPps", UNSET)

        schema_port_counters = cls(
            carrier_transitions=carrier_transitions,
            collected_at=collected_at,
            id=id,
            in_bitsps=in_bitsps,
            in_broadcast_pkts=in_broadcast_pkts,
            in_discards=in_discards,
            in_errors=in_errors,
            in_fcs_errors=in_fcs_errors,
            in_multicast_pkts=in_multicast_pkts,
            in_octets=in_octets,
            in_pfc_0_pkts=in_pfc_0_pkts,
            in_pfc_1_pkts=in_pfc_1_pkts,
            in_pfc_2_pkts=in_pfc_2_pkts,
            in_pfc_3_pkts=in_pfc_3_pkts,
            in_pfc_4_pkts=in_pfc_4_pkts,
            in_pfc_5_pkts=in_pfc_5_pkts,
            in_pfc_6_pkts=in_pfc_6_pkts,
            in_pfc_7_pkts=in_pfc_7_pkts,
            in_pfc_pps=in_pfc_pps,
            in_pkts=in_pkts,
            in_pps=in_pps,
            in_unicast_pkts=in_unicast_pkts,
            in_unicast_pps=in_unicast_pps,
            in_unknown_protos=in_unknown_protos,
            last_clear=last_clear,
            out_bitsps=out_bitsps,
            out_broadcast_pkts=out_broadcast_pkts,
            out_discards=out_discards,
            out_errors=out_errors,
            out_multicast_pkts=out_multicast_pkts,
            out_octets=out_octets,
            out_pfc_0_pkts=out_pfc_0_pkts,
            out_pfc_1_pkts=out_pfc_1_pkts,
            out_pfc_2_pkts=out_pfc_2_pkts,
            out_pfc_3_pkts=out_pfc_3_pkts,
            out_pfc_4_pkts=out_pfc_4_pkts,
            out_pfc_5_pkts=out_pfc_5_pkts,
            out_pfc_6_pkts=out_pfc_6_pkts,
            out_pfc_7_pkts=out_pfc_7_pkts,
            out_pfc_pps=out_pfc_pps,
            out_pkts=out_pkts,
            out_pps=out_pps,
            out_unicast_pkts=out_unicast_pkts,
            out_unicast_pps=out_unicast_pps,
        )

        schema_port_counters.additional_properties = d
        return schema_port_counters

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
