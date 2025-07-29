from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fabric_response_v4_sitemanagement_get_type_0 import FabricResponseV4SitemanagementGETType0
    from ..models.fabric_response_v4_sitemanagement_get_type_1 import FabricResponseV4SitemanagementGETType1
    from ..models.fabric_response_v4_sitemanagement_get_type_2 import FabricResponseV4SitemanagementGETType2
    from ..models.fabric_response_v4_sitemanagement_get_type_3 import FabricResponseV4SitemanagementGETType3


T = TypeVar("T", bound="FabricStatusWrapperV4SitemanagementGET")


@_attrs_define
class FabricStatusWrapperV4SitemanagementGET:
    """
    Attributes:
        site_list (Union['FabricResponseV4SitemanagementGETType0', 'FabricResponseV4SitemanagementGETType1',
            'FabricResponseV4SitemanagementGETType2', 'FabricResponseV4SitemanagementGETType3', Unset]):
        site_type (Union[Unset, str]): site type - ACI/NDFC/DCNM
    """

    site_list: Union[
        "FabricResponseV4SitemanagementGETType0",
        "FabricResponseV4SitemanagementGETType1",
        "FabricResponseV4SitemanagementGETType2",
        "FabricResponseV4SitemanagementGETType3",
        Unset,
    ] = UNSET
    site_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.fabric_response_v4_sitemanagement_get_type_0 import FabricResponseV4SitemanagementGETType0
        from ..models.fabric_response_v4_sitemanagement_get_type_1 import FabricResponseV4SitemanagementGETType1
        from ..models.fabric_response_v4_sitemanagement_get_type_2 import FabricResponseV4SitemanagementGETType2

        site_list: Union[Unset, dict[str, Any]]
        if isinstance(self.site_list, Unset):
            site_list = UNSET
        elif isinstance(self.site_list, FabricResponseV4SitemanagementGETType0):
            site_list = self.site_list.to_dict()
        elif isinstance(self.site_list, FabricResponseV4SitemanagementGETType1):
            site_list = self.site_list.to_dict()
        elif isinstance(self.site_list, FabricResponseV4SitemanagementGETType2):
            site_list = self.site_list.to_dict()
        else:
            site_list = self.site_list.to_dict()

        site_type = self.site_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_list is not UNSET:
            field_dict["siteList"] = site_list
        if site_type is not UNSET:
            field_dict["siteType"] = site_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fabric_response_v4_sitemanagement_get_type_0 import FabricResponseV4SitemanagementGETType0
        from ..models.fabric_response_v4_sitemanagement_get_type_1 import FabricResponseV4SitemanagementGETType1
        from ..models.fabric_response_v4_sitemanagement_get_type_2 import FabricResponseV4SitemanagementGETType2
        from ..models.fabric_response_v4_sitemanagement_get_type_3 import FabricResponseV4SitemanagementGETType3

        d = dict(src_dict)

        def _parse_site_list(
            data: object,
        ) -> Union[
            "FabricResponseV4SitemanagementGETType0",
            "FabricResponseV4SitemanagementGETType1",
            "FabricResponseV4SitemanagementGETType2",
            "FabricResponseV4SitemanagementGETType3",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_fabric_response_v_4_sitemanagement_get_type_0 = (
                    FabricResponseV4SitemanagementGETType0.from_dict(data)
                )

                return componentsschemas_fabric_response_v_4_sitemanagement_get_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_fabric_response_v_4_sitemanagement_get_type_1 = (
                    FabricResponseV4SitemanagementGETType1.from_dict(data)
                )

                return componentsschemas_fabric_response_v_4_sitemanagement_get_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_fabric_response_v_4_sitemanagement_get_type_2 = (
                    FabricResponseV4SitemanagementGETType2.from_dict(data)
                )

                return componentsschemas_fabric_response_v_4_sitemanagement_get_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_fabric_response_v_4_sitemanagement_get_type_3 = (
                FabricResponseV4SitemanagementGETType3.from_dict(data)
            )

            return componentsschemas_fabric_response_v_4_sitemanagement_get_type_3

        site_list = _parse_site_list(d.pop("siteList", UNSET))

        site_type = d.pop("siteType", UNSET)

        fabric_status_wrapper_v4_sitemanagement_get = cls(
            site_list=site_list,
            site_type=site_type,
        )

        fabric_status_wrapper_v4_sitemanagement_get.additional_properties = d
        return fabric_status_wrapper_v4_sitemanagement_get

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
