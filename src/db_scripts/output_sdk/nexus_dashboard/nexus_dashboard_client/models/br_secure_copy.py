from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.br_secure_copy_authentication import BrSecureCopyAuthentication
from ..models.br_secure_copy_protocol import BrSecureCopyProtocol

T = TypeVar("T", bound="BrSecureCopy")


@_attrs_define
class BrSecureCopy:
    """
    Attributes:
        name (str): Name of the remote scp/sftp location
        host (str): Host name or ip address
        protocol (BrSecureCopyProtocol): Protocol to use
        path (str): Path to existing directory on the remote location
        port (int): Port Default: 22.
        authentication (BrSecureCopyAuthentication): Authentication method
        username (str): Username
        password (str): Password (for password-based authentication)
        ssh_key (str): Private Key (for publickey-based authentication)
        passphrase (str): Passphrase for the private key
        accept_host_key (bool): True if the host key must be accepted, false otherwise (post/put requests only)
    """

    name: str
    host: str
    protocol: BrSecureCopyProtocol
    path: str
    authentication: BrSecureCopyAuthentication
    username: str
    password: str
    ssh_key: str
    passphrase: str
    accept_host_key: bool
    port: int = 22
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        host = self.host

        protocol = self.protocol.value

        path = self.path

        port = self.port

        authentication = self.authentication.value

        username = self.username

        password = self.password

        ssh_key = self.ssh_key

        passphrase = self.passphrase

        accept_host_key = self.accept_host_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "host": host,
                "protocol": protocol,
                "path": path,
                "port": port,
                "authentication": authentication,
                "username": username,
                "password": password,
                "sshKey": ssh_key,
                "passphrase": passphrase,
                "acceptHostKey": accept_host_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        host = d.pop("host")

        protocol = BrSecureCopyProtocol(d.pop("protocol"))

        path = d.pop("path")

        port = d.pop("port")

        authentication = BrSecureCopyAuthentication(d.pop("authentication"))

        username = d.pop("username")

        password = d.pop("password")

        ssh_key = d.pop("sshKey")

        passphrase = d.pop("passphrase")

        accept_host_key = d.pop("acceptHostKey")

        br_secure_copy = cls(
            name=name,
            host=host,
            protocol=protocol,
            path=path,
            port=port,
            authentication=authentication,
            username=username,
            password=password,
            ssh_key=ssh_key,
            passphrase=passphrase,
            accept_host_key=accept_host_key,
        )

        br_secure_copy.additional_properties = d
        return br_secure_copy

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
