from enum import Enum


class LDAPConfigV4AaaGETOption(str, Enum):
    CISCOAVPAIR = "CiscoAVPair"
    LDAPGROUPMAP = "LDAPGroupMap"

    def __str__(self) -> str:
        return str(self.value)
