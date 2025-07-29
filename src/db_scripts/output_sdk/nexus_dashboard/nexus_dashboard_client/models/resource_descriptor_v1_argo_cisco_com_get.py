from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_descriptor_v1_argo_cisco_com_get_url import ResourceDescriptorV1ArgoCiscoComGETUrl


T = TypeVar("T", bound="ResourceDescriptorV1ArgoCiscoComGET")


@_attrs_define
class ResourceDescriptorV1ArgoCiscoComGET:
    """
    Attributes:
        endpoint (Union[Unset, str]):
        name (Union[Unset, str]):
        service (Union[Unset, str]):
        url (Union[Unset, ResourceDescriptorV1ArgoCiscoComGETUrl]):
    """

    endpoint: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    service: Union[Unset, str] = UNSET
    url: Union[Unset, "ResourceDescriptorV1ArgoCiscoComGETUrl"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint = self.endpoint

        name = self.name

        service = self.service

        url: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.url, Unset):
            url = self.url.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if name is not UNSET:
            field_dict["name"] = name
        if service is not UNSET:
            field_dict["service"] = service
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_descriptor_v1_argo_cisco_com_get_url import ResourceDescriptorV1ArgoCiscoComGETUrl

        d = dict(src_dict)
        endpoint = d.pop("endpoint", UNSET)

        name = d.pop("name", UNSET)

        service = d.pop("service", UNSET)

        _url = d.pop("url", UNSET)
        url: Union[Unset, ResourceDescriptorV1ArgoCiscoComGETUrl]
        if isinstance(_url, Unset):
            url = UNSET
        else:
            url = ResourceDescriptorV1ArgoCiscoComGETUrl.from_dict(_url)

        resource_descriptor_v1_argo_cisco_com_get = cls(
            endpoint=endpoint,
            name=name,
            service=service,
            url=url,
        )

        resource_descriptor_v1_argo_cisco_com_get.additional_properties = d
        return resource_descriptor_v1_argo_cisco_com_get

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
