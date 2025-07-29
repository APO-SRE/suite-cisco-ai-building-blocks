from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.br_status_operation import BrStatusOperation
from ..models.br_status_state import BrStatusState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.br_status_details import BrStatusDetails
    from ..models.br_status_restore_config import BrStatusRestoreConfig


T = TypeVar("T", bound="BrStatus")


@_attrs_define
class BrStatus:
    """
    Attributes:
        id (Union[Unset, str]): internal operation id
        operation (Union[Unset, BrStatusOperation]): Type of operation
        state (Union[Unset, BrStatusState]): Current state of the operation
        error (Union[Unset, str]): Error occurred during the operation
        restore_config (Union[Unset, BrStatusRestoreConfig]): Configuration used for restore operations
        details (Union[Unset, BrStatusDetails]): Backup/Restore operation details
    """

    id: Union[Unset, str] = UNSET
    operation: Union[Unset, BrStatusOperation] = UNSET
    state: Union[Unset, BrStatusState] = UNSET
    error: Union[Unset, str] = UNSET
    restore_config: Union[Unset, "BrStatusRestoreConfig"] = UNSET
    details: Union[Unset, "BrStatusDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        operation: Union[Unset, str] = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        error = self.error

        restore_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.restore_config, Unset):
            restore_config = self.restore_config.to_dict()

        details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if operation is not UNSET:
            field_dict["operation"] = operation
        if state is not UNSET:
            field_dict["state"] = state
        if error is not UNSET:
            field_dict["error"] = error
        if restore_config is not UNSET:
            field_dict["restoreConfig"] = restore_config
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.br_status_details import BrStatusDetails
        from ..models.br_status_restore_config import BrStatusRestoreConfig

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _operation = d.pop("operation", UNSET)
        operation: Union[Unset, BrStatusOperation]
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = BrStatusOperation(_operation)

        _state = d.pop("state", UNSET)
        state: Union[Unset, BrStatusState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = BrStatusState(_state)

        error = d.pop("error", UNSET)

        _restore_config = d.pop("restoreConfig", UNSET)
        restore_config: Union[Unset, BrStatusRestoreConfig]
        if isinstance(_restore_config, Unset):
            restore_config = UNSET
        else:
            restore_config = BrStatusRestoreConfig.from_dict(_restore_config)

        _details = d.pop("details", UNSET)
        details: Union[Unset, BrStatusDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = BrStatusDetails.from_dict(_details)

        br_status = cls(
            id=id,
            operation=operation,
            state=state,
            error=error,
            restore_config=restore_config,
            details=details,
        )

        br_status.additional_properties = d
        return br_status

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
