from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reconcile_record_spec_v1_argo_cisco_com_post_instances import (
        ReconcileRecordSpecV1ArgoCiscoComPOSTInstances,
    )


T = TypeVar("T", bound="ReconcileRecordSpecV1ArgoCiscoComPOST")


@_attrs_define
class ReconcileRecordSpecV1ArgoCiscoComPOST:
    """
    Attributes:
        instances (Union[Unset, ReconcileRecordSpecV1ArgoCiscoComPOSTInstances]):
        kind (Union[Unset, str]):
    """

    instances: Union[Unset, "ReconcileRecordSpecV1ArgoCiscoComPOSTInstances"] = UNSET
    kind: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instances: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.instances, Unset):
            instances = self.instances.to_dict()

        kind = self.kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instances is not UNSET:
            field_dict["instances"] = instances
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reconcile_record_spec_v1_argo_cisco_com_post_instances import (
            ReconcileRecordSpecV1ArgoCiscoComPOSTInstances,
        )

        d = dict(src_dict)
        _instances = d.pop("instances", UNSET)
        instances: Union[Unset, ReconcileRecordSpecV1ArgoCiscoComPOSTInstances]
        if isinstance(_instances, Unset):
            instances = UNSET
        else:
            instances = ReconcileRecordSpecV1ArgoCiscoComPOSTInstances.from_dict(_instances)

        kind = d.pop("kind", UNSET)

        reconcile_record_spec_v1_argo_cisco_com_post = cls(
            instances=instances,
            kind=kind,
        )

        reconcile_record_spec_v1_argo_cisco_com_post.additional_properties = d
        return reconcile_record_spec_v1_argo_cisco_com_post

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
