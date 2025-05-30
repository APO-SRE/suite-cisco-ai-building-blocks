from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_condition import NotificationCondition
    from ..models.notification_receiver import NotificationReceiver


T = TypeVar("T", bound="NotificationsField")


@_attrs_define
class NotificationsField:
    """
    Attributes:
        receiver (NotificationReceiver):
        type_ (str): The notification type - "LocationUpdate", "Absence", "Association" and "In/Out" Example:
            LocationUpdate.
        name (str): The notification name. Example: Test Notification.
        conditions (NotificationCondition):
        enable_mac_scrambling (Union[Unset, bool]): Enable mac scrambling Example: True.
        created (Union[Unset, float]): The notification creation time. Example: 1525930551725.
        userid (Union[Unset, str]): The user ID. Example: testuser.
        enabled (Union[Unset, bool]): The notification is enabled or not Example: True.
        internal (Union[Unset, bool]): System defined notifications
        tenant_id (Union[Unset, str]): Tenant ID Example: 9.
        mac_scrambling_salt (Union[Unset, str]): mac hash key Example: hashit.
        id (Union[Unset, UUID]):  Example: 7a226a48-80e6-4ed3-b558-22f24a404c3d.
        updated (Union[Unset, float]): Last updated time Example: 1525930551725.
    """

    receiver: "NotificationReceiver"
    type_: str
    name: str
    conditions: "NotificationCondition"
    enable_mac_scrambling: Union[Unset, bool] = UNSET
    created: Union[Unset, float] = UNSET
    userid: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    internal: Union[Unset, bool] = UNSET
    tenant_id: Union[Unset, str] = UNSET
    mac_scrambling_salt: Union[Unset, str] = UNSET
    id: Union[Unset, UUID] = UNSET
    updated: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        receiver = self.receiver.to_dict()

        type_ = self.type_

        name = self.name

        conditions = self.conditions.to_dict()

        enable_mac_scrambling = self.enable_mac_scrambling

        created = self.created

        userid = self.userid

        enabled = self.enabled

        internal = self.internal

        tenant_id = self.tenant_id

        mac_scrambling_salt = self.mac_scrambling_salt

        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "receiver": receiver,
                "type": type_,
                "name": name,
                "conditions": conditions,
            }
        )
        if enable_mac_scrambling is not UNSET:
            field_dict["enableMacScrambling"] = enable_mac_scrambling
        if created is not UNSET:
            field_dict["created"] = created
        if userid is not UNSET:
            field_dict["userid"] = userid
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if internal is not UNSET:
            field_dict["internal"] = internal
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if mac_scrambling_salt is not UNSET:
            field_dict["macScramblingSalt"] = mac_scrambling_salt
        if id is not UNSET:
            field_dict["id"] = id
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_condition import NotificationCondition
        from ..models.notification_receiver import NotificationReceiver

        d = dict(src_dict)
        receiver = NotificationReceiver.from_dict(d.pop("receiver"))

        type_ = d.pop("type")

        name = d.pop("name")

        conditions = NotificationCondition.from_dict(d.pop("conditions"))

        enable_mac_scrambling = d.pop("enableMacScrambling", UNSET)

        created = d.pop("created", UNSET)

        userid = d.pop("userid", UNSET)

        enabled = d.pop("enabled", UNSET)

        internal = d.pop("internal", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        mac_scrambling_salt = d.pop("macScramblingSalt", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        updated = d.pop("updated", UNSET)

        notifications_field = cls(
            receiver=receiver,
            type_=type_,
            name=name,
            conditions=conditions,
            enable_mac_scrambling=enable_mac_scrambling,
            created=created,
            userid=userid,
            enabled=enabled,
            internal=internal,
            tenant_id=tenant_id,
            mac_scrambling_salt=mac_scrambling_salt,
            id=id,
            updated=updated,
        )

        notifications_field.additional_properties = d
        return notifications_field

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
