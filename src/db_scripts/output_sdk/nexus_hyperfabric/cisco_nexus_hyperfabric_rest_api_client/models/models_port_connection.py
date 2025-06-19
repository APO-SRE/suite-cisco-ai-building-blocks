from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_os_type import ModelsOsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_port_endpoint import ModelsPortEndpoint


T = TypeVar("T", bound="ModelsPortConnection")


@_attrs_define
class ModelsPortConnection:
    """A Connection represents the bidirectional physical interconnection between two ports of two nodes in a fabric. The
    role of the ports in a connection will be automatically configured as `FABRIC_PORT`. Cisco Nexus Hyperfabric uses
    the connections to generate a possible Bill Of Material, cabling plan and to verify the correct implementation of
    the desired connectivity intent in a fabric.

        Attributes:
            description (Union[Unset, str]): The description is a user-defined field to store notes about the connection.
            fabric_id (Union[Unset, str]): This is a read-only field. The identifier of the fabric to which this connection
                belongs to.
            id (Union[Unset, str]): This is a read-only field. The unique identifier of the connection.
            local (Union[Unset, ModelsPortEndpoint]): PortEndpoint defines a globally unique port location or endpoint.
            os_type (Union[Unset, ModelsOsType]): OsType defines an enumeration of various device operating system types.
            pluggable (Union[Unset, str]): The type or name of the model (PID) of the pluggable cable or optic expected to
                be used for the connection.
            remote (Union[Unset, ModelsPortEndpoint]): PortEndpoint defines a globally unique port location or endpoint.
            unrecognized (Union[Unset, bool]): This is a read-only field. The flag that indicates if the remote side of the
                connection is recognized or not.
    """

    description: Union[Unset, str] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    local: Union[Unset, "ModelsPortEndpoint"] = UNSET
    os_type: Union[Unset, ModelsOsType] = UNSET
    pluggable: Union[Unset, str] = UNSET
    remote: Union[Unset, "ModelsPortEndpoint"] = UNSET
    unrecognized: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        fabric_id = self.fabric_id

        id = self.id

        local: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.local, Unset):
            local = self.local.to_dict()

        os_type: Union[Unset, str] = UNSET
        if not isinstance(self.os_type, Unset):
            os_type = self.os_type.value

        pluggable = self.pluggable

        remote: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.remote, Unset):
            remote = self.remote.to_dict()

        unrecognized = self.unrecognized

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if fabric_id is not UNSET:
            field_dict["fabricId"] = fabric_id
        if id is not UNSET:
            field_dict["id"] = id
        if local is not UNSET:
            field_dict["local"] = local
        if os_type is not UNSET:
            field_dict["osType"] = os_type
        if pluggable is not UNSET:
            field_dict["pluggable"] = pluggable
        if remote is not UNSET:
            field_dict["remote"] = remote
        if unrecognized is not UNSET:
            field_dict["unrecognized"] = unrecognized

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_port_endpoint import ModelsPortEndpoint

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        fabric_id = d.pop("fabricId", UNSET)

        id = d.pop("id", UNSET)

        _local = d.pop("local", UNSET)
        local: Union[Unset, ModelsPortEndpoint]
        if isinstance(_local, Unset):
            local = UNSET
        else:
            local = ModelsPortEndpoint.from_dict(_local)

        _os_type = d.pop("osType", UNSET)
        os_type: Union[Unset, ModelsOsType]
        if isinstance(_os_type, Unset):
            os_type = UNSET
        else:
            os_type = ModelsOsType(_os_type)

        pluggable = d.pop("pluggable", UNSET)

        _remote = d.pop("remote", UNSET)
        remote: Union[Unset, ModelsPortEndpoint]
        if isinstance(_remote, Unset):
            remote = UNSET
        else:
            remote = ModelsPortEndpoint.from_dict(_remote)

        unrecognized = d.pop("unrecognized", UNSET)

        models_port_connection = cls(
            description=description,
            fabric_id=fabric_id,
            id=id,
            local=local,
            os_type=os_type,
            pluggable=pluggable,
            remote=remote,
            unrecognized=unrecognized,
        )

        models_port_connection.additional_properties = d
        return models_port_connection

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
