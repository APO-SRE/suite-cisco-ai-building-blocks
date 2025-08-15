from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.managed_object_meta_v1_argo_cisco_com_get_annotations import (
        ManagedObjectMetaV1ArgoCiscoComGETAnnotations,
    )
    from ..models.managed_object_meta_v1_argo_cisco_com_get_finalizers import (
        ManagedObjectMetaV1ArgoCiscoComGETFinalizers,
    )
    from ..models.managed_object_meta_v1_argo_cisco_com_get_labels import ManagedObjectMetaV1ArgoCiscoComGETLabels


T = TypeVar("T", bound="ManagedObjectMetaV1ArgoCiscoComGET")


@_attrs_define
class ManagedObjectMetaV1ArgoCiscoComGET:
    """
    Attributes:
        account (Union[Unset, str]): An account to which the resource belongs to.
        annotations (Union[Unset, ManagedObjectMetaV1ArgoCiscoComGETAnnotations]): A map of string key-value pairs that
            are used to store arbitrary metadata.
        creation_timestamp (Union[Unset, str]): A timestamp at which the resource was created.
        deletion_timestamp (Union[Unset, str]): A timestamp at which the resource has been marked for deletion.
        finalizers (Union[Unset, ManagedObjectMetaV1ArgoCiscoComGETFinalizers]): A set of entries that are interested in
            the deletion of the resource. This set must be empty before the resource is fully deleted from the system.
        generation (Union[Unset, int]): A running sequence number that represents the current generation of the
            resource.
        id (Union[Unset, str]): A Unique ID associated with the resource.
        intra_type_id (Union[Unset, str]):
        intra_type_id_key (Union[Unset, str]):
        kind (Union[Unset, str]): A kind to which the resource belongs to.
        labels (Union[Unset, ManagedObjectMetaV1ArgoCiscoComGETLabels]): A map of string key-value pairs that are used
            to categorize objects and perform label selection.
        modification_timestamp (Union[Unset, str]): A timestamp at which the resource was last modified.
        namespace (Union[Unset, str]): A namespace to which the resource belongs to. Can be empty for non-namespaced
            resources.
        org (Union[Unset, str]): An organization to which the resource belongs to.
        resource_version (Union[Unset, int]): A value that identifies the internal revision of the resource. This is
            used for optimistic concurrency control.
        schema_version (Union[Unset, str]): A value that identifies the minor revision of the resource schema.
        status_generation (Union[Unset, int]): A running sequence number that represents the current generation of the
            status portion of the resource.
    """

    account: Union[Unset, str] = UNSET
    annotations: Union[Unset, "ManagedObjectMetaV1ArgoCiscoComGETAnnotations"] = UNSET
    creation_timestamp: Union[Unset, str] = UNSET
    deletion_timestamp: Union[Unset, str] = UNSET
    finalizers: Union[Unset, "ManagedObjectMetaV1ArgoCiscoComGETFinalizers"] = UNSET
    generation: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    intra_type_id: Union[Unset, str] = UNSET
    intra_type_id_key: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    labels: Union[Unset, "ManagedObjectMetaV1ArgoCiscoComGETLabels"] = UNSET
    modification_timestamp: Union[Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    org: Union[Unset, str] = UNSET
    resource_version: Union[Unset, int] = UNSET
    schema_version: Union[Unset, str] = UNSET
    status_generation: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account = self.account

        annotations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        creation_timestamp = self.creation_timestamp

        deletion_timestamp = self.deletion_timestamp

        finalizers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.finalizers, Unset):
            finalizers = self.finalizers.to_dict()

        generation = self.generation

        id = self.id

        intra_type_id = self.intra_type_id

        intra_type_id_key = self.intra_type_id_key

        kind = self.kind

        labels: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        modification_timestamp = self.modification_timestamp

        namespace = self.namespace

        org = self.org

        resource_version = self.resource_version

        schema_version = self.schema_version

        status_generation = self.status_generation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if creation_timestamp is not UNSET:
            field_dict["creationTimestamp"] = creation_timestamp
        if deletion_timestamp is not UNSET:
            field_dict["deletionTimestamp"] = deletion_timestamp
        if finalizers is not UNSET:
            field_dict["finalizers"] = finalizers
        if generation is not UNSET:
            field_dict["generation"] = generation
        if id is not UNSET:
            field_dict["id"] = id
        if intra_type_id is not UNSET:
            field_dict["intraTypeID"] = intra_type_id
        if intra_type_id_key is not UNSET:
            field_dict["intraTypeIDKey"] = intra_type_id_key
        if kind is not UNSET:
            field_dict["kind"] = kind
        if labels is not UNSET:
            field_dict["labels"] = labels
        if modification_timestamp is not UNSET:
            field_dict["modificationTimestamp"] = modification_timestamp
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if org is not UNSET:
            field_dict["org"] = org
        if resource_version is not UNSET:
            field_dict["resourceVersion"] = resource_version
        if schema_version is not UNSET:
            field_dict["schemaVersion"] = schema_version
        if status_generation is not UNSET:
            field_dict["statusGeneration"] = status_generation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.managed_object_meta_v1_argo_cisco_com_get_annotations import (
            ManagedObjectMetaV1ArgoCiscoComGETAnnotations,
        )
        from ..models.managed_object_meta_v1_argo_cisco_com_get_finalizers import (
            ManagedObjectMetaV1ArgoCiscoComGETFinalizers,
        )
        from ..models.managed_object_meta_v1_argo_cisco_com_get_labels import ManagedObjectMetaV1ArgoCiscoComGETLabels

        d = dict(src_dict)
        account = d.pop("account", UNSET)

        _annotations = d.pop("annotations", UNSET)
        annotations: Union[Unset, ManagedObjectMetaV1ArgoCiscoComGETAnnotations]
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = ManagedObjectMetaV1ArgoCiscoComGETAnnotations.from_dict(_annotations)

        creation_timestamp = d.pop("creationTimestamp", UNSET)

        deletion_timestamp = d.pop("deletionTimestamp", UNSET)

        _finalizers = d.pop("finalizers", UNSET)
        finalizers: Union[Unset, ManagedObjectMetaV1ArgoCiscoComGETFinalizers]
        if isinstance(_finalizers, Unset):
            finalizers = UNSET
        else:
            finalizers = ManagedObjectMetaV1ArgoCiscoComGETFinalizers.from_dict(_finalizers)

        generation = d.pop("generation", UNSET)

        id = d.pop("id", UNSET)

        intra_type_id = d.pop("intraTypeID", UNSET)

        intra_type_id_key = d.pop("intraTypeIDKey", UNSET)

        kind = d.pop("kind", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: Union[Unset, ManagedObjectMetaV1ArgoCiscoComGETLabels]
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = ManagedObjectMetaV1ArgoCiscoComGETLabels.from_dict(_labels)

        modification_timestamp = d.pop("modificationTimestamp", UNSET)

        namespace = d.pop("namespace", UNSET)

        org = d.pop("org", UNSET)

        resource_version = d.pop("resourceVersion", UNSET)

        schema_version = d.pop("schemaVersion", UNSET)

        status_generation = d.pop("statusGeneration", UNSET)

        managed_object_meta_v1_argo_cisco_com_get = cls(
            account=account,
            annotations=annotations,
            creation_timestamp=creation_timestamp,
            deletion_timestamp=deletion_timestamp,
            finalizers=finalizers,
            generation=generation,
            id=id,
            intra_type_id=intra_type_id,
            intra_type_id_key=intra_type_id_key,
            kind=kind,
            labels=labels,
            modification_timestamp=modification_timestamp,
            namespace=namespace,
            org=org,
            resource_version=resource_version,
            schema_version=schema_version,
            status_generation=status_generation,
        )

        managed_object_meta_v1_argo_cisco_com_get.additional_properties = d
        return managed_object_meta_v1_argo_cisco_com_get

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
