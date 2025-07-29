from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReconcileSpecWrapperV1ArgoCiscoComPOST")


@_attrs_define
class ReconcileSpecWrapperV1ArgoCiscoComPOST:
    """
    Attributes:
        dn (Union[Unset, str]):
        kind (Union[Unset, str]):
        org (Union[Unset, str]):
    """

    dn: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    org: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dn = self.dn

        kind = self.kind

        org = self.org

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dn is not UNSET:
            field_dict["dn"] = dn
        if kind is not UNSET:
            field_dict["kind"] = kind
        if org is not UNSET:
            field_dict["org"] = org

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dn = d.pop("dn", UNSET)

        kind = d.pop("kind", UNSET)

        org = d.pop("org", UNSET)

        reconcile_spec_wrapper_v1_argo_cisco_com_post = cls(
            dn=dn,
            kind=kind,
            org=org,
        )

        reconcile_spec_wrapper_v1_argo_cisco_com_post.additional_properties = d
        return reconcile_spec_wrapper_v1_argo_cisco_com_post

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
