from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_reachability_status_v4_sitemanagement_get import NodeReachabilityStatusV4SitemanagementGET


T = TypeVar("T", bound="SiteReachabiltyStatusV4SitemanagementGET")


@_attrs_define
class SiteReachabiltyStatusV4SitemanagementGET:
    """
    Attributes:
        description (Union[Unset, str]): site reachability description
        node_reachability (Union[Unset, list['NodeReachabilityStatusV4SitemanagementGET']]): node reachability
            information
        state (Union[Unset, str]): site reachability status
    """

    description: Union[Unset, str] = UNSET
    node_reachability: Union[Unset, list["NodeReachabilityStatusV4SitemanagementGET"]] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        node_reachability: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.node_reachability, Unset):
            node_reachability = []
            for node_reachability_item_data in self.node_reachability:
                node_reachability_item = node_reachability_item_data.to_dict()
                node_reachability.append(node_reachability_item)

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if node_reachability is not UNSET:
            field_dict["nodeReachability"] = node_reachability
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node_reachability_status_v4_sitemanagement_get import NodeReachabilityStatusV4SitemanagementGET

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        node_reachability = []
        _node_reachability = d.pop("nodeReachability", UNSET)
        for node_reachability_item_data in _node_reachability or []:
            node_reachability_item = NodeReachabilityStatusV4SitemanagementGET.from_dict(node_reachability_item_data)

            node_reachability.append(node_reachability_item)

        state = d.pop("state", UNSET)

        site_reachabilty_status_v4_sitemanagement_get = cls(
            description=description,
            node_reachability=node_reachability,
            state=state,
        )

        site_reachabilty_status_v4_sitemanagement_get.additional_properties = d
        return site_reachabilty_status_v4_sitemanagement_get

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
