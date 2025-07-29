from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_config_v1_eventmonitoring_get import AlertConfigV1EventmonitoringGET
    from ..models.retention_policy_v1_eventmonitoring_get import RetentionPolicyV1EventmonitoringGET
    from ..models.trigger_group_v1_eventmonitoring_get import TriggerGroupV1EventmonitoringGET


T = TypeVar("T", bound="EventConfigSpecV1EventmonitoringGET")


@_attrs_define
class EventConfigSpecV1EventmonitoringGET:
    """Spec portion of EventConfig resource

    Attributes:
        alert_config (Union[Unset, AlertConfigV1EventmonitoringGET]): Alert configuration being monitored as part of
            event configuration
        data_source_key (Union[Unset, str]): Data source for the config
        id (Union[Unset, str]): domain.metaName appended with name for event configuration
        involved_object (Union[Unset, str]): ND resource or object being monitored
        labels (Union[Unset, list[str]]): Labels supported to elaborate on the resources that the event configuration is
            connected with
        message (Union[Unset, str]): Description about the event configuration being monitored
        name (Union[Unset, str]): Unique name for event configuration
        prettified_name (Union[Unset, str]): User readable name for event configuration
        reason (Union[Unset, str]): Reason for the alert being raised
        retention_policy (Union[Unset, RetentionPolicyV1EventmonitoringGET]): Retention policy for the generated event
            records as part of the parent event configuration
        source (Union[Unset, str]): Source of the issue
        trigger_groups (Union[Unset, list['TriggerGroupV1EventmonitoringGET']]): List of triggers that govern the stream
            types where the alert can be broadcasted
    """

    alert_config: Union[Unset, "AlertConfigV1EventmonitoringGET"] = UNSET
    data_source_key: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    involved_object: Union[Unset, str] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    message: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    prettified_name: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    retention_policy: Union[Unset, "RetentionPolicyV1EventmonitoringGET"] = UNSET
    source: Union[Unset, str] = UNSET
    trigger_groups: Union[Unset, list["TriggerGroupV1EventmonitoringGET"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.alert_config, Unset):
            alert_config = self.alert_config.to_dict()

        data_source_key = self.data_source_key

        id = self.id

        involved_object = self.involved_object

        labels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        message = self.message

        name = self.name

        prettified_name = self.prettified_name

        reason = self.reason

        retention_policy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.retention_policy, Unset):
            retention_policy = self.retention_policy.to_dict()

        source = self.source

        trigger_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.trigger_groups, Unset):
            trigger_groups = []
            for trigger_groups_item_data in self.trigger_groups:
                trigger_groups_item = trigger_groups_item_data.to_dict()
                trigger_groups.append(trigger_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_config is not UNSET:
            field_dict["alertConfig"] = alert_config
        if data_source_key is not UNSET:
            field_dict["dataSourceKey"] = data_source_key
        if id is not UNSET:
            field_dict["id"] = id
        if involved_object is not UNSET:
            field_dict["involvedObject"] = involved_object
        if labels is not UNSET:
            field_dict["labels"] = labels
        if message is not UNSET:
            field_dict["message"] = message
        if name is not UNSET:
            field_dict["name"] = name
        if prettified_name is not UNSET:
            field_dict["prettifiedName"] = prettified_name
        if reason is not UNSET:
            field_dict["reason"] = reason
        if retention_policy is not UNSET:
            field_dict["retentionPolicy"] = retention_policy
        if source is not UNSET:
            field_dict["source"] = source
        if trigger_groups is not UNSET:
            field_dict["triggerGroups"] = trigger_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_config_v1_eventmonitoring_get import AlertConfigV1EventmonitoringGET
        from ..models.retention_policy_v1_eventmonitoring_get import RetentionPolicyV1EventmonitoringGET
        from ..models.trigger_group_v1_eventmonitoring_get import TriggerGroupV1EventmonitoringGET

        d = dict(src_dict)
        _alert_config = d.pop("alertConfig", UNSET)
        alert_config: Union[Unset, AlertConfigV1EventmonitoringGET]
        if isinstance(_alert_config, Unset):
            alert_config = UNSET
        else:
            alert_config = AlertConfigV1EventmonitoringGET.from_dict(_alert_config)

        data_source_key = d.pop("dataSourceKey", UNSET)

        id = d.pop("id", UNSET)

        involved_object = d.pop("involvedObject", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        message = d.pop("message", UNSET)

        name = d.pop("name", UNSET)

        prettified_name = d.pop("prettifiedName", UNSET)

        reason = d.pop("reason", UNSET)

        _retention_policy = d.pop("retentionPolicy", UNSET)
        retention_policy: Union[Unset, RetentionPolicyV1EventmonitoringGET]
        if isinstance(_retention_policy, Unset):
            retention_policy = UNSET
        else:
            retention_policy = RetentionPolicyV1EventmonitoringGET.from_dict(_retention_policy)

        source = d.pop("source", UNSET)

        trigger_groups = []
        _trigger_groups = d.pop("triggerGroups", UNSET)
        for trigger_groups_item_data in _trigger_groups or []:
            trigger_groups_item = TriggerGroupV1EventmonitoringGET.from_dict(trigger_groups_item_data)

            trigger_groups.append(trigger_groups_item)

        event_config_spec_v1_eventmonitoring_get = cls(
            alert_config=alert_config,
            data_source_key=data_source_key,
            id=id,
            involved_object=involved_object,
            labels=labels,
            message=message,
            name=name,
            prettified_name=prettified_name,
            reason=reason,
            retention_policy=retention_policy,
            source=source,
            trigger_groups=trigger_groups,
        )

        event_config_spec_v1_eventmonitoring_get.additional_properties = d
        return event_config_spec_v1_eventmonitoring_get

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
