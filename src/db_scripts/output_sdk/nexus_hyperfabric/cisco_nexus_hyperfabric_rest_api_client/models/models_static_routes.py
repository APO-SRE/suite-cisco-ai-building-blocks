from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_annotation import ModelsAnnotation
    from ..models.models_metadata import ModelsMetadata
    from ..models.models_route_info import ModelsRouteInfo


T = TypeVar("T", bound="ModelsStaticRoutes")


@_attrs_define
class ModelsStaticRoutes:
    """The Static Routes object is a child object of a VRF that encapsulates a set of IP static routes pointing to a next-
    hop. The next-hop must be accessible through one of the routed interfaces associated with the parent VRF.

        Attributes:
            annotations (Union[Unset, list['ModelsAnnotation']]): A list of name-value annotations to store user-defined
                data including complex data such as JSON associated with the static routes.
            description (Union[Unset, str]): The description is a user-defined field to store notes about the static routes.
            enabled (Union[Unset, bool]): The enabled state of the static routes which indicates if the static routes is
                enabled or disabled.
            fabric_id (Union[Unset, str]): This is a read-only field. The unique identifier of the fabric to which this
                static routes belong.
            id (Union[Unset, str]): This is a read-only field. The unique identifier of the static routes object.
            labels (Union[Unset, list[str]]): A list of user-defined labels that can be used for grouping and filtering
                static routes.
            metadata (Union[Unset, ModelsMetadata]): Metadata defines a map of attributes related to the lifecycle of the
                object.
            name (Union[Unset, str]): The user-defined name of the static routes. The static routes name has to be unique,
                and is case-insensitive.
            routes (Union[Unset, list['ModelsRouteInfo']]): A list of IP static route definitions.
            vrf_id (Union[Unset, str]): This is a read-only field. The unique identifier of the VRF to which this static
                routes belong to. The VRF identifier is immutable once set.
    """

    annotations: Union[Unset, list["ModelsAnnotation"]] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    metadata: Union[Unset, "ModelsMetadata"] = UNSET
    name: Union[Unset, str] = UNSET
    routes: Union[Unset, list["ModelsRouteInfo"]] = UNSET
    vrf_id: Union[Unset, str] = UNSET
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

        fabric_id = self.fabric_id

        id = self.id

        labels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        routes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.routes, Unset):
            routes = []
            for routes_item_data in self.routes:
                routes_item = routes_item_data.to_dict()
                routes.append(routes_item)

        vrf_id = self.vrf_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if fabric_id is not UNSET:
            field_dict["fabricId"] = fabric_id
        if id is not UNSET:
            field_dict["id"] = id
        if labels is not UNSET:
            field_dict["labels"] = labels
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if routes is not UNSET:
            field_dict["routes"] = routes
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_annotation import ModelsAnnotation
        from ..models.models_metadata import ModelsMetadata
        from ..models.models_route_info import ModelsRouteInfo

        d = dict(src_dict)
        annotations = []
        _annotations = d.pop("annotations", UNSET)
        for annotations_item_data in _annotations or []:
            annotations_item = ModelsAnnotation.from_dict(annotations_item_data)

            annotations.append(annotations_item)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        fabric_id = d.pop("fabricId", UNSET)

        id = d.pop("id", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        routes = []
        _routes = d.pop("routes", UNSET)
        for routes_item_data in _routes or []:
            routes_item = ModelsRouteInfo.from_dict(routes_item_data)

            routes.append(routes_item)

        vrf_id = d.pop("vrfId", UNSET)

        models_static_routes = cls(
            annotations=annotations,
            description=description,
            enabled=enabled,
            fabric_id=fabric_id,
            id=id,
            labels=labels,
            metadata=metadata,
            name=name,
            routes=routes,
            vrf_id=vrf_id,
        )

        models_static_routes.additional_properties = d
        return models_static_routes

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
