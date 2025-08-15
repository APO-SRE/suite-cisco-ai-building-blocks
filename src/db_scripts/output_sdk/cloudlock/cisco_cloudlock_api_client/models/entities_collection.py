from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.permission_resource import PermissionResource
    from ..models.vendor import Vendor


T = TypeVar("T", bound="EntitiesCollection")


@_attrs_define
class EntitiesCollection:
    """
    Attributes:
        id (Union[Unset, str]): The unique internal identifier for the asset.
        vendor (Union[Unset, Vendor]):
        origin_id (Union[Unset, str]): The unique identifier for the asset provided by the origin platform/vendor.
        origin_type (Union[Unset, str]): The equivalent to vendor_type. Example: document, post, event, app, site.
        asset_type (Union[Unset, str]): google_document, google_spreadsheet, google_form, google_drawing Example:
            google_presentation, google_site, folder, non_native_file, pdf.
        owners (Union[Unset, list['PermissionResource']]):
        mime_type (Union[Unset, str]):
        exposure (Union[Unset, str]): The exposure level of the document. Example: public, externally shared,
            organization-wide, internally shared, private.
        collaborators_count (Union[Unset, int]): The total number of collaborators on an asset.
        name (Union[Unset, str]): The title, name of the asset.
        size (Union[Unset, int]): The size of the asset in bytes.
        updated_at (Union[Unset, str]): The last time the asset has been modified, specified as a timestamp in UTC.
        created_at (Union[Unset, str]): The time at which the asset was created, specified as a timestamp in UTC.
        direct_url (Union[Unset, str]): The URL for the asset.
        collaborators (Union[Unset, list['PermissionResource']]):
    """

    id: Union[Unset, str] = UNSET
    vendor: Union[Unset, "Vendor"] = UNSET
    origin_id: Union[Unset, str] = UNSET
    origin_type: Union[Unset, str] = UNSET
    asset_type: Union[Unset, str] = UNSET
    owners: Union[Unset, list["PermissionResource"]] = UNSET
    mime_type: Union[Unset, str] = UNSET
    exposure: Union[Unset, str] = UNSET
    collaborators_count: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    updated_at: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    direct_url: Union[Unset, str] = UNSET
    collaborators: Union[Unset, list["PermissionResource"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        vendor: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vendor, Unset):
            vendor = self.vendor.to_dict()

        origin_id = self.origin_id

        origin_type = self.origin_type

        asset_type = self.asset_type

        owners: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.owners, Unset):
            owners = []
            for owners_item_data in self.owners:
                owners_item = owners_item_data.to_dict()
                owners.append(owners_item)

        mime_type = self.mime_type

        exposure = self.exposure

        collaborators_count = self.collaborators_count

        name = self.name

        size = self.size

        updated_at = self.updated_at

        created_at = self.created_at

        direct_url = self.direct_url

        collaborators: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.collaborators, Unset):
            collaborators = []
            for collaborators_item_data in self.collaborators:
                collaborators_item = collaborators_item_data.to_dict()
                collaborators.append(collaborators_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if origin_id is not UNSET:
            field_dict["origin_id"] = origin_id
        if origin_type is not UNSET:
            field_dict["origin_type"] = origin_type
        if asset_type is not UNSET:
            field_dict["asset_type"] = asset_type
        if owners is not UNSET:
            field_dict["owners"] = owners
        if mime_type is not UNSET:
            field_dict["mime_type"] = mime_type
        if exposure is not UNSET:
            field_dict["exposure"] = exposure
        if collaborators_count is not UNSET:
            field_dict["collaborators_count"] = collaborators_count
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if direct_url is not UNSET:
            field_dict["direct_url"] = direct_url
        if collaborators is not UNSET:
            field_dict["collaborators"] = collaborators

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_resource import PermissionResource
        from ..models.vendor import Vendor

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _vendor = d.pop("vendor", UNSET)
        vendor: Union[Unset, Vendor]
        if isinstance(_vendor, Unset):
            vendor = UNSET
        else:
            vendor = Vendor.from_dict(_vendor)

        origin_id = d.pop("origin_id", UNSET)

        origin_type = d.pop("origin_type", UNSET)

        asset_type = d.pop("asset_type", UNSET)

        owners = []
        _owners = d.pop("owners", UNSET)
        for owners_item_data in _owners or []:
            owners_item = PermissionResource.from_dict(owners_item_data)

            owners.append(owners_item)

        mime_type = d.pop("mime_type", UNSET)

        exposure = d.pop("exposure", UNSET)

        collaborators_count = d.pop("collaborators_count", UNSET)

        name = d.pop("name", UNSET)

        size = d.pop("size", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        direct_url = d.pop("direct_url", UNSET)

        collaborators = []
        _collaborators = d.pop("collaborators", UNSET)
        for collaborators_item_data in _collaborators or []:
            collaborators_item = PermissionResource.from_dict(collaborators_item_data)

            collaborators.append(collaborators_item)

        entities_collection = cls(
            id=id,
            vendor=vendor,
            origin_id=origin_id,
            origin_type=origin_type,
            asset_type=asset_type,
            owners=owners,
            mime_type=mime_type,
            exposure=exposure,
            collaborators_count=collaborators_count,
            name=name,
            size=size,
            updated_at=updated_at,
            created_at=created_at,
            direct_url=direct_url,
            collaborators=collaborators,
        )

        entities_collection.additional_properties = d
        return entities_collection

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
