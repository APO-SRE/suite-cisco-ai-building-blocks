from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_static_routes import ModelsStaticRoutes


T = TypeVar("T", bound="ConfigFabricStaticRoutesResponse")


@_attrs_define
class ConfigFabricStaticRoutesResponse:
    """The response returned to a request for the list of static routes of a specific VRF in a fabric.

    Attributes:
        static_routes (Union[Unset, list['ModelsStaticRoutes']]): A list of static routes definitions.
    """

    static_routes: Union[Unset, list["ModelsStaticRoutes"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        static_routes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.static_routes, Unset):
            static_routes = []
            for static_routes_item_data in self.static_routes:
                static_routes_item = static_routes_item_data.to_dict()
                static_routes.append(static_routes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if static_routes is not UNSET:
            field_dict["staticRoutes"] = static_routes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_static_routes import ModelsStaticRoutes

        d = dict(src_dict)
        static_routes = []
        _static_routes = d.pop("staticRoutes", UNSET)
        for static_routes_item_data in _static_routes or []:
            static_routes_item = ModelsStaticRoutes.from_dict(static_routes_item_data)

            static_routes.append(static_routes_item)

        config_fabric_static_routes_response = cls(
            static_routes=static_routes,
        )

        config_fabric_static_routes_response.additional_properties = d
        return config_fabric_static_routes_response

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
