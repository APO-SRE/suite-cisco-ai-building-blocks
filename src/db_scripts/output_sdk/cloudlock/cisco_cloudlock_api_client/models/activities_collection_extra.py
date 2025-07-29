from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activities_collection_extra_auth import ActivitiesCollectionExtraAuth


T = TypeVar("T", bound="ActivitiesCollectionExtra")


@_attrs_define
class ActivitiesCollectionExtra:
    """Additional information related to the activity

    Attributes:
        auth (Union[Unset, ActivitiesCollectionExtraAuth]):
    """

    auth: Union[Unset, "ActivitiesCollectionExtraAuth"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.auth, Unset):
            auth = self.auth.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth is not UNSET:
            field_dict["auth"] = auth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activities_collection_extra_auth import ActivitiesCollectionExtraAuth

        d = dict(src_dict)
        _auth = d.pop("auth", UNSET)
        auth: Union[Unset, ActivitiesCollectionExtraAuth]
        if isinstance(_auth, Unset):
            auth = UNSET
        else:
            auth = ActivitiesCollectionExtraAuth.from_dict(_auth)

        activities_collection_extra = cls(
            auth=auth,
        )

        activities_collection_extra.additional_properties = d
        return activities_collection_extra

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
