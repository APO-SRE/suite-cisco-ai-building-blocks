from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.config_latch_state import ConfigLatchState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_path_path_id import SchemaPathPathId


T = TypeVar("T", bound="ConfigAssertion")


@_attrs_define
class ConfigAssertion:
    """Description not available

    Attributes:
        path (Union[Unset, SchemaPathPathId]): PathId identifies the specific "schema coordinates" identifier of an
            object in the schema tree.
        state (Union[Unset, ConfigLatchState]): Specifies the latch state for an assertion.
    """

    path: Union[Unset, "SchemaPathPathId"] = UNSET
    state: Union[Unset, ConfigLatchState] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.path, Unset):
            path = self.path.to_dict()

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_path_path_id import SchemaPathPathId

        d = dict(src_dict)
        _path = d.pop("path", UNSET)
        path: Union[Unset, SchemaPathPathId]
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = SchemaPathPathId.from_dict(_path)

        _state = d.pop("state", UNSET)
        state: Union[Unset, ConfigLatchState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ConfigLatchState(_state)

        config_assertion = cls(
            path=path,
            state=state,
        )

        config_assertion.additional_properties = d
        return config_assertion

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
