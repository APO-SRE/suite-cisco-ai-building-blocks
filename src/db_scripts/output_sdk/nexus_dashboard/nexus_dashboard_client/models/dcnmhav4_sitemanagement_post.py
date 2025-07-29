from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DCNMHAV4SitemanagementPOST")


@_attrs_define
class DCNMHAV4SitemanagementPOST:
    """
    Attributes:
        inband_ip (Union[Unset, str]): DCNM controller node inbandIP
        mode (Union[Unset, str]): DCNM controller node mode - active/standby/standalone
        outofband_ip (Union[Unset, str]): DCNM controller node outofbandIP
        version (Union[Unset, str]): DCNM controller node version
    """

    inband_ip: Union[Unset, str] = UNSET
    mode: Union[Unset, str] = UNSET
    outofband_ip: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inband_ip = self.inband_ip

        mode = self.mode

        outofband_ip = self.outofband_ip

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inband_ip is not UNSET:
            field_dict["inbandIP"] = inband_ip
        if mode is not UNSET:
            field_dict["mode"] = mode
        if outofband_ip is not UNSET:
            field_dict["outofbandIP"] = outofband_ip
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inband_ip = d.pop("inbandIP", UNSET)

        mode = d.pop("mode", UNSET)

        outofband_ip = d.pop("outofbandIP", UNSET)

        version = d.pop("version", UNSET)

        dcnmhav4_sitemanagement_post = cls(
            inband_ip=inband_ip,
            mode=mode,
            outofband_ip=outofband_ip,
            version=version,
        )

        dcnmhav4_sitemanagement_post.additional_properties = d
        return dcnmhav4_sitemanagement_post

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
