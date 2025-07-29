from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.radius_config_v4_aaa_put_providers import RADIUSConfigV4AaaPUTProviders


T = TypeVar("T", bound="RADIUSConfigV4AaaPUT")


@_attrs_define
class RADIUSConfigV4AaaPUT:
    """
    Attributes:
        providers (Union[Unset, RADIUSConfigV4AaaPUTProviders]): RADIUS login domain configuration
    """

    providers: Union[Unset, "RADIUSConfigV4AaaPUTProviders"] = UNSET
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
        from ..models.radius_config_v4_aaa_put_providers import RADIUSConfigV4AaaPUTProviders

        d = dict(src_dict)
        _providers = d.pop("providers", UNSET)
        providers: Union[Unset, RADIUSConfigV4AaaPUTProviders]
        if isinstance(_providers, Unset):
            providers = UNSET
        else:
            providers = RADIUSConfigV4AaaPUTProviders.from_dict(_providers)

        radius_config_v4_aaa_put = cls(
            providers=providers,
        )

        radius_config_v4_aaa_put.additional_properties = d
        return radius_config_v4_aaa_put

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
