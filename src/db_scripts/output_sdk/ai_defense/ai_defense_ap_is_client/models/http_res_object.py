from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_hdr_object import HttpHdrObject


T = TypeVar("T", bound="HttpResObject")


@_attrs_define
class HttpResObject:
    """The HTTP response body

    Attributes:
        status_code (int): Status code of the response
        body (str): base64 encoded response body, partial or full
        status_string (Union[Unset, str]): HTTP status string
        headers (Union[Unset, HttpHdrObject]): HTTP headers
        split (Union[Unset, bool]): whether HTTP response body split into chunks. Note, this is not the same as HTTP
            transfer-encoding
        last (Union[Unset, bool]): whether this is last chunk of the split body.
    """

    status_code: int
    body: str
    status_string: Union[Unset, str] = UNSET
    headers: Union[Unset, "HttpHdrObject"] = UNSET
    split: Union[Unset, bool] = UNSET
    last: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_code = self.status_code

        body = self.body

        status_string = self.status_string

        headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        split = self.split

        last = self.last

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "statusCode": status_code,
                "body": body,
            }
        )
        if status_string is not UNSET:
            field_dict["statusString"] = status_string
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
        status_code = d.pop("statusCode")

        body = d.pop("body")

        status_string = d.pop("statusString", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, HttpHdrObject]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = HttpHdrObject.from_dict(_headers)

        split = d.pop("split", UNSET)

        last = d.pop("last", UNSET)

        http_res_object = cls(
            status_code=status_code,
            body=body,
            status_string=status_string,
            headers=headers,
            split=split,
            last=last,
        )

        http_res_object.additional_properties = d
        return http_res_object

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
