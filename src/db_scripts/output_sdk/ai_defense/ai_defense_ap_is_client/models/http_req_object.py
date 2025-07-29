from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_hdr_object import HttpHdrObject


T = TypeVar("T", bound="HttpReqObject")


@_attrs_define
class HttpReqObject:
    """The HTTP request body

    Attributes:
        body (str): base64 encoded request body, partial or full
        method (Union[Unset, str]): HTTP method name
        headers (Union[Unset, HttpHdrObject]): HTTP headers
        split (Union[Unset, bool]): whether HTTP request body split into chunks. Note, this is not the same as HTTP
            transfer-encoding
        last (Union[Unset, bool]): whether this is last chunk of the split body.
    """

    body: str
    method: Union[Unset, str] = UNSET
    headers: Union[Unset, "HttpHdrObject"] = UNSET
    split: Union[Unset, bool] = UNSET
    last: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        method = self.method

        headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        split = self.split

        last = self.last

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
            }
        )
        if method is not UNSET:
            field_dict["method"] = method
        if headers is not UNSET:
            field_dict["headers"] = headers
        if split is not UNSET:
            field_dict["split"] = split
        if last is not UNSET:
            field_dict["last"] = last

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.http_hdr_object import HttpHdrObject

        d = dict(src_dict)
        body = d.pop("body")

        method = d.pop("method", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, HttpHdrObject]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = HttpHdrObject.from_dict(_headers)

        split = d.pop("split", UNSET)

        last = d.pop("last", UNSET)

        http_req_object = cls(
            body=body,
            method=method,
            headers=headers,
            split=split,
            last=last,
        )

        http_req_object.additional_properties = d
        return http_req_object

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
