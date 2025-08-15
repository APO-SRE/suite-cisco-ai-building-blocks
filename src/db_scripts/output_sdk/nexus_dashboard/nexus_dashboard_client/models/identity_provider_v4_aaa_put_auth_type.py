from enum import Enum


class IdentityProviderV4AaaPUTAuthType(str, Enum):
    CISCOAVPAIR = "CiscoAVPair"
    GROUPS = "Groups"
    LOCALUSER = "Localuser"

    def __str__(self) -> str:
        return str(self.value)
