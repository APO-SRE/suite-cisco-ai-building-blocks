from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_vlan_member import ModelsVlanMember


T = TypeVar("T", bound="ConfigFabricVniMembersResponse")


@_attrs_define
class ConfigFabricVniMembersResponse:
    """Description not available

    Attributes:
        members (Union[Unset, list['ModelsVlanMember']]): Description not available
    """

    members: Union[Unset, list["ModelsVlanMember"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        members: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_vlan_member import ModelsVlanMember

        d = dict(src_dict)
        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in _members or []:
            members_item = ModelsVlanMember.from_dict(members_item_data)

            members.append(members_item)

        config_fabric_vni_members_response = cls(
            members=members,
        )

        config_fabric_vni_members_response.additional_properties = d
        return config_fabric_vni_members_response

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
