from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_assertion import ConfigAssertion


T = TypeVar("T", bound="ConfigAssertionsResponse")


@_attrs_define
class ConfigAssertionsResponse:
    """A response to latching one or more assertions.

    Attributes:
        assertions (Union[Unset, list['ConfigAssertion']]): The list of assertions which were succesfully latched.
    """

    assertions: Union[Unset, list["ConfigAssertion"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assertions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.assertions, Unset):
            assertions = []
            for assertions_item_data in self.assertions:
                assertions_item = assertions_item_data.to_dict()
                assertions.append(assertions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assertions is not UNSET:
            field_dict["assertions"] = assertions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_assertion import ConfigAssertion

        d = dict(src_dict)
        assertions = []
        _assertions = d.pop("assertions", UNSET)
        for assertions_item_data in _assertions or []:
            assertions_item = ConfigAssertion.from_dict(assertions_item_data)

            assertions.append(assertions_item)

        config_assertions_response = cls(
            assertions=assertions,
        )

        config_assertions_response.additional_properties = d
        return config_assertions_response

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
