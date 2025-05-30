from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_tenant_objects import ConfigTenantObjects
    from ..models.models_fabric import ModelsFabric
    from ..models.models_per_vlan_stp import ModelsPerVlanStp


T = TypeVar("T", bound="ConfigFabricConfig")


@_attrs_define
class ConfigFabricConfig:
    """FabricConfig encapsulates entire config of a fabric.

    Attributes:
        fabric (Union[Unset, ModelsFabric]): Fabric is a collection of nodes and port interconnections.  - nodes: A set
            of nodes classified as LEAF, SPINE.  - connections: Physical port interconnections between nodes.
        per_vlan_stp (Union[Unset, ModelsPerVlanStp]): PerVlanStp encapsulates properties of a Per-Vlan spanning tree
            protocol config object. There can be only one PerVlanStp config for a fabric.
        tenants (Union[Unset, list['ConfigTenantObjects']]): Tenant objects.
    """

    fabric: Union[Unset, "ModelsFabric"] = UNSET
    per_vlan_stp: Union[Unset, "ModelsPerVlanStp"] = UNSET
    tenants: Union[Unset, list["ConfigTenantObjects"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fabric: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fabric, Unset):
            fabric = self.fabric.to_dict()

        per_vlan_stp: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.per_vlan_stp, Unset):
            per_vlan_stp = self.per_vlan_stp.to_dict()

        tenants: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tenants, Unset):
            tenants = []
            for tenants_item_data in self.tenants:
                tenants_item = tenants_item_data.to_dict()
                tenants.append(tenants_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fabric is not UNSET:
            field_dict["fabric"] = fabric
        if per_vlan_stp is not UNSET:
            field_dict["perVlanStp"] = per_vlan_stp
        if tenants is not UNSET:
            field_dict["tenants"] = tenants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_tenant_objects import ConfigTenantObjects
        from ..models.models_fabric import ModelsFabric
        from ..models.models_per_vlan_stp import ModelsPerVlanStp

        d = dict(src_dict)
        _fabric = d.pop("fabric", UNSET)
        fabric: Union[Unset, ModelsFabric]
        if isinstance(_fabric, Unset):
            fabric = UNSET
        else:
            fabric = ModelsFabric.from_dict(_fabric)

        _per_vlan_stp = d.pop("perVlanStp", UNSET)
        per_vlan_stp: Union[Unset, ModelsPerVlanStp]
        if isinstance(_per_vlan_stp, Unset):
            per_vlan_stp = UNSET
        else:
            per_vlan_stp = ModelsPerVlanStp.from_dict(_per_vlan_stp)

        tenants = []
        _tenants = d.pop("tenants", UNSET)
        for tenants_item_data in _tenants or []:
            tenants_item = ConfigTenantObjects.from_dict(tenants_item_data)

            tenants.append(tenants_item)

        config_fabric_config = cls(
            fabric=fabric,
            per_vlan_stp=per_vlan_stp,
            tenants=tenants,
        )

        config_fabric_config.additional_properties = d
        return config_fabric_config

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
