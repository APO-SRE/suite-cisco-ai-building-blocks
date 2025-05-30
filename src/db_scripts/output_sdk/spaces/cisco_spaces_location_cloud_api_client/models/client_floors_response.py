from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_floors_response_item import ClientFloorsResponseItem


T = TypeVar("T", bound="ClientFloorsResponse")


@_attrs_define
class ClientFloorsResponse:
    """
    Attributes:
        results (Union[Unset, list['ClientFloorsResponseItem']]):
        success (Union[Unset, bool]):  Example: True.
    """

    results: Union[Unset, list["ClientFloorsResponseItem"]] = UNSET
    success: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.client_floors_response_item import ClientFloorsResponseItem

        d = dict(src_dict)
        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            results_item = ClientFloorsResponseItem.from_dict(results_item_data)

            results.append(results_item)

        success = d.pop("success", UNSET)

        client_floors_response = cls(
            results=results,
            success=success,
        )

        client_floors_response.additional_properties = d
        return client_floors_response

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
