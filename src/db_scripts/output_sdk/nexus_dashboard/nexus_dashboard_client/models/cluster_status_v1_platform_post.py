from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cluster_status_v1_platform_post_state import ClusterStatusV1PlatformPOSTState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cluster_status_error_v1_platform_post import ClusterStatusErrorV1PlatformPOST


T = TypeVar("T", bound="ClusterStatusV1PlatformPOST")


@_attrs_define
class ClusterStatusV1PlatformPOST:
    """Cluster status information

    Attributes:
        current_version (Union[Unset, str]): Cluster version
        error (Union[Unset, ClusterStatusErrorV1PlatformPOST]): error is the last observed error, if any.
        state (Union[Unset, ClusterStatusV1PlatformPOSTState]): State of dual-stack mode in cluster
        target_version (Union[Unset, str]): If mid-upgrade, the version this cluster is updating to
        uuid (Union[Unset, str]): Cluster uuid
    """

    current_version: Union[Unset, str] = UNSET
    error: Union[Unset, "ClusterStatusErrorV1PlatformPOST"] = UNSET
    state: Union[Unset, ClusterStatusV1PlatformPOSTState] = UNSET
    target_version: Union[Unset, str] = UNSET
    uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_version = self.current_version

        error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        target_version = self.target_version

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_version is not UNSET:
            field_dict["currentVersion"] = current_version
        if error is not UNSET:
            field_dict["error"] = error
        if state is not UNSET:
            field_dict["state"] = state
        if target_version is not UNSET:
            field_dict["targetVersion"] = target_version
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cluster_status_error_v1_platform_post import ClusterStatusErrorV1PlatformPOST

        d = dict(src_dict)
        current_version = d.pop("currentVersion", UNSET)

        _error = d.pop("error", UNSET)
        error: Union[Unset, ClusterStatusErrorV1PlatformPOST]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ClusterStatusErrorV1PlatformPOST.from_dict(_error)

        _state = d.pop("state", UNSET)
        state: Union[Unset, ClusterStatusV1PlatformPOSTState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ClusterStatusV1PlatformPOSTState(_state)

        target_version = d.pop("targetVersion", UNSET)

        uuid = d.pop("uuid", UNSET)

        cluster_status_v1_platform_post = cls(
            current_version=current_version,
            error=error,
            state=state,
            target_version=target_version,
            uuid=uuid,
        )

        cluster_status_v1_platform_post.additional_properties = d
        return cluster_status_v1_platform_post

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
