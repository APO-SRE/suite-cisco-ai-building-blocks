from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_hdr_kv_object import HttpHdrKvObject


T = TypeVar("T", bound="HttpHdrObject")


@_attrs_define
class HttpHdrObject:
    """HTTP headers

    Attributes:
        hdr_kvs (Union[Unset, list['HttpHdrKvObject']]):
    """

    hdr_kvs: Union[Unset, list["HttpHdrKvObject"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hdr_kvs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.hdr_kvs, Unset):
            hdr_kvs = []
            for hdr_kvs_item_data in self.hdr_kvs:
                hdr_kvs_item = hdr_kvs_item_data.to_dict()
                hdr_kvs.append(hdr_kvs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hdr_kvs is not UNSET:
            field_dict["hdrKvs"] = hdr_kvs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.http_hdr_kv_object import HttpHdrKvObject

        d = dict(src_dict)
        hdr_kvs = []
        _hdr_kvs = d.pop("hdrKvs", UNSET)
        for hdr_kvs_item_data in _hdr_kvs or []:
            hdr_kvs_item = HttpHdrKvObject.from_dict(hdr_kvs_item_data)

            hdr_kvs.append(hdr_kvs_item)

        http_hdr_object = cls(
            hdr_kvs=hdr_kvs,
        )

        http_hdr_object.additional_properties = d
        return http_hdr_object

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
