from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_controller_v4_sitemanagement_get import SiteControllerV4SitemanagementGET
    from ..models.site_federation_info_v4_sitemanagement_get import SiteFederationInfoV4SitemanagementGET
    from ..models.site_reachabilty_status_v4_sitemanagement_get import SiteReachabiltyStatusV4SitemanagementGET
    from ..models.site_status_data_v4_sitemanagement_get_type_0 import SiteStatusDataV4SitemanagementGETType0
    from ..models.site_status_data_v4_sitemanagement_get_type_1 import SiteStatusDataV4SitemanagementGETType1
    from ..models.site_status_data_v4_sitemanagement_get_type_2 import SiteStatusDataV4SitemanagementGETType2
    from ..models.site_status_data_v4_sitemanagement_get_type_3 import SiteStatusDataV4SitemanagementGETType3
    from ..models.switch_v4_sitemanagement_get import SwitchV4SitemanagementGET


T = TypeVar("T", bound="SiteStatusWrapperV4SitemanagementGET")


@_attrs_define
class SiteStatusWrapperV4SitemanagementGET:
    """
    Attributes:
        apps (Union[Unset, list[str]]): apps using the site
        controllers (Union[Unset, list['SiteControllerV4SitemanagementGET']]): controller nodes information
        federation_info (Union[Unset, SiteFederationInfoV4SitemanagementGET]):
        launch_url (Union[Unset, str]): URL need to be used for SSO for NDFC
        notify_reason (Union[Unset, str]): last site status notification sent to the apps
        polling_detection_done (Union[Unset, bool]): polling auto detectetion status
        polling_type (Union[Unset, str]): polling auto detected type
        site_data (Union['SiteStatusDataV4SitemanagementGETType0', 'SiteStatusDataV4SitemanagementGETType1',
            'SiteStatusDataV4SitemanagementGETType2', 'SiteStatusDataV4SitemanagementGETType3', Unset]):
        site_health (Union[Unset, str]): health of the fabric
        site_reachabilty (Union[Unset, SiteReachabiltyStatusV4SitemanagementGET]):
        switches (Union[Unset, list['SwitchV4SitemanagementGET']]): switches connected to the fabric
    """

    apps: Union[Unset, list[str]] = UNSET
    controllers: Union[Unset, list["SiteControllerV4SitemanagementGET"]] = UNSET
    federation_info: Union[Unset, "SiteFederationInfoV4SitemanagementGET"] = UNSET
    launch_url: Union[Unset, str] = UNSET
    notify_reason: Union[Unset, str] = UNSET
    polling_detection_done: Union[Unset, bool] = UNSET
    polling_type: Union[Unset, str] = UNSET
    site_data: Union[
        "SiteStatusDataV4SitemanagementGETType0",
        "SiteStatusDataV4SitemanagementGETType1",
        "SiteStatusDataV4SitemanagementGETType2",
        "SiteStatusDataV4SitemanagementGETType3",
        Unset,
    ] = UNSET
    site_health: Union[Unset, str] = UNSET
    site_reachabilty: Union[Unset, "SiteReachabiltyStatusV4SitemanagementGET"] = UNSET
    switches: Union[Unset, list["SwitchV4SitemanagementGET"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.site_status_data_v4_sitemanagement_get_type_0 import SiteStatusDataV4SitemanagementGETType0
        from ..models.site_status_data_v4_sitemanagement_get_type_1 import SiteStatusDataV4SitemanagementGETType1
        from ..models.site_status_data_v4_sitemanagement_get_type_2 import SiteStatusDataV4SitemanagementGETType2

        apps: Union[Unset, list[str]] = UNSET
        if not isinstance(self.apps, Unset):
            apps = self.apps

        controllers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.controllers, Unset):
            controllers = []
            for controllers_item_data in self.controllers:
                controllers_item = controllers_item_data.to_dict()
                controllers.append(controllers_item)

        federation_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.federation_info, Unset):
            federation_info = self.federation_info.to_dict()

        launch_url = self.launch_url

        notify_reason = self.notify_reason

        polling_detection_done = self.polling_detection_done

        polling_type = self.polling_type

        site_data: Union[Unset, dict[str, Any]]
        if isinstance(self.site_data, Unset):
            site_data = UNSET
        elif isinstance(self.site_data, SiteStatusDataV4SitemanagementGETType0):
            site_data = self.site_data.to_dict()
        elif isinstance(self.site_data, SiteStatusDataV4SitemanagementGETType1):
            site_data = self.site_data.to_dict()
        elif isinstance(self.site_data, SiteStatusDataV4SitemanagementGETType2):
            site_data = self.site_data.to_dict()
        else:
            site_data = self.site_data.to_dict()

        site_health = self.site_health

        site_reachabilty: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.site_reachabilty, Unset):
            site_reachabilty = self.site_reachabilty.to_dict()

        switches: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.switches, Unset):
            switches = []
            for switches_item_data in self.switches:
                switches_item = switches_item_data.to_dict()
                switches.append(switches_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apps is not UNSET:
            field_dict["apps"] = apps
        if controllers is not UNSET:
            field_dict["controllers"] = controllers
        if federation_info is not UNSET:
            field_dict["federationInfo"] = federation_info
        if launch_url is not UNSET:
            field_dict["launchURL"] = launch_url
        if notify_reason is not UNSET:
            field_dict["notifyReason"] = notify_reason
        if polling_detection_done is not UNSET:
            field_dict["pollingDetectionDone"] = polling_detection_done
        if polling_type is not UNSET:
            field_dict["pollingType"] = polling_type
        if site_data is not UNSET:
            field_dict["siteData"] = site_data
        if site_health is not UNSET:
            field_dict["siteHealth"] = site_health
        if site_reachabilty is not UNSET:
            field_dict["siteReachabilty"] = site_reachabilty
        if switches is not UNSET:
            field_dict["switches"] = switches

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.site_controller_v4_sitemanagement_get import SiteControllerV4SitemanagementGET
        from ..models.site_federation_info_v4_sitemanagement_get import SiteFederationInfoV4SitemanagementGET
        from ..models.site_reachabilty_status_v4_sitemanagement_get import SiteReachabiltyStatusV4SitemanagementGET
        from ..models.site_status_data_v4_sitemanagement_get_type_0 import SiteStatusDataV4SitemanagementGETType0
        from ..models.site_status_data_v4_sitemanagement_get_type_1 import SiteStatusDataV4SitemanagementGETType1
        from ..models.site_status_data_v4_sitemanagement_get_type_2 import SiteStatusDataV4SitemanagementGETType2
        from ..models.site_status_data_v4_sitemanagement_get_type_3 import SiteStatusDataV4SitemanagementGETType3
        from ..models.switch_v4_sitemanagement_get import SwitchV4SitemanagementGET

        d = dict(src_dict)
        apps = cast(list[str], d.pop("apps", UNSET))

        controllers = []
        _controllers = d.pop("controllers", UNSET)
        for controllers_item_data in _controllers or []:
            controllers_item = SiteControllerV4SitemanagementGET.from_dict(controllers_item_data)

            controllers.append(controllers_item)

        _federation_info = d.pop("federationInfo", UNSET)
        federation_info: Union[Unset, SiteFederationInfoV4SitemanagementGET]
        if isinstance(_federation_info, Unset):
            federation_info = UNSET
        else:
            federation_info = SiteFederationInfoV4SitemanagementGET.from_dict(_federation_info)

        launch_url = d.pop("launchURL", UNSET)

        notify_reason = d.pop("notifyReason", UNSET)

        polling_detection_done = d.pop("pollingDetectionDone", UNSET)

        polling_type = d.pop("pollingType", UNSET)

        def _parse_site_data(
            data: object,
        ) -> Union[
            "SiteStatusDataV4SitemanagementGETType0",
            "SiteStatusDataV4SitemanagementGETType1",
            "SiteStatusDataV4SitemanagementGETType2",
            "SiteStatusDataV4SitemanagementGETType3",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_site_status_data_v_4_sitemanagement_get_type_0 = (
                    SiteStatusDataV4SitemanagementGETType0.from_dict(data)
                )

                return componentsschemas_site_status_data_v_4_sitemanagement_get_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_site_status_data_v_4_sitemanagement_get_type_1 = (
                    SiteStatusDataV4SitemanagementGETType1.from_dict(data)
                )

                return componentsschemas_site_status_data_v_4_sitemanagement_get_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_site_status_data_v_4_sitemanagement_get_type_2 = (
                    SiteStatusDataV4SitemanagementGETType2.from_dict(data)
                )

                return componentsschemas_site_status_data_v_4_sitemanagement_get_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_site_status_data_v_4_sitemanagement_get_type_3 = (
                SiteStatusDataV4SitemanagementGETType3.from_dict(data)
            )

            return componentsschemas_site_status_data_v_4_sitemanagement_get_type_3

        site_data = _parse_site_data(d.pop("siteData", UNSET))

        site_health = d.pop("siteHealth", UNSET)

        _site_reachabilty = d.pop("siteReachabilty", UNSET)
        site_reachabilty: Union[Unset, SiteReachabiltyStatusV4SitemanagementGET]
        if isinstance(_site_reachabilty, Unset):
            site_reachabilty = UNSET
        else:
            site_reachabilty = SiteReachabiltyStatusV4SitemanagementGET.from_dict(_site_reachabilty)

        switches = []
        _switches = d.pop("switches", UNSET)
        for switches_item_data in _switches or []:
            switches_item = SwitchV4SitemanagementGET.from_dict(switches_item_data)

            switches.append(switches_item)

        site_status_wrapper_v4_sitemanagement_get = cls(
            apps=apps,
            controllers=controllers,
            federation_info=federation_info,
            launch_url=launch_url,
            notify_reason=notify_reason,
            polling_detection_done=polling_detection_done,
            polling_type=polling_type,
            site_data=site_data,
            site_health=site_health,
            site_reachabilty=site_reachabilty,
            switches=switches,
        )

        site_status_wrapper_v4_sitemanagement_get.additional_properties = d
        return site_status_wrapper_v4_sitemanagement_get

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
