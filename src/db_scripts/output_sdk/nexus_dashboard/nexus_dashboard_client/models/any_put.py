from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.any_put_spec import AnyPUTSpec
    from ..models.any_put_status import AnyPUTStatus
    from ..models.managed_object_meta_v1_argo_cisco_com_put import ManagedObjectMetaV1ArgoCiscoComPUT


T = TypeVar("T", bound="AnyPUT")


@_attrs_define
class AnyPUT:
    """
    Attributes:
        metadata (Union[Unset, ManagedObjectMetaV1ArgoCiscoComPUT]):
        spec (Union[Unset, AnyPUTSpec]):
        status (Union[Unset, AnyPUTStatus]):
    """

    metadata: Union[Unset, "ManagedObjectMetaV1ArgoCiscoComPUT"] = UNSET
    spec: Union[Unset, "AnyPUTSpec"] = UNSET
    status: Union[Unset, "AnyPUTStatus"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        spec: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if spec is not UNSET:
            field_dict["spec"] = spec
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.any_put_spec import AnyPUTSpec
        from ..models.any_put_status import AnyPUTStatus
        from ..models.managed_object_meta_v1_argo_cisco_com_put import ManagedObjectMetaV1ArgoCiscoComPUT

        d = dict(src_dict)
        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ManagedObjectMetaV1ArgoCiscoComPUT]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ManagedObjectMetaV1ArgoCiscoComPUT.from_dict(_metadata)

        _spec = d.pop("spec", UNSET)
        spec: Union[Unset, AnyPUTSpec]
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = AnyPUTSpec.from_dict(_spec)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AnyPUTStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AnyPUTStatus.from_dict(_status)

        any_put = cls(
            metadata=metadata,
            spec=spec,
            status=status,
        )

        any_put.additional_properties = d
        return any_put

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
