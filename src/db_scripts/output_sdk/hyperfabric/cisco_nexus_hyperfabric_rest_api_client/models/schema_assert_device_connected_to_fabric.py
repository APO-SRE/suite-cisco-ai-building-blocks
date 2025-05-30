import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.models_assert_category_type import ModelsAssertCategoryType
from ..models.models_assert_state_type import ModelsAssertStateType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_assert_config_connected_to_fabric_data import SchemaAssertConfigConnectedToFabricData
    from ..models.schema_path_path_id import SchemaPathPathId


T = TypeVar("T", bound="SchemaAssertDeviceConnectedToFabric")


@_attrs_define
class SchemaAssertDeviceConnectedToFabric:
    """Description not available

    Attributes:
        assert_state (Union[Unset, ModelsAssertStateType]): AssertStateType specifies the various kinds of states of an
            assertions.
        category (Union[Unset, ModelsAssertCategoryType]): AssertCategoryType specifies the various kinds of assertion
            categories.
        config (Union[Unset, SchemaAssertConfigConnectedToFabricData]): Description not available
        id (Union[Unset, SchemaPathPathId]): PathId identifies the specific "schema coordinates" identifier of an object
            in the schema tree.
        masked (Union[Unset, bool]): Description not available
        masked_by_connection_to_cloud (Union[Unset, bool]): Description not available
        masked_by_port_link_up (Union[Unset, bool]): Description not available
        modified_at (Union[Unset, datetime.datetime]): Description not available
        ready_to_latch_at (Union[Unset, datetime.datetime]): Description not available
    """

    assert_state: Union[Unset, ModelsAssertStateType] = UNSET
    category: Union[Unset, ModelsAssertCategoryType] = UNSET
    config: Union[Unset, "SchemaAssertConfigConnectedToFabricData"] = UNSET
    id: Union[Unset, "SchemaPathPathId"] = UNSET
    masked: Union[Unset, bool] = UNSET
    masked_by_connection_to_cloud: Union[Unset, bool] = UNSET
    masked_by_port_link_up: Union[Unset, bool] = UNSET
    modified_at: Union[Unset, datetime.datetime] = UNSET
    ready_to_latch_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assert_state: Union[Unset, str] = UNSET
        if not isinstance(self.assert_state, Unset):
            assert_state = self.assert_state.value

        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        id: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        masked = self.masked

        masked_by_connection_to_cloud = self.masked_by_connection_to_cloud

        masked_by_port_link_up = self.masked_by_port_link_up

        modified_at: Union[Unset, str] = UNSET
        if not isinstance(self.modified_at, Unset):
            modified_at = self.modified_at.isoformat()

        ready_to_latch_at: Union[Unset, str] = UNSET
        if not isinstance(self.ready_to_latch_at, Unset):
            ready_to_latch_at = self.ready_to_latch_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assert_state is not UNSET:
            field_dict["assertState"] = assert_state
        if category is not UNSET:
            field_dict["category"] = category
        if config is not UNSET:
            field_dict["config"] = config
        if id is not UNSET:
            field_dict["id"] = id
        if masked is not UNSET:
            field_dict["masked"] = masked
        if masked_by_connection_to_cloud is not UNSET:
            field_dict["maskedByConnectionToCloud"] = masked_by_connection_to_cloud
        if masked_by_port_link_up is not UNSET:
            field_dict["maskedByPortLinkUp"] = masked_by_port_link_up
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if ready_to_latch_at is not UNSET:
            field_dict["readyToLatchAt"] = ready_to_latch_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_assert_config_connected_to_fabric_data import SchemaAssertConfigConnectedToFabricData
        from ..models.schema_path_path_id import SchemaPathPathId

        d = dict(src_dict)
        _assert_state = d.pop("assertState", UNSET)
        assert_state: Union[Unset, ModelsAssertStateType]
        if isinstance(_assert_state, Unset):
            assert_state = UNSET
        else:
            assert_state = ModelsAssertStateType(_assert_state)

        _category = d.pop("category", UNSET)
        category: Union[Unset, ModelsAssertCategoryType]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ModelsAssertCategoryType(_category)

        _config = d.pop("config", UNSET)
        config: Union[Unset, SchemaAssertConfigConnectedToFabricData]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = SchemaAssertConfigConnectedToFabricData.from_dict(_config)

        _id = d.pop("id", UNSET)
        id: Union[Unset, SchemaPathPathId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = SchemaPathPathId.from_dict(_id)

        masked = d.pop("masked", UNSET)

        masked_by_connection_to_cloud = d.pop("maskedByConnectionToCloud", UNSET)

        masked_by_port_link_up = d.pop("maskedByPortLinkUp", UNSET)

        _modified_at = d.pop("modifiedAt", UNSET)
        modified_at: Union[Unset, datetime.datetime]
        if isinstance(_modified_at, Unset):
            modified_at = UNSET
        else:
            modified_at = isoparse(_modified_at)

        _ready_to_latch_at = d.pop("readyToLatchAt", UNSET)
        ready_to_latch_at: Union[Unset, datetime.datetime]
        if isinstance(_ready_to_latch_at, Unset):
            ready_to_latch_at = UNSET
        else:
            ready_to_latch_at = isoparse(_ready_to_latch_at)

        schema_assert_device_connected_to_fabric = cls(
            assert_state=assert_state,
            category=category,
            config=config,
            id=id,
            masked=masked,
            masked_by_connection_to_cloud=masked_by_connection_to_cloud,
            masked_by_port_link_up=masked_by_port_link_up,
            modified_at=modified_at,
            ready_to_latch_at=ready_to_latch_at,
        )

        schema_assert_device_connected_to_fabric.additional_properties = d
        return schema_assert_device_connected_to_fabric

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
