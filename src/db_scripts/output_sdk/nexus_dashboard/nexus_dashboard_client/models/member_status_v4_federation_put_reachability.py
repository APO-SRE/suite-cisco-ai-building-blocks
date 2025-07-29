from enum import Enum


class MemberStatusV4FederationPUTReachability(str, Enum):
    DOWN = "Down"
    UNKNOWN = "Unknown"
    UP = "Up"

    def __str__(self) -> str:
        return str(self.value)
