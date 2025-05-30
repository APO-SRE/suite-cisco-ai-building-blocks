from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_basic_counters import SchemaBasicCounters
    from ..models.schema_dac_counters import SchemaDacCounters
    from ..models.schema_port_counters import SchemaPortCounters
    from ..models.schema_vlan_counters import SchemaVlanCounters


T = TypeVar("T", bound="StateCounter")


@_attrs_define
class StateCounter:
    """Description not available

    Attributes:
        basic (Union[Unset, SchemaBasicCounters]): Universal counters for L2/L3 entities
        dac (Union[Unset, SchemaDacCounters]): Description not available
        port (Union[Unset, SchemaPortCounters]): Description not available
        vlans (Union[Unset, SchemaVlanCounters]): Description not available
    """

    basic: Union[Unset, "SchemaBasicCounters"] = UNSET
    dac: Union[Unset, "SchemaDacCounters"] = UNSET
    port: Union[Unset, "SchemaPortCounters"] = UNSET
    vlans: Union[Unset, "SchemaVlanCounters"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        basic: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.basic, Unset):
            basic = self.basic.to_dict()

        dac: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dac, Unset):
            dac = self.dac.to_dict()

        port: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.port, Unset):
            port = self.port.to_dict()

        vlans: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vlans, Unset):
            vlans = self.vlans.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if basic is not UNSET:
            field_dict["basic"] = basic
        if dac is not UNSET:
            field_dict["dac"] = dac
        if port is not UNSET:
            field_dict["port"] = port
        if vlans is not UNSET:
            field_dict["vlans"] = vlans

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_basic_counters import SchemaBasicCounters
        from ..models.schema_dac_counters import SchemaDacCounters
        from ..models.schema_port_counters import SchemaPortCounters
        from ..models.schema_vlan_counters import SchemaVlanCounters

        d = dict(src_dict)
        _basic = d.pop("basic", UNSET)
        basic: Union[Unset, SchemaBasicCounters]
        if isinstance(_basic, Unset):
            basic = UNSET
        else:
            basic = SchemaBasicCounters.from_dict(_basic)

        _dac = d.pop("dac", UNSET)
        dac: Union[Unset, SchemaDacCounters]
        if isinstance(_dac, Unset):
            dac = UNSET
        else:
            dac = SchemaDacCounters.from_dict(_dac)

        _port = d.pop("port", UNSET)
        port: Union[Unset, SchemaPortCounters]
        if isinstance(_port, Unset):
            port = UNSET
        else:
            port = SchemaPortCounters.from_dict(_port)

        _vlans = d.pop("vlans", UNSET)
        vlans: Union[Unset, SchemaVlanCounters]
        if isinstance(_vlans, Unset):
            vlans = UNSET
        else:
            vlans = SchemaVlanCounters.from_dict(_vlans)

        state_counter = cls(
            basic=basic,
            dac=dac,
            port=port,
            vlans=vlans,
        )

        state_counter.additional_properties = d
        return state_counter

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
