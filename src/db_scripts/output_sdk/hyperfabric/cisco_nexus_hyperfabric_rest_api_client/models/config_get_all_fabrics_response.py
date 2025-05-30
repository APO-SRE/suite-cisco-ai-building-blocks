from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_fabric import ConfigFabric


T = TypeVar("T", bound="ConfigGetAllFabricsResponse")


@_attrs_define
class ConfigGetAllFabricsResponse:
    """Description not available

    Attributes:
        fabrics (Union[Unset, list['ConfigFabric']]): Description not available
    """

    fabrics: Union[Unset, list["ConfigFabric"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fabrics: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fabrics, Unset):
            fabrics = []
            for fabrics_item_data in self.fabrics:
                fabrics_item = fabrics_item_data.to_dict()
                fabrics.append(fabrics_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fabrics is not UNSET:
            field_dict["fabrics"] = fabrics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_fabric import ConfigFabric

        d = dict(src_dict)
        fabrics = []
        _fabrics = d.pop("fabrics", UNSET)
        for fabrics_item_data in _fabrics or []:
            fabrics_item = ConfigFabric.from_dict(fabrics_item_data)

            fabrics.append(fabrics_item)

        config_get_all_fabrics_response = cls(
            fabrics=fabrics,
        )

        config_get_all_fabrics_response.additional_properties = d
        return config_get_all_fabrics_response

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
