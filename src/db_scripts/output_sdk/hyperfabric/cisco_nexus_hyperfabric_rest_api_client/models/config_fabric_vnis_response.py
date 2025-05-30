from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_vni import ModelsVni


T = TypeVar("T", bound="ConfigFabricVnisResponse")


@_attrs_define
class ConfigFabricVnisResponse:
    """Description not available

    Attributes:
        vnis (Union[Unset, list['ModelsVni']]): Description not available
    """

    vnis: Union[Unset, list["ModelsVni"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vnis: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vnis, Unset):
            vnis = []
            for vnis_item_data in self.vnis:
                vnis_item = vnis_item_data.to_dict()
                vnis.append(vnis_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vnis is not UNSET:
            field_dict["vnis"] = vnis

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_vni import ModelsVni

        d = dict(src_dict)
        vnis = []
        _vnis = d.pop("vnis", UNSET)
        for vnis_item_data in _vnis or []:
            vnis_item = ModelsVni.from_dict(vnis_item_data)

            vnis.append(vnis_item)

        config_fabric_vnis_response = cls(
            vnis=vnis,
        )

        config_fabric_vnis_response.additional_properties = d
        return config_fabric_vnis_response

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
