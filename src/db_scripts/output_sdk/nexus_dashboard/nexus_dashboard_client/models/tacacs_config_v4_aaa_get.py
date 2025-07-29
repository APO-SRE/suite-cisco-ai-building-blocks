from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tacacs_config_v4_aaa_get_providers import TACACSConfigV4AaaGETProviders


T = TypeVar("T", bound="TACACSConfigV4AaaGET")


@_attrs_define
class TACACSConfigV4AaaGET:
    """
    Attributes:
        providers (Union[Unset, TACACSConfigV4AaaGETProviders]): TACACS login domain configuration
    """

    providers: Union[Unset, "TACACSConfigV4AaaGETProviders"] = UNSET
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
        from ..models.tacacs_config_v4_aaa_get_providers import TACACSConfigV4AaaGETProviders

        d = dict(src_dict)
        _providers = d.pop("providers", UNSET)
        providers: Union[Unset, TACACSConfigV4AaaGETProviders]
        if isinstance(_providers, Unset):
            providers = UNSET
        else:
            providers = TACACSConfigV4AaaGETProviders.from_dict(_providers)

        tacacs_config_v4_aaa_get = cls(
            providers=providers,
        )

        tacacs_config_v4_aaa_get.additional_properties = d
        return tacacs_config_v4_aaa_get

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
