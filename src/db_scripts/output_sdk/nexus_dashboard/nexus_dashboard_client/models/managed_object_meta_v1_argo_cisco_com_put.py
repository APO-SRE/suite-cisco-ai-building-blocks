from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.managed_object_meta_v1_argo_cisco_com_put_annotations import (
        ManagedObjectMetaV1ArgoCiscoComPUTAnnotations,
    )
    from ..models.managed_object_meta_v1_argo_cisco_com_put_labels import ManagedObjectMetaV1ArgoCiscoComPUTLabels


T = TypeVar("T", bound="ManagedObjectMetaV1ArgoCiscoComPUT")


@_attrs_define
class ManagedObjectMetaV1ArgoCiscoComPUT:
    """
    Attributes:
        annotations (Union[Unset, ManagedObjectMetaV1ArgoCiscoComPUTAnnotations]): A map of string key-value pairs that
            are used to store arbitrary metadata.
        kind (Union[Unset, str]): A kind to which the resource belongs to.
        labels (Union[Unset, ManagedObjectMetaV1ArgoCiscoComPUTLabels]): A map of string key-value pairs that are used
            to categorize objects and perform label selection.
        org (Union[Unset, str]): An organization to which the resource belongs to.
    """

    annotations: Union[Unset, "ManagedObjectMetaV1ArgoCiscoComPUTAnnotations"] = UNSET
    kind: Union[Unset, str] = UNSET
    labels: Union[Unset, "ManagedObjectMetaV1ArgoCiscoComPUTLabels"] = UNSET
    org: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        kind = self.kind

        labels: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        org = self.org

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if kind is not UNSET:
            field_dict["kind"] = kind
        if labels is not UNSET:
            field_dict["labels"] = labels
        if org is not UNSET:
            field_dict["org"] = org

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.managed_object_meta_v1_argo_cisco_com_put_annotations import (
            ManagedObjectMetaV1ArgoCiscoComPUTAnnotations,
        )
        from ..models.managed_object_meta_v1_argo_cisco_com_put_labels import ManagedObjectMetaV1ArgoCiscoComPUTLabels

        d = dict(src_dict)
        _annotations = d.pop("annotations", UNSET)
        annotations: Union[Unset, ManagedObjectMetaV1ArgoCiscoComPUTAnnotations]
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = ManagedObjectMetaV1ArgoCiscoComPUTAnnotations.from_dict(_annotations)

        kind = d.pop("kind", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: Union[Unset, ManagedObjectMetaV1ArgoCiscoComPUTLabels]
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = ManagedObjectMetaV1ArgoCiscoComPUTLabels.from_dict(_labels)

        org = d.pop("org", UNSET)

        managed_object_meta_v1_argo_cisco_com_put = cls(
            annotations=annotations,
            kind=kind,
            labels=labels,
            org=org,
        )

        managed_object_meta_v1_argo_cisco_com_put.additional_properties = d
        return managed_object_meta_v1_argo_cisco_com_put

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
