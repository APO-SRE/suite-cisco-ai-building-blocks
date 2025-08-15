from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rbacv4_aaa_put import RBACV4AaaPUT


T = TypeVar("T", bound="RemoteUserSpecV4AaaPUT")


@_attrs_define
class RemoteUserSpecV4AaaPUT:
    """
    Attributes:
        cisco_av_pair (Union[Unset, str]): Remote user ciscoAVPair
        description (Union[Unset, str]): Description about remote user
        login_domain (Union[Unset, str]): Login domain that the remote user has logged in to
        login_id (Union[Unset, str]): Remote user login ID
        login_time (Union[Unset, str]): Remote user login timestamp
        rbac (Union[Unset, RBACV4AaaPUT]):
    """

    cisco_av_pair: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    login_domain: Union[Unset, str] = UNSET
    login_id: Union[Unset, str] = UNSET
    login_time: Union[Unset, str] = UNSET
    rbac: Union[Unset, "RBACV4AaaPUT"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cisco_av_pair = self.cisco_av_pair

        description = self.description

        login_domain = self.login_domain

        login_id = self.login_id

        login_time = self.login_time

        rbac: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rbac, Unset):
            rbac = self.rbac.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cisco_av_pair is not UNSET:
            field_dict["ciscoAVPair"] = cisco_av_pair
        if description is not UNSET:
            field_dict["description"] = description
        if login_domain is not UNSET:
            field_dict["loginDomain"] = login_domain
        if login_id is not UNSET:
            field_dict["loginID"] = login_id
        if login_time is not UNSET:
            field_dict["loginTime"] = login_time
        if rbac is not UNSET:
            field_dict["rbac"] = rbac

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rbacv4_aaa_put import RBACV4AaaPUT

        d = dict(src_dict)
        cisco_av_pair = d.pop("ciscoAVPair", UNSET)

        description = d.pop("description", UNSET)

        login_domain = d.pop("loginDomain", UNSET)

        login_id = d.pop("loginID", UNSET)

        login_time = d.pop("loginTime", UNSET)

        _rbac = d.pop("rbac", UNSET)
        rbac: Union[Unset, RBACV4AaaPUT]
        if isinstance(_rbac, Unset):
            rbac = UNSET
        else:
            rbac = RBACV4AaaPUT.from_dict(_rbac)

        remote_user_spec_v4_aaa_put = cls(
            cisco_av_pair=cisco_av_pair,
            description=description,
            login_domain=login_domain,
            login_id=login_id,
            login_time=login_time,
            rbac=rbac,
        )

        remote_user_spec_v4_aaa_put.additional_properties = d
        return remote_user_spec_v4_aaa_put

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
