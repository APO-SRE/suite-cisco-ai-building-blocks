from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reconcile_record_entry_v1_argo_cisco_com_get import ReconcileRecordEntryV1ArgoCiscoComGET


T = TypeVar("T", bound="ReconcileRecordSpecWrapperV1ArgoCiscoComGETInstances")


@_attrs_define
class ReconcileRecordSpecWrapperV1ArgoCiscoComGETInstances:
    """ """

    additional_properties: dict[str, "ReconcileRecordEntryV1ArgoCiscoComGET"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reconcile_record_entry_v1_argo_cisco_com_get import ReconcileRecordEntryV1ArgoCiscoComGET

        d = dict(src_dict)
        reconcile_record_spec_wrapper_v1_argo_cisco_com_get_instances = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ReconcileRecordEntryV1ArgoCiscoComGET.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        reconcile_record_spec_wrapper_v1_argo_cisco_com_get_instances.additional_properties = additional_properties
        return reconcile_record_spec_wrapper_v1_argo_cisco_com_get_instances

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "ReconcileRecordEntryV1ArgoCiscoComGET":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "ReconcileRecordEntryV1ArgoCiscoComGET") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
