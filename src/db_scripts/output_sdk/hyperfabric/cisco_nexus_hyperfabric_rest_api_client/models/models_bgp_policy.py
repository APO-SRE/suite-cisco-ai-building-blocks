from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_annotation import ModelsAnnotation
    from ..models.models_bgp_rule import ModelsBgpRule
    from ..models.models_metadata import ModelsMetadata


T = TypeVar("T", bound="ModelsBgpPolicy")


@_attrs_define
class ModelsBgpPolicy:
    """BgpPolicy encapsulates properties of a BGP peering policy. BgpPolicy objects are attached to BgpPeer object.

    Attributes:
        annotations (Union[Unset, list['ModelsAnnotation']]): A set of annotations to store user-defined data.
        description (Union[Unset, str]): A user-defined description of BgpPolicy. Description can be up to 2000
            characters.
        enabled (Union[Unset, bool]): Indicates if BgpPolicy is enabled or disabled.
        export (Union[Unset, bool]): Indicates if the policy is a route export or import policy.
        fabric_id (Union[Unset, str]): The identifier of Fabric to which this BgpPolicy belongs. Fabric identifier is
            mandatory, and immutable once set.
        id (Union[Unset, str]): The unique identifier of BgpPolicy. Identifier is required to update an existing
            BgpPolicy. If identifier is missing, then set operation defaults to CREATE mode.
        is_default (Union[Unset, bool]): Indicates that policy is a default BGP policy.
        labels (Union[Unset, list[str]]): A set of user-defined labels for searching and locating objects.
        metadata (Union[Unset, ModelsMetadata]): Metadata defines metadata of all objects in the service.
        name (Union[Unset, str]): The user-defined name of BgpPolicy. BgpPolicy name is unique, and is case-insensitive.
        rules (Union[Unset, list['ModelsBgpRule']]): A set of BGP rules. User may specify up to 10 rules.
    """

    annotations: Union[Unset, list["ModelsAnnotation"]] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    export: Union[Unset, bool] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    is_default: Union[Unset, bool] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    name: Union[Unset, str] = UNSET
    rules: Union[Unset, list["ModelsBgpRule"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = []
            for annotations_item_data in self.annotations:
                annotations_item = annotations_item_data.to_dict()
                annotations.append(annotations_item)

        description = self.description

        enabled = self.enabled

        export = self.export

        fabric_id = self.fabric_id

        id = self.id

        is_default = self.is_default

        labels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if export is not UNSET:
            field_dict["export"] = export
        if fabric_id is not UNSET:
            field_dict["fabricId"] = fabric_id
        if id is not UNSET:
            field_dict["id"] = id
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if labels is not UNSET:
            field_dict["labels"] = labels
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_annotation import ModelsAnnotation
        from ..models.models_bgp_rule import ModelsBgpRule
        from ..models.models_metadata import ModelsMetadata

        d = dict(src_dict)
        annotations = []
        _annotations = d.pop("annotations", UNSET)
        for annotations_item_data in _annotations or []:
            annotations_item = ModelsAnnotation.from_dict(annotations_item_data)

            annotations.append(annotations_item)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        export = d.pop("export", UNSET)

        fabric_id = d.pop("fabricId", UNSET)

        id = d.pop("id", UNSET)

        is_default = d.pop("isDefault", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = ModelsBgpRule.from_dict(rules_item_data)

            rules.append(rules_item)

        models_bgp_policy = cls(
            annotations=annotations,
            description=description,
            enabled=enabled,
            export=export,
            fabric_id=fabric_id,
            id=id,
            is_default=is_default,
            labels=labels,
            metadata=metadata,
            name=name,
            rules=rules,
        )

        models_bgp_policy.additional_properties = d
        return models_bgp_policy

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
