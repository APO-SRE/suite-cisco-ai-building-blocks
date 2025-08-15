from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.severity_condition_v1_eventmonitoring_put_severity import SeverityConditionV1EventmonitoringPUTSeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="SeverityConditionV1EventmonitoringPUT")


@_attrs_define
class SeverityConditionV1EventmonitoringPUT:
    """Types of severity conditions to track

    Attributes:
        alert_description (Union[Unset, str]): Description of the alert being raised
        is_deactivated (Union[Unset, bool]): Whether the SeverityCondition is not activated to be monitored
        key (Union[Unset, str]): label or key to compare value
        lvalue (Union[Unset, str]): Threshold value being tracked
        operator (Union[Unset, str]): Comparison operator for the prometheus metric being tracked
        rvalue (Union[Unset, str]): Upper bound of threshold value when "between" operator is used
        severity (Union[Unset, SeverityConditionV1EventmonitoringPUTSeverity]): Severity of the alert to be raised
    """

    alert_description: Union[Unset, str] = UNSET
    is_deactivated: Union[Unset, bool] = UNSET
    key: Union[Unset, str] = UNSET
    lvalue: Union[Unset, str] = UNSET
    operator: Union[Unset, str] = UNSET
    rvalue: Union[Unset, str] = UNSET
    severity: Union[Unset, SeverityConditionV1EventmonitoringPUTSeverity] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_description = self.alert_description

        is_deactivated = self.is_deactivated

        key = self.key

        lvalue = self.lvalue

        operator = self.operator

        rvalue = self.rvalue

        severity: Union[Unset, str] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_description is not UNSET:
            field_dict["alertDescription"] = alert_description
        if is_deactivated is not UNSET:
            field_dict["isDeactivated"] = is_deactivated
        if key is not UNSET:
            field_dict["key"] = key
        if lvalue is not UNSET:
            field_dict["lvalue"] = lvalue
        if operator is not UNSET:
            field_dict["operator"] = operator
        if rvalue is not UNSET:
            field_dict["rvalue"] = rvalue
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alert_description = d.pop("alertDescription", UNSET)

        is_deactivated = d.pop("isDeactivated", UNSET)

        key = d.pop("key", UNSET)

        lvalue = d.pop("lvalue", UNSET)

        operator = d.pop("operator", UNSET)

        rvalue = d.pop("rvalue", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, SeverityConditionV1EventmonitoringPUTSeverity]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = SeverityConditionV1EventmonitoringPUTSeverity(_severity)

        severity_condition_v1_eventmonitoring_put = cls(
            alert_description=alert_description,
            is_deactivated=is_deactivated,
            key=key,
            lvalue=lvalue,
            operator=operator,
            rvalue=rvalue,
            severity=severity,
        )

        severity_condition_v1_eventmonitoring_put.additional_properties = d
        return severity_condition_v1_eventmonitoring_put

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
