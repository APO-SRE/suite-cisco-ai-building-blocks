from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.app_instances_v4_aaa_get import AppInstancesV4AaaGET


T = TypeVar("T", bound="UserPreferenceSpecV4AaaGETDisplayedAppInstances")


@_attrs_define
class UserPreferenceSpecV4AaaGETDisplayedAppInstances:
    """Application instances for which What's New already displayed"""

    additional_properties: dict[str, "AppInstancesV4AaaGET"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_instances_v4_aaa_get import AppInstancesV4AaaGET

        d = dict(src_dict)
        user_preference_spec_v4_aaa_get_displayed_app_instances = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = AppInstancesV4AaaGET.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        user_preference_spec_v4_aaa_get_displayed_app_instances.additional_properties = additional_properties
        return user_preference_spec_v4_aaa_get_displayed_app_instances

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "AppInstancesV4AaaGET":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "AppInstancesV4AaaGET") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
