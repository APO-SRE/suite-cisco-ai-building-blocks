from enum import Enum


class LDAPConfigV4AaaPOSTOption(str, Enum):
    CISCOAVPAIR = "CiscoAVPair"
    LDAPGROUPMAP = "LDAPGroupMap"

    def __str__(self) -> str:
        return str(self.value)
