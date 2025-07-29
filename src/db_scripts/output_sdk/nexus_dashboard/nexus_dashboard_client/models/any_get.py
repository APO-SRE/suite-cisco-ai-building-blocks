from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.any_get_spec import AnyGETSpec
    from ..models.any_get_status import AnyGETStatus
    from ..models.managed_object_meta_v1_argo_cisco_com_get import ManagedObjectMetaV1ArgoCiscoComGET


T = TypeVar("T", bound="AnyGET")


@_attrs_define
class AnyGET:
    """
    Attributes:
        metadata (ManagedObjectMetaV1ArgoCiscoComGET):
        spec (Union[Unset, AnyGETSpec]):
        status (Union[Unset, AnyGETStatus]):
    """

    metadata: "ManagedObjectMetaV1ArgoCiscoComGET"
    spec: Union[Unset, "AnyGETSpec"] = UNSET
    status: Union[Unset, "AnyGETStatus"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata = self.metadata.to_dict()

        spec: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata": metadata,
            }
        )
        if spec is not UNSET:
            field_dict["spec"] = spec
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.any_get_spec import AnyGETSpec
        from ..models.any_get_status import AnyGETStatus
        from ..models.managed_object_meta_v1_argo_cisco_com_get import ManagedObjectMetaV1ArgoCiscoComGET

        d = dict(src_dict)
        metadata = ManagedObjectMetaV1ArgoCiscoComGET.from_dict(d.pop("metadata"))

        _spec = d.pop("spec", UNSET)
        spec: Union[Unset, AnyGETSpec]
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = AnyGETSpec.from_dict(_spec)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AnyGETStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AnyGETStatus.from_dict(_status)

        any_get = cls(
            metadata=metadata,
            spec=spec,
            status=status,
        )

        any_get.additional_properties = d
        return any_get

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
