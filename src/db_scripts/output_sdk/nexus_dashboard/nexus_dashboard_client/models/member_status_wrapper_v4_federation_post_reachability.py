from enum import Enum


class MemberStatusWrapperV4FederationPOSTReachability(str, Enum):
    DOWN = "Down"
    UNKNOWN = "Unknown"
    UP = "Up"

    def __str__(self) -> str:
        return str(self.value)
