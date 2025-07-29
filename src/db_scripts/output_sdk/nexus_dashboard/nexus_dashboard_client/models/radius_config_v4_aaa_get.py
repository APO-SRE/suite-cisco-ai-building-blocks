from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.radius_config_v4_aaa_get_providers import RADIUSConfigV4AaaGETProviders


T = TypeVar("T", bound="RADIUSConfigV4AaaGET")


@_attrs_define
class RADIUSConfigV4AaaGET:
    """
    Attributes:
        providers (Union[Unset, RADIUSConfigV4AaaGETProviders]): RADIUS login domain configuration
    """

    providers: Union[Unset, "RADIUSConfigV4AaaGETProviders"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        providers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.providers, Unset):
            providers = self.providers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if providers is not UNSET:
            field_dict["providers"] = providers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.radius_config_v4_aaa_get_providers import RADIUSConfigV4AaaGETProviders

        d = dict(src_dict)
        _providers = d.pop("providers", UNSET)
        providers: Union[Unset, RADIUSConfigV4AaaGETProviders]
        if isinstance(_providers, Unset):
            providers = UNSET
        else:
            providers = RADIUSConfigV4AaaGETProviders.from_dict(_providers)

        radius_config_v4_aaa_get = cls(
            providers=providers,
        )

        radius_config_v4_aaa_get.additional_properties = d
        return radius_config_v4_aaa_get

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
