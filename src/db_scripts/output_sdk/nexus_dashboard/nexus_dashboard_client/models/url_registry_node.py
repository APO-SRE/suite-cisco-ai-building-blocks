from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.url_registry_node_children import URLRegistryNodeChildren
    from ..models.url_registry_node_nested_ops import URLRegistryNodeNestedOps
    from ..models.url_registry_node_own_ops import URLRegistryNodeOwnOps


T = TypeVar("T", bound="URLRegistryNode")


@_attrs_define
class URLRegistryNode:
    """
    Attributes:
        children (Union[Unset, URLRegistryNodeChildren]):
        meta_key (Union[Unset, str]):
        nested_ops (Union[Unset, URLRegistryNodeNestedOps]):
        own_ops (Union[Unset, URLRegistryNodeOwnOps]):
        url_entry (Union[Unset, str]):
    """

    children: Union[Unset, "URLRegistryNodeChildren"] = UNSET
    meta_key: Union[Unset, str] = UNSET
    nested_ops: Union[Unset, "URLRegistryNodeNestedOps"] = UNSET
    own_ops: Union[Unset, "URLRegistryNodeOwnOps"] = UNSET
    url_entry: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        children: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.children, Unset):
            children = self.children.to_dict()

        meta_key = self.meta_key

        nested_ops: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.nested_ops, Unset):
            nested_ops = self.nested_ops.to_dict()

        own_ops: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.own_ops, Unset):
            own_ops = self.own_ops.to_dict()

        url_entry = self.url_entry

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if children is not UNSET:
            field_dict["Children"] = children
        if meta_key is not UNSET:
            field_dict["MetaKey"] = meta_key
        if nested_ops is not UNSET:
            field_dict["NestedOps"] = nested_ops
        if own_ops is not UNSET:
            field_dict["OwnOps"] = own_ops
        if url_entry is not UNSET:
            field_dict["URLEntry"] = url_entry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.url_registry_node_children import URLRegistryNodeChildren
        from ..models.url_registry_node_nested_ops import URLRegistryNodeNestedOps
        from ..models.url_registry_node_own_ops import URLRegistryNodeOwnOps

        d = dict(src_dict)
        _children = d.pop("Children", UNSET)
        children: Union[Unset, URLRegistryNodeChildren]
        if isinstance(_children, Unset):
            children = UNSET
        else:
            children = URLRegistryNodeChildren.from_dict(_children)

        meta_key = d.pop("MetaKey", UNSET)

        _nested_ops = d.pop("NestedOps", UNSET)
        nested_ops: Union[Unset, URLRegistryNodeNestedOps]
        if isinstance(_nested_ops, Unset):
            nested_ops = UNSET
        else:
            nested_ops = URLRegistryNodeNestedOps.from_dict(_nested_ops)

        _own_ops = d.pop("OwnOps", UNSET)
        own_ops: Union[Unset, URLRegistryNodeOwnOps]
        if isinstance(_own_ops, Unset):
            own_ops = UNSET
        else:
            own_ops = URLRegistryNodeOwnOps.from_dict(_own_ops)

        url_entry = d.pop("URLEntry", UNSET)

        url_registry_node = cls(
            children=children,
            meta_key=meta_key,
            nested_ops=nested_ops,
            own_ops=own_ops,
            url_entry=url_entry,
        )

        url_registry_node.additional_properties = d
        return url_registry_node

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
