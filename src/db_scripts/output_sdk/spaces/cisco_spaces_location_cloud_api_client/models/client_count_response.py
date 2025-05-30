from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_count_response_query import ClientCountResponseQuery
    from ..models.client_count_response_res import ClientCountResponseRes


T = TypeVar("T", bound="ClientCountResponse")


@_attrs_define
class ClientCountResponse:
    """
    Attributes:
        results (ClientCountResponseRes):
        querystring (Union[Unset, ClientCountResponseQuery]):
        success (Union[Unset, bool]): operation status. true means successful, false otherwise. Example: True.
    """

    results: "ClientCountResponseRes"
    querystring: Union[Unset, "ClientCountResponseQuery"] = UNSET
    success: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = self.results.to_dict()

        querystring: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.querystring, Unset):
            querystring = self.querystring.to_dict()

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
            }
        )
        if querystring is not UNSET:
            field_dict["querystring"] = querystring
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.client_count_response_query import ClientCountResponseQuery
        from ..models.client_count_response_res import ClientCountResponseRes

        d = dict(src_dict)
        results = ClientCountResponseRes.from_dict(d.pop("results"))

        _querystring = d.pop("querystring", UNSET)
        querystring: Union[Unset, ClientCountResponseQuery]
        if isinstance(_querystring, Unset):
            querystring = UNSET
        else:
            querystring = ClientCountResponseQuery.from_dict(_querystring)

        success = d.pop("success", UNSET)

        client_count_response = cls(
            results=results,
            querystring=querystring,
            success=success,
        )

        client_count_response.additional_properties = d
        return client_count_response

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
