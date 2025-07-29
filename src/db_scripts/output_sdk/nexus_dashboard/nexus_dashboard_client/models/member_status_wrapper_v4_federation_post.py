from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.member_status_wrapper_v4_federation_post_reachability import (
    MemberStatusWrapperV4FederationPOSTReachability,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cluster_node_v4_federation_post import ClusterNodeV4FederationPOST


T = TypeVar("T", bound="MemberStatusWrapperV4FederationPOST")


@_attrs_define
class MemberStatusWrapperV4FederationPOST:
    """
    Attributes:
        member_id (str): unique ID assigned to the federation member
        cluster_info (Union[Unset, list['ClusterNodeV4FederationPOST']]):
        federation_id (Union[Unset, str]): ID of the federation member associated with
        manager (Union[Unset, bool]): Federation member is also federation manager, set to true.
        name (Union[Unset, str]): clustername of the member in the federation
        reachability (Union[Unset, MemberStatusWrapperV4FederationPOSTReachability]): Member reachability status -
            Unknown/Up/Down
    """

    member_id: str
    cluster_info: Union[Unset, list["ClusterNodeV4FederationPOST"]] = UNSET
    federation_id: Union[Unset, str] = UNSET
    manager: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    reachability: Union[Unset, MemberStatusWrapperV4FederationPOSTReachability] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member_id = self.member_id

        cluster_info: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cluster_info, Unset):
            cluster_info = []
            for cluster_info_item_data in self.cluster_info:
                cluster_info_item = cluster_info_item_data.to_dict()
                cluster_info.append(cluster_info_item)

        federation_id = self.federation_id

        manager = self.manager

        name = self.name

        reachability: Union[Unset, str] = UNSET
        if not isinstance(self.reachability, Unset):
            reachability = self.reachability.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "memberID": member_id,
            }
        )
        if cluster_info is not UNSET:
            field_dict["clusterInfo"] = cluster_info
        if federation_id is not UNSET:
            field_dict["federationID"] = federation_id
        if manager is not UNSET:
            field_dict["manager"] = manager
        if name is not UNSET:
            field_dict["name"] = name
        if reachability is not UNSET:
            field_dict["reachability"] = reachability

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cluster_node_v4_federation_post import ClusterNodeV4FederationPOST

        d = dict(src_dict)
        member_id = d.pop("memberID")

        cluster_info = []
        _cluster_info = d.pop("clusterInfo", UNSET)
        for cluster_info_item_data in _cluster_info or []:
            cluster_info_item = ClusterNodeV4FederationPOST.from_dict(cluster_info_item_data)

            cluster_info.append(cluster_info_item)

        federation_id = d.pop("federationID", UNSET)

        manager = d.pop("manager", UNSET)

        name = d.pop("name", UNSET)

        _reachability = d.pop("reachability", UNSET)
        reachability: Union[Unset, MemberStatusWrapperV4FederationPOSTReachability]
        if isinstance(_reachability, Unset):
            reachability = UNSET
        else:
            reachability = MemberStatusWrapperV4FederationPOSTReachability(_reachability)

        member_status_wrapper_v4_federation_post = cls(
            member_id=member_id,
            cluster_info=cluster_info,
            federation_id=federation_id,
            manager=manager,
            name=name,
            reachability=reachability,
        )

        member_status_wrapper_v4_federation_post.additional_properties = d
        return member_status_wrapper_v4_federation_post

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
