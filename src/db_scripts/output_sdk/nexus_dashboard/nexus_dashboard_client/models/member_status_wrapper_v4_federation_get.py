from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.member_status_wrapper_v4_federation_get_reachability import MemberStatusWrapperV4FederationGETReachability
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cluster_node_v4_federation_get import ClusterNodeV4FederationGET


T = TypeVar("T", bound="MemberStatusWrapperV4FederationGET")


@_attrs_define
class MemberStatusWrapperV4FederationGET:
    """
    Attributes:
        cluster_info (Union[Unset, list['ClusterNodeV4FederationGET']]):
        federation_id (Union[Unset, str]): ID of the federation member associated with
        manager (Union[Unset, bool]): Federation member is also federation manager, set to true.
        member_id (Union[Unset, str]): unique ID assigned to the federation member
        name (Union[Unset, str]): clustername of the member in the federation
        reachability (Union[Unset, MemberStatusWrapperV4FederationGETReachability]): Member reachability status -
            Unknown/Up/Down
    """

    cluster_info: Union[Unset, list["ClusterNodeV4FederationGET"]] = UNSET
    federation_id: Union[Unset, str] = UNSET
    manager: Union[Unset, bool] = UNSET
    member_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    reachability: Union[Unset, MemberStatusWrapperV4FederationGETReachability] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster_info: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cluster_info, Unset):
            cluster_info = []
            for cluster_info_item_data in self.cluster_info:
                cluster_info_item = cluster_info_item_data.to_dict()
                cluster_info.append(cluster_info_item)

        federation_id = self.federation_id

        manager = self.manager

        member_id = self.member_id

        name = self.name

        reachability: Union[Unset, str] = UNSET
        if not isinstance(self.reachability, Unset):
            reachability = self.reachability.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster_info is not UNSET:
            field_dict["clusterInfo"] = cluster_info
        if federation_id is not UNSET:
            field_dict["federationID"] = federation_id
        if manager is not UNSET:
            field_dict["manager"] = manager
        if member_id is not UNSET:
            field_dict["memberID"] = member_id
        if name is not UNSET:
            field_dict["name"] = name
        if reachability is not UNSET:
            field_dict["reachability"] = reachability

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cluster_node_v4_federation_get import ClusterNodeV4FederationGET

        d = dict(src_dict)
        cluster_info = []
        _cluster_info = d.pop("clusterInfo", UNSET)
        for cluster_info_item_data in _cluster_info or []:
            cluster_info_item = ClusterNodeV4FederationGET.from_dict(cluster_info_item_data)

            cluster_info.append(cluster_info_item)

        federation_id = d.pop("federationID", UNSET)

        manager = d.pop("manager", UNSET)

        member_id = d.pop("memberID", UNSET)

        name = d.pop("name", UNSET)

        _reachability = d.pop("reachability", UNSET)
        reachability: Union[Unset, MemberStatusWrapperV4FederationGETReachability]
        if isinstance(_reachability, Unset):
            reachability = UNSET
        else:
            reachability = MemberStatusWrapperV4FederationGETReachability(_reachability)

        member_status_wrapper_v4_federation_get = cls(
            cluster_info=cluster_info,
            federation_id=federation_id,
            manager=manager,
            member_id=member_id,
            name=name,
            reachability=reachability,
        )

        member_status_wrapper_v4_federation_get.additional_properties = d
        return member_status_wrapper_v4_federation_get

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
