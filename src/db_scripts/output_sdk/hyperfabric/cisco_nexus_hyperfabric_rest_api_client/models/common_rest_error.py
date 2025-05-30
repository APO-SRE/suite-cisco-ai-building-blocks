from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.common_err_code import CommonErrCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommonRestError")


@_attrs_define
class CommonRestError:
    """RestError encapsulates the properties of a REST error.

    Attributes:
        causes (Union[Unset, list[str]]): A list of underlying causes.
        critical (Union[Unset, bool]): Indicates that the error is a critical error.
        err_code (Union[Unset, CommonErrCode]): An error code provides additional information about a failed API
            request.
        field (Union[Unset, str]): The name of relevant field.
        message (Union[Unset, str]): The error message.
        notes (Union[Unset, str]): Additional information about the error.
        status (Union[Unset, int]): The http status code.
        tracking_id (Union[Unset, str]): A unique value for each request, used for tracking purposes.
        value (Union[Unset, str]): The value of relevant field.
    """

    causes: Union[Unset, list[str]] = UNSET
    critical: Union[Unset, bool] = UNSET
    err_code: Union[Unset, CommonErrCode] = UNSET
    field: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    status: Union[Unset, int] = UNSET
    tracking_id: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        causes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.causes, Unset):
            causes = self.causes

        critical = self.critical

        err_code: Union[Unset, str] = UNSET
        if not isinstance(self.err_code, Unset):
            err_code = self.err_code.value

        field = self.field

        message = self.message

        notes = self.notes

        status = self.status

        tracking_id = self.tracking_id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if causes is not UNSET:
            field_dict["causes"] = causes
        if critical is not UNSET:
            field_dict["critical"] = critical
        if err_code is not UNSET:
            field_dict["errCode"] = err_code
        if field is not UNSET:
            field_dict["field"] = field
        if message is not UNSET:
            field_dict["message"] = message
        if notes is not UNSET:
            field_dict["notes"] = notes
        if status is not UNSET:
            field_dict["status"] = status
        if tracking_id is not UNSET:
            field_dict["trackingId"] = tracking_id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        causes = cast(list[str], d.pop("causes", UNSET))

        critical = d.pop("critical", UNSET)

        _err_code = d.pop("errCode", UNSET)
        err_code: Union[Unset, CommonErrCode]
        if isinstance(_err_code, Unset):
            err_code = UNSET
        else:
            err_code = CommonErrCode(_err_code)

        field = d.pop("field", UNSET)

        message = d.pop("message", UNSET)

        notes = d.pop("notes", UNSET)

        status = d.pop("status", UNSET)

        tracking_id = d.pop("trackingId", UNSET)

        value = d.pop("value", UNSET)

        common_rest_error = cls(
            causes=causes,
            critical=critical,
            err_code=err_code,
            field=field,
            message=message,
            notes=notes,
            status=status,
            tracking_id=tracking_id,
            value=value,
        )

        common_rest_error.additional_properties = d
        return common_rest_error

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
