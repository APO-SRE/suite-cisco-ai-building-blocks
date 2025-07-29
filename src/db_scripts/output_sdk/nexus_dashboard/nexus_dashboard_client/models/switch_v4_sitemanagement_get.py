from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SwitchV4SitemanagementGET")


@_attrs_define
class SwitchV4SitemanagementGET:
    """
    Attributes:
        inband_ip (Union[Unset, str]): switch inband IP
        model (Union[Unset, str]): switch model
        outofband_ip (Union[Unset, str]): switch outofband IP
        sn (Union[Unset, str]): switch serial number
        type_ (Union[Unset, str]): switch type
        version (Union[Unset, str]): switch image version
    """

    inband_ip: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    outofband_ip: Union[Unset, str] = UNSET
    sn: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inband_ip = self.inband_ip

        model = self.model

        outofband_ip = self.outofband_ip

        sn = self.sn

        type_ = self.type_

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inband_ip is not UNSET:
            field_dict["inbandIP"] = inband_ip
        if model is not UNSET:
            field_dict["model"] = model
        if outofband_ip is not UNSET:
            field_dict["outofbandIP"] = outofband_ip
        if sn is not UNSET:
            field_dict["sn"] = sn
        if type_ is not UNSET:
            field_dict["type"] = type_
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inband_ip = d.pop("inbandIP", UNSET)

        model = d.pop("model", UNSET)

        outofband_ip = d.pop("outofbandIP", UNSET)

        sn = d.pop("sn", UNSET)

        type_ = d.pop("type", UNSET)

        version = d.pop("version", UNSET)

        switch_v4_sitemanagement_get = cls(
            inband_ip=inband_ip,
            model=model,
            outofband_ip=outofband_ip,
            sn=sn,
            type_=type_,
            version=version,
        )

        switch_v4_sitemanagement_get.additional_properties = d
        return switch_v4_sitemanagement_get

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
