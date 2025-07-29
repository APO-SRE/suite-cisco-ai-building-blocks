from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ndfc_fabric_response_v4_sitemanagement_post import NDFCFabricResponseV4SitemanagementPOST


T = TypeVar("T", bound="FabricResponseV4SitemanagementPOSTType3")


@_attrs_define
class FabricResponseV4SitemanagementPOSTType3:
    """
    Attributes:
        ndfc (Union[Unset, list['NDFCFabricResponseV4SitemanagementPOST']]):
    """

    ndfc: Union[Unset, list["NDFCFabricResponseV4SitemanagementPOST"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ndfc: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ndfc, Unset):
            ndfc = []
            for ndfc_item_data in self.ndfc:
                ndfc_item = ndfc_item_data.to_dict()
                ndfc.append(ndfc_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ndfc is not UNSET:
            field_dict["ndfc"] = ndfc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ndfc_fabric_response_v4_sitemanagement_post import NDFCFabricResponseV4SitemanagementPOST

        d = dict(src_dict)
        ndfc = []
        _ndfc = d.pop("ndfc", UNSET)
        for ndfc_item_data in _ndfc or []:
            ndfc_item = NDFCFabricResponseV4SitemanagementPOST.from_dict(ndfc_item_data)

            ndfc.append(ndfc_item)

        fabric_response_v4_sitemanagement_post_type_3 = cls(
            ndfc=ndfc,
        )

        fabric_response_v4_sitemanagement_post_type_3.additional_properties = d
        return fabric_response_v4_sitemanagement_post_type_3

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
