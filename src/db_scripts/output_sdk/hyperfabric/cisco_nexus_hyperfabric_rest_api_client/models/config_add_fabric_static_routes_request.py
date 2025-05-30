from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_static_routes import ModelsStaticRoutes


T = TypeVar("T", bound="ConfigAddFabricStaticRoutesRequest")


@_attrs_define
class ConfigAddFabricStaticRoutesRequest:
    """Description not available

    Attributes:
        fabric_id (Union[Unset, str]): The fabric id or name.
        static_routes (Union[Unset, list['ModelsStaticRoutes']]): The static routes to be added.
        vrf_id (Union[Unset, str]): The vrf id.
    """

    fabric_id: Union[Unset, str] = UNSET
    static_routes: Union[Unset, list["ModelsStaticRoutes"]] = UNSET
    vrf_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fabric_id = self.fabric_id

        static_routes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.static_routes, Unset):
            static_routes = []
            for static_routes_item_data in self.static_routes:
                static_routes_item = static_routes_item_data.to_dict()
                static_routes.append(static_routes_item)

        vrf_id = self.vrf_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fabric_id is not UNSET:
            field_dict["fabricId"] = fabric_id
        if static_routes is not UNSET:
            field_dict["staticRoutes"] = static_routes
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_static_routes import ModelsStaticRoutes

        d = dict(src_dict)
        fabric_id = d.pop("fabricId", UNSET)

        static_routes = []
        _static_routes = d.pop("staticRoutes", UNSET)
        for static_routes_item_data in _static_routes or []:
            static_routes_item = ModelsStaticRoutes.from_dict(static_routes_item_data)

            static_routes.append(static_routes_item)

        vrf_id = d.pop("vrfId", UNSET)

        config_add_fabric_static_routes_request = cls(
            fabric_id=fabric_id,
            static_routes=static_routes,
            vrf_id=vrf_id,
        )

        config_add_fabric_static_routes_request.additional_properties = d
        return config_add_fabric_static_routes_request

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
