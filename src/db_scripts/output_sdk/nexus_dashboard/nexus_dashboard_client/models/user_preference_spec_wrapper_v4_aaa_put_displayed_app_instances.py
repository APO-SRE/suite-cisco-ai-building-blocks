from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.app_instances_v4_aaa_put import AppInstancesV4AaaPUT


T = TypeVar("T", bound="UserPreferenceSpecWrapperV4AaaPUTDisplayedAppInstances")


@_attrs_define
class UserPreferenceSpecWrapperV4AaaPUTDisplayedAppInstances:
    """Application instances for which What's New already displayed"""

    additional_properties: dict[str, "AppInstancesV4AaaPUT"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_instances_v4_aaa_put import AppInstancesV4AaaPUT

        d = dict(src_dict)
        user_preference_spec_wrapper_v4_aaa_put_displayed_app_instances = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = AppInstancesV4AaaPUT.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        user_preference_spec_wrapper_v4_aaa_put_displayed_app_instances.additional_properties = additional_properties
        return user_preference_spec_wrapper_v4_aaa_put_displayed_app_instances

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "AppInstancesV4AaaPUT":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "AppInstancesV4AaaPUT") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
