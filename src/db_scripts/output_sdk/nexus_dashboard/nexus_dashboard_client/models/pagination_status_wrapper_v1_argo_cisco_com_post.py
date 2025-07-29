from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_object_descriptor_v1_argo_cisco_com_post import PaginatedObjectDescriptorV1ArgoCiscoComPOST
    from ..models.pagination_status_wrapper_v1_argo_cisco_com_post_intra_type_i_ds import (
        PaginationStatusWrapperV1ArgoCiscoComPOSTIntraTypeIDs,
    )


T = TypeVar("T", bound="PaginationStatusWrapperV1ArgoCiscoComPOST")


@_attrs_define
class PaginationStatusWrapperV1ArgoCiscoComPOST:
    """
    Attributes:
        fields_resolve_meta_ptrs (Union[Unset, list[str]]):
        inc (Union[Unset, bool]):
        intra_type_i_ds (Union[Unset, PaginationStatusWrapperV1ArgoCiscoComPOSTIntraTypeIDs]):
        match_expression (Union[Unset, str]):
        order_by (Union[Unset, list[str]]):
        results (Union[Unset, list['PaginatedObjectDescriptorV1ArgoCiscoComPOST']]):
        updated (Union[Unset, str]):
    """

    fields_resolve_meta_ptrs: Union[Unset, list[str]] = UNSET
    inc: Union[Unset, bool] = UNSET
    intra_type_i_ds: Union[Unset, "PaginationStatusWrapperV1ArgoCiscoComPOSTIntraTypeIDs"] = UNSET
    match_expression: Union[Unset, str] = UNSET
    order_by: Union[Unset, list[str]] = UNSET
    results: Union[Unset, list["PaginatedObjectDescriptorV1ArgoCiscoComPOST"]] = UNSET
    updated: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fields_resolve_meta_ptrs: Union[Unset, list[str]] = UNSET
        if not isinstance(self.fields_resolve_meta_ptrs, Unset):
            fields_resolve_meta_ptrs = self.fields_resolve_meta_ptrs

        inc = self.inc

        intra_type_i_ds: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.intra_type_i_ds, Unset):
            intra_type_i_ds = self.intra_type_i_ds.to_dict()

        match_expression = self.match_expression

        order_by: Union[Unset, list[str]] = UNSET
        if not isinstance(self.order_by, Unset):
            order_by = self.order_by

        results: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fields_resolve_meta_ptrs is not UNSET:
            field_dict["fieldsResolveMetaPtrs"] = fields_resolve_meta_ptrs
        if inc is not UNSET:
            field_dict["inc"] = inc
        if intra_type_i_ds is not UNSET:
            field_dict["intraTypeIDs"] = intra_type_i_ds
        if match_expression is not UNSET:
            field_dict["matchExpression"] = match_expression
        if order_by is not UNSET:
            field_dict["orderBy"] = order_by
        if results is not UNSET:
            field_dict["results"] = results
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_object_descriptor_v1_argo_cisco_com_post import (
            PaginatedObjectDescriptorV1ArgoCiscoComPOST,
        )
        from ..models.pagination_status_wrapper_v1_argo_cisco_com_post_intra_type_i_ds import (
            PaginationStatusWrapperV1ArgoCiscoComPOSTIntraTypeIDs,
        )

        d = dict(src_dict)
        fields_resolve_meta_ptrs = cast(list[str], d.pop("fieldsResolveMetaPtrs", UNSET))

        inc = d.pop("inc", UNSET)

        _intra_type_i_ds = d.pop("intraTypeIDs", UNSET)
        intra_type_i_ds: Union[Unset, PaginationStatusWrapperV1ArgoCiscoComPOSTIntraTypeIDs]
        if isinstance(_intra_type_i_ds, Unset):
            intra_type_i_ds = UNSET
        else:
            intra_type_i_ds = PaginationStatusWrapperV1ArgoCiscoComPOSTIntraTypeIDs.from_dict(_intra_type_i_ds)

        match_expression = d.pop("matchExpression", UNSET)

        order_by = cast(list[str], d.pop("orderBy", UNSET))

        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            results_item = PaginatedObjectDescriptorV1ArgoCiscoComPOST.from_dict(results_item_data)

            results.append(results_item)

        updated = d.pop("updated", UNSET)

        pagination_status_wrapper_v1_argo_cisco_com_post = cls(
            fields_resolve_meta_ptrs=fields_resolve_meta_ptrs,
            inc=inc,
            intra_type_i_ds=intra_type_i_ds,
            match_expression=match_expression,
            order_by=order_by,
            results=results,
            updated=updated,
        )

        pagination_status_wrapper_v1_argo_cisco_com_post.additional_properties = d
        return pagination_status_wrapper_v1_argo_cisco_com_post

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
