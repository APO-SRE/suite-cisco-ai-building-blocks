from enum import Enum


class MemberStatusWrapperV4FederationPUTReachability(str, Enum):
    DOWN = "Down"
    UNKNOWN = "Unknown"
    UP = "Up"

    def __str__(self) -> str:
        return str(self.value)
