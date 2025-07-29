from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tacacs_config_v4_aaa_get import TACACSConfigV4AaaGET


T = TypeVar("T", bound="ProviderDataV4AaaGETType2")


@_attrs_define
class ProviderDataV4AaaGETType2:
    """
    Attributes:
        tacacs (Union[Unset, TACACSConfigV4AaaGET]):
    """

    tacacs: Union[Unset, "TACACSConfigV4AaaGET"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tacacs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tacacs, Unset):
            tacacs = self.tacacs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tacacs is not UNSET:
            field_dict["tacacs"] = tacacs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tacacs_config_v4_aaa_get import TACACSConfigV4AaaGET

        d = dict(src_dict)
        _tacacs = d.pop("tacacs", UNSET)
        tacacs: Union[Unset, TACACSConfigV4AaaGET]
        if isinstance(_tacacs, Unset):
            tacacs = UNSET
        else:
            tacacs = TACACSConfigV4AaaGET.from_dict(_tacacs)

        provider_data_v4_aaa_get_type_2 = cls(
            tacacs=tacacs,
        )

        provider_data_v4_aaa_get_type_2.additional_properties = d
        return provider_data_v4_aaa_get_type_2

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
