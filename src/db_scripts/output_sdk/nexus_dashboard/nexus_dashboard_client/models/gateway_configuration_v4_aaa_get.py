from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_configuration_spec_wrapper_v4_aaa_get import GatewayConfigurationSpecWrapperV4AaaGET
    from ..models.managed_object_meta_v1_argo_cisco_com_get import ManagedObjectMetaV1ArgoCiscoComGET


T = TypeVar("T", bound="GatewayConfigurationV4AaaGET")


@_attrs_define
class GatewayConfigurationV4AaaGET:
    """API Gateway Configuration Resource

    Attributes:
        spec (GatewayConfigurationSpecWrapperV4AaaGET):
        metadata (Union[Unset, ManagedObjectMetaV1ArgoCiscoComGET]):
    """

    spec: "GatewayConfigurationSpecWrapperV4AaaGET"
    metadata: Union[Unset, "ManagedObjectMetaV1ArgoCiscoComGET"] = UNSET
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
        from ..models.gateway_configuration_spec_wrapper_v4_aaa_get import GatewayConfigurationSpecWrapperV4AaaGET
        from ..models.managed_object_meta_v1_argo_cisco_com_get import ManagedObjectMetaV1ArgoCiscoComGET

        d = dict(src_dict)
        spec = GatewayConfigurationSpecWrapperV4AaaGET.from_dict(d.pop("spec"))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ManagedObjectMetaV1ArgoCiscoComGET]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ManagedObjectMetaV1ArgoCiscoComGET.from_dict(_metadata)

        gateway_configuration_v4_aaa_get = cls(
            spec=spec,
            metadata=metadata,
        )

        gateway_configuration_v4_aaa_get.additional_properties = d
        return gateway_configuration_v4_aaa_get

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
