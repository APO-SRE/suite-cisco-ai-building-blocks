from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_descriptor_v1_argo_cisco_com_get import ResourceDescriptorV1ArgoCiscoComGET
    from ..models.service_descriptor_v1_argo_cisco_com_get import ServiceDescriptorV1ArgoCiscoComGET


T = TypeVar("T", bound="ApplicationSpecWrapperV1ArgoCiscoComGET")


@_attrs_define
class ApplicationSpecWrapperV1ArgoCiscoComGET:
    """
    Attributes:
        name (Union[Unset, str]):
        realm (Union[Unset, str]):
        resources (Union[Unset, list['ResourceDescriptorV1ArgoCiscoComGET']]):
        services (Union[Unset, list['ServiceDescriptorV1ArgoCiscoComGET']]):
        url_list (Union[Unset, list[str]]):
        url_tree (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    realm: Union[Unset, str] = UNSET
    resources: Union[Unset, list["ResourceDescriptorV1ArgoCiscoComGET"]] = UNSET
    services: Union[Unset, list["ServiceDescriptorV1ArgoCiscoComGET"]] = UNSET
    url_list: Union[Unset, list[str]] = UNSET
    url_tree: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        realm = self.realm

        resources: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = []
            for resources_item_data in self.resources:
                resources_item = resources_item_data.to_dict()
                resources.append(resources_item)

        services: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        url_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.url_list, Unset):
            url_list = self.url_list

        url_tree = self.url_tree

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if realm is not UNSET:
            field_dict["realm"] = realm
        if resources is not UNSET:
            field_dict["resources"] = resources
        if services is not UNSET:
            field_dict["services"] = services
        if url_list is not UNSET:
            field_dict["urlList"] = url_list
        if url_tree is not UNSET:
            field_dict["urlTree"] = url_tree
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_descriptor_v1_argo_cisco_com_get import ResourceDescriptorV1ArgoCiscoComGET
        from ..models.service_descriptor_v1_argo_cisco_com_get import ServiceDescriptorV1ArgoCiscoComGET

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        realm = d.pop("realm", UNSET)

        resources = []
        _resources = d.pop("resources", UNSET)
        for resources_item_data in _resources or []:
            resources_item = ResourceDescriptorV1ArgoCiscoComGET.from_dict(resources_item_data)

            resources.append(resources_item)

        services = []
        _services = d.pop("services", UNSET)
        for services_item_data in _services or []:
            services_item = ServiceDescriptorV1ArgoCiscoComGET.from_dict(services_item_data)

            services.append(services_item)

        url_list = cast(list[str], d.pop("urlList", UNSET))

        url_tree = d.pop("urlTree", UNSET)

        version = d.pop("version", UNSET)

        application_spec_wrapper_v1_argo_cisco_com_get = cls(
            name=name,
            realm=realm,
            resources=resources,
            services=services,
            url_list=url_list,
            url_tree=url_tree,
            version=version,
        )

        application_spec_wrapper_v1_argo_cisco_com_get.additional_properties = d
        return application_spec_wrapper_v1_argo_cisco_com_get

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
