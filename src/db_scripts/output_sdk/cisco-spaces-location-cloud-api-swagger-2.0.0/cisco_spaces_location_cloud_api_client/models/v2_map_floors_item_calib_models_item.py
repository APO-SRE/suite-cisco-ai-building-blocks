from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V2MapFloorsItemCalibModelsItem")


@_attrs_define
class V2MapFloorsItemCalibModelsItem:
    """
    Attributes:
        dot_11_a_param_1_with_walls (Union[Unset, float]):  Example: -3.6.
        dot_11_b_param_2 (Union[Unset, float]):  Example: -40.
        heat_map_cutoff (Union[Unset, float]):  Example: -112.
        dot_11_b_param_3 (Union[Unset, float]):  Example: 7.
        use_walls (Union[Unset, bool]):
        cov_dot_11_b_param_3 (Union[Unset, float]):  Example: 7.
        dot_11_b_param_1 (Union[Unset, float]):  Example: -3.6.
        cov_dot_11_b_param_2 (Union[Unset, float]):  Example: -40.
        sweep_client_power (Union[Unset, bool]):
        cov_dot_11_b_param_1 (Union[Unset, float]):  Example: -3.6.
        calibration_type (Union[Unset, str]):  Example: NOT_SITE_SURVEY.
        imported_id (Union[Unset, float]):  Example: -6550507210156278000.
        dot_11_b_param_3_with_walls (Union[Unset, float]):  Example: 7.
        id (Union[Unset, str]): Unique Location ID Example: 22d7c349-4735-44cf-b42e-b94d3c7f9e4a.
        dot_11_a_param_3_with_walls (Union[Unset, float]):  Example: 7.
        cov_dot_11_a_param_3 (Union[Unset, float]):  Example: 7.
        dot_11_b_param_2_with_walls (Union[Unset, float]):  Example: -40.
        dot_11_a_param_1 (Union[Unset, float]):  Example: -3.6.
        dot_11_a_param_2 (Union[Unset, float]):  Example: -47.
        dot_11_a_param_3 (Union[Unset, float]):  Example: 7.
        bin_size (Union[Unset, float]):  Example: 8.
        cov_dot_11_a_param_2 (Union[Unset, float]):  Example: -47.
        cov_dot_11_a_param_1 (Union[Unset, float]):  Example: -3.6.
        model_name (Union[Unset, str]): Model name Example: Cubes And Walled Offices.
        dot_11_a_param_2_with_walls (Union[Unset, float]):  Example: -47.
        dot_11_b_param_1_with_walls (Union[Unset, float]):  Example: -3.6.
    """

    dot_11_a_param_1_with_walls: Union[Unset, float] = UNSET
    dot_11_b_param_2: Union[Unset, float] = UNSET
    heat_map_cutoff: Union[Unset, float] = UNSET
    dot_11_b_param_3: Union[Unset, float] = UNSET
    use_walls: Union[Unset, bool] = UNSET
    cov_dot_11_b_param_3: Union[Unset, float] = UNSET
    dot_11_b_param_1: Union[Unset, float] = UNSET
    cov_dot_11_b_param_2: Union[Unset, float] = UNSET
    sweep_client_power: Union[Unset, bool] = UNSET
    cov_dot_11_b_param_1: Union[Unset, float] = UNSET
    calibration_type: Union[Unset, str] = UNSET
    imported_id: Union[Unset, float] = UNSET
    dot_11_b_param_3_with_walls: Union[Unset, float] = UNSET
    id: Union[Unset, str] = UNSET
    dot_11_a_param_3_with_walls: Union[Unset, float] = UNSET
    cov_dot_11_a_param_3: Union[Unset, float] = UNSET
    dot_11_b_param_2_with_walls: Union[Unset, float] = UNSET
    dot_11_a_param_1: Union[Unset, float] = UNSET
    dot_11_a_param_2: Union[Unset, float] = UNSET
    dot_11_a_param_3: Union[Unset, float] = UNSET
    bin_size: Union[Unset, float] = UNSET
    cov_dot_11_a_param_2: Union[Unset, float] = UNSET
    cov_dot_11_a_param_1: Union[Unset, float] = UNSET
    model_name: Union[Unset, str] = UNSET
    dot_11_a_param_2_with_walls: Union[Unset, float] = UNSET
    dot_11_b_param_1_with_walls: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dot_11_a_param_1_with_walls = self.dot_11_a_param_1_with_walls

        dot_11_b_param_2 = self.dot_11_b_param_2

        heat_map_cutoff = self.heat_map_cutoff

        dot_11_b_param_3 = self.dot_11_b_param_3

        use_walls = self.use_walls

        cov_dot_11_b_param_3 = self.cov_dot_11_b_param_3

        dot_11_b_param_1 = self.dot_11_b_param_1

        cov_dot_11_b_param_2 = self.cov_dot_11_b_param_2

        sweep_client_power = self.sweep_client_power

        cov_dot_11_b_param_1 = self.cov_dot_11_b_param_1

        calibration_type = self.calibration_type

        imported_id = self.imported_id

        dot_11_b_param_3_with_walls = self.dot_11_b_param_3_with_walls

        id = self.id

        dot_11_a_param_3_with_walls = self.dot_11_a_param_3_with_walls

        cov_dot_11_a_param_3 = self.cov_dot_11_a_param_3

        dot_11_b_param_2_with_walls = self.dot_11_b_param_2_with_walls

        dot_11_a_param_1 = self.dot_11_a_param_1

        dot_11_a_param_2 = self.dot_11_a_param_2

        dot_11_a_param_3 = self.dot_11_a_param_3

        bin_size = self.bin_size

        cov_dot_11_a_param_2 = self.cov_dot_11_a_param_2

        cov_dot_11_a_param_1 = self.cov_dot_11_a_param_1

        model_name = self.model_name

        dot_11_a_param_2_with_walls = self.dot_11_a_param_2_with_walls

        dot_11_b_param_1_with_walls = self.dot_11_b_param_1_with_walls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dot_11_a_param_1_with_walls is not UNSET:
            field_dict["dot11aParam1WithWalls"] = dot_11_a_param_1_with_walls
        if dot_11_b_param_2 is not UNSET:
            field_dict["dot11bParam2"] = dot_11_b_param_2
        if heat_map_cutoff is not UNSET:
            field_dict["heatMapCutoff"] = heat_map_cutoff
        if dot_11_b_param_3 is not UNSET:
            field_dict["dot11bParam3"] = dot_11_b_param_3
        if use_walls is not UNSET:
            field_dict["useWalls"] = use_walls
        if cov_dot_11_b_param_3 is not UNSET:
            field_dict["covDot11bParam3"] = cov_dot_11_b_param_3
        if dot_11_b_param_1 is not UNSET:
            field_dict["dot11bParam1"] = dot_11_b_param_1
        if cov_dot_11_b_param_2 is not UNSET:
            field_dict["covDot11bParam2"] = cov_dot_11_b_param_2
        if sweep_client_power is not UNSET:
            field_dict["sweepClientPower"] = sweep_client_power
        if cov_dot_11_b_param_1 is not UNSET:
            field_dict["covDot11bParam1"] = cov_dot_11_b_param_1
        if calibration_type is not UNSET:
            field_dict["calibrationType"] = calibration_type
        if imported_id is not UNSET:
            field_dict["importedId"] = imported_id
        if dot_11_b_param_3_with_walls is not UNSET:
            field_dict["dot11bParam3WithWalls"] = dot_11_b_param_3_with_walls
        if id is not UNSET:
            field_dict["id"] = id
        if dot_11_a_param_3_with_walls is not UNSET:
            field_dict["dot11aParam3WithWalls"] = dot_11_a_param_3_with_walls
        if cov_dot_11_a_param_3 is not UNSET:
            field_dict["covDot11aParam3"] = cov_dot_11_a_param_3
        if dot_11_b_param_2_with_walls is not UNSET:
            field_dict["dot11bParam2WithWalls"] = dot_11_b_param_2_with_walls
        if dot_11_a_param_1 is not UNSET:
            field_dict["dot11aParam1"] = dot_11_a_param_1
        if dot_11_a_param_2 is not UNSET:
            field_dict["dot11aParam2"] = dot_11_a_param_2
        if dot_11_a_param_3 is not UNSET:
            field_dict["dot11aParam3"] = dot_11_a_param_3
        if bin_size is not UNSET:
            field_dict["binSize"] = bin_size
        if cov_dot_11_a_param_2 is not UNSET:
            field_dict["covDot11aParam2"] = cov_dot_11_a_param_2
        if cov_dot_11_a_param_1 is not UNSET:
            field_dict["covDot11aParam1"] = cov_dot_11_a_param_1
        if model_name is not UNSET:
            field_dict["modelName"] = model_name
        if dot_11_a_param_2_with_walls is not UNSET:
            field_dict["dot11aParam2WithWalls"] = dot_11_a_param_2_with_walls
        if dot_11_b_param_1_with_walls is not UNSET:
            field_dict["dot11bParam1WithWalls"] = dot_11_b_param_1_with_walls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dot_11_a_param_1_with_walls = d.pop("dot11aParam1WithWalls", UNSET)

        dot_11_b_param_2 = d.pop("dot11bParam2", UNSET)

        heat_map_cutoff = d.pop("heatMapCutoff", UNSET)

        dot_11_b_param_3 = d.pop("dot11bParam3", UNSET)

        use_walls = d.pop("useWalls", UNSET)

        cov_dot_11_b_param_3 = d.pop("covDot11bParam3", UNSET)

        dot_11_b_param_1 = d.pop("dot11bParam1", UNSET)

        cov_dot_11_b_param_2 = d.pop("covDot11bParam2", UNSET)

        sweep_client_power = d.pop("sweepClientPower", UNSET)

        cov_dot_11_b_param_1 = d.pop("covDot11bParam1", UNSET)

        calibration_type = d.pop("calibrationType", UNSET)

        imported_id = d.pop("importedId", UNSET)

        dot_11_b_param_3_with_walls = d.pop("dot11bParam3WithWalls", UNSET)

        id = d.pop("id", UNSET)

        dot_11_a_param_3_with_walls = d.pop("dot11aParam3WithWalls", UNSET)

        cov_dot_11_a_param_3 = d.pop("covDot11aParam3", UNSET)

        dot_11_b_param_2_with_walls = d.pop("dot11bParam2WithWalls", UNSET)

        dot_11_a_param_1 = d.pop("dot11aParam1", UNSET)

        dot_11_a_param_2 = d.pop("dot11aParam2", UNSET)

        dot_11_a_param_3 = d.pop("dot11aParam3", UNSET)

        bin_size = d.pop("binSize", UNSET)

        cov_dot_11_a_param_2 = d.pop("covDot11aParam2", UNSET)

        cov_dot_11_a_param_1 = d.pop("covDot11aParam1", UNSET)

        model_name = d.pop("modelName", UNSET)

        dot_11_a_param_2_with_walls = d.pop("dot11aParam2WithWalls", UNSET)

        dot_11_b_param_1_with_walls = d.pop("dot11bParam1WithWalls", UNSET)

        v2_map_floors_item_calib_models_item = cls(
            dot_11_a_param_1_with_walls=dot_11_a_param_1_with_walls,
            dot_11_b_param_2=dot_11_b_param_2,
            heat_map_cutoff=heat_map_cutoff,
            dot_11_b_param_3=dot_11_b_param_3,
            use_walls=use_walls,
            cov_dot_11_b_param_3=cov_dot_11_b_param_3,
            dot_11_b_param_1=dot_11_b_param_1,
            cov_dot_11_b_param_2=cov_dot_11_b_param_2,
            sweep_client_power=sweep_client_power,
            cov_dot_11_b_param_1=cov_dot_11_b_param_1,
            calibration_type=calibration_type,
            imported_id=imported_id,
            dot_11_b_param_3_with_walls=dot_11_b_param_3_with_walls,
            id=id,
            dot_11_a_param_3_with_walls=dot_11_a_param_3_with_walls,
            cov_dot_11_a_param_3=cov_dot_11_a_param_3,
            dot_11_b_param_2_with_walls=dot_11_b_param_2_with_walls,
            dot_11_a_param_1=dot_11_a_param_1,
            dot_11_a_param_2=dot_11_a_param_2,
            dot_11_a_param_3=dot_11_a_param_3,
            bin_size=bin_size,
            cov_dot_11_a_param_2=cov_dot_11_a_param_2,
            cov_dot_11_a_param_1=cov_dot_11_a_param_1,
            model_name=model_name,
            dot_11_a_param_2_with_walls=dot_11_a_param_2_with_walls,
            dot_11_b_param_1_with_walls=dot_11_b_param_1_with_walls,
        )

        v2_map_floors_item_calib_models_item.additional_properties = d
        return v2_map_floors_item_calib_models_item

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
