from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ACIStatusV4SitemanagementGET")


@_attrs_define
class ACIStatusV4SitemanagementGET:
    """
    Attributes:
        app_user_name (Union[Unset, str]): appuser created in the ACI/cloudACI controller
    """

    app_user_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_user_name = self.app_user_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_user_name is not UNSET:
            field_dict["appUserName"] = app_user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_user_name = d.pop("appUserName", UNSET)

        aci_status_v4_sitemanagement_get = cls(
            app_user_name=app_user_name,
        )

        aci_status_v4_sitemanagement_get.additional_properties = d
        return aci_status_v4_sitemanagement_get

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
