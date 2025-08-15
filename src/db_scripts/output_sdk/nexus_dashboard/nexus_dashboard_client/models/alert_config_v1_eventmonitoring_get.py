from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.severity_condition_v1_eventmonitoring_get import SeverityConditionV1EventmonitoringGET


T = TypeVar("T", bound="AlertConfigV1EventmonitoringGET")


@_attrs_define
class AlertConfigV1EventmonitoringGET:
    """Alert configuration being monitored as part of event configuration

    Attributes:
        allow_empty_result (Union[Unset, bool]): allow metric result to be empty
        autoclear (Union[Unset, bool]): whether the alert can be auto cleared or needs mandatory customer ack
        is_encrypted (Union[Unset, bool]): Whether the alert config needs to be encrypted
        metric_expression (Union[Unset, str]): Prometheus metric being tracked such as cluster-wide CPU usage
        record_labels (Union[Unset, list[str]]): Query result labels that differentiate between multiple entities being
            tracked under the same parent event configuration
        severity_conditions (Union[Unset, list['SeverityConditionV1EventmonitoringGET']]): Types of severity conditions
            to track
    """

    allow_empty_result: Union[Unset, bool] = UNSET
    autoclear: Union[Unset, bool] = UNSET
    is_encrypted: Union[Unset, bool] = UNSET
    metric_expression: Union[Unset, str] = UNSET
    record_labels: Union[Unset, list[str]] = UNSET
    severity_conditions: Union[Unset, list["SeverityConditionV1EventmonitoringGET"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_empty_result = self.allow_empty_result

        autoclear = self.autoclear

        is_encrypted = self.is_encrypted

        metric_expression = self.metric_expression

        record_labels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.record_labels, Unset):
            record_labels = self.record_labels

        severity_conditions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.severity_conditions, Unset):
            severity_conditions = []
            for severity_conditions_item_data in self.severity_conditions:
                severity_conditions_item = severity_conditions_item_data.to_dict()
                severity_conditions.append(severity_conditions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_empty_result is not UNSET:
            field_dict["allowEmptyResult"] = allow_empty_result
        if autoclear is not UNSET:
            field_dict["autoclear"] = autoclear
        if is_encrypted is not UNSET:
            field_dict["isEncrypted"] = is_encrypted
        if metric_expression is not UNSET:
            field_dict["metricExpression"] = metric_expression
        if record_labels is not UNSET:
            field_dict["recordLabels"] = record_labels
        if severity_conditions is not UNSET:
            field_dict["severityConditions"] = severity_conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.severity_condition_v1_eventmonitoring_get import SeverityConditionV1EventmonitoringGET

        d = dict(src_dict)
        allow_empty_result = d.pop("allowEmptyResult", UNSET)

        autoclear = d.pop("autoclear", UNSET)

        is_encrypted = d.pop("isEncrypted", UNSET)

        metric_expression = d.pop("metricExpression", UNSET)

        record_labels = cast(list[str], d.pop("recordLabels", UNSET))

        severity_conditions = []
        _severity_conditions = d.pop("severityConditions", UNSET)
        for severity_conditions_item_data in _severity_conditions or []:
            severity_conditions_item = SeverityConditionV1EventmonitoringGET.from_dict(severity_conditions_item_data)

            severity_conditions.append(severity_conditions_item)

        alert_config_v1_eventmonitoring_get = cls(
            allow_empty_result=allow_empty_result,
            autoclear=autoclear,
            is_encrypted=is_encrypted,
            metric_expression=metric_expression,
            record_labels=record_labels,
            severity_conditions=severity_conditions,
        )

        alert_config_v1_eventmonitoring_get.additional_properties = d
        return alert_config_v1_eventmonitoring_get

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
