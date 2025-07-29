from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aci_fabric_response_v4_sitemanagement_post import ACIFabricResponseV4SitemanagementPOST


T = TypeVar("T", bound="FabricResponseV4SitemanagementPOSTType0")


@_attrs_define
class FabricResponseV4SitemanagementPOSTType0:
    """
    Attributes:
        aci (Union[Unset, list['ACIFabricResponseV4SitemanagementPOST']]):
    """

    aci: Union[Unset, list["ACIFabricResponseV4SitemanagementPOST"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aci: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.aci, Unset):
            aci = []
            for aci_item_data in self.aci:
                aci_item = aci_item_data.to_dict()
                aci.append(aci_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aci is not UNSET:
            field_dict["aci"] = aci

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aci_fabric_response_v4_sitemanagement_post import ACIFabricResponseV4SitemanagementPOST

        d = dict(src_dict)
        aci = []
        _aci = d.pop("aci", UNSET)
        for aci_item_data in _aci or []:
            aci_item = ACIFabricResponseV4SitemanagementPOST.from_dict(aci_item_data)

            aci.append(aci_item)

        fabric_response_v4_sitemanagement_post_type_0 = cls(
            aci=aci,
        )

        fabric_response_v4_sitemanagement_post_type_0.additional_properties = d
        return fabric_response_v4_sitemanagement_post_type_0

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
