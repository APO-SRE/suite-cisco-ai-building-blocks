from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.radius_config_v4_aaa_put import RADIUSConfigV4AaaPUT


T = TypeVar("T", bound="ProviderDataV4AaaPUTType3")


@_attrs_define
class ProviderDataV4AaaPUTType3:
    """
    Attributes:
        radius (Union[Unset, RADIUSConfigV4AaaPUT]):
    """

    radius: Union[Unset, "RADIUSConfigV4AaaPUT"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radius: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.radius, Unset):
            radius = self.radius.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if radius is not UNSET:
            field_dict["radius"] = radius

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.radius_config_v4_aaa_put import RADIUSConfigV4AaaPUT

        d = dict(src_dict)
        _radius = d.pop("radius", UNSET)
        radius: Union[Unset, RADIUSConfigV4AaaPUT]
        if isinstance(_radius, Unset):
            radius = UNSET
        else:
            radius = RADIUSConfigV4AaaPUT.from_dict(_radius)

        provider_data_v4_aaa_put_type_3 = cls(
            radius=radius,
        )

        provider_data_v4_aaa_put_type_3.additional_properties = d
        return provider_data_v4_aaa_put_type_3

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
