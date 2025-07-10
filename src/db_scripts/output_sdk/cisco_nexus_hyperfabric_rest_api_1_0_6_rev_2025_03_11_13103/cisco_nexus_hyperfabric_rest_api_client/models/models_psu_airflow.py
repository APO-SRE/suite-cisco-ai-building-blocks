from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_airflow_type import ModelsAirflowType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsPsuAirflow")


@_attrs_define
class ModelsPsuAirflow:
    """PsuAirflow encapsulates Airflow and corresponding Psu model.

    Attributes:
        airflow (Union[Unset, ModelsAirflowType]): Airflow enumerates various types of Airflow.
        psu_model (Union[Unset, str]): Description not available
    """

    airflow: Union[Unset, ModelsAirflowType] = UNSET
    psu_model: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        airflow: Union[Unset, str] = UNSET
        if not isinstance(self.airflow, Unset):
            airflow = self.airflow.value

        psu_model = self.psu_model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if airflow is not UNSET:
            field_dict["airflow"] = airflow
        if psu_model is not UNSET:
            field_dict["psuModel"] = psu_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _airflow = d.pop("airflow", UNSET)
        airflow: Union[Unset, ModelsAirflowType]
        if isinstance(_airflow, Unset):
            airflow = UNSET
        else:
            airflow = ModelsAirflowType(_airflow)

        psu_model = d.pop("psuModel", UNSET)

        models_psu_airflow = cls(
            airflow=airflow,
            psu_model=psu_model,
        )

        models_psu_airflow.additional_properties = d
        return models_psu_airflow

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
