from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.password_policy_v4_aaa_get import PasswordPolicyV4AaaGET
    from ..models.rbacv4_aaa_get import RBACV4AaaGET


T = TypeVar("T", bound="LocalUserSpecWrapperV4AaaGET")


@_attrs_define
class LocalUserSpecWrapperV4AaaGET:
    """
    Attributes:
        email (Union[Unset, str]): Local user email
        first_name (Union[Unset, str]): Local user first name
        last_name (Union[Unset, str]): Local user last name
        login_id (Union[Unset, str]): Local user login ID
        password (Union[Unset, str]): Base64 encoded local user password
        password_policy (Union[Unset, PasswordPolicyV4AaaGET]):
        phone (Union[Unset, str]): Local user phone
        rbac (Union[Unset, RBACV4AaaGET]):
        remote_id_claim (Union[Unset, str]): CX UserID mapped to localuser
        user_id (Union[Unset, str]): Local user ID
        x_launch (Union[Unset, bool]): Local user cross launch Option
    """

    email: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    login_id: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    password_policy: Union[Unset, "PasswordPolicyV4AaaGET"] = UNSET
    phone: Union[Unset, str] = UNSET
    rbac: Union[Unset, "RBACV4AaaGET"] = UNSET
    remote_id_claim: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    x_launch: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        login_id = self.login_id

        password = self.password

        password_policy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.password_policy, Unset):
            password_policy = self.password_policy.to_dict()

        phone = self.phone

        rbac: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rbac, Unset):
            rbac = self.rbac.to_dict()

        remote_id_claim = self.remote_id_claim

        user_id = self.user_id

        x_launch = self.x_launch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if login_id is not UNSET:
            field_dict["loginID"] = login_id
        if password is not UNSET:
            field_dict["password"] = password
        if password_policy is not UNSET:
            field_dict["passwordPolicy"] = password_policy
        if phone is not UNSET:
            field_dict["phone"] = phone
        if rbac is not UNSET:
            field_dict["rbac"] = rbac
        if remote_id_claim is not UNSET:
            field_dict["remoteIDClaim"] = remote_id_claim
        if user_id is not UNSET:
            field_dict["userID"] = user_id
        if x_launch is not UNSET:
            field_dict["xLaunch"] = x_launch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.password_policy_v4_aaa_get import PasswordPolicyV4AaaGET
        from ..models.rbacv4_aaa_get import RBACV4AaaGET

        d = dict(src_dict)
        email = d.pop("email", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        login_id = d.pop("loginID", UNSET)

        password = d.pop("password", UNSET)

        _password_policy = d.pop("passwordPolicy", UNSET)
        password_policy: Union[Unset, PasswordPolicyV4AaaGET]
        if isinstance(_password_policy, Unset):
            password_policy = UNSET
        else:
            password_policy = PasswordPolicyV4AaaGET.from_dict(_password_policy)

        phone = d.pop("phone", UNSET)

        _rbac = d.pop("rbac", UNSET)
        rbac: Union[Unset, RBACV4AaaGET]
        if isinstance(_rbac, Unset):
            rbac = UNSET
        else:
            rbac = RBACV4AaaGET.from_dict(_rbac)

        remote_id_claim = d.pop("remoteIDClaim", UNSET)

        user_id = d.pop("userID", UNSET)

        x_launch = d.pop("xLaunch", UNSET)

        local_user_spec_wrapper_v4_aaa_get = cls(
            email=email,
            first_name=first_name,
            last_name=last_name,
            login_id=login_id,
            password=password,
            password_policy=password_policy,
            phone=phone,
            rbac=rbac,
            remote_id_claim=remote_id_claim,
            user_id=user_id,
            x_launch=x_launch,
        )

        local_user_spec_wrapper_v4_aaa_get.additional_properties = d
        return local_user_spec_wrapper_v4_aaa_get

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
