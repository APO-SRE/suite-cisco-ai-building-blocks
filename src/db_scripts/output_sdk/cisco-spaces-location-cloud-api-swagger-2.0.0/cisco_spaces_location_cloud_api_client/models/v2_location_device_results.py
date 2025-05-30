from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v2_location_device import V2LocationDevice


T = TypeVar("T", bound="V2LocationDeviceResults")


@_attrs_define
class V2LocationDeviceResults:
    """
    Attributes:
        results (Union[Unset, list['V2LocationDevice']]): The list of device location data, include associated AP
            devices location data as the first item and each device's mac address and coordinates as following items in the
            list. (As "oneof" schema is not supported in current version of swagger editor(2.0), please refer to model
            "LocationDeviceDetails" for schema reference as well)
        querystring (Union[Unset, Any]):
        success (Union[Unset, bool]): True in a successful response. Example: True.
        more_page (Union[Unset, bool]): True to indicate there is next page, false otherwise
    """

    results: Union[Unset, list["V2LocationDevice"]] = UNSET
    querystring: Union[Unset, Any] = UNSET
    success: Union[Unset, bool] = UNSET
    more_page: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        querystring = self.querystring

        success = self.success

        more_page = self.more_page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results
        if querystring is not UNSET:
            field_dict["querystring"] = querystring
        if success is not UNSET:
            field_dict["success"] = success
        if more_page is not UNSET:
            field_dict["morePage"] = more_page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v2_location_device import V2LocationDevice

        d = dict(src_dict)
        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            results_item = V2LocationDevice.from_dict(results_item_data)

            results.append(results_item)

        querystring = d.pop("querystring", UNSET)

        success = d.pop("success", UNSET)

        more_page = d.pop("morePage", UNSET)

        v2_location_device_results = cls(
            results=results,
            querystring=querystring,
            success=success,
            more_page=more_page,
        )

        v2_location_device_results.additional_properties = d
        return v2_location_device_results

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
