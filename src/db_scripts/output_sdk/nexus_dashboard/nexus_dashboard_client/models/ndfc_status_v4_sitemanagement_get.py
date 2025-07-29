from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nxos_fabric_v4_sitemanagement_get import NXOSFabricV4SitemanagementGET


T = TypeVar("T", bound="NDFCStatusV4SitemanagementGET")


@_attrs_define
class NDFCStatusV4SitemanagementGET:
    """
    Attributes:
        fabric (Union[Unset, NXOSFabricV4SitemanagementGET]):
    """

    fabric: Union[Unset, "NXOSFabricV4SitemanagementGET"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fabric: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fabric, Unset):
            fabric = self.fabric.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fabric is not UNSET:
            field_dict["fabric"] = fabric

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nxos_fabric_v4_sitemanagement_get import NXOSFabricV4SitemanagementGET

        d = dict(src_dict)
        _fabric = d.pop("fabric", UNSET)
        fabric: Union[Unset, NXOSFabricV4SitemanagementGET]
        if isinstance(_fabric, Unset):
            fabric = UNSET
        else:
            fabric = NXOSFabricV4SitemanagementGET.from_dict(_fabric)

        ndfc_status_v4_sitemanagement_get = cls(
            fabric=fabric,
        )

        ndfc_status_v4_sitemanagement_get.additional_properties = d
        return ndfc_status_v4_sitemanagement_get

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
