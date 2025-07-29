import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetadataObject")


@_attrs_define
class MetadataObject:
    """Additional information, such as user identity and application identity

    Attributes:
        user (Union[Unset, str]): Notion of user identity as maybe supplied by the caller
        created_at (Union[Unset, datetime.datetime]): The time the prompt or completion was created
        src_app (Union[Unset, str]): Notion of source application identity as maybe supplied by the caller
        dst_app (Union[Unset, str]): Notion of destination application identity as maybe supplied by the caller
        sni (Union[Unset, str]): Server name indication from TLS inspection as maybe supplied by the caller
        dst_ip (Union[Unset, str]): Destination IP Address, as maybe supplied by the caller
        src_ip (Union[Unset, str]): Source IP address, as maybe supplied by the caller
        dst_host (Union[Unset, str]): Destination host
        user_agent (Union[Unset, str]): User agent string if extracted
        client_transaction_id (Union[Unset, str]): The client transaction ID to be returned in the inspection response
            for correlation by the client side
    """

    user: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    src_app: Union[Unset, str] = UNSET
    dst_app: Union[Unset, str] = UNSET
    sni: Union[Unset, str] = UNSET
    dst_ip: Union[Unset, str] = UNSET
    src_ip: Union[Unset, str] = UNSET
    dst_host: Union[Unset, str] = UNSET
    user_agent: Union[Unset, str] = UNSET
    client_transaction_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        src_app = self.src_app

        dst_app = self.dst_app

        sni = self.sni

        dst_ip = self.dst_ip

        src_ip = self.src_ip

        dst_host = self.dst_host

        user_agent = self.user_agent

        client_transaction_id = self.client_transaction_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if src_app is not UNSET:
            field_dict["src_app"] = src_app
        if dst_app is not UNSET:
            field_dict["dst_app"] = dst_app
        if sni is not UNSET:
            field_dict["sni"] = sni
        if dst_ip is not UNSET:
            field_dict["dst_ip"] = dst_ip
        if src_ip is not UNSET:
            field_dict["src_ip"] = src_ip
        if dst_host is not UNSET:
            field_dict["dst_host"] = dst_host
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent
        if client_transaction_id is not UNSET:
            field_dict["client_transaction_id"] = client_transaction_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user = d.pop("user", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        src_app = d.pop("src_app", UNSET)

        dst_app = d.pop("dst_app", UNSET)

        sni = d.pop("sni", UNSET)

        dst_ip = d.pop("dst_ip", UNSET)

        src_ip = d.pop("src_ip", UNSET)

        dst_host = d.pop("dst_host", UNSET)

        user_agent = d.pop("user_agent", UNSET)

        client_transaction_id = d.pop("client_transaction_id", UNSET)

        metadata_object = cls(
            user=user,
            created_at=created_at,
            src_app=src_app,
            dst_app=dst_app,
            sni=sni,
            dst_ip=dst_ip,
            src_ip=src_ip,
            dst_host=dst_host,
            user_agent=user_agent,
            client_transaction_id=client_transaction_id,
        )

        metadata_object.additional_properties = d
        return metadata_object

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
