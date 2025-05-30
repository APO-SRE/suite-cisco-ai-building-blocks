from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_fabric_config import ConfigFabricConfig


T = TypeVar("T", bound="ConfigGetFabricConfigResponse")


@_attrs_define
class ConfigGetFabricConfigResponse:
    """Description not available

    Attributes:
        candidate (Union[Unset, str]): The candidate name.
        config (Union[Unset, ConfigFabricConfig]): FabricConfig encapsulates entire config of a fabric.
    """

    candidate: Union[Unset, str] = UNSET
    config: Union[Unset, "ConfigFabricConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        candidate = self.candidate

        config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if candidate is not UNSET:
            field_dict["candidate"] = candidate
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_fabric_config import ConfigFabricConfig

        d = dict(src_dict)
        candidate = d.pop("candidate", UNSET)

        _config = d.pop("config", UNSET)
        config: Union[Unset, ConfigFabricConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ConfigFabricConfig.from_dict(_config)

        config_get_fabric_config_response = cls(
            candidate=candidate,
            config=config,
        )

        config_get_fabric_config_response.additional_properties = d
        return config_get_fabric_config_response

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
