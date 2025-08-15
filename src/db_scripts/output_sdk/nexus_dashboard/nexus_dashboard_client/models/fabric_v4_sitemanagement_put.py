from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fabric_spec_wrapper_v4_sitemanagement_put import FabricSpecWrapperV4SitemanagementPUT
    from ..models.managed_object_meta_v1_argo_cisco_com_put import ManagedObjectMetaV1ArgoCiscoComPUT


T = TypeVar("T", bound="FabricV4SitemanagementPUT")


@_attrs_define
class FabricV4SitemanagementPUT:
    """Fabric Resource

    Attributes:
        spec (FabricSpecWrapperV4SitemanagementPUT):
        metadata (Union[Unset, ManagedObjectMetaV1ArgoCiscoComPUT]):
    """

    spec: "FabricSpecWrapperV4SitemanagementPUT"
    metadata: Union[Unset, "ManagedObjectMetaV1ArgoCiscoComPUT"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spec = self.spec.to_dict()

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spec": spec,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fabric_spec_wrapper_v4_sitemanagement_put import FabricSpecWrapperV4SitemanagementPUT
        from ..models.managed_object_meta_v1_argo_cisco_com_put import ManagedObjectMetaV1ArgoCiscoComPUT

        d = dict(src_dict)
        spec = FabricSpecWrapperV4SitemanagementPUT.from_dict(d.pop("spec"))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ManagedObjectMetaV1ArgoCiscoComPUT]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ManagedObjectMetaV1ArgoCiscoComPUT.from_dict(_metadata)

        fabric_v4_sitemanagement_put = cls(
            spec=spec,
            metadata=metadata,
        )

        fabric_v4_sitemanagement_put.additional_properties = d
        return fabric_v4_sitemanagement_put

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
