from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_preference_spec_wrapper_v4_aaa_put_custom_preferences import (
        UserPreferenceSpecWrapperV4AaaPUTCustomPreferences,
    )
    from ..models.user_preference_spec_wrapper_v4_aaa_put_displayed_app_instances import (
        UserPreferenceSpecWrapperV4AaaPUTDisplayedAppInstances,
    )


T = TypeVar("T", bound="UserPreferenceSpecWrapperV4AaaPUT")


@_attrs_define
class UserPreferenceSpecWrapperV4AaaPUT:
    """
    Attributes:
        custom_preferences (Union[Unset, UserPreferenceSpecWrapperV4AaaPUTCustomPreferences]): Custom user preferences
            fields
        displayed_app_instances (Union[Unset, UserPreferenceSpecWrapperV4AaaPUTDisplayedAppInstances]): Application
            instances for which What's New already displayed
        last_logged_in_version (Union[Unset, str]): Last logged in version of ND
        login_id (Union[Unset, str]): User login ID
        show_welcome_screen (Union[Unset, bool]): Option to show welcome screen on login
        ui_idle_timeout_seconds (Union[Unset, int]): UI idle timeout in seconds
    """

    custom_preferences: Union[Unset, "UserPreferenceSpecWrapperV4AaaPUTCustomPreferences"] = UNSET
    displayed_app_instances: Union[Unset, "UserPreferenceSpecWrapperV4AaaPUTDisplayedAppInstances"] = UNSET
    last_logged_in_version: Union[Unset, str] = UNSET
    login_id: Union[Unset, str] = UNSET
    show_welcome_screen: Union[Unset, bool] = UNSET
    ui_idle_timeout_seconds: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_preferences: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_preferences, Unset):
            custom_preferences = self.custom_preferences.to_dict()

        displayed_app_instances: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.displayed_app_instances, Unset):
            displayed_app_instances = self.displayed_app_instances.to_dict()

        last_logged_in_version = self.last_logged_in_version

        login_id = self.login_id

        show_welcome_screen = self.show_welcome_screen

        ui_idle_timeout_seconds = self.ui_idle_timeout_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_preferences is not UNSET:
            field_dict["customPreferences"] = custom_preferences
        if displayed_app_instances is not UNSET:
            field_dict["displayedAppInstances"] = displayed_app_instances
        if last_logged_in_version is not UNSET:
            field_dict["lastLoggedInVersion"] = last_logged_in_version
        if login_id is not UNSET:
            field_dict["loginID"] = login_id
        if show_welcome_screen is not UNSET:
            field_dict["showWelcomeScreen"] = show_welcome_screen
        if ui_idle_timeout_seconds is not UNSET:
            field_dict["uiIdleTimeoutSeconds"] = ui_idle_timeout_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_preference_spec_wrapper_v4_aaa_put_custom_preferences import (
            UserPreferenceSpecWrapperV4AaaPUTCustomPreferences,
        )
        from ..models.user_preference_spec_wrapper_v4_aaa_put_displayed_app_instances import (
            UserPreferenceSpecWrapperV4AaaPUTDisplayedAppInstances,
        )

        d = dict(src_dict)
        _custom_preferences = d.pop("customPreferences", UNSET)
        custom_preferences: Union[Unset, UserPreferenceSpecWrapperV4AaaPUTCustomPreferences]
        if isinstance(_custom_preferences, Unset):
            custom_preferences = UNSET
        else:
            custom_preferences = UserPreferenceSpecWrapperV4AaaPUTCustomPreferences.from_dict(_custom_preferences)

        _displayed_app_instances = d.pop("displayedAppInstances", UNSET)
        displayed_app_instances: Union[Unset, UserPreferenceSpecWrapperV4AaaPUTDisplayedAppInstances]
        if isinstance(_displayed_app_instances, Unset):
            displayed_app_instances = UNSET
        else:
            displayed_app_instances = UserPreferenceSpecWrapperV4AaaPUTDisplayedAppInstances.from_dict(
                _displayed_app_instances
            )

        last_logged_in_version = d.pop("lastLoggedInVersion", UNSET)

        login_id = d.pop("loginID", UNSET)

        show_welcome_screen = d.pop("showWelcomeScreen", UNSET)

        ui_idle_timeout_seconds = d.pop("uiIdleTimeoutSeconds", UNSET)

        user_preference_spec_wrapper_v4_aaa_put = cls(
            custom_preferences=custom_preferences,
            displayed_app_instances=displayed_app_instances,
            last_logged_in_version=last_logged_in_version,
            login_id=login_id,
            show_welcome_screen=show_welcome_screen,
            ui_idle_timeout_seconds=ui_idle_timeout_seconds,
        )

        user_preference_spec_wrapper_v4_aaa_put.additional_properties = d
        return user_preference_spec_wrapper_v4_aaa_put

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
