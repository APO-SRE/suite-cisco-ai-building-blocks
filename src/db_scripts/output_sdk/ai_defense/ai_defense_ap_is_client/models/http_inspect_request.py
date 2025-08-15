from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_object import ConfigObject
    from ..models.http_meta_object import HttpMetaObject
    from ..models.http_req_object import HttpReqObject
    from ..models.http_res_object import HttpResObject
    from ..models.metadata_object import MetadataObject


T = TypeVar("T", bound="HttpInspectRequest")


@_attrs_define
class HttpInspectRequest:
    """The request to inspect a HTTP request or HTTP response

    Attributes:
        http_req (HttpReqObject): The HTTP request body
        http_res (Union[Unset, HttpResObject]): The HTTP response body
        http_meta (Union[Unset, HttpMetaObject]): Metadata useful to both HTTP request and response
        metadata (Union[Unset, MetadataObject]): Additional information, such as user identity and application identity
        config (Union[Unset, ConfigObject]): The configuration for inspection
    """

    http_req: "HttpReqObject"
    http_res: Union[Unset, "HttpResObject"] = UNSET
    http_meta: Union[Unset, "HttpMetaObject"] = UNSET
    metadata: Union[Unset, "MetadataObject"] = UNSET
    config: Union[Unset, "ConfigObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        http_req = self.http_req.to_dict()

        http_res: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.http_res, Unset):
            http_res = self.http_res.to_dict()

        http_meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.http_meta, Unset):
            http_meta = self.http_meta.to_dict()

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "http_req": http_req,
            }
        )
        if http_res is not UNSET:
            field_dict["http_res"] = http_res
        if http_meta is not UNSET:
            field_dict["http_meta"] = http_meta
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_object import ConfigObject
        from ..models.http_meta_object import HttpMetaObject
        from ..models.http_req_object import HttpReqObject
        from ..models.http_res_object import HttpResObject
        from ..models.metadata_object import MetadataObject

        d = dict(src_dict)
        http_req = HttpReqObject.from_dict(d.pop("http_req"))

        _http_res = d.pop("http_res", UNSET)
        http_res: Union[Unset, HttpResObject]
        if isinstance(_http_res, Unset):
            http_res = UNSET
        else:
            http_res = HttpResObject.from_dict(_http_res)

        _http_meta = d.pop("http_meta", UNSET)
        http_meta: Union[Unset, HttpMetaObject]
        if isinstance(_http_meta, Unset):
            http_meta = UNSET
        else:
            http_meta = HttpMetaObject.from_dict(_http_meta)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, MetadataObject]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = MetadataObject.from_dict(_metadata)

        _config = d.pop("config", UNSET)
        config: Union[Unset, ConfigObject]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ConfigObject.from_dict(_config)

        http_inspect_request = cls(
            http_req=http_req,
            http_res=http_res,
            http_meta=http_meta,
            metadata=metadata,
            config=config,
        )

        http_inspect_request.additional_properties = d
        return http_inspect_request

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
