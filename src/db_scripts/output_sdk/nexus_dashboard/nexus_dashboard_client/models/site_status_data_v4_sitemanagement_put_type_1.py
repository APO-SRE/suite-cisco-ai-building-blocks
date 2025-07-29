from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cloud_aci_status_v4_sitemanagement_put import CloudACIStatusV4SitemanagementPUT


T = TypeVar("T", bound="SiteStatusDataV4SitemanagementPUTType1")


@_attrs_define
class SiteStatusDataV4SitemanagementPUTType1:
    """
    Attributes:
        cloud_aci (Union[Unset, CloudACIStatusV4SitemanagementPUT]):
    """

    cloud_aci: Union[Unset, "CloudACIStatusV4SitemanagementPUT"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_aci: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cloud_aci, Unset):
            cloud_aci = self.cloud_aci.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloud_aci is not UNSET:
            field_dict["CloudACI"] = cloud_aci

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cloud_aci_status_v4_sitemanagement_put import CloudACIStatusV4SitemanagementPUT

        d = dict(src_dict)
        _cloud_aci = d.pop("CloudACI", UNSET)
        cloud_aci: Union[Unset, CloudACIStatusV4SitemanagementPUT]
        if isinstance(_cloud_aci, Unset):
            cloud_aci = UNSET
        else:
            cloud_aci = CloudACIStatusV4SitemanagementPUT.from_dict(_cloud_aci)

        site_status_data_v4_sitemanagement_put_type_1 = cls(
            cloud_aci=cloud_aci,
        )

        site_status_data_v4_sitemanagement_put_type_1.additional_properties = d
        return site_status_data_v4_sitemanagement_put_type_1

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
