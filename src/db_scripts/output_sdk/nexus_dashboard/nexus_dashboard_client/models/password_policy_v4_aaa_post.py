from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PasswordPolicyV4AaaPOST")


@_attrs_define
class PasswordPolicyV4AaaPOST:
    """
    Attributes:
        reuse_limitation (Union[Unset, int]): Password Reuse Limitation
        time_interval_limitation (Union[Unset, int]): Password Time Interval Limitation
    """

    reuse_limitation: Union[Unset, int] = UNSET
    time_interval_limitation: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reuse_limitation = self.reuse_limitation

        time_interval_limitation = self.time_interval_limitation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reuse_limitation is not UNSET:
            field_dict["reuseLimitation"] = reuse_limitation
        if time_interval_limitation is not UNSET:
            field_dict["timeIntervalLimitation"] = time_interval_limitation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reuse_limitation = d.pop("reuseLimitation", UNSET)

        time_interval_limitation = d.pop("timeIntervalLimitation", UNSET)

        password_policy_v4_aaa_post = cls(
            reuse_limitation=reuse_limitation,
            time_interval_limitation=time_interval_limitation,
        )

        password_policy_v4_aaa_post.additional_properties = d
        return password_policy_v4_aaa_post

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
