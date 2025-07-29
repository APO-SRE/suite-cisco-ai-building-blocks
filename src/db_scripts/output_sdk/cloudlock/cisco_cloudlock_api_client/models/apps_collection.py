from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app import App
    from ..models.classification import Classification
    from ..models.scope_category import ScopeCategory


T = TypeVar("T", bound="AppsCollection")


@_attrs_define
class AppsCollection:
    """
    Attributes:
        id (Union[Unset, str]): The application's internal CloudLock ID.
        app (Union[Unset, App]): The information about the application.
        scope_categories (Union[Unset, list['ScopeCategory']]): The list of application scope category.
        classification (Union[Unset, Classification]): The application's classification resource.
        detected_at (Union[Unset, str]): The time when the app was detected, specified as a timestamp in UTC.
        users_count (Union[Unset, int]): The number of users that have the application installed.
        admins_count (Union[Unset, int]): The number of administrators that have the application installed.
    """

    id: Union[Unset, str] = UNSET
    app: Union[Unset, "App"] = UNSET
    scope_categories: Union[Unset, list["ScopeCategory"]] = UNSET
    classification: Union[Unset, "Classification"] = UNSET
    detected_at: Union[Unset, str] = UNSET
    users_count: Union[Unset, int] = UNSET
    admins_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        app: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app, Unset):
            app = self.app.to_dict()

        scope_categories: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.scope_categories, Unset):
            scope_categories = []
            for scope_categories_item_data in self.scope_categories:
                scope_categories_item = scope_categories_item_data.to_dict()
                scope_categories.append(scope_categories_item)

        classification: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.classification, Unset):
            classification = self.classification.to_dict()

        detected_at = self.detected_at

        users_count = self.users_count

        admins_count = self.admins_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if app is not UNSET:
            field_dict["app"] = app
        if scope_categories is not UNSET:
            field_dict["scope_categories"] = scope_categories
        if classification is not UNSET:
            field_dict["classification"] = classification
        if detected_at is not UNSET:
            field_dict["detected_at"] = detected_at
        if users_count is not UNSET:
            field_dict["users_count"] = users_count
        if admins_count is not UNSET:
            field_dict["admins_count"] = admins_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app import App
        from ..models.classification import Classification
        from ..models.scope_category import ScopeCategory

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _app = d.pop("app", UNSET)
        app: Union[Unset, App]
        if isinstance(_app, Unset):
            app = UNSET
        else:
            app = App.from_dict(_app)

        scope_categories = []
        _scope_categories = d.pop("scope_categories", UNSET)
        for scope_categories_item_data in _scope_categories or []:
            scope_categories_item = ScopeCategory.from_dict(scope_categories_item_data)

            scope_categories.append(scope_categories_item)

        _classification = d.pop("classification", UNSET)
        classification: Union[Unset, Classification]
        if isinstance(_classification, Unset):
            classification = UNSET
        else:
            classification = Classification.from_dict(_classification)

        detected_at = d.pop("detected_at", UNSET)

        users_count = d.pop("users_count", UNSET)

        admins_count = d.pop("admins_count", UNSET)

        apps_collection = cls(
            id=id,
            app=app,
            scope_categories=scope_categories,
            classification=classification,
            detected_at=detected_at,
            users_count=users_count,
            admins_count=admins_count,
        )

        apps_collection.additional_properties = d
        return apps_collection

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
