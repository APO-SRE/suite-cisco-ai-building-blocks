from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cloud_aci_fabric_response_v4_sitemanagement_get import CloudACIFabricResponseV4SitemanagementGET


T = TypeVar("T", bound="FabricResponseV4SitemanagementGETType1")


@_attrs_define
class FabricResponseV4SitemanagementGETType1:
    """
    Attributes:
        cloud_aci (Union[Unset, list['CloudACIFabricResponseV4SitemanagementGET']]):
    """

    cloud_aci: Union[Unset, list["CloudACIFabricResponseV4SitemanagementGET"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_aci: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cloud_aci, Unset):
            cloud_aci = []
            for cloud_aci_item_data in self.cloud_aci:
                cloud_aci_item = cloud_aci_item_data.to_dict()
                cloud_aci.append(cloud_aci_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloud_aci is not UNSET:
            field_dict["CloudACI"] = cloud_aci

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cloud_aci_fabric_response_v4_sitemanagement_get import CloudACIFabricResponseV4SitemanagementGET

        d = dict(src_dict)
        cloud_aci = []
        _cloud_aci = d.pop("CloudACI", UNSET)
        for cloud_aci_item_data in _cloud_aci or []:
            cloud_aci_item = CloudACIFabricResponseV4SitemanagementGET.from_dict(cloud_aci_item_data)

            cloud_aci.append(cloud_aci_item)

        fabric_response_v4_sitemanagement_get_type_1 = cls(
            cloud_aci=cloud_aci,
        )

        fabric_response_v4_sitemanagement_get_type_1.additional_properties = d
        return fabric_response_v4_sitemanagement_get_type_1

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
