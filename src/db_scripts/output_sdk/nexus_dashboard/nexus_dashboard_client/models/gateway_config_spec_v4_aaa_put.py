from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_server_options_v4_aaa_put import HTTPServerOptionsV4AaaPUT


T = TypeVar("T", bound="GatewayConfigSpecV4AaaPUT")


@_attrs_define
class GatewayConfigSpecV4AaaPUT:
    """
    Attributes:
        http_server_options (Union[Unset, HTTPServerOptionsV4AaaPUT]):
        idle_session_timeout_seconds (Union[Unset, int]): Idle Session Timeout
        jwt_session_timeout_seconds (Union[Unset, int]): JWT Session Timeout
        name (Union[Unset, str]): APIGW Config Name
    """

    http_server_options: Union[Unset, "HTTPServerOptionsV4AaaPUT"] = UNSET
    idle_session_timeout_seconds: Union[Unset, int] = UNSET
    jwt_session_timeout_seconds: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        http_server_options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.http_server_options, Unset):
            http_server_options = self.http_server_options.to_dict()

        idle_session_timeout_seconds = self.idle_session_timeout_seconds

        jwt_session_timeout_seconds = self.jwt_session_timeout_seconds

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if http_server_options is not UNSET:
            field_dict["httpServerOptions"] = http_server_options
        if idle_session_timeout_seconds is not UNSET:
            field_dict["idleSessionTimeoutSeconds"] = idle_session_timeout_seconds
        if jwt_session_timeout_seconds is not UNSET:
            field_dict["jwtSessionTimeoutSeconds"] = jwt_session_timeout_seconds
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.http_server_options_v4_aaa_put import HTTPServerOptionsV4AaaPUT

        d = dict(src_dict)
        _http_server_options = d.pop("httpServerOptions", UNSET)
        http_server_options: Union[Unset, HTTPServerOptionsV4AaaPUT]
        if isinstance(_http_server_options, Unset):
            http_server_options = UNSET
        else:
            http_server_options = HTTPServerOptionsV4AaaPUT.from_dict(_http_server_options)

        idle_session_timeout_seconds = d.pop("idleSessionTimeoutSeconds", UNSET)

        jwt_session_timeout_seconds = d.pop("jwtSessionTimeoutSeconds", UNSET)

        name = d.pop("name", UNSET)

        gateway_config_spec_v4_aaa_put = cls(
            http_server_options=http_server_options,
            idle_session_timeout_seconds=idle_session_timeout_seconds,
            jwt_session_timeout_seconds=jwt_session_timeout_seconds,
            name=name,
        )

        gateway_config_spec_v4_aaa_put.additional_properties = d
        return gateway_config_spec_v4_aaa_put

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
