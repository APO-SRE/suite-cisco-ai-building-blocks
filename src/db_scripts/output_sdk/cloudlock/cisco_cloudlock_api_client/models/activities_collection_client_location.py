from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activities_collection_client_location_country import ActivitiesCollectionClientLocationCountry
    from ..models.activities_collection_client_location_region import ActivitiesCollectionClientLocationRegion


T = TypeVar("T", bound="ActivitiesCollectionClientLocation")


@_attrs_define
class ActivitiesCollectionClientLocation:
    """The client location information.

    Attributes:
        city (Union[Unset, str]):
        country (Union[Unset, ActivitiesCollectionClientLocationCountry]):
        lat (Union[Unset, str]):
        lng (Union[Unset, str]):
        region (Union[Unset, ActivitiesCollectionClientLocationRegion]):
    """

    city: Union[Unset, str] = UNSET
    country: Union[Unset, "ActivitiesCollectionClientLocationCountry"] = UNSET
    lat: Union[Unset, str] = UNSET
    lng: Union[Unset, str] = UNSET
    region: Union[Unset, "ActivitiesCollectionClientLocationRegion"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        city = self.city

        country: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        lat = self.lat

        lng = self.lng

        region: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lng is not UNSET:
            field_dict["lng"] = lng
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activities_collection_client_location_country import ActivitiesCollectionClientLocationCountry
        from ..models.activities_collection_client_location_region import ActivitiesCollectionClientLocationRegion

        d = dict(src_dict)
        city = d.pop("city", UNSET)

        _country = d.pop("country", UNSET)
        country: Union[Unset, ActivitiesCollectionClientLocationCountry]
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = ActivitiesCollectionClientLocationCountry.from_dict(_country)

        lat = d.pop("lat", UNSET)

        lng = d.pop("lng", UNSET)

        _region = d.pop("region", UNSET)
        region: Union[Unset, ActivitiesCollectionClientLocationRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = ActivitiesCollectionClientLocationRegion.from_dict(_region)

        activities_collection_client_location = cls(
            city=city,
            country=country,
            lat=lat,
            lng=lng,
            region=region,
        )

        activities_collection_client_location.additional_properties = d
        return activities_collection_client_location

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
