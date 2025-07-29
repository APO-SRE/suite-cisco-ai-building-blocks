from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vendor import Vendor


T = TypeVar("T", bound="App")


@_attrs_define
class App:
    """The information about the application.

    Attributes:
        category (Union[Unset, str]): The app's category.
        id (Union[Unset, str]): The internal Cloudlock id for the application.
        install_type (Union[Unset, str]): A string that describes the installation type (across the domain or by a
            user). Possible values are: domain_wide, user.
        is_revokable (Union[Unset, bool]): Indicates whether the app can be revoked.
        name (Union[Unset, str]): The name of the application, for example: Google Drive.
        origin_id (Union[Unset, str]): The location where the app was installed.
        trust_rating (Union[Unset, str]): The community trust rating score.
        vendor (Union[Unset, Vendor]):
    """

    category: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    install_type: Union[Unset, str] = UNSET
    is_revokable: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    origin_id: Union[Unset, str] = UNSET
    trust_rating: Union[Unset, str] = UNSET
    vendor: Union[Unset, "Vendor"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        id = self.id

        install_type = self.install_type

        is_revokable = self.is_revokable

        name = self.name

        origin_id = self.origin_id

        trust_rating = self.trust_rating

        vendor: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vendor, Unset):
            vendor = self.vendor.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if id is not UNSET:
            field_dict["id"] = id
        if install_type is not UNSET:
            field_dict["install_type"] = install_type
        if is_revokable is not UNSET:
            field_dict["is_revokable"] = is_revokable
        if name is not UNSET:
            field_dict["name"] = name
        if origin_id is not UNSET:
            field_dict["origin_id"] = origin_id
        if trust_rating is not UNSET:
            field_dict["trust_rating"] = trust_rating
        if vendor is not UNSET:
            field_dict["vendor"] = vendor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vendor import Vendor

        d = dict(src_dict)
        category = d.pop("category", UNSET)

        id = d.pop("id", UNSET)

        install_type = d.pop("install_type", UNSET)

        is_revokable = d.pop("is_revokable", UNSET)

        name = d.pop("name", UNSET)

        origin_id = d.pop("origin_id", UNSET)

        trust_rating = d.pop("trust_rating", UNSET)

        _vendor = d.pop("vendor", UNSET)
        vendor: Union[Unset, Vendor]
        if isinstance(_vendor, Unset):
            vendor = UNSET
        else:
            vendor = Vendor.from_dict(_vendor)

        app = cls(
            category=category,
            id=id,
            install_type=install_type,
            is_revokable=is_revokable,
            name=name,
            origin_id=origin_id,
            trust_rating=trust_rating,
            vendor=vendor,
        )

        app.additional_properties = d
        return app

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
