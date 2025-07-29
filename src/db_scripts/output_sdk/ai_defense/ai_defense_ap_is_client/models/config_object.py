from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rule_object import RuleObject


T = TypeVar("T", bound="ConfigObject")


@_attrs_define
class ConfigObject:
    """The configuration for inspection

    Attributes:
        enabled_rules (Union[Unset, list['RuleObject']]): A list of rules to enable for inspection. Either of
            enabled_rules or integration_profile_id, integration_profile_version, integration_tenant_id, integration_type
            must be provided.
        integration_profile_id (Union[Unset, str]): The unique identifier corresponding to the integration profile to be
            applied for inspection. Either of enabled_rules or integration_profile_id, integration_profile_version,
            integration_tenant_id, integration_type must be provided.
        integration_profile_version (Union[Unset, str]): The version of the integration profile to be applied for
            inspection. Either of enabled_rules or integration_profile_id, integration_profile_version,
            integration_tenant_id, integration_type must be provided.
        integration_tenant_id (Union[Unset, str]): The tenant ID of the integration profile to be applied for
            inspection. Either of enabled_rules or integration_profile_id, integration_profile_version,
            integration_tenant_id, integration_type must be provided.
        integration_type (Union[Unset, str]): The type of integration profile to be applied for inspection. Either of
            enabled_rules or integration_profile_id, integration_profile_version, integration_tenant_id, integration_type
            must be provided.
    """

    enabled_rules: Union[Unset, list["RuleObject"]] = UNSET
    integration_profile_id: Union[Unset, str] = UNSET
    integration_profile_version: Union[Unset, str] = UNSET
    integration_tenant_id: Union[Unset, str] = UNSET
    integration_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled_rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.enabled_rules, Unset):
            enabled_rules = []
            for enabled_rules_item_data in self.enabled_rules:
                enabled_rules_item = enabled_rules_item_data.to_dict()
                enabled_rules.append(enabled_rules_item)

        integration_profile_id = self.integration_profile_id

        integration_profile_version = self.integration_profile_version

        integration_tenant_id = self.integration_tenant_id

        integration_type = self.integration_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled_rules is not UNSET:
            field_dict["enabled_rules"] = enabled_rules
        if integration_profile_id is not UNSET:
            field_dict["integration_profile_id"] = integration_profile_id
        if integration_profile_version is not UNSET:
            field_dict["integration_profile_version"] = integration_profile_version
        if integration_tenant_id is not UNSET:
            field_dict["integration_tenant_id"] = integration_tenant_id
        if integration_type is not UNSET:
            field_dict["integration_type"] = integration_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rule_object import RuleObject

        d = dict(src_dict)
        enabled_rules = []
        _enabled_rules = d.pop("enabled_rules", UNSET)
        for enabled_rules_item_data in _enabled_rules or []:
            enabled_rules_item = RuleObject.from_dict(enabled_rules_item_data)

            enabled_rules.append(enabled_rules_item)

        integration_profile_id = d.pop("integration_profile_id", UNSET)

        integration_profile_version = d.pop("integration_profile_version", UNSET)

        integration_tenant_id = d.pop("integration_tenant_id", UNSET)

        integration_type = d.pop("integration_type", UNSET)

        config_object = cls(
            enabled_rules=enabled_rules,
            integration_profile_id=integration_profile_id,
            integration_profile_version=integration_profile_version,
            integration_tenant_id=integration_tenant_id,
            integration_type=integration_type,
        )

        config_object.additional_properties = d
        return config_object

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
