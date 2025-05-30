from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_condition_hierarchy import NotificationConditionHierarchy


T = TypeVar("T", bound="NotificationCondition")


@_attrs_define
class NotificationCondition:
    """
    Attributes:
        device_type (Union[Unset, str]): The notification device type. Example: Client.
        association (Union[Unset, bool]): in association type or not
        mac_address (Union[Unset, list[str]]):
        hierarchy (Union[Unset, NotificationConditionHierarchy]):
    """

    device_type: Union[Unset, str] = UNSET
    association: Union[Unset, bool] = UNSET
    mac_address: Union[Unset, list[str]] = UNSET
    hierarchy: Union[Unset, "NotificationConditionHierarchy"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_type = self.device_type

        association = self.association

        mac_address: Union[Unset, list[str]] = UNSET
        if not isinstance(self.mac_address, Unset):
            mac_address = self.mac_address

        hierarchy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.hierarchy, Unset):
            hierarchy = self.hierarchy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if association is not UNSET:
            field_dict["association"] = association
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if hierarchy is not UNSET:
            field_dict["hierarchy"] = hierarchy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_condition_hierarchy import NotificationConditionHierarchy

        d = dict(src_dict)
        device_type = d.pop("deviceType", UNSET)

        association = d.pop("association", UNSET)

        mac_address = cast(list[str], d.pop("macAddress", UNSET))

        _hierarchy = d.pop("hierarchy", UNSET)
        hierarchy: Union[Unset, NotificationConditionHierarchy]
        if isinstance(_hierarchy, Unset):
            hierarchy = UNSET
        else:
            hierarchy = NotificationConditionHierarchy.from_dict(_hierarchy)

        notification_condition = cls(
            device_type=device_type,
            association=association,
            mac_address=mac_address,
            hierarchy=hierarchy,
        )

        notification_condition.additional_properties = d
        return notification_condition

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
