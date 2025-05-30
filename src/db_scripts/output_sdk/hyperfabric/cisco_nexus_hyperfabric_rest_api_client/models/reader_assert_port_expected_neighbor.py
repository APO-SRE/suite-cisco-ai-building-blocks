import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.models_assert_category_type import ModelsAssertCategoryType
from ..models.models_assert_state_type import ModelsAssertStateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReaderAssertPortExpectedNeighbor")


@_attrs_define
class ReaderAssertPortExpectedNeighbor:
    """Description not available

    Attributes:
        assert_state (Union[Unset, ModelsAssertStateType]): AssertStateType specifies the various kinds of states of an
            assertions.
        breakout (Union[Unset, int]): Description not available
        category (Union[Unset, ModelsAssertCategoryType]): AssertCategoryType specifies the various kinds of assertion
            categories.
        device (Union[Unset, str]): Description not available
        fabric (Union[Unset, str]): Description not available
        implicit (Union[Unset, bool]): Description not available
        latch_time (Union[Unset, str]): Description not available
        latched_at (Union[Unset, datetime.datetime]): Description not available
        line_card (Union[Unset, int]): Description not available
        masked (Union[Unset, bool]): Description not available
        modified_at (Union[Unset, datetime.datetime]): Description not available
        node_id (Union[Unset, str]): Description not available
        num_neighbors (Union[Unset, int]): Description not available
        port (Union[Unset, str]): Description not available
        port_name (Union[Unset, str]): Description not available
        remote_device (Union[Unset, str]): Description not available
        remote_node_id (Union[Unset, str]): Description not available
        remote_port_name (Union[Unset, str]): Description not available
    """

    assert_state: Union[Unset, ModelsAssertStateType] = UNSET
    breakout: Union[Unset, int] = UNSET
    category: Union[Unset, ModelsAssertCategoryType] = UNSET
    device: Union[Unset, str] = UNSET
    fabric: Union[Unset, str] = UNSET
    implicit: Union[Unset, bool] = UNSET
    latch_time: Union[Unset, str] = UNSET
    latched_at: Union[Unset, datetime.datetime] = UNSET
    line_card: Union[Unset, int] = UNSET
    masked: Union[Unset, bool] = UNSET
    modified_at: Union[Unset, datetime.datetime] = UNSET
    node_id: Union[Unset, str] = UNSET
    num_neighbors: Union[Unset, int] = UNSET
    port: Union[Unset, str] = UNSET
    port_name: Union[Unset, str] = UNSET
    remote_device: Union[Unset, str] = UNSET
    remote_node_id: Union[Unset, str] = UNSET
    remote_port_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assert_state: Union[Unset, str] = UNSET
        if not isinstance(self.assert_state, Unset):
            assert_state = self.assert_state.value

        breakout = self.breakout

        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        device = self.device

        fabric = self.fabric

        implicit = self.implicit

        latch_time = self.latch_time

        latched_at: Union[Unset, str] = UNSET
        if not isinstance(self.latched_at, Unset):
            latched_at = self.latched_at.isoformat()

        line_card = self.line_card

        masked = self.masked

        modified_at: Union[Unset, str] = UNSET
        if not isinstance(self.modified_at, Unset):
            modified_at = self.modified_at.isoformat()

        node_id = self.node_id

        num_neighbors = self.num_neighbors

        port = self.port

        port_name = self.port_name

        remote_device = self.remote_device

        remote_node_id = self.remote_node_id

        remote_port_name = self.remote_port_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assert_state is not UNSET:
            field_dict["assertState"] = assert_state
        if breakout is not UNSET:
            field_dict["breakout"] = breakout
        if category is not UNSET:
            field_dict["category"] = category
        if device is not UNSET:
            field_dict["device"] = device
        if fabric is not UNSET:
            field_dict["fabric"] = fabric
        if implicit is not UNSET:
            field_dict["implicit"] = implicit
        if latch_time is not UNSET:
            field_dict["latchTime"] = latch_time
        if latched_at is not UNSET:
            field_dict["latchedAt"] = latched_at
        if line_card is not UNSET:
            field_dict["lineCard"] = line_card
        if masked is not UNSET:
            field_dict["masked"] = masked
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if num_neighbors is not UNSET:
            field_dict["numNeighbors"] = num_neighbors
        if port is not UNSET:
            field_dict["port"] = port
        if port_name is not UNSET:
            field_dict["portName"] = port_name
        if remote_device is not UNSET:
            field_dict["remoteDevice"] = remote_device
        if remote_node_id is not UNSET:
            field_dict["remoteNodeId"] = remote_node_id
        if remote_port_name is not UNSET:
            field_dict["remotePortName"] = remote_port_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _assert_state = d.pop("assertState", UNSET)
        assert_state: Union[Unset, ModelsAssertStateType]
        if isinstance(_assert_state, Unset):
            assert_state = UNSET
        else:
            assert_state = ModelsAssertStateType(_assert_state)

        breakout = d.pop("breakout", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, ModelsAssertCategoryType]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ModelsAssertCategoryType(_category)

        device = d.pop("device", UNSET)

        fabric = d.pop("fabric", UNSET)

        implicit = d.pop("implicit", UNSET)

        latch_time = d.pop("latchTime", UNSET)

        _latched_at = d.pop("latchedAt", UNSET)
        latched_at: Union[Unset, datetime.datetime]
        if isinstance(_latched_at, Unset):
            latched_at = UNSET
        else:
            latched_at = isoparse(_latched_at)

        line_card = d.pop("lineCard", UNSET)

        masked = d.pop("masked", UNSET)

        _modified_at = d.pop("modifiedAt", UNSET)
        modified_at: Union[Unset, datetime.datetime]
        if isinstance(_modified_at, Unset):
            modified_at = UNSET
        else:
            modified_at = isoparse(_modified_at)

        node_id = d.pop("nodeId", UNSET)

        num_neighbors = d.pop("numNeighbors", UNSET)

        port = d.pop("port", UNSET)

        port_name = d.pop("portName", UNSET)

        remote_device = d.pop("remoteDevice", UNSET)

        remote_node_id = d.pop("remoteNodeId", UNSET)

        remote_port_name = d.pop("remotePortName", UNSET)

        reader_assert_port_expected_neighbor = cls(
            assert_state=assert_state,
            breakout=breakout,
            category=category,
            device=device,
            fabric=fabric,
            implicit=implicit,
            latch_time=latch_time,
            latched_at=latched_at,
            line_card=line_card,
            masked=masked,
            modified_at=modified_at,
            node_id=node_id,
            num_neighbors=num_neighbors,
            port=port,
            port_name=port_name,
            remote_device=remote_device,
            remote_node_id=remote_node_id,
            remote_port_name=remote_port_name,
        )

        reader_assert_port_expected_neighbor.additional_properties = d
        return reader_assert_port_expected_neighbor

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
