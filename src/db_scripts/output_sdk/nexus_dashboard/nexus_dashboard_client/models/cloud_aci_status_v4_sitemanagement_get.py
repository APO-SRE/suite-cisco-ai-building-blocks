from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudACIStatusV4SitemanagementGET")


@_attrs_define
class CloudACIStatusV4SitemanagementGET:
    """
    Attributes:
        app_user_name (Union[Unset, str]): appuser created in the ACI/cloudACI controller
        provider (Union[Unset, str]): cloudACI provider name
        region_count (Union[Unset, str]): cloudACI region count
        region_name (Union[Unset, str]): cloudACI region name
        router_count (Union[Unset, str]): cloudACI router count
        virtual_network_count (Union[Unset, str]): cloudACI virtual network count
        vpc_count (Union[Unset, str]): cloudACI vpc count
    """

    app_user_name: Union[Unset, str] = UNSET
    provider: Union[Unset, str] = UNSET
    region_count: Union[Unset, str] = UNSET
    region_name: Union[Unset, str] = UNSET
    router_count: Union[Unset, str] = UNSET
    virtual_network_count: Union[Unset, str] = UNSET
    vpc_count: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_user_name = self.app_user_name

        provider = self.provider

        region_count = self.region_count

        region_name = self.region_name

        router_count = self.router_count

        virtual_network_count = self.virtual_network_count

        vpc_count = self.vpc_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_user_name is not UNSET:
            field_dict["appUserName"] = app_user_name
        if provider is not UNSET:
            field_dict["provider"] = provider
        if region_count is not UNSET:
            field_dict["regionCount"] = region_count
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if router_count is not UNSET:
            field_dict["routerCount"] = router_count
        if virtual_network_count is not UNSET:
            field_dict["virtualNetworkCount"] = virtual_network_count
        if vpc_count is not UNSET:
            field_dict["vpcCount"] = vpc_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_user_name = d.pop("appUserName", UNSET)

        provider = d.pop("provider", UNSET)

        region_count = d.pop("regionCount", UNSET)

        region_name = d.pop("regionName", UNSET)

        router_count = d.pop("routerCount", UNSET)

        virtual_network_count = d.pop("virtualNetworkCount", UNSET)

        vpc_count = d.pop("vpcCount", UNSET)

        cloud_aci_status_v4_sitemanagement_get = cls(
            app_user_name=app_user_name,
            provider=provider,
            region_count=region_count,
            region_name=region_name,
            router_count=router_count,
            virtual_network_count=virtual_network_count,
            vpc_count=vpc_count,
        )

        cloud_aci_status_v4_sitemanagement_get.additional_properties = d
        return cloud_aci_status_v4_sitemanagement_get

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
