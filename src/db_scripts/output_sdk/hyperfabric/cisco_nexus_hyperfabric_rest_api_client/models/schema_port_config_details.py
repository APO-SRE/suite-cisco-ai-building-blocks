import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.models_admin_state import ModelsAdminState
from ..models.models_port_role import ModelsPortRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaPortConfigDetails")


@_attrs_define
class SchemaPortConfigDetails:
    """Description not available

    Attributes:
        admin_state (Union[Unset, ModelsAdminState]): AdminState defines an enumeration for object's administrative
            states.
        break_out (Union[Unset, bool]): Description not available
        device_id (Union[Unset, str]): Description not available
        modified_at (Union[Unset, datetime.datetime]): Description not available
        mtu (Union[Unset, int]): Description not available
        port_index (Union[Unset, int]): Description not available
        port_name (Union[Unset, str]): Description not available
        port_role (Union[Unset, ModelsPortRole]): PortType enumerates different physical port types.
        target_device_id (Union[Unset, str]): Description not available
        target_port_name (Union[Unset, str]): Description not available
    """

    admin_state: Union[Unset, ModelsAdminState] = UNSET
    break_out: Union[Unset, bool] = UNSET
    device_id: Union[Unset, str] = UNSET
    modified_at: Union[Unset, datetime.datetime] = UNSET
    mtu: Union[Unset, int] = UNSET
    port_index: Union[Unset, int] = UNSET
    port_name: Union[Unset, str] = UNSET
    port_role: Union[Unset, ModelsPortRole] = UNSET
    target_device_id: Union[Unset, str] = UNSET
    target_port_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin_state: Union[Unset, str] = UNSET
        if not isinstance(self.admin_state, Unset):
            admin_state = self.admin_state.value

        break_out = self.break_out

        device_id = self.device_id

        modified_at: Union[Unset, str] = UNSET
        if not isinstance(self.modified_at, Unset):
            modified_at = self.modified_at.isoformat()

        mtu = self.mtu

        port_index = self.port_index

        port_name = self.port_name

        port_role: Union[Unset, str] = UNSET
        if not isinstance(self.port_role, Unset):
            port_role = self.port_role.value

        target_device_id = self.target_device_id

        target_port_name = self.target_port_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin_state is not UNSET:
            field_dict["adminState"] = admin_state
        if break_out is not UNSET:
            field_dict["breakOut"] = break_out
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if port_index is not UNSET:
            field_dict["portIndex"] = port_index
        if port_name is not UNSET:
            field_dict["portName"] = port_name
        if port_role is not UNSET:
            field_dict["portRole"] = port_role
        if target_device_id is not UNSET:
            field_dict["targetDeviceId"] = target_device_id
        if target_port_name is not UNSET:
            field_dict["targetPortName"] = target_port_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _admin_state = d.pop("adminState", UNSET)
        admin_state: Union[Unset, ModelsAdminState]
        if isinstance(_admin_state, Unset):
            admin_state = UNSET
        else:
            admin_state = ModelsAdminState(_admin_state)

        break_out = d.pop("breakOut", UNSET)

        device_id = d.pop("deviceId", UNSET)

        _modified_at = d.pop("modifiedAt", UNSET)
        modified_at: Union[Unset, datetime.datetime]
        if isinstance(_modified_at, Unset):
            modified_at = UNSET
        else:
            modified_at = isoparse(_modified_at)

        mtu = d.pop("mtu", UNSET)

        port_index = d.pop("portIndex", UNSET)

        port_name = d.pop("portName", UNSET)

        _port_role = d.pop("portRole", UNSET)
        port_role: Union[Unset, ModelsPortRole]
        if isinstance(_port_role, Unset):
            port_role = UNSET
        else:
            port_role = ModelsPortRole(_port_role)

        target_device_id = d.pop("targetDeviceId", UNSET)

        target_port_name = d.pop("targetPortName", UNSET)

        schema_port_config_details = cls(
            admin_state=admin_state,
            break_out=break_out,
            device_id=device_id,
            modified_at=modified_at,
            mtu=mtu,
            port_index=port_index,
            port_name=port_name,
            port_role=port_role,
            target_device_id=target_device_id,
            target_port_name=target_port_name,
        )

        schema_port_config_details.additional_properties = d
        return schema_port_config_details

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
