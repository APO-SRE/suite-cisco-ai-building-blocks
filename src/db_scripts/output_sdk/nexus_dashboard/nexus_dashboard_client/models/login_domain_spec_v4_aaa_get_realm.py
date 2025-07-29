from enum import Enum


class LoginDomainSpecV4AaaGETRealm(str, Enum):
    LDAP = "LDAP"
    LOCAL = "Local"
    OIDC = "OIDC"
    RADIUS = "RADIUS"
    TACACS = "TACACS"

    def __str__(self) -> str:
        return str(self.value)
