from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_community import ModelsCommunity
    from ..models.models_ip_prefix import ModelsIpPrefix


T = TypeVar("T", bound="ModelsBgpMatchGroup")


@_attrs_define
class ModelsBgpMatchGroup:
    """BgpMatchGroup encapsulates "MATCH" part of a BgpRule. E.g. match community <COMMUNITY_LIST>. Note that prefixes are
    mutually exclusive for matching. That means caller must not provide both IPv4 and IPv6 prefixes.

        Attributes:
            communities (Union[Unset, list['ModelsCommunity']]): A set of communities to match on. May provide up to 10
                communities.
            ipv_4_prefix_list_id (Union[Unset, str]): IPv4 prefix list identifier. May provide either IPv4 list identifier
                or IPv4 prefixes, but not both.
            ipv_4_prefixes (Union[Unset, list['ModelsIpPrefix']]): A set of IPv4 prefixes to match on. May provide up to 10
                prefixes.
            ipv_6_prefix_list_id (Union[Unset, str]): IPv6 prefix list identifier. May provide either IPv6 list identifier
                or IPv6 prefixes, but not both.
            ipv_6_prefixes (Union[Unset, list['ModelsIpPrefix']]): A set of IPv6 prefixes to match on. May provide up to 10
                prefixes.
            tag (Union[Unset, int]): Match on a specific tag. Tag value range is 1-4294967295.
    """

    communities: Union[Unset, list["ModelsCommunity"]] = UNSET
    ipv_4_prefix_list_id: Union[Unset, str] = UNSET
    ipv_4_prefixes: Union[Unset, list["ModelsIpPrefix"]] = UNSET
    ipv_6_prefix_list_id: Union[Unset, str] = UNSET
    ipv_6_prefixes: Union[Unset, list["ModelsIpPrefix"]] = UNSET
    tag: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        communities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.communities, Unset):
            communities = []
            for communities_item_data in self.communities:
                communities_item = communities_item_data.to_dict()
                communities.append(communities_item)

        ipv_4_prefix_list_id = self.ipv_4_prefix_list_id

        ipv_4_prefixes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ipv_4_prefixes, Unset):
            ipv_4_prefixes = []
            for ipv_4_prefixes_item_data in self.ipv_4_prefixes:
                ipv_4_prefixes_item = ipv_4_prefixes_item_data.to_dict()
                ipv_4_prefixes.append(ipv_4_prefixes_item)

        ipv_6_prefix_list_id = self.ipv_6_prefix_list_id

        ipv_6_prefixes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ipv_6_prefixes, Unset):
            ipv_6_prefixes = []
            for ipv_6_prefixes_item_data in self.ipv_6_prefixes:
                ipv_6_prefixes_item = ipv_6_prefixes_item_data.to_dict()
                ipv_6_prefixes.append(ipv_6_prefixes_item)

        tag = self.tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if communities is not UNSET:
            field_dict["communities"] = communities
        if ipv_4_prefix_list_id is not UNSET:
            field_dict["ipv4PrefixListId"] = ipv_4_prefix_list_id
        if ipv_4_prefixes is not UNSET:
            field_dict["ipv4Prefixes"] = ipv_4_prefixes
        if ipv_6_prefix_list_id is not UNSET:
            field_dict["ipv6PrefixListId"] = ipv_6_prefix_list_id
        if ipv_6_prefixes is not UNSET:
            field_dict["ipv6Prefixes"] = ipv_6_prefixes
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_community import ModelsCommunity
        from ..models.models_ip_prefix import ModelsIpPrefix

        d = dict(src_dict)
        communities = []
        _communities = d.pop("communities", UNSET)
        for communities_item_data in _communities or []:
            communities_item = ModelsCommunity.from_dict(communities_item_data)

            communities.append(communities_item)

        ipv_4_prefix_list_id = d.pop("ipv4PrefixListId", UNSET)

        ipv_4_prefixes = []
        _ipv_4_prefixes = d.pop("ipv4Prefixes", UNSET)
        for ipv_4_prefixes_item_data in _ipv_4_prefixes or []:
            ipv_4_prefixes_item = ModelsIpPrefix.from_dict(ipv_4_prefixes_item_data)

            ipv_4_prefixes.append(ipv_4_prefixes_item)

        ipv_6_prefix_list_id = d.pop("ipv6PrefixListId", UNSET)

        ipv_6_prefixes = []
        _ipv_6_prefixes = d.pop("ipv6Prefixes", UNSET)
        for ipv_6_prefixes_item_data in _ipv_6_prefixes or []:
            ipv_6_prefixes_item = ModelsIpPrefix.from_dict(ipv_6_prefixes_item_data)

            ipv_6_prefixes.append(ipv_6_prefixes_item)

        tag = d.pop("tag", UNSET)

        models_bgp_match_group = cls(
            communities=communities,
            ipv_4_prefix_list_id=ipv_4_prefix_list_id,
            ipv_4_prefixes=ipv_4_prefixes,
            ipv_6_prefix_list_id=ipv_6_prefix_list_id,
            ipv_6_prefixes=ipv_6_prefixes,
            tag=tag,
        )

        models_bgp_match_group.additional_properties = d
        return models_bgp_match_group

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
